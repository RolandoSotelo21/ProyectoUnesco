
from src.config import (
    RAW_DATA_PATH,
    PROCESSED_DATA_DIR,
    CLEAN_DATA_PATH,
    SQL_READY_PATH,
    REQUIRED_COLUMNS
)

from src.load_data import load_dataset

from src.clean_data import clean_dataset

from src.feature_engineering import create_features

from src.utils import (
    print_null_report,
    check_duplicates
)


def validate_columns(df):

    missing = [

        col for col in REQUIRED_COLUMNS

        if col not in df.columns

    ]

    if missing:

        raise ValueError(

            f"Missing columns: {missing}"

        )


def main():

    print("\n=== UNESCO Journalist Analysis Pipeline ===\n")


    # Create processed folder
    PROCESSED_DATA_DIR.mkdir(

        parents=True,

        exist_ok=True
    )


    # Load
    df = load_dataset(RAW_DATA_PATH)


    # Validate schema
    print("[INFO] Validating columns...")

    validate_columns(df)

    print("[SUCCESS] Schema validated")


    # Initial quality report
    print_null_report(df)

    check_duplicates(df)


    # Cleaning
    df = clean_dataset(df)


    # Feature engineering
    df = create_features(df)

    print("\n[FINAL COLUMNS]")

    print(df.columns.tolist())

    print(f"\nFinal shape: {df.shape}")


    # Save cleaned version
    df.to_csv(

        CLEAN_DATA_PATH,

        index=False
    )


    # SQL ready version
    df.to_csv(

        SQL_READY_PATH,

        index=False
    )


    print(

        f"\n[SUCCESS] Files saved in: {PROCESSED_DATA_DIR}"

    )


if __name__ == "__main__":

    main()