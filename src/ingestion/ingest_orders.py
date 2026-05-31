import sys
from src.ingestion.base_ingestion import BaseIngestion
from src.exception import CustomException
from src.logger import logging

class OrdersIngestion(BaseIngestion):
    def ingest(self, file_path):
        try:
            logging.info("Starting Orders ingestion")

            df = self.read_csv(file_path)

            logging.info(f"Orders datafrme loaded with {df.count()} rows")

            return df
        except Exception as e:
            raise CustomException(e, sys)