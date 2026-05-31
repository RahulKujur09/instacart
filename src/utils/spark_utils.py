from pyspark.sql import SparkSession
from constants.constant import (
    APP_NAME,
    MASTER,
    DEFAULT_SHUFFLE_PARTITIONS
)

def create_spark_session():
    spark = (
        SparkSession.builder.appName(APP_NAME).master(MASTER).config(
            "spark.sql.shuffle.partitions",
            DEFAULT_SHUFFLE_PARTITIONS
        ).getOrCreate()
    )

    return spark