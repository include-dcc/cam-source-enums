# Auto generated from cam_source_enums.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-05-20T09:59:12
# Schema: cam-source-enums
#
# id: https://includedcc.org/cam-source-enums
# description: LinkML Schema for the Common Access Model Source Enums
# license: MIT

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import String

metamodel_version = "1.11.0"
version = None

# Namespaces
DUO = CurieNamespace('DUO', 'http://purl.obolibrary.org/obo/DUO_')
HP = CurieNamespace('HP', 'http://purl.obolibrary.org/obo/HP_')
MONDO = CurieNamespace('MONDO', 'http://purl.obolibrary.org/obo/MONDO_')
NCIT = CurieNamespace('NCIT', 'http://purl.obolibrary.org/obo/NCIT_')
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
CAM = CurieNamespace('cam', 'https://includedcc.org/common-access-model/')
CDC_RACE_ETH = CurieNamespace('cdc_race_eth', 'urn:oid:2.16.840.1.113883.6.238/')
HL7_NULL = CurieNamespace('hl7_null', 'http://terminology.hl7.org/CodeSystem/v3-NullFlavor/')
IG2_BIOSPECIMEN_AVAILABILITY = CurieNamespace('ig2_biospecimen_availability', 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/CodeSystem/biospecimen-availability/')
IG2DAC = CurieNamespace('ig2dac', 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/CodeSystem/research-data-access-code/')
IG2DAT = CurieNamespace('ig2dat', 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/CodeSystem/research-data-access-type/')
IG_DOB_METHOD = CurieNamespace('ig_dob_method', 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/CodeSystem/research-data-date-of-birth-method/')
IGCONDTYPE = CurieNamespace('igcondtype', 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/CodeSystem/condition-type/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
MESH = CurieNamespace('mesh', 'http://id.nlm.nih.gov/mesh/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SNOMED_CT = CurieNamespace('snomed_ct', 'http://snomed.info/id/')
DEFAULT_ = CAM


# Types

# Class references



@dataclass(repr=False)
class RequiredClass(YAMLRoot):
    """
    Required description for classes.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CAM["RequiredClass"]
    class_class_curie: ClassVar[str] = "cam:RequiredClass"
    class_name: ClassVar[str] = "RequiredClass"
    class_model_uri: ClassVar[URIRef] = CAM.RequiredClass

    id: Optional[str] = None
    full_name: Optional[str] = None
    aliases: Optional[str] = None
    phone: Optional[str] = None
    age: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.id is not None and not isinstance(self.id, str):
            self.id = str(self.id)

        if self.full_name is not None and not isinstance(self.full_name, str):
            self.full_name = str(self.full_name)

        if self.aliases is not None and not isinstance(self.aliases, str):
            self.aliases = str(self.aliases)

        if self.phone is not None and not isinstance(self.phone, str):
            self.phone = str(self.phone)

        if self.age is not None and not isinstance(self.age, str):
            self.age = str(self.age)

        super().__post_init__(**kwargs)


# Enumerations
class EnumDataUsePermission(EnumDefinitionImpl):
    """
    Data Use Ontology (DUO) terms for data use permissions.
    """
    _defn = EnumDefinition(
        name="EnumDataUsePermission",
        description="Data Use Ontology (DUO) terms for data use permissions.",
    )

class EnumDataUseModifier(EnumDefinitionImpl):
    """
    Data Use Ontology (DUO) terms for data use modifiers.
    """
    _defn = EnumDefinition(
        name="EnumDataUseModifier",
        description="Data Use Ontology (DUO) terms for data use modifiers.",
    )

class EnumProgram(EnumDefinitionImpl):
    """
    Funding programs relevant to inform operations.
    """
    include = PermissibleValue(
        text="include",
        title="INCLUDE")
    kf = PermissibleValue(
        text="kf",
        title="KF")
    other = PermissibleValue(
        text="other",
        title="Other")

    _defn = EnumDefinition(
        name="EnumProgram",
        description="Funding programs relevant to inform operations.",
    )

class EnumResearchDomain(EnumDefinitionImpl):
    """
    Domains of Research used to find studies.
    """
    behavior_and_behavior_mechanisms = PermissibleValue(
        text="behavior_and_behavior_mechanisms",
        title="Behavior and Behavior Mechanisms",
        meaning=MESH["D001520"])
    congenital_heart_defects = PermissibleValue(
        text="congenital_heart_defects",
        title="Congenital Heart Defects",
        meaning=MESH["D006330"])
    immune_system_diseases = PermissibleValue(
        text="immune_system_diseases",
        title="Immune System Diseases",
        meaning=MESH["D007154"])
    hematologic_diseases = PermissibleValue(
        text="hematologic_diseases",
        title="Hematologic Diseases",
        meaning=MESH["D006402"])
    neurodevelopment = PermissibleValue(
        text="neurodevelopment",
        title="Neurodevelopment",
        meaning=MESH["D065886"])
    sleep_wake_disorders = PermissibleValue(
        text="sleep_wake_disorders",
        title="Sleep Wake Disorders",
        meaning=MESH["D012893"])
    all_co_occurring_conditions = PermissibleValue(
        text="all_co_occurring_conditions",
        title="All Co-occurring Conditions",
        meaning=MESH["D013568"])
    physical_fitness = PermissibleValue(
        text="physical_fitness",
        title="Physical Fitness",
        meaning=MESH["D010809"])
    other = PermissibleValue(
        text="other",
        title="Other")

    _defn = EnumDefinition(
        name="EnumResearchDomain",
        description="Domains of Research used to find studies.",
    )

class EnumParticipantLifespanStage(EnumDefinitionImpl):
    """
    Stages of life during which participants may be recruited.
    """
    fetal = PermissibleValue(
        text="fetal",
        title="Fetal",
        description="Before birth")
    neonatal = PermissibleValue(
        text="neonatal",
        title="Neonatal",
        description="0-28 days old")
    pediatric = PermissibleValue(
        text="pediatric",
        title="Pediatric",
        description="Birth-17 years old")
    adult = PermissibleValue(
        text="adult",
        title="Adult",
        description="18+ years old")

    _defn = EnumDefinition(
        name="EnumParticipantLifespanStage",
        description="Stages of life during which participants may be recruited.",
    )

class EnumStudyDesign(EnumDefinitionImpl):
    """
    Approaches for collecting data, investigating interventions, and/or analyzing data.
    """
    case_control = PermissibleValue(
        text="case_control",
        title="Case-Control")
    case_set = PermissibleValue(
        text="case_set",
        title="Case Set")
    control_set = PermissibleValue(
        text="control_set",
        title="Control Set")
    clinical_trial = PermissibleValue(
        text="clinical_trial",
        title="Clinical Trial")
    cross_sectional = PermissibleValue(
        text="cross_sectional",
        title="Cross-Sectional")
    family_twins_trios = PermissibleValue(
        text="family_twins_trios",
        title="Family/Twins/Trios")
    interventional = PermissibleValue(
        text="interventional",
        title="Interventional")
    longitudinal = PermissibleValue(
        text="longitudinal",
        title="Longitudinal")
    trial_readiness_study = PermissibleValue(
        text="trial_readiness_study",
        title="Trial Readiness Study")
    tumor_vs_matched_normal = PermissibleValue(
        text="tumor_vs_matched_normal",
        title="Tumor vs Matched Normal")

    _defn = EnumDefinition(
        name="EnumStudyDesign",
        description="Approaches for collecting data, investigating interventions, and/or analyzing data.",
    )

class EnumClinicalDataSourceType(EnumDefinitionImpl):
    """
    Approaches to ascertain clinical information about a participant.
    """
    medical_record = PermissibleValue(
        text="medical_record",
        title="Medical Record",
        description="Data obtained directly from medical record")
    investigator_assessment = PermissibleValue(
        text="investigator_assessment",
        title="Investigator Assessment",
        description="Data obtained by examination, interview, etc. with investigator")
    participant_or_caregiver_report = PermissibleValue(
        text="participant_or_caregiver_report",
        title="Participant or Caregiver Report",
        description="Data obtained from survey, questionnaire, etc. filled out by participant or caregiver")
    other = PermissibleValue(
        text="other",
        title="Other",
        description="Data obtained from other source, such as tissue bank")
    unknown = PermissibleValue(
        text="unknown",
        title="Unknown")

    _defn = EnumDefinition(
        name="EnumClinicalDataSourceType",
        description="Approaches to ascertain clinical information about a participant.",
    )

class EnumDataCategory(EnumDefinitionImpl):
    """
    Categories of data which may be collected about participants.
    """
    unharmonized_demographic_clinical_data = PermissibleValue(
        text="unharmonized_demographic_clinical_data",
        title="Unharmonized Demographic/Clinical Data")
    harmonized_demographic_clinical_data = PermissibleValue(
        text="harmonized_demographic_clinical_data",
        title="Harmonized Demographic/Clinical Data")
    genomics = PermissibleValue(
        text="genomics",
        title="Genomics")
    transcriptomics = PermissibleValue(
        text="transcriptomics",
        title="Transcriptomics")
    epigenomics = PermissibleValue(
        text="epigenomics",
        title="Epigenomics")
    proteomics = PermissibleValue(
        text="proteomics",
        title="Proteomics")
    metabolomics = PermissibleValue(
        text="metabolomics",
        title="Metabolomics")
    cognitive_behavioral = PermissibleValue(
        text="cognitive_behavioral",
        title="Cognitive/Behavioral")
    immune_profiling = PermissibleValue(
        text="immune_profiling",
        title="Immune Profiling")
    imaging = PermissibleValue(
        text="imaging",
        title="Imaging")
    microbiome = PermissibleValue(
        text="microbiome",
        title="Microbiome")
    fitness = PermissibleValue(
        text="fitness",
        title="Fitness")
    physical_activity = PermissibleValue(
        text="physical_activity",
        title="Physical Activity")
    other = PermissibleValue(
        text="other",
        title="Other")
    sleep_study = PermissibleValue(
        text="sleep_study",
        title="Sleep Study")

    _defn = EnumDefinition(
        name="EnumDataCategory",
        description="Categories of data which may be collected about participants.",
    )

class EnumSubjectType(EnumDefinitionImpl):
    """
    Types of Subject entities
    """
    participant = PermissibleValue(
        text="participant",
        description="Study participant with consent, assent, or waiver of consent.")
    non_participant = PermissibleValue(
        text="non_participant",
        description="""An individual associated with a study who was not explictly consented, eg, the subject of a reported family history.""")
    cell_line = PermissibleValue(
        text="cell_line",
        description="Cell Line")
    animal_model = PermissibleValue(
        text="animal_model",
        description="Animal model")
    group = PermissibleValue(
        text="group",
        description="A group of individuals or entities.")
    other = PermissibleValue(
        text="other",
        description="A different entity type- ideally this will be resolved!")

    _defn = EnumDefinition(
        name="EnumSubjectType",
        description="Types of Subject entities",
    )

class EnumSex(EnumDefinitionImpl):
    """
    Subject Sex
    """
    female = PermissibleValue(
        text="female",
        title="Female",
        meaning=NCIT["C16576"])
    male = PermissibleValue(
        text="male",
        title="Male",
        meaning=NCIT["C20197"])
    other = PermissibleValue(
        text="other",
        title="Other",
        meaning=NCIT["C17649"])
    unknown = PermissibleValue(
        text="unknown",
        title="Unknown",
        meaning=NCIT["C17998"])

    _defn = EnumDefinition(
        name="EnumSex",
        description="Subject Sex",
    )

class EnumRace(EnumDefinitionImpl):
    """
    Participant Race
    """
    american_indian_or_alaska_native = PermissibleValue(
        text="american_indian_or_alaska_native",
        title="American Indian or Alaska Native",
        meaning=NCIT["C41259"])
    asian = PermissibleValue(
        text="asian",
        title="Asian",
        meaning=NCIT["C41260"])
    black_or_african_american = PermissibleValue(
        text="black_or_african_american",
        title="Black or African American",
        meaning=NCIT["C16352"])
    more_than_one_race = PermissibleValue(
        text="more_than_one_race",
        title="More than one race",
        meaning=NCIT["C67109"])
    native_hawaiian_or_other_pacific_islander = PermissibleValue(
        text="native_hawaiian_or_other_pacific_islander",
        title="Native Hawaiian or Other Pacific Islander",
        meaning=NCIT["C41219"])
    other = PermissibleValue(
        text="other",
        title="Other",
        meaning=NCIT["C17649"])
    white = PermissibleValue(
        text="white",
        title="White",
        meaning=NCIT["C41261"])
    prefer_not_to_answer = PermissibleValue(
        text="prefer_not_to_answer",
        title="Prefer not to answer",
        meaning=NCIT["C132222"])
    unknown = PermissibleValue(
        text="unknown",
        title="Unknown",
        meaning=NCIT["C17998"])
    east_asian = PermissibleValue(
        text="east_asian",
        title="East Asian",
        description="UK only; do not use for US data",
        meaning=NCIT["C161419"])
    latin_american = PermissibleValue(
        text="latin_american",
        title="Latin American",
        description="UK only; do not use for US data",
        meaning=NCIT["C126531"])
    middle_eastern_or_north_african = PermissibleValue(
        text="middle_eastern_or_north_african",
        title="Middle Eastern or North African",
        description="UK only; do not use for US data",
        meaning=NCIT["C43866"])
    south_asian = PermissibleValue(
        text="south_asian",
        title="South Asian",
        description="UK only; do not use for US data",
        meaning=NCIT["C41263"])

    _defn = EnumDefinition(
        name="EnumRace",
        description="Participant Race",
    )

class EnumEthnicity(EnumDefinitionImpl):
    """
    Participant ethnicity, specific to Hispanic or Latino.
    """
    hispanic_or_latino = PermissibleValue(
        text="hispanic_or_latino",
        title="Hispanic or Latino",
        meaning=NCIT["C17459"])
    not_hispanic_or_latino = PermissibleValue(
        text="not_hispanic_or_latino",
        title="Not Hispanic or Latino",
        meaning=NCIT["C41222"])
    prefer_not_to_answer = PermissibleValue(
        text="prefer_not_to_answer",
        title="Prefer not to answer",
        meaning=NCIT["C132222"])
    unknown = PermissibleValue(
        text="unknown",
        title="Unknown",
        meaning=NCIT["C17998"])

    _defn = EnumDefinition(
        name="EnumEthnicity",
        description="Participant ethnicity, specific to Hispanic or Latino.",
    )

class EnumVitalStatus(EnumDefinitionImpl):
    """
    Descriptions of a Subject's vital status
    """
    dead = PermissibleValue(
        text="dead",
        title="Dead",
        meaning=NCIT["C28554"])
    alive = PermissibleValue(
        text="alive",
        title="Alive",
        meaning=NCIT["C37987"])

    _defn = EnumDefinition(
        name="EnumVitalStatus",
        description="Descriptions of a Subject's vital status",
    )

class EnumNull(EnumDefinitionImpl):
    """
    Base enumeration providing null options.
    """
    unknown = PermissibleValue(
        text="unknown",
        title="Unknown",
        meaning=NCIT["C17998"])

    _defn = EnumDefinition(
        name="EnumNull",
        description="Base enumeration providing null options.",
    )

class EnumFamilyType(EnumDefinitionImpl):
    """
    Enumerations describing research family type
    """
    control_only = PermissibleValue(
        text="control_only",
        title="Control-only",
        description="Control Only")
    duo = PermissibleValue(
        text="duo",
        title="Duo",
        description="Duo")
    proband_only = PermissibleValue(
        text="proband_only",
        title="Proband-only",
        description="Proband Only")
    trio = PermissibleValue(
        text="trio",
        title="Trio",
        description="Trio (2 parents and affected child)")
    trio_plus = PermissibleValue(
        text="trio_plus",
        title="Trio+",
        description="2 Parents and 2 or more children")

    _defn = EnumDefinition(
        name="EnumFamilyType",
        description="Enumerations describing research family type",
    )

class EnumConsanguinityAssertion(EnumDefinitionImpl):
    """
    Asserts known or suspected consanguinity in this study family
    """
    not_suspected = PermissibleValue(
        text="not_suspected",
        title="not-suspected",
        description="Not suspected",
        meaning=SNOMED_CT["428263003"])
    suspected = PermissibleValue(
        text="suspected",
        title="suspected",
        description="Suspected",
        meaning=SNOMED_CT["415684004"])
    known_present = PermissibleValue(
        text="known_present",
        title="known-present",
        description="Known Present",
        meaning=SNOMED_CT["410515003"])
    unknown = PermissibleValue(
        text="unknown",
        title="unknown",
        description="Unknown",
        meaning=SNOMED_CT["261665006"])

    _defn = EnumDefinition(
        name="EnumConsanguinityAssertion",
        description="Asserts known or suspected consanguinity in this study family",
    )

class EnumAssertionProvenance(EnumDefinitionImpl):
    """
    Possible data sources for assertions.
    """
    medical_record = PermissibleValue(
        text="medical_record",
        title="Medical Record",
        description="Data obtained from a medical record")
    investigator_assessment = PermissibleValue(
        text="investigator_assessment",
        title="Investigator Assessment",
        description="Data obtained by examination, interview, etc. with investigator")
    participant_or_caregiver_report = PermissibleValue(
        text="participant_or_caregiver_report",
        title="Participant or Caregiver Report",
        description="Data obtained from survey, questionnaire, etc. filled out by participant or caregiver")
    other = PermissibleValue(
        text="other",
        title="Other",
        description="Data obtained from other source, such as tissue bank")

    _defn = EnumDefinition(
        name="EnumAssertionProvenance",
        description="Possible data sources for assertions.",
    )

class EnumAvailabilityStatus(EnumDefinitionImpl):
    """
    Is the biospecimen available for use?
    """
    available = PermissibleValue(
        text="available",
        title="Available",
        description="Biospecimen is Available",
        meaning=IG2_BIOSPECIMEN_AVAILABILITY["available"])
    unavailable = PermissibleValue(
        text="unavailable",
        title="Unavailable",
        description="Biospecimen is Unavailable",
        meaning=IG2_BIOSPECIMEN_AVAILABILITY["unavailable"])

    _defn = EnumDefinition(
        name="EnumAvailabilityStatus",
        description="Is the biospecimen available for use?",
    )

class EnumSampleCollectionMethod(EnumDefinitionImpl):
    """
    The approach used to collect the biospecimen. [LOINC](https://loinc.org) is recommended.
    """
    _defn = EnumDefinition(
        name="EnumSampleCollectionMethod",
        description="The approach used to collect the biospecimen. [LOINC](https://loinc.org) is recommended.",
    )

class EnumSite(EnumDefinitionImpl):
    """
    The location of the specimen collection. [SNOMED Body Site](https://hl7.org/fhir/R4B/valueset-body-site.html) is
    recommended.
    """
    _defn = EnumDefinition(
        name="EnumSite",
        description="""The location of the specimen collection. [SNOMED Body Site](https://hl7.org/fhir/R4B/valueset-body-site.html) is recommended.""",
    )

class EnumSpatialQualifiers(EnumDefinitionImpl):
    """
    Any spatial/location qualifiers.
    """
    _defn = EnumDefinition(
        name="EnumSpatialQualifiers",
        description="Any spatial/location qualifiers.",
    )

class EnumLaterality(EnumDefinitionImpl):
    """
    Laterality information for the site
    """
    _defn = EnumDefinition(
        name="EnumLaterality",
        description="Laterality information for the site",
    )

class EnumEDAMFormats(EnumDefinitionImpl):
    """
    Data formats from the EDAM ontology.
    """
    _defn = EnumDefinition(
        name="EnumEDAMFormats",
        description="Data formats from the EDAM ontology.",
    )

class EnumEDAMDataTypes(EnumDefinitionImpl):
    """
    Data types from the EDAM ontology.
    """
    _defn = EnumDefinition(
        name="EnumEDAMDataTypes",
        description="Data types from the EDAM ontology.",
    )

class EnumFileHashType(EnumDefinitionImpl):
    """
    Types of file hashes supported.
    """
    md5 = PermissibleValue(
        text="md5",
        title="MD5")
    etag = PermissibleValue(
        text="etag",
        title="ETag")
    sha1 = PermissibleValue(
        text="sha1",
        title="SHA-1")

    _defn = EnumDefinition(
        name="EnumFileHashType",
        description="Types of file hashes supported.",
    )

# Slots
class slots:
    pass

slots.requiredClass__id = Slot(uri=CAM.id, name="requiredClass__id", curie=CAM.curie('id'),
                   model_uri=CAM.requiredClass__id, domain=None, range=Optional[str])

slots.requiredClass__full_name = Slot(uri=CAM.full_name, name="requiredClass__full_name", curie=CAM.curie('full_name'),
                   model_uri=CAM.requiredClass__full_name, domain=None, range=Optional[str])

slots.requiredClass__aliases = Slot(uri=CAM.aliases, name="requiredClass__aliases", curie=CAM.curie('aliases'),
                   model_uri=CAM.requiredClass__aliases, domain=None, range=Optional[str])

slots.requiredClass__phone = Slot(uri=CAM.phone, name="requiredClass__phone", curie=CAM.curie('phone'),
                   model_uri=CAM.requiredClass__phone, domain=None, range=Optional[str])

slots.requiredClass__age = Slot(uri=CAM.age, name="requiredClass__age", curie=CAM.curie('age'),
                   model_uri=CAM.requiredClass__age, domain=None, range=Optional[str])
