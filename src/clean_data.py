
import pandas as pd

from src.config import DROP_COLUMNS


def clean_dataset(df):

    print("[INFO] Cleaning dataset...")


    # Drop unnecessary columns
    df.drop(

        columns=DROP_COLUMNS,

        inplace=True,

        errors="ignore"

    )


    # Fill missing enquiry status
    if "Enquiry status" in df.columns:

        df["Enquiry status"] = df[
            "Enquiry status"
        ].fillna("Unknown")


    # Convert date columns safely
    if "Date" in df.columns:

        df["Date"] = pd.to_datetime(

            df["Date"],

            errors="coerce"
        )


    if "Date resolution" in df.columns:

        df["Date resolution"] = pd.to_datetime(

            df["Date resolution"],

            errors="coerce"
        )


    # Remove duplicate rows
    df.drop_duplicates(inplace=True)


    print(f"[SUCCESS] Clean dataset: {df.shape}")

    return df