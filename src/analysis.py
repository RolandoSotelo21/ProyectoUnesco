import pandas as pd


def calculate_kpis(df):

    kpis = {

        "total_cases": len(df),

        "countries_affected":
            df["Countries"].nunique(),

        "resolution_rate":
            df["resolved"].mean() * 100,

        "impunity_rate":
            df["impunity"].mean() * 100,

        "avg_resolution_days":
            df["resolution_days"].mean()

    }

    return pd.DataFrame(
        kpis.items(),
        columns=["Metric", "Value"]
    )