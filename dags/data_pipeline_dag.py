import logging
import sys
import datetime

from airflow.decorators import dag, task

from libs.si_stock_scrapper import si_web_scrapper

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

    scrape_br_stocks()


data_pipeline_dag = data_pipeline_dag()
