from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.artifact_entity import DataIngestionArtifact
import os
import sys
import numpy as np
import pymongo
from typing import List
import pandas as pd 
from sklearn.model_selection import train_test_split

from dotenv import load_dotenv
load_dotenv()
MONGO_DB_URL = os.getenv("MONGGO_DB_URI")

class DataIngestion:
    def __init__(self,data_ingestion_config:DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            logging.info("Exception occurred",e)
            raise NetworkSecurityException(e,sys)
        
    def export_collection_as_dataframe(self):
        try:
            logging.info("getting data from mongodb")
            database_name = self.data_ingestion_config.database_name
            collection_name = self.data_ingestion_config.collection_name
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)
            collection = self.mongo_client[database_name][collection_name]
            logging.info("Getting data from the Mongodb")
        
            df = pd.DataFrame(list(collection.find()))
            if "_id" in df.columns.to_list():
                df = df.drop(columns = ["_id"],axis = 1)
            df.replace({"na":np.nan},inplace = True)
            logging.info("Exported data as Dataframe")
            return df

        except Exception as e:
            logging.info("Exception",e)
            raise NetworkSecurityException(e,sys)
        
    def export_data_into_feature_store(self, dataframe:pd.DataFrame):
        try:
            feature_store_file_path = self.data_ingestion_config.feature_store_file_path
            logging.info("creating feature store in local")
            dir_path = os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path,exist_ok=True)
            dataframe.to_csv(feature_store_file_path,index=False,header=True)
            logging.info("Raw data added to the feature store as CSV")
            return dataframe
        except Exception as e:
            logging.info("Exception",e)
            raise NetworkSecurityException(e,sys)
        
    def split_data_as_train_test(self,dataframe:pd.DataFrame):
        try:
            train_set,test_set = train_test_split(dataframe,test_size=
                                                self.data_ingestion_config.train_test_split_ratio)
            logging.info("The data was split into train and test ")
            logging.info("exited from split_data_as_train_test methof from dataingestion class")

            dir_path = os.path.dirname(self.data_ingestion_config.training_file_path)
            os.makedirs(dir_path,exist_ok=True)

            logging.info("Exported train and test to file path")

            train_set.to_csv(
                self.data_ingestion_config.training_file_path,index = False,header = True
            )
            test_set.to_csv(
                self.data_ingestion_config.testing_file_path,index = False, header = True
            )
            logging.info("Ingested with the train and test data")
        
        except Exception as e:
            logging.info("Exception",e)
            raise NetworkSecurityException(e,sys)

    def initiate_data_ingestion(self):
        try:
            dataframe = self.export_collection_as_dataframe()
            dataframe = self.export_data_into_feature_store(dataframe)
            self.split_data_as_train_test(dataframe)
            DataIngestion_Artifact = DataIngestionArtifact(trained_file_path = self.data_ingestion_config.training_file_path,
                                                          test_file_path = self.data_ingestion_config.testing_file_path)
            
            logging.info("Data set was loaded to the project")
            return DataIngestion_Artifact
            
            
        except Exception as e:
            logging.info("Exception",e)
            raise NetworkSecurityException(e,sys)
            
