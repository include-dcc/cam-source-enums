from __future__ import annotations

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal
from enum import Enum
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    SerializationInfo,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer
)


metamodel_version = "1.11.0"
version = "None"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias = True,
        validate_by_name = True,
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )





class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_prefix': 'cam',
     'default_range': 'string',
     'description': 'LinkML Schema for the Common Access Model Source Enums',
     'id': 'https://includedcc.org/cam-source-enums',
     'imports': ['linkml:types',
                 'EnumDataUsePermission',
                 'EnumDataUseModifier',
                 'EnumProgram',
                 'EnumResearchDomain',
                 'EnumParticipantLifespanStage',
                 'EnumStudyDesign',
                 'EnumClinicalDataSourceType',
                 'EnumDataCategory',
                 'EnumSubjectType',
                 'EnumSex',
                 'EnumRace',
                 'EnumEthnicity',
                 'EnumVitalStatus',
                 'EnumNull',
                 'EnumFamilyType',
                 'EnumConsanguinityAssertion',
                 'EnumAssertionProvenance',
                 'EnumAvailabilityStatus',
                 'EnumSampleCollectionMethod',
                 'EnumSite',
                 'EnumSpatialQualifiers',
                 'EnumLaterality',
                 'EnumEDAMFormats',
                 'EnumEDAMDataTypes',
                 'EnumFileHashType'],
     'license': 'MIT',
     'name': 'cam-source-enums',
     'prefixes': {'DUO': {'prefix_prefix': 'DUO',
                          'prefix_reference': 'http://purl.obolibrary.org/obo/DUO_'},
                  'HP': {'prefix_prefix': 'HP',
                         'prefix_reference': 'http://purl.obolibrary.org/obo/HP_'},
                  'MONDO': {'prefix_prefix': 'MONDO',
                            'prefix_reference': 'http://purl.obolibrary.org/obo/MONDO_'},
                  'NCIT': {'prefix_prefix': 'NCIT',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/NCIT_'},
                  'PATO': {'prefix_prefix': 'PATO',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/PATO_'},
                  'cam': {'prefix_prefix': 'cam',
                          'prefix_reference': 'https://includedcc.org/common-access-model/'},
                  'cdc_race_eth': {'prefix_prefix': 'cdc_race_eth',
                                   'prefix_reference': 'urn:oid:2.16.840.1.113883.6.238/'},
                  'hl7_null': {'prefix_prefix': 'hl7_null',
                               'prefix_reference': 'http://terminology.hl7.org/CodeSystem/v3-NullFlavor/'},
                  'ig2_biospecimen_availability': {'prefix_prefix': 'ig2_biospecimen_availability',
                                                   'prefix_reference': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/CodeSystem/biospecimen-availability/'},
                  'ig2dac': {'prefix_prefix': 'ig2dac',
                             'prefix_reference': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/CodeSystem/research-data-access-code/'},
                  'ig2dat': {'prefix_prefix': 'ig2dat',
                             'prefix_reference': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/CodeSystem/research-data-access-type/'},
                  'ig_dob_method': {'prefix_prefix': 'ig_dob_method',
                                    'prefix_reference': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/CodeSystem/research-data-date-of-birth-method/'},
                  'igcondtype': {'prefix_prefix': 'igcondtype',
                                 'prefix_reference': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/CodeSystem/condition-type/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'mesh': {'prefix_prefix': 'mesh',
                           'prefix_reference': 'http://id.nlm.nih.gov/mesh/'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'},
                  'snomed_ct': {'prefix_prefix': 'snomed_ct',
                                'prefix_reference': 'http://snomed.info/id/'}},
     'see_also': ['https://includedcc.github.io/common-access-model'],
     'source_file': 'src/cam_source_enums/schema/cam_source_enums.yaml',
     'title': 'Common Access Model Source Enums'} )

class EnumDataUsePermission(str):
    """
    Data Use Ontology (DUO) terms for data use permissions.
    """
    pass


class EnumDataUseModifier(str):
    """
    Data Use Ontology (DUO) terms for data use modifiers.
    """
    pass


class EnumProgram(str, Enum):
    """
    Funding programs relevant to inform operations.
    """
    INCLUDE = "include"
    KF = "kf"
    Other = "other"


class EnumResearchDomain(str, Enum):
    """
    Domains of Research used to find studies.
    """
    Behavior_and_Behavior_Mechanisms = "behavior_and_behavior_mechanisms"
    Congenital_Heart_Defects = "congenital_heart_defects"
    Immune_System_Diseases = "immune_system_diseases"
    Hematologic_Diseases = "hematologic_diseases"
    Neurodevelopment = "neurodevelopment"
    Sleep_Wake_Disorders = "sleep_wake_disorders"
    All_Co_occurring_Conditions = "all_co_occurring_conditions"
    Physical_Fitness = "physical_fitness"
    Other = "other"


class EnumParticipantLifespanStage(str, Enum):
    """
    Stages of life during which participants may be recruited.
    """
    Fetal = "fetal"
    """
    Before birth
    """
    Neonatal = "neonatal"
    """
    0-28 days old
    """
    Pediatric = "pediatric"
    """
    Birth-17 years old
    """
    Adult = "adult"
    """
    18+ years old
    """


class EnumStudyDesign(str, Enum):
    """
    Approaches for collecting data, investigating interventions, and/or analyzing data.
    """
    Case_Control = "case_control"
    Case_Set = "case_set"
    Control_Set = "control_set"
    Clinical_Trial = "clinical_trial"
    Cross_Sectional = "cross_sectional"
    FamilySOLIDUSTwinsSOLIDUSTrios = "family_twins_trios"
    Interventional = "interventional"
    Longitudinal = "longitudinal"
    Trial_Readiness_Study = "trial_readiness_study"
    Tumor_vs_Matched_Normal = "tumor_vs_matched_normal"


class EnumClinicalDataSourceType(str, Enum):
    """
    Approaches to ascertain clinical information about a participant.
    """
    Medical_Record = "medical_record"
    """
    Data obtained directly from medical record
    """
    Investigator_Assessment = "investigator_assessment"
    """
    Data obtained by examination, interview, etc. with investigator
    """
    Participant_or_Caregiver_Report = "participant_or_caregiver_report"
    """
    Data obtained from survey, questionnaire, etc. filled out by participant or caregiver
    """
    Other = "other"
    """
    Data obtained from other source, such as tissue bank
    """
    Unknown = "unknown"


class EnumDataCategory(str, Enum):
    """
    Categories of data which may be collected about participants.
    """
    Unharmonized_DemographicSOLIDUSClinical_Data = "unharmonized_demographic_clinical_data"
    Harmonized_DemographicSOLIDUSClinical_Data = "harmonized_demographic_clinical_data"
    Genomics = "genomics"
    Transcriptomics = "transcriptomics"
    Epigenomics = "epigenomics"
    Proteomics = "proteomics"
    Metabolomics = "metabolomics"
    CognitiveSOLIDUSBehavioral = "cognitive_behavioral"
    Immune_Profiling = "immune_profiling"
    Imaging = "imaging"
    Microbiome = "microbiome"
    Fitness = "fitness"
    Physical_Activity = "physical_activity"
    Other = "other"
    Sleep_Study = "sleep_study"


class EnumSubjectType(str, Enum):
    """
    Types of Subject entities
    """
    participant = "participant"
    """
    Study participant with consent, assent, or waiver of consent.
    """
    non_participant = "non_participant"
    """
    An individual associated with a study who was not explictly consented, eg, the subject of a reported family history.
    """
    cell_line = "cell_line"
    """
    Cell Line
    """
    animal_model = "animal_model"
    """
    Animal model
    """
    group = "group"
    """
    A group of individuals or entities.
    """
    other = "other"
    """
    A different entity type- ideally this will be resolved!
    """


class EnumSex(str, Enum):
    """
    Subject Sex
    """
    Female = "female"
    Male = "male"
    Other = "other"
    Unknown = "unknown"


class EnumRace(str, Enum):
    """
    Participant Race
    """
    American_Indian_or_Alaska_Native = "american_indian_or_alaska_native"
    Asian = "asian"
    Black_or_African_American = "black_or_african_american"
    More_than_one_race = "more_than_one_race"
    Native_Hawaiian_or_Other_Pacific_Islander = "native_hawaiian_or_other_pacific_islander"
    Other = "other"
    White = "white"
    Prefer_not_to_answer = "prefer_not_to_answer"
    Unknown = "unknown"
    East_Asian = "east_asian"
    """
    UK only; do not use for US data
    """
    Latin_American = "latin_american"
    """
    UK only; do not use for US data
    """
    Middle_Eastern_or_North_African = "middle_eastern_or_north_african"
    """
    UK only; do not use for US data
    """
    South_Asian = "south_asian"
    """
    UK only; do not use for US data
    """


class EnumEthnicity(str, Enum):
    """
    Participant ethnicity, specific to Hispanic or Latino.
    """
    Hispanic_or_Latino = "hispanic_or_latino"
    Not_Hispanic_or_Latino = "not_hispanic_or_latino"
    Prefer_not_to_answer = "prefer_not_to_answer"
    Unknown = "unknown"


class EnumVitalStatus(str, Enum):
    """
    Descriptions of a Subject's vital status
    """
    Dead = "dead"
    Alive = "alive"


class EnumNull(str, Enum):
    """
    Base enumeration providing null options.
    """
    Unknown = "unknown"


class EnumFamilyType(str, Enum):
    """
    Enumerations describing research family type
    """
    Control_only = "control_only"
    """
    Control Only
    """
    Duo = "duo"
    """
    Duo
    """
    Proband_only = "proband_only"
    """
    Proband Only
    """
    Trio = "trio"
    """
    Trio (2 parents and affected child)
    """
    TrioPLUS_SIGN = "trio_plus"
    """
    2 Parents and 2 or more children
    """


class EnumConsanguinityAssertion(str, Enum):
    """
    Asserts known or suspected consanguinity in this study family
    """
    not_suspected = "not_suspected"
    """
    Not suspected
    """
    suspected = "suspected"
    """
    Suspected
    """
    known_present = "known_present"
    """
    Known Present
    """
    unknown = "unknown"
    """
    Unknown
    """


class EnumAssertionProvenance(str, Enum):
    """
    Possible data sources for assertions.
    """
    Medical_Record = "medical_record"
    """
    Data obtained from a medical record
    """
    Investigator_Assessment = "investigator_assessment"
    """
    Data obtained by examination, interview, etc. with investigator
    """
    Participant_or_Caregiver_Report = "participant_or_caregiver_report"
    """
    Data obtained from survey, questionnaire, etc. filled out by participant or caregiver
    """
    Other = "other"
    """
    Data obtained from other source, such as tissue bank
    """


class EnumAvailabilityStatus(str, Enum):
    """
    Is the biospecimen available for use?
    """
    Available = "available"
    """
    Biospecimen is Available
    """
    Unavailable = "unavailable"
    """
    Biospecimen is Unavailable
    """


class EnumSampleCollectionMethod(str):
    """
    The approach used to collect the biospecimen. [LOINC](https://loinc.org) is recommended.
    """
    pass


class EnumSite(str):
    """
    The location of the specimen collection. [SNOMED Body Site](https://hl7.org/fhir/R4B/valueset-body-site.html) is recommended.
    """
    pass


class EnumSpatialQualifiers(str):
    """
    Any spatial/location qualifiers.
    """
    pass


class EnumLaterality(str):
    """
    Laterality information for the site
    """
    pass


class EnumEDAMFormats(str):
    """
    Data formats from the EDAM ontology.
    """
    pass


class EnumEDAMDataTypes(str):
    """
    Data types from the EDAM ontology.
    """
    pass


class EnumFileHashType(str, Enum):
    """
    Types of file hashes supported.
    """
    MD5 = "md5"
    ETag = "etag"
    SHA_1 = "sha1"



class RequiredClass(ConfiguredBaseModel):
    """
    Required description for classes.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://includedcc.org/cam-source-enums'})

    id: Optional[str] = Field(default=None, description="""Unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['RequiredClass']} })
    full_name: Optional[str] = Field(default=None, description="""Full name""", json_schema_extra = { "linkml_meta": {'domain_of': ['RequiredClass']} })
    aliases: Optional[str] = Field(default=None, description="""Aliases""", json_schema_extra = { "linkml_meta": {'domain_of': ['RequiredClass']} })
    phone: Optional[str] = Field(default=None, description="""Phone number""", json_schema_extra = { "linkml_meta": {'domain_of': ['RequiredClass']} })
    age: Optional[str] = Field(default=None, description="""Age""", json_schema_extra = { "linkml_meta": {'domain_of': ['RequiredClass']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
RequiredClass.model_rebuild()
