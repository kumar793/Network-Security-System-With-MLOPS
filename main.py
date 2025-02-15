from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

import sys

if __name__ == "__main__":
    try:
        trainingPipelineConfig = TrainingPipelineConfig() 
        dataIngestionConfig = DataIngestionConfig(trainingPipelineConfig)
        dataingestion = DataIngestion(dataIngestionConfig)
        dataingestionartifact = dataingestion.initiate_data_ingestion()
        print(dataingestionartifact)
    except Exception as e:
        logging.info("")
        raise NetworkSecurityException(e,sys)
