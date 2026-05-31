import os
import sys

sys.path.append(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)

from src.monitoring.pipeline_logger import PipelineLogger


PipelineLogger.log_start("orders_ingestion")

try:
    x = 10 / 2
except Exception as e:
    PipelineLogger.log_failure(
        "orders_ingestion",
        str(e)
    )

PipelineLogger.log_end("orders_ingestion")