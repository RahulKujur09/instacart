import os, sys
sys.path.append(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)
from src.utils.spark_utils import create_spark_session

from src.validation.schema_validation import (
    validate_columns
)

from src.validation.null_validation import (
    get_null_counts,
    get_duplicate_count
)

from src.ingestion.ingest_orders import OrdersIngestion

from constants.schema import EXPECTED_ORDER_COLUMNS



spark = create_spark_session()
orders = OrdersIngestion(spark)

df = orders.ingest("D:/instacart_market_busket_analysis/data/raw/orders.csv")

schame_valid = validate_columns(df, EXPECTED_ORDER_COLUMNS)

print("Schema Valid:", schame_valid)

null_df = get_null_counts(df)

duplicate_count = get_duplicate_count(df)

null_df.show()
print("Duplicated Count:", duplicate_count)

spark.stop()