# Crossref Metadata

Crossref Members send Crossref scholarly metadata on research which is collated and 
standardised into the Crossref metadata dataset. This dataset is made available through 
services and tools for manuscript tracking, searching, bibliographic management, 
library systems, author profiling, specialist subject databases, scholarly sharing networks
. _- source: [Crossref Metadata](https://www.crossref.org/services/metadata-retrieval/)_ 
and [data details](https://github.com/CrossRef/rest-api-doc)

---

**Schema**

+ **issn_type** [*Record*]
    + **type** [*String*]
    + **value** [*String*]
+ **ISSN** [*String*]
+ **ISBN** [*String*]
+ **URL** [*String*]
+ **publisher_location** [*String*]
+ **references_count** [*Integer*]
+ **alternative_id** [*String*]
+ **issued** [*Record*]
    + **date_parts** [*Integer*]
+ **posted** [*Record*]
    + **date_parts** [*Integer*]
+ **group_title** [*String*]
+ **score** [*String*]
+ **subject** [*String*]
+ **abstract** [*String*]
+ **deposited** [*Record*]
    + **timestamp** [*Integer*]
    + **date_time** [*Timestamp*]
    + **date_parts** [*Integer*]
+ **link** [*Record*]
    + **intended_application** [*String*]
    + **content_version** [*String*]
    + **content_type** [*String*]
    + **URL** [*String*]
+ **published_print** [*Record*]
    + **date_parts** [*Integer*]
+ **accepted** [*Record*]
    + **date_parts** [*Integer*]
+ **indexed** [*Record*]
    + **timestamp** [*Integer*]
    + **date_time** [*Timestamp*]
    + **date_parts** [*Integer*]
+ **update_to** [*Record*]
    + **updated** [*Record*]
        + **timestamp** [*Integer*]
        + **date_time** [*String*]
        + **date_parts** [*Integer*]
    + **DOI** [*String*]
    + **type** [*String*]
    + **label** [*String*]
+ **approved** [*Record*]
    + **date_parts** [*Integer*]
+ **source** [*String*]
+ **content_created** [*Record*]
    + **date_parts** [*Integer*]
+ **content_updated** [*Record*]
    + **date_parts** [*Integer*]
+ **DOI** [*String*]
+ **content_domain** [*Record*]
    + **crossmark_restriction** [*Boolean*]
    + **domain** [*String*]
+ **relation** [*Record*]
    + **cites** [*String*]
    + **has_preprint** [*Record*]
        + **id_type** [*String*]
        + **id** [*String*]
        + **asserted_by** [*String*]
    + **has_part** [*Record*]
        + **id_type** [*String*]
        + **id** [*String*]
        + **asserted_by** [*String*]
    + **has_review** [*Record*]
        + **id_type** [*String*]
        + **id** [*String*]
        + **asserted_by** [*String*]
    + **is_supplemented_by** [*Record*]
        + **id_type** [*String*]
        + **id** [*String*]
        + **asserted_by** [*String*]
    + **is_part_of** [*Record*]
        + **id_type** [*String*]
        + **id** [*String*]
        + **asserted_by** [*String*]
    + **is_identical_to** [*Record*]
        + **id_type** [*String*]
        + **id** [*String*]
        + **asserted_by** [*String*]
    + **references** [*Record*]
        + **id_type** [*String*]
        + **id** [*String*]
        + **asserted_by** [*String*]
    + **has_manifestation** [*Record*]
        + **id_type** [*String*]
        + **id** [*String*]
        + **asserted_by** [*String*]
    + **is_reply_to** [*Record*]
        + **id_type** [*String*]
        + **id** [*String*]
        + **asserted_by** [*String*]
    + **is_based_on** [*Record*]
        + **id_type** [*String*]
        + **id** [*String*]
        + **asserted_by** [*String*]
    + **is_review_of** [*Record*]
        + **id_type** [*String*]
        + **id** [*String*]
        + **asserted_by** [*String*]
    + **has_reply** [*Record*]
        + **id_type** [*String*]
        + **id** [*String*]
        + **asserted_by** [*String*]
    + **is_replaced_by** [*Record*]
        + **id_type** [*String*]
        + **id** [*String*]
        + **asserted_by** [*String*]
    + **has_comment** [*Record*]
        + **id_type** [*String*]
        + **id** [*String*]
        + **asserted_by** [*String*]
    + **documents** [*Record*]
        + **id_type** [*String*]
        + **id** [*String*]
        + **asserted_by** [*String*]
    + **is_version_of** [*Record*]
        + **id_type** [*String*]
        + **id** [*String*]
        + **asserted_by** [*String*]
    + **has_version** [*Record*]
        + **id_type** [*String*]
        + **id** [*String*]
        + **asserted_by** [*String*]
    + **has_related_material** [*Record*]
        + **id_type** [*String*]
        + **id** [*String*]
        + **asserted_by** [*String*]
    + **is_compiled_by** [*Record*]
        + **id_type** [*String*]
        + **id** [*String*]
        + **asserted_by** [*String*]
    + **has_translation** [*Record*]
        + **id_type** [*String*]
        + **id** [*String*]
        + **asserted_by** [*String*]
    + **is_translation_of** [*Record*]
        + **id_type** [*String*]
        + **id** [*String*]
        + **asserted_by** [*String*]
    + **is_preprint_of** [*Record*]
        + **id_type** [*String*]
        + **id** [*String*]
        + **asserted_by** [*String*]
    + **is_referenced_by** [*Record*]
        + **id_type** [*String*]
        + **id** [*String*]
        + **asserted_by** [*String*]
    + **is_supplement_to** [*Record*]
        + **id_type** [*String*]
        + **id** [*String*]
        + **asserted_by** [*String*]
    + **is_variant_form_of** [*Record*]
        + **id_type** [*String*]
        + **id** [*String*]
        + **asserted_by** [*String*]
    + **replaces** [*Record*]
        + **id_type** [*String*]
        + **id** [*String*]
        + **asserted_by** [*String*]
    + **is_manifestation_of** [*Record*]
        + **id_type** [*String*]
        + **id** [*String*]
        + **asserted_by** [*String*]
    + **is_related_material** [*Record*]
        + **id_type** [*String*]
        + **id** [*String*]
        + **asserted_by** [*String*]
    + **is_basis_for** [*Record*]
        + **id_type** [*String*]
        + **id** [*String*]
        + **asserted_by** [*String*]
    + **is_comment_on** [*Record*]
        + **id_type** [*String*]
        + **id** [*String*]
        + **asserted_by** [*String*]
    + **continues** [*Record*]
        + **id_type** [*String*]
        + **id** [*String*]
        + **asserted_by** [*String*]
    + **is_continued_by** [*Record*]
        + **id_type** [*String*]
        + **id** [*String*]
        + **asserted_by** [*String*]
    + **has_derivation** [*Record*]
        + **id_type** [*String*]
        + **id** [*String*]
        + **asserted_by** [*String*]
    + **is_data_basis_for** [*Record*]
        + **id_type** [*String*]
        + **id** [*String*]
        + **asserted_by** [*String*]
    + **is_documented_by** [*Record*]
        + **id_type** [*String*]
        + **id** [*String*]
        + **asserted_by** [*String*]
    + **is_derived_from** [*Record*]
        + **id_type** [*String*]
        + **id** [*String*]
        + **asserted_by** [*String*]
    + **has_manuscript** [*Record*]
        + **id_type** [*String*]
        + **id** [*String*]
        + **asserted_by** [*String*]
    + **is_manuscript_of** [*Record*]
        + **id_type** [*String*]
        + **id** [*String*]
        + **asserted_by** [*String*]
    + **based_on_data** [*Record*]
        + **id_type** [*String*]
        + **id** [*String*]
        + **asserted_by** [*String*]
    + **is_original_form_of** [*Record*]
        + **id_type** [*String*]
        + **id** [*String*]
        + **asserted_by** [*String*]
    + **is_varient_form_of** [*Record*]
        + **id_type** [*String*]
        + **id** [*String*]
        + **asserted_by** [*String*]
+ **license** [*Record*]
    + **content_version** [*String*]
    + **delay_in_days** [*Integer*]
    + **start** [*Record*]
        + **timestamp** [*Integer*]
        + **date_time** [*String*]
        + **date_parts** [*Integer*]
    + **URL** [*String*]
+ **volume** [*String*]
+ **funder** [*Record*]
    + **DOI** [*String*]
    + **name** [*String*]
    + **doi_asserted_by** [*String*]
    + **award** [*String*]
+ **is_referenced_by_count** [*Integer*]
+ **degree** [*String*]
+ **subtitle** [*String*]
+ **issue** [*String*]
+ **reference_count** [*Integer*]
+ **type** [*String*]
+ **page** [*String*]
+ **update_policy** [*String*]
+ **title** [*String*]
+ **publisher** [*String*]
+ **created** [*Record*]
    + **timestamp** [*Integer*]
    + **date_time** [*Timestamp*]
    + **date_parts** [*Integer*]
+ **prefix** [*Float*]
+ **author** [*Record*]
    + **affiliation** [*Record*]
        + **name** [*String*]
    + **family** [*String*]
    + **given** [*String*]
    + **name** [*String*]
    + **suffix** [*String*]
    + **ORCID** [*String*]
    + **authenticated_orcid** [*Boolean*]
+ **editor** [*Record*]
    + **affiliation** [*Record*]
        + **name** [*String*]
    + **family** [*String*]
    + **given** [*String*]
    + **name** [*String*]
    + **suffix** [*String*]
    + **ORCID** [*String*]
    + **authenticated_orcid** [*Boolean*]
+ **translator** [*Record*]
    + **affiliation** [*Record*]
        + **name** [*String*]
    + **family** [*String*]
    + **given** [*String*]
    + **name** [*String*]
    + **suffix** [*String*]
    + **ORCID** [*String*]
    + **authenticated_orcid** [*Boolean*]
+ **chair** [*Record*]
    + **affiliation** [*Record*]
        + **name** [*String*]
    + **family** [*String*]
    + **given** [*String*]
    + **name** [*String*]
    + **suffix** [*String*]
    + **ORCID** [*String*]
    + **authenticated_orcid** [*Boolean*]
+ **member** [*Integer*]
+ **short_container_title** [*String*]
+ **reference** [*Record*]
    + **unstructured** [*String*]
    + **key** [*String*]
    + **journal_title** [*String*]
    + **first_page** [*String*]
    + **ISBN** [*String*]
    + **doi_asserted_by** [*String*]
    + **series_title** [*String*]
    + **article_title** [*String*]
    + **volume** [*String*]
    + **author** [*String*]
    + **year** [*String*]
    + **DOI** [*String*]
    + **ISSN** [*String*]
    + **issn_type** [*String*]
    + **isbn_type** [*String*]
    + **volume_title** [*String*]
    + **issue** [*String*]
    + **edition** [*String*]
    + **component** [*String*]
    + **standards_body** [*String*]
    + **standard_designator** [*String*]
+ **event** [*Record*]
    + **name** [*String*]
    + **location** [*String*]
    + **acronym** [*String*]
    + **sponsor** [*String*]
    + **number** [*String*]
    + **theme** [*String*]
    + **start** [*Record*]
        + **date_parts** [*Integer*]
    + **end** [*Record*]
        + **date_parts** [*Integer*]
+ **standards_body** [*Record*]
    + **name** [*String*]
    + **acronym** [*String*]
+ **container_title** [*String*]
+ **short_title** [*String*]
+ **original_title** [*String*]
+ **published_online** [*Record*]
    + **date_parts** [*Integer*]
+ **assertion** [*Record*]
    + **value** [*String*]
    + **name** [*String*]
    + **url** [*String*]
    + **group** [*Record*]
        + **name** [*String*]
        + **label** [*String*]
    + **label** [*String*]
    + **explanation** [*Record*]
        + **URL** [*String*]
    + **order** [*Integer*]
+ **article_number** [*String*]
+ **archive** [*String*]
+ **clinical_trial_number** [*Record*]
    + **clinical_trial_number** [*String*]
    + **registry** [*String*]
    + **type** [*String*]
