import os, sys
from constants.path import RAW_DIR

sys.path.append(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)

from src.utils.file_utils import (
    create_directory,
    file_exists,
    list_files
)

create_directory(RAW_DIR)
print(file_exists(RAW_DIR))
print(list_files(RAW_DIR))