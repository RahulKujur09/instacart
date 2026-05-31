from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("test")
    .master("local[*]")
    .getOrCreate()
)

print("Spark Version", spark.version)

df = spark.createDataFrame(
    [
        (1, "Rahul"),
        (2, "Spark")
    ],
    ["id", "name"]
)

df.show()

df.write.mode("overwrite").parquet("test_output")

print("PARQUET WRITE SUCCESS")

spark.stop()