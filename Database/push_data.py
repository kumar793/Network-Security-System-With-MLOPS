import os
import sys
import json
from dotenv import load_dotenv
import certifi
import pandas as pd
import numpy as np
import pymongo
from networksecurity.logging.logger import logging
from networksecurity.exception.exception import NetworkSecurityException
load_dotenv()

MONGO_DB_URL = os.getenv("MONGGO_DB_URI")
ca = certifi.where()

class NetworkDataExtract:
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def csv_to_json_converter(self, file_path):
        try:
            self.__data = pd.read_csv(file_path)
            logging.info("data received")
            self.__data.reset_index(drop = True, inplace = True)
            #converting into json 
            self.__records = list(json.loads(self.__data.T.to_json()).values())
            logging.info("created the records in JSon format")
            return self.__records
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def insert_data_mongodb(self,records,database,collection):
        try:
            self.database = database
            self.collection = collection
            self.records = records
            logging.info("data received")
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)
            logging.info("Connected to database")
            self.database = self.mongo_client[self.database]
            self.collection = self.database[self.collection]
            logging.info("collection initaited")
            self.collection.insert_many(self.records)
            logging.info("records uploaded to mongodb")
            return len(self.records)
        except Exception as e:
            raise NetworkSecurityException(e,sys)

if __name__ == "__main__":
    FILE_PATH = "/workspaces/Network-Security-System-With-MLOPS/Network_Data/phisingData.csv"
    DATABASE = "Network-kumar"
    Collection = "Network data"
    networkobj = NetworkDataExtract()
    records = networkobj.csv_to_json_converter(file_path=FILE_PATH)
    no_of_records = networkobj.insert_data_mongodb(records,DATABASE,Collection)
    print(no_of_records)