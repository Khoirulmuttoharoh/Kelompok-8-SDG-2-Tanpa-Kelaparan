import os

import pandas as pd
from deltalake import DeltaTable, write_deltalake


BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

BRONZE_PATH = os.path.join(
    BASE_DIR,
    "lakehouse",
    "bronze",
    "food_loss"
)

SILVER_PATH = os.path.join(
    BASE_DIR,
    "lakehouse",
    "silver",
    "food_loss"
)

PARQUET_PATH = os.path.join(
    BASE_DIR,
    "lakehouse",
    "silver",
    "silver_food_loss.parquet"
)


def run_silver():

    print("=" * 60)
    print("SILVER LAYER - FOOD LOSS")
    print("=" * 60)

    os.makedirs(SILVER_PATH, exist_ok=True)
    os.makedirs(os.path.dirname(PARQUET_PATH), exist_ok=True)

    print("\n[1] Membaca Bronze Delta...")

    df = DeltaTable(
        BRONZE_PATH
    ).to_pandas()

    print(f"Baris Bronze : {len(df):,}")

    print("\n[2] Data Cleaning...")

    # Hapus duplikat
    before = len(df)
    df = df.drop_duplicates()
    print(f"  Duplikat dihapus     : {before - len(df):,}")

    # Hapus missing values pada kolom wajib
    before = len(df)
    df = df.dropna(
        subset=[
            "country",
            "commodity",
            "year",
            "loss_percentage"
        ]
    )
    print(f"  Missing values hapus : {before - len(df):,}")

    # Validasi nilai loss_percentage (harus 0–100)
    before = len(df)
    df = df[
        (df["loss_percentage"] >= 0) &
        (df["loss_percentage"] <= 100)
    ]
    print(f"  Nilai tidak valid    : {before - len(df):,}")

    # Standarisasi kolom string
    str_cols = [
        "country",
        "commodity",
        "food_supply_stage",
        "cause_of_loss"
    ]

    for col in str_cols:
        if col in df.columns:
            df[col] = (
                df[col]
                .astype(str)
                .str.strip()
                .str.title()
            )

    # Standarisasi tipe data
    df["year"] = pd.to_numeric(
        df["year"],
        errors="coerce"
    ).astype("Int64")

    df["loss_percentage"] = pd.to_numeric(
        df["loss_percentage"],
        errors="coerce"
    )

    df["_layer"] = "silver"

    print(f"\n  Baris Silver : {len(df):,}")

    print("\n[3] Menyimpan Silver Delta...")

    write_deltalake(
        SILVER_PATH,
        df,
        mode="overwrite"
    )

    print(f"  Lokasi : {SILVER_PATH}")

    print("\n[4] Export ke Parquet...")

    df.to_parquet(PARQUET_PATH, index=False)

    print(f"  silver_food_loss.parquet ({len(df):,} baris)")

    print("\n[SUCCESS]")
    print(f"Delta   : {SILVER_PATH}")
    print(f"Parquet : {PARQUET_PATH}")


if __name__ == "__main__":
    run_silver()
