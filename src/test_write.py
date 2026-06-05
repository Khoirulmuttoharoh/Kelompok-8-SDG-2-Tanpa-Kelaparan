from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .master("local[1]")
    .appName("Test")
    .getOrCreate()
)

data = [("A", 1), ("B", 2)]

df = spark.createDataFrame(data, ["nama", "nilai"])

print("Jumlah baris:", df.count())

df.show()

spark.stop()

print("SELESAI")