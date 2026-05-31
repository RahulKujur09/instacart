import os
import sys

sys.path.append(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)

from src.monitoring.pipeline_logger import PipeLineLogger


PipeLineLogger.log_start("orders_ingestion")

try:
    x = 10 / 2
except Exception as e:
    PipeLineLogger.log_failure(
        "orders_ingestion",
        str(e)
    )

PipeLineLogger.log_end("orders_ingestion")