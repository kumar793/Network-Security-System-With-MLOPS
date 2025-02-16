from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.entity.config_entity import DataIngestionConfig,DataValidationConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.components.data_validation import DataValidation
from networksecurity.logging.logger import logging

import sys

if __name__ == "__main__":
    try:
        trainingPipelineConfig = TrainingPipelineConfig() 
        dataIngestionConfig = DataIngestionConfig(trainingPipelineConfig)
        dataingestion = DataIngestion(dataIngestionConfig)
        dataingestionartifact = dataingestion.initiate_data_ingestion()
        logging.info("Data Ingestion completed")
        data_validation_config = DataValidationConfig(trainingPipelineConfig)
        datavalidation = DataValidation(dataingestionartifact,data_validation_config)
        dataValidationArtifact = datavalidation.initiate_data_validation()
        logging.info("Data Validation completed.")
        print(dataValidationArtifact)
    except Exception as e:
        logging.info("")
        raise NetworkSecurityException(e,sys)
