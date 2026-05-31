import os, sys

import os, sys

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.dirname(
                os.path.abspath(__file__)
            )
        )
    )
)

from src.exception import CustomException
from src.logger import logging

from src.utils.spark_utils import create_spark_session
from src.ingestion.ingest_orders import OrdersIngestion
from src.validation.schema_validation import validate_columns

from src.validation.null_validation import (
    get_null_counts,
    get_duplicate_count
)

from src.monitoring.pipeline_logger import PipelineLogger
from src.utils.file_utils import write_parquet
from constants.schema import EXPECTED_ORDER_COLUMNS
from constants.path import BRONZE_DIR, RAW_DIR

def run_orders_pipeline():
    job_name = "orders_bronze_pipeline"

    try:
        PipelineLogger.log_start(job_name)
        spark = create_spark_session()
        orders = OrdersIngestion(spark)
        input_path = f"{RAW_DIR}/orders.csv"

        df = orders.ingest(input_path)

        validate_columns(df, EXPECTED_ORDER_COLUMNS)

        null_df = get_null_counts(df)

        duplicate_df = get_duplicate_count(df)

        null_df.show()

        print(
            f"Duplicate Count: {duplicate_df}"
        )

        output_path = f"{BRONZE_DIR}/orders"

        write_parquet(df, output_path)

        PipelineLogger.log_end(job_name)

        spark.stop()
    except Exception as e:
        PipelineLogger.log_failure(job_name, str(e))
        raise CustomException(e, sys)
    

if __name__ == "__main__":
    run_orders_pipeline()