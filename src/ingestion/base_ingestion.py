import os, sys

from src.exception import CustomException

class BaseIngestion:
    def __init__(self, spark):
        self.spark = spark
    
    def read_csv(
            self,
            file_path : str,
            header : bool = True,
            infer_schema : bool = True
    ):
        try:
            df = self.spark.read.option("header", header).option("inferSchema", infer_schema).csv(file_path)

            return df
        except Exception as e:
            raise CustomException(e, sys)