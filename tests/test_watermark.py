import os, sys
sys.path.append(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

from src.metadata.watermark_manager import (
    get_watermark,
    update_watermark
)

print(
    "Before",
    get_watermark()
)

update_watermark(
    "orders.csv"
)

print(
    "After",
    get_watermark()
)