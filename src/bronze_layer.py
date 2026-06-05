import os
from datetime import datetime

import pandas as pd
from deltalake import write_deltalake, DeltaTable
from pyspark.sql import functions as F

from spark_session import get_spark_session


BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

CSV_PATH = os.path.join(
    BASE_DIR,
    "data",
    "food_loss.csv"
)

BRONZE_PATH = os.path.join(
    BASE_DIR,
    "lakehouse",
    "bronze",
    "food_loss"
)

PARQUET_PATH = os.path.join(
    BASE_DIR,
    "lakehouse",
    "bronze",
    "bronze_food_loss.parquet"
)


def run_bronze():

    print("=" * 60)
    print("BRONZE LAYER - FAO FOOD LOSS")
    print("=" * 60)

    os.makedirs(BRONZE_PATH, exist_ok=True)
    os.makedirs(os.path.dirname(PARQUET_PATH), exist_ok=True)

    spark = get_spark_session(
        "FoodLossBronze"
    )

    print("\n[1] Membaca CSV...")

    df = (
        spark.read
        .option("header", True)
        .option("inferSchema", True)
        .option("quote", '"')
        .option("escape", '"')
        .csv(CSV_PATH)
    )

    print(f"Jumlah Baris : {df.count():,}")
    print(f"Jumlah Kolom : {len(df.columns)}")

    print("\n[2] Menambahkan Metadata...")

    df = (
        df
        .withColumn(
            "_ingest_timestamp",
            F.current_timestamp()
        )
        .withColumn(
            "_source_file",
            F.lit("food_loss.csv")
        )
        .withColumn(
            "_layer",
            F.lit("bronze")
        )
    )

    print("\n[3] Preview Data")

    df.select(
        "country",
        "commodity",
        "year",
        "loss_percentage",
        "food_supply_stage"
    ).show(5, truncate=False)

    print("\n[4] Menyimpan ke Delta Lake...")

    pdf = df.toPandas()

    pdf["_ingest_timestamp"] = datetime.now()

    write_deltalake(
        BRONZE_PATH,
        pdf,
        mode="overwrite"
    )

    total_delta = (
        DeltaTable(BRONZE_PATH)
        .to_pandas()
        .shape[0]
    )

    print(f"  Baris Delta : {total_delta:,}")
    print(f"  Lokasi      : {BRONZE_PATH}")

    print("\n[5] Export ke Parquet...")

    pdf.to_parquet(PARQUET_PATH, index=False)

    print(f"  bronze_food_loss.parquet ({total_delta:,} baris)")

    print("\n[SUCCESS]")
    print(f"Delta   : {BRONZE_PATH}")
    print(f"Parquet : {PARQUET_PATH}")

    spark.stop()


if __name__ == "__main__":
    run_bronze()
