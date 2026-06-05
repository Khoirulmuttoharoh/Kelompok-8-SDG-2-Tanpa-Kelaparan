from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Read Food Loss") \
    .master("local[*]") \
    .getOrCreate()

print("=" * 60)
print("MEMBACA DATASET FAO FOOD LOSS")
print("=" * 60)

df = spark.read \
    .option("header", True) \
    .option("inferSchema", True) \
    .option("quote", '"') \
    .option("escape", '"') \
    .csv("data/food_loss.csv")

print(f"\nJumlah Baris : {df.count():,}")
print(f"Jumlah Kolom : {len(df.columns)}")

print("\nDAFTAR KOLOM:")
for i, col in enumerate(df.columns, start=1):
    print(f"{i}. {col}")

print("\n5 BARIS PERTAMA:")
df.show(5, truncate=False)

spark.stop()