
from pathlib import Path


# Root project folder
BASE_DIR = Path(__file__).resolve().parent.parent


# Data folders
RAW_DATA_PATH = BASE_DIR / "data" / "raw" / "unesco_journalists.csv"

PROCESSED_DATA_DIR = BASE_DIR / "data" / "processed"

CLEAN_DATA_PATH = PROCESSED_DATA_DIR / "cleaned_unesco.csv"

SQL_READY_PATH = PROCESSED_DATA_DIR / "sql_ready.csv"


# Columns expected in dataset
REQUIRED_COLUMNS = [

    "ID",
    "Countries",
    "Date",
    "Gender",
    "Enquiry status",
    "Staff",
    "Local",
    "Conflict Zone",
    "Media",
    "Date resolution",
    "state_response",
    "country_Regional Group"

]


# Columns to drop
DROP_COLUMNS = [

    # Empty/useless columns
    "Language",
    "Area coverage",
    "main_image",

    # CMS metadata
    "Created At",
    "Updated At",
    "Published At",
    "UUID",
    "Document Id",
    "strapi_stage",
    "strapi_assignee",

    # Descriptions
    "description_en",
    "description_es",
    "description_fr",

    # Geographic heavy columns
    "Country UUID",
    "country_Geometry",
    "Geo Shape",

    # Redundant judicial columns
    "Enquiry status home",
    "Enquiry status stat",
    "Enquiry status min"
]