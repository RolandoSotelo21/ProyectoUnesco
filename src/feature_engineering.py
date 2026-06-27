
import pandas as pd
import numpy as np


def classify_case(status):

    if status == "Resolved":

        return "Resolved"

    elif status == "Unknown":

        return "Unknown"

    else:

        return "Unresolved"


def government_response_flag(value):

    if pd.isna(value):

        return 0

    if str(value).strip() == "[]":

        return 0

    return 1


def create_features(df):

    print("[INFO] Creating engineered features...")


    # year
    if "year" not in df.columns:

        df["year"] = df["Date"].dt.year


    # month
    if "month" not in df.columns:

        df["month"] = df["Date"].dt.month


    # case category
    df["case_category"] = df[
        "Enquiry status"
    ].apply(classify_case)


    # resolved
    if "resolved" not in df.columns:

        df["resolved"] = np.where(

            df["case_category"] == "Resolved",

            1,

            0
        )


    # impunity
    if "impunity" not in df.columns:

        df["impunity"] = np.where(

            df["resolved"] == 1,

            0,

            1
        )


    # government response
    df["government_responded"] = df[
        "state_response"
    ].apply(government_response_flag)


    # primary region
    df["primary_region"] = df[
        "country_Regional Group"
    ].astype(str).str.split(",").str[0]


    # resolution days
    if "resolution_days" not in df.columns:

        df["resolution_days"] = (

            df["Date resolution"]

            - df["Date"]

        ).dt.days


    print("[SUCCESS] Features created")

    return df