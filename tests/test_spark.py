from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("Instacart Test")
    .master("local[*]")
    .getOrCreate()
)

print("Spark Version", spark.version)

df = spark.createDataFrame(
    [(1,"Rahul"), (2, "Spark")],
    ["id", "name"]
)

df.show()

spark.stop()