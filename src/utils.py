# src/utils.py

import pandas as pd


def print_null_report(df):

    print("\n[NULL REPORT]")

    nulls = df.isnull().sum()

    percentage = round(
        df.isnull().mean() * 100,
        2
    )

    report = pd.DataFrame({

        "missing_values": nulls,
        "missing_percentage": percentage

    })

    print(
        report.sort_values(
            "missing_percentage",
            ascending=False
        )
    )


def check_duplicates(df):

    duplicates = df.duplicated().sum()

    print(f"\n[DUPLICATES] {duplicates}")

    return duplicates