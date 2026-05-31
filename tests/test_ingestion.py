import sys, os
sys.path.append(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)
from src.utils.spark_utils import create_spark_session
from src.ingestion.ingest_orders import OrdersIngestion

spark = create_spark_session()

orders = OrdersIngestion(spark)

df = orders.ingest("data/raw/orders.csv")

df.printSchema()

df.show(5)

spark.stop()