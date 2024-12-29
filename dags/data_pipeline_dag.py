import logging
import sys
import datetime

from airflow.decorators import dag, task
from airflow.operators.bash_operator import BashOperator

from libs.si_stock_scrapper import si_web_scrapper
from libs.data_loader import data_loader

log = logging.getLogger(__name__)


PATH_TO_PYTHON_BINARY = sys.executable


@dag(
    schedule_interval=None,
    start_date=datetime.datetime(2024, 12, 1),
    catchup=False,
)
def data_pipeline_dag():

    @task(task_id="scrape_br_stocks")
    def scrape_br_stocks(ds=None, **kwargs):
        si_web_scrapper(ds, "brazilian_stocks")

    @task(task_id="scrape_us_stocks")
    def scrape_us_stocks(ds=None, **kwargs):
        si_web_scrapper(ds, "us_stocks")

    @task(task_id="load_br_stocks")
    def load_br_stocks(ds=None, **kwargs):
        data_loader(ds, "brazilian_stocks")

    @task(task_id="load_us_stocks")
    def load_us_stocks(ds=None, **kwargs):
        data_loader(ds, "us_stocks")
    
    run_dbt_seed = BashOperator(
        task_id='run_dbt_seed',
        bash_command='cd /opt/airflow/dags; dbt seed --profiles-dir /opt/airflow/dags',
    )
    
    run_dbt_model = BashOperator(
        task_id='run_dbt_model',
        bash_command='cd /opt/airflow/dags; dbt run --profiles-dir /opt/airflow/dags',
    )

    scrape_br_stocks() >> load_br_stocks() >> run_dbt_seed >> run_dbt_model
    scrape_us_stocks() >> load_us_stocks() >> run_dbt_seed >> run_dbt_model


data_pipeline_dag = data_pipeline_dag()
