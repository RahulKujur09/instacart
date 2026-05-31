import os, sys
import shutil

from src.logger import logging
from src.exception import CustomException

def create_directory(path:str):
    try:
        os.makedirs(path, exist_ok=True)
        logging.info(f"Directory created: {path}")
    except Exception as e:
        raise CustomException(e, sys)
    
def file_exists(path: str):
    try:
        return os.path.exists(path)
    except Exception as e:
        raise CustomException(e, sys)

def list_files(path:str):
    try:
        files = [
            os.path.join(path, file)
            for file in os.listdir(path)
        ]

        logging.info(f"Found {len(files)} files in {path}")

        return files
    except Exception as e:
        raise CustomException(e, sys)
    
def move_file(source:str, destination:str):
    try:
        shutil.move(source, destination)

        logging.info(f"Moved file from {source} to {destination}")
    except Exception as e:
        raise CustomException(e, sys)

def delete_file(path:str):
    try:
        if os.path.exists(path):
            os.remove(path)

            logging.info(f"Deleted file: {path}")
    except Exception as e:
        raise CustomException(e, sys)
    
def write_parquet(df, output_path, mode="overwrite"):
    try:
        if mode == "overwrite" and os.path.exists(output_path):
            shutil.rmtree(output_path)

        logging.info(
            f"Writing dataframe to parquet: {output_path}"
        )

        df.write.mode(mode).parquet(output_path)

        logging.info(
            f"Successfully written parquet: {output_path}"
        )

    except Exception as e:
        logging.error(str(e))
        raise CustomException(e, sys)