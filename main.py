from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.components.data_validation import DataValidation
from networksecurity.entity.config_entity import ModelTrainerConfig
from networksecurity.components.model_trainer import ModelTrainer
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
        data_transformation_config  = DataTransformationConfig(trainingPipelineConfig)
        datatransformation = DataTransformation(dataValidationArtifact,data_transformation_config)
        logging.info("data transformation started")
        dataTransoformationArtifact = datatransformation.initiate_data_transformation()
        logging.info("data transformation completed")
        modelTrainerConfig = ModelTrainerConfig(trainingPipelineConfig)
        model_trainer = ModelTrainer(modelTrainerConfig,dataTransoformationArtifact)
        modelTrainerArtifact = model_trainer.initiate_model_trainer()
        print(modelTrainerArtifact)
    except Exception as e:
        logging.info("")
        raise NetworkSecurityException(e,sys)
