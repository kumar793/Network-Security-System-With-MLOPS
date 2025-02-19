# Network-Security-System-With-MLOPS

## Overview

This project implements a Network Security System with MLOPS (Machine Learning Operations) principles. It focuses on building a robust and scalable system for network security threat detection using machine learning and automated pipelines.

## Project Structure

The project is organized into the following directories:

- `.github/`: Includes GitHub workflow configurations.
- `.vscode/`: Contains VSCode specific settings for the project.
- `data_schema/`: Defines the schema for the input data, including `schema.yaml`.
- `Database/`: Contains scripts and configurations related to database operations, including:
    - `__init__.py`: Initialization file for the database package.
    - `demo.py`: Example database interactions.
    - `ETL pipeline.py`: Scripts for Extract, Transform, Load data into the database.
    - `test_mongodb.py`: Test scripts for MongoDB database.
- `Network_Data/`: Stores network data, such as `phisingData.csv`.
- `networksecurity/`: Contains the core network security application code, structured into sub-packages:
    - `cloud/`: Cloud-related functionalities, like `s3_Syncer.py` for S3 synchronization.
    - `components/`: Individual components of the MLOPS pipeline:
        - `data_ingestion.py`: For data intake.
        - `data_transformation.py`: For data preprocessing.
        - `data_validation.py`: For data quality checks.
        - `model_trainer.py`: For training machine learning models.
    - `constants/`: Defines constant values used throughout the project, especially for training pipelines.
    - `entity/`: Defines data entities and structures, including configurations and artifacts.
    - `exception/`: Custom exception handling.
    - `logging/`: Logging configurations and utilities.
    - `pipeline/`: Defines the MLOPS pipelines, such as `training_pipeline.py` and `batch_prediction.py`.
    - `utils/`: Utility modules, including:
        - `main_utils/`: General utility functions.
        - `ml_utils/`: Machine learning specific utilities, including metrics and model handling.
- `predicted data/`: Location for storing model predictions, e.g., `output.csv`.
- `templates/`: HTML templates, e.g., `table.html`.
- `valid_data/`: Contains validated data, e.g., `test.csv`.
- `app.py`: Main application entry point, likely for running the system.
- `Dockerfile`: Docker configuration for containerizing the application.
- `README.md`: Project documentation (this file).
- `requirements.txt`: Lists Python dependencies.
- `setup.py`: Script for installing the project as a Python package.
- `.gitignore`: Specifies intentionally untracked files that Git should ignore.

Docker Setup In EC2 commands to be Executed
#optinal

sudo apt-get update -y

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker

the setup github runner.

## Setup and Run

To set up and run the project, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone <repository_url>
   cd Network-Security-System-With-MLOPS-main
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Linux/macOS
   venv\Scripts\activate  # On Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install the project (editable mode recommended):**
   ```bash
   pip install -e .
   ```

5. **Run the application:**
   ```bash
   python app.py
   ```

   Refer to the `app.py` or project documentation for specific run configurations and available options.

## Data Sources

The project utilizes network data, potentially including phishing datasets, as indicated by `Network_Data/phisingData.csv`. Ensure that the data is properly placed in the `Network_Data/` directory or configure the data paths as needed in the project's configuration files.

## MLOPS Pipeline

The MLOPS pipeline is implemented within the `networksecurity/pipeline/` and `networksecurity/components/` directories. It includes stages for:

- **Data Ingestion**: Fetching and loading data (`data_ingestion.py`).
- **Data Validation**: Ensuring data quality and integrity (`data_validation.py`).
- **Data Transformation**: Preprocessing and feature engineering (`data_transformation.py`).
- **Model Training**: Training machine learning models for network security threat detection (`model_trainer.py`).

The pipeline orchestrations are defined in `networksecurity/pipeline/training_pipeline.py` and potentially `batch_prediction.py` for batch predictions.


