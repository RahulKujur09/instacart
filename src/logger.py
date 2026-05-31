import os, sys
import logging
from datetime import datetime

# Project root
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Log directory
LOG_DIR = os.path.join(PROJECT_ROOT, "logs")

# Create timestamp folder
CURRENT_DATE = datetime.now().strftime("%y-%m-%d")

LOG_FOLDER = os.path.join(LOG_DIR, CURRENT_DATE)

os.makedirs(LOG_FOLDER, exist_ok=True)

# Log file name
LOG_FILE = f"{datetime.now().strftime('%H-%M-%S')}.log"

LOG_FILE_PATH = os.path.join(LOG_FOLDER, LOG_FILE)

# Configuring Logging

logging.basicConfig(
    filename = LOG_FILE_PATH,
    format= "[ %(asctime)s ] %(levelname)s | %(name)s | %(message)s",
    level=logging.INFO
)

# Console Logging
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(
    logging.Formatter(
        '[ %(asctime)s ] %(levelname)s | %(name)s | %(message)s'
    )
)

logging.getLogger().addHandler(console_handler)