#!/usr/bin/python3

# Copyright 2020 Curtin University
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Author: Tuan Chien


import logging
import datetime
import pandas as pd

from observatory.dags.dataquality.autofetchcache import AutoFetchCache
from jinja2 import Environment, PackageLoader
from observatory.dags.dataquality.config import JinjaParams, MagCacheKey, MagTableKey
from observatory.dags.dataquality.es_mag import MagPapersMetrics
from observatory.dags.dataquality.analyser import MagAnalyserModule
from observatory.dags.dataquality.es_utils import (
    get_or_init_doc_count,
    search_count_by_release,
    clear_index,
    bulk_index,
    delete_index,
)

class PaperMetricsModule(MagAnalyserModule):
    """
    MagAnalyser module to compute some basic metrics for the Papers dataset in MAG.
    Example metrics: total number of papers, null counts for year, doi, doctype, familyid and their proportionality.
    """

    BQ_COUNT = 'count'  # SQL column for the counts.

    def __init__(self, project_id: str, dataset_id: str, cache: AutoFetchCache):
        """ Initialise the module.
        @param project_id: Project ID in BigQuery.
        @param dataset_id: Dataset ID in BigQuery.
        @param cache: Analyser cache to use.
        """

        logging.info(f'{self.name()}: initialising.')
        self._project_id = project_id
        self._dataset_id = dataset_id
        self._cache = cache

        self._es_count = get_or_init_doc_count(MagPapersMetrics)

        self._tpl_env = Environment(
            loader=PackageLoader(JinjaParams.PKG_NAME, JinjaParams.TEMPLATE_PATHS))
        self._tpl_null_count = self._tpl_env.get_template('null_count.sql.jinja2')

    def run(self, **kwargs):
        """ Run the module.
        @param kwargs: Unused.
        """

        logging.info(f'{self.name()}: executing.')
        releases = self._cache[MagCacheKey.RELEASES]
        num_releases = len(releases)

        # If records exist in elastic search, skip.  This is not robust to partial records (past interrupted loads).
        if self._es_count == num_releases:
            return

        docs = list()
        for release in releases:
            # If records exist in elastic search, skip.  This is not robust to partial records (past interrupted loads).
            if search_count_by_release(MagPapersMetrics, release) > 0:
                continue

            doc = self._construct_es_docs(release)
            docs.append(doc)

        logging.info(f'{self.name()}: indexing {len(docs)} docs of type MagPapersMetrics.')
        if len(docs) > 0:
            bulk_index(docs)

    def erase(self, index: bool = False, **kwargs):
        """
        Erase elastic search records used by the module and delete the index.
        @param index: If index=True, will also delete indices.
        @param kwargs: Unused.
        """

        clear_index(MagPapersMetrics)

        if index:
            delete_index(MagPapersMetrics)

    def _construct_es_docs(self, release: datetime.datetime) -> MagPapersMetrics:
        """ Construct the elastic search documents.
        @param release: Release timestamp.
        @return: List of constructed documents.
        """

        eps = 1e-9

        # Generate the elastic search document.
        null_metrics = self._get_paper_null_counts(release)
        es_paper_metrics = MagPapersMetrics(release=release.isoformat())
        es_paper_metrics.total = null_metrics[PaperMetricsModule.BQ_COUNT][0] + eps

        es_paper_metrics.null_year = null_metrics[MagTableKey.COL_YEAR][0] + eps
        es_paper_metrics.null_doi = null_metrics[MagTableKey.COL_DOI][0] + eps
        es_paper_metrics.null_doctype = null_metrics[MagTableKey.COL_DOC_TYPE][0] + eps
        es_paper_metrics.null_familyid = null_metrics[MagTableKey.COL_FAMILY_ID][0] + eps

        es_paper_metrics.pnull_year = es_paper_metrics.null_year / es_paper_metrics.total
        es_paper_metrics.pnull_doi = es_paper_metrics.null_doi / es_paper_metrics.total
        es_paper_metrics.pnull_doctype = es_paper_metrics.null_doctype / es_paper_metrics.total
        es_paper_metrics.pnull_familyid = es_paper_metrics.null_familyid / es_paper_metrics.total

        return es_paper_metrics


    def _get_paper_null_counts(self, release: datetime.date) -> pd.DataFrame:
        """ Get the null counts of some Papers fields for a given release.
        @param release: Release date.
        @return Null count information.
        """

        ts = release.strftime('%Y%m%d')
        table_id = f'{MagTableKey.TID_PAPERS}{ts}'
        sql = self._tpl_null_count.render(
            project_id=self._project_id, dataset_id=self._dataset_id, table_id=table_id,
            null_count=[MagTableKey.COL_DOI, MagTableKey.COL_DOC_TYPE, MagTableKey.COL_YEAR,
                        MagTableKey.COL_FAMILY_ID],
            count=PaperMetricsModule.BQ_COUNT
        )
        return pd.read_gbq(sql, project_id=self._project_id, progress_bar_type=None)
