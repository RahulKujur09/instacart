import os

PROJECT_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

DATA_DIR = os.path.join(PROJECT_DIR, "data")

RAW_DIR = os.path.join(DATA_DIR, "raw")
BRONZE_DIR = os.path.join(DATA_DIR, "bronze")
SILVER_DIR = os.path.join(DATA_DIR, "silver")
GOLD_DIR = os.path.join(DATA_DIR, "gold")

CONFIG_DIR = os.path.join(PROJECT_DIR, "configs")
ARTIFACT_DIR = os.path.join(PROJECT_DIR, "artifacts")

METADATA_DIR = ARTIFACT_DIR

WATERMARK_FILE = os.path.join(
    METADATA_DIR,
    "watermark.json"
)