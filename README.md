# StockSentinelLLM
This project demonstrates a simple end-to-end data pipeline using open source designed to scrape, process, transform, and store data. The pipeline is built with a combination of tools and technologies, including MinIO for storage, PostgreSQL for database management, dbt for data transformation, and Apache Airflow for orchestration. The entire infrastructure is containerized using Docker for ease of deployment and portability.


## Pipeline Steps

### Step 1: Data Scraping and Storage
- **Task**: Scrape data from `statusinvest.com.br` and save it as a JSON file.
- **Technology**: Custom Python script for web scraping.
- **Output**: JSON file stored in the landing zone within MinIO.

### Step 2: Data Parsing and Loading
- **Task**: Parse the JSON file using Pandas and load the data into a PostgreSQL database.
- **Technology**: Python (Pandas library).
- **Database Schema**: Data is stored in the **raw_layer schema** of PostgreSQL.

### Step 3: Data Cleaning and Transformation (Silver Layer)
- **Task**: Clean and enhance the raw data using dbt models.
- **Technology**: dbt (Data Build Tool).
- **Output**: Cleaned and enhanced data stored in the **dw_silver_layer schema** of PostgreSQL.

### Step 4: Testing Silver Layer Data
- **Task**: Run dbt tests to validate the quality and integrity of the data in the silver layer.
- **Technology**: dbt testing framework.

### Step 5: Unification and Final Transformation (Gold Layer)
- **Task**: Unify and further transform the silver layer data into a final model.
- **Technology**: dbt models.
- **Output**: Final unified data stored in the **dw_gold_layer schema** of PostgreSQL.

### Step 6: Testing Gold Layer Data
- **Task**: Run dbt tests to ensure the accuracy and quality of the gold layer data.
- **Technology**: dbt testing framework.

## Infrastructure and Orchestration

### Orchestration
- **Tool**: Apache Airflow orchestrates the pipeline steps. Each step is defined as an Airflow task, ensuring smooth execution and dependencies.

### Storage
- **Tool**: MinIO serves as the landing zone for storing scraped JSON files.

### Database
- **Tool**: PostgreSQL is used to store and manage raw, silver, and gold layer schemas.

### Transformation
- **Tool**: dbt (Data Build Tool) handles data cleaning, enhancement, unification, and testing.

### Containerization
- **Tool**: Docker is used to containerize all components for consistent and portable deployment.

## Prerequisites
- **Docker** installed on your machine.
- **Python 3.8+** installed locally for custom scripts.

## Setup Instructions
1. Install Docker
2. Install docker-compose
3. Run `docker-compose up`
4. Run Airflow:
   - Access the Airflow UI at `http://localhost:8080`.
   - Trigger the pipeline DAG.

## dbt Project Structure
- `dags`: Contains the dag definition and dbt related yml files.
- `dags/libs`: Contains the code called by the PythonOperators and its supporting functions.
- `dags/models/staging`: Contains models for cleaning and enhancing raw data.
- `dags/models/`: Contains models for unifying data into the final schema.

## Running the LLM Agent
1. Create a virtual environment for the project
   - `python -m venv .venv`
2. Activate the newly created virtual environment
   `source .venv/bin/activate`
3. Install the required dependencies
   - `pip install -r requirements.txt`
4. Install [Ollama](https://github.com/ollama/ollama) and get the `llama3-groq-tool-use` model
   - `ollama pull llama3-groq-tool-use`
5. Create a new kernel with the libraries installed in requirements.txt
   - `python -m ipykernel install --user --name=local_venv --display-name "Python (.venv)"`
6. Start jupyter lab to load the llm_agent notebook
   - `jupyter lab`
7. Select the newly created kerned named **Python (.venv)**


## License
This project is licensed under the Apache-2.0 License. See the `LICENSE` file for details.
