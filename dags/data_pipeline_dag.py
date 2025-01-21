import logging
import sys
import datetime

from airflow.decorators import dag, task
from airflow.operators.bash_operator import BashOperator
from airflow.operators.empty import EmptyOperator

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

    start_task = EmptyOperator(task_id='start')
    end_task = EmptyOperator(task_id='end')

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
    
    run_dbt_stg = BashOperator(
        task_id='run_dbt_stg',
        bash_command='cd /opt/airflow/dags; dbt run --models staging --profiles-dir /opt/airflow/dags',
    )

    run_dbt_test_stg = BashOperator(
        task_id='run_dbt_test_stg',
        bash_command='cd /opt/airflow/dags; dbt test --models staging --profiles-dir /opt/airflow/dags',
    )
    
    run_dbt_gold = BashOperator(
        task_id='run_dbt_gold',
        bash_command='cd /opt/airflow/dags; dbt run --models stocks --profiles-dir /opt/airflow/dags',
    )

    run_dbt_test_gold = BashOperator(
        task_id='run_dbt_test_gold',
        bash_command='cd /opt/airflow/dags; dbt test --models stocks --profiles-dir /opt/airflow/dags',
    )

    scrape_br_stocks_task = scrape_br_stocks()
    scrape_us_stocks_task = scrape_us_stocks()

    start_task >> scrape_br_stocks_task
    start_task >> scrape_us_stocks_task

    scrape_br_stocks_task >> load_br_stocks() >> run_dbt_stg
    scrape_us_stocks_task >> load_us_stocks() >> run_dbt_stg

    run_dbt_stg >> run_dbt_test_stg >> run_dbt_gold >> run_dbt_test_gold >> end_task


data_pipeline_dag = data_pipeline_dag()
