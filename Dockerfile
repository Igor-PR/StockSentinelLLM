FROM apache/airflow:2.3.0
COPY airflow_requirements/requirements.txt /
RUN pip install --no-cache-dir "apache-airflow==2.3.0" -r /requirements.txt
