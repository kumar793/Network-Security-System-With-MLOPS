import os
import sys
import numpy as np 
import pandas as pd


"""
Defining common constant for training
"""
TARGET_COLUMN = "Result"
PIPELINE_NAME:str = "NetworkSecurity"
ARTIFACT_DIR:str = "Artifacts"
FILE_NAME:str = "phishingData.csv"
TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"

"""
Database  related constants
"""

DATA_INGESTION_COLLECTION_NAME:str= "Network data"
DATA_INGESTION_DATABASE_NAME:str = "Network-kumar"
DATA_INGESTION_DIR_NAME:str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR:str = "feature_store"
DATA_INGESTION_INGESTED_DIR:str = "ingested"
DATA_INGESTION_TARIN_TEST_SPLIT_RATION:float = 0.2