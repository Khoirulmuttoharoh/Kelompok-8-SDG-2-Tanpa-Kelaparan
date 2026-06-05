import os

import pandas as pd
from deltalake import DeltaTable, write_deltalake


BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

SILVER_PATH = os.path.join(
    BASE_DIR,
    "lakehouse",
    "silver",
    "food_loss"
)

GOLD_DIR = os.path.join(
    BASE_DIR,
    "lakehouse",
    "gold"
)

CSV_DIR = os.path.join(
    BASE_DIR,
    "lakehouse",
    "gold",
    "csv"
)


def save_delta(df, table_name):
    path = os.path.join(GOLD_DIR, table_name)
    os.makedirs(path, exist_ok=True)
    write_deltalake(path, df, mode="overwrite")
    print(f"  {table_name} ({len(df):,} baris)")


def save_csv(df, filename):
    path = os.path.join(CSV_DIR, filename)
    df.to_csv(path, index=False)
    print(f"  {filename} ({len(df):,} baris)")


def run_gold():

    print("=" * 60)
    print("GOLD LAYER - FOOD LOSS")
    print("=" * 60)

    print("\n[1] Membaca Silver Delta...")

    df = DeltaTable(
        SILVER_PATH
    ).to_pandas()

    print(f"Baris Silver : {len(df):,}")

    print("\n[2] Membuat Ringkasan Analitik...")

    # food_loss_by_country
    by_country = (
        df.groupby("country")["loss_percentage"]
        .mean()
        .reset_index()
        .rename(columns={"loss_percentage": "avg_loss_percentage"})
        .sort_values("avg_loss_percentage", ascending=False)
    )

    # food_loss_by_region
    region_col = next(
        (c for c in df.columns if "region" in c.lower()),
        None
    )
    if region_col:
        by_region = (
            df.groupby(region_col)["loss_percentage"]
            .mean()
            .reset_index()
            .rename(columns={
                region_col: "region",
                "loss_percentage": "avg_loss_percentage"
            })
            .sort_values("avg_loss_percentage", ascending=False)
        )
    else:
        by_region = pd.DataFrame(
            columns=["region", "avg_loss_percentage"]
        )
        print("  [WARN] Kolom region tidak ditemukan.")

    # food_loss_by_commodity
    by_commodity = (
        df.groupby("commodity")["loss_percentage"]
        .mean()
        .reset_index()
        .rename(columns={"loss_percentage": "avg_loss_percentage"})
        .sort_values("avg_loss_percentage", ascending=False)
    )

    # food_loss_by_stage
    by_stage = (
        df.groupby("food_supply_stage")["loss_percentage"]
        .mean()
        .reset_index()
        .rename(columns={"loss_percentage": "avg_loss_percentage"})
        .sort_values("avg_loss_percentage", ascending=False)
    )

    # food_loss_by_cause
    cause_col = next(
        (c for c in df.columns if "cause" in c.lower()),
        None
    )
    if cause_col:
        by_cause = (
            df.dropna(subset=[cause_col])
            .groupby(cause_col)["loss_percentage"]
            .mean()
            .reset_index()
            .rename(columns={
                cause_col: "cause_of_loss",
                "loss_percentage": "avg_loss_percentage"
            })
            .sort_values("avg_loss_percentage", ascending=False)
        )
    else:
        by_cause = pd.DataFrame(
            columns=["cause_of_loss", "avg_loss_percentage"]
        )
        print("  [WARN] Kolom cause tidak ditemukan.")

    # food_loss_trend
    by_trend = (
        df.groupby("year")["loss_percentage"]
        .mean()
        .reset_index()
        .rename(columns={"loss_percentage": "avg_loss_percentage"})
        .sort_values("year")
    )

    print("\n[3] Menyimpan Gold Delta...")

    save_delta(by_country,   "food_loss_by_country")
    save_delta(by_region,    "food_loss_by_region")
    save_delta(by_commodity, "food_loss_by_commodity")
    save_delta(by_stage,     "food_loss_by_stage")
    save_delta(by_cause,     "food_loss_by_cause")
    save_delta(by_trend,     "food_loss_trend")

    print("\n[4] Export ke CSV...")

    os.makedirs(CSV_DIR, exist_ok=True)

    save_csv(by_country,   "food_loss_by_country.csv")
    save_csv(by_region,    "food_loss_by_region.csv")
    save_csv(by_commodity, "food_loss_by_commodity.csv")
    save_csv(by_stage,     "food_loss_by_stage.csv")
    save_csv(by_cause,     "food_loss_by_cause.csv")
    save_csv(by_trend,     "food_loss_trend.csv")

    print("\n[SUCCESS]")
    print(f"Delta : {GOLD_DIR}")
    print(f"CSV   : {CSV_DIR}")


if __name__ == "__main__":
    run_gold()
