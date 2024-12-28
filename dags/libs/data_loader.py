import os
import logging

import pandas as pd
from sqlalchemy import create_engine

from libs.utils.commons import get_minio_client
from libs.utils.dataframes_dtypes import retrieve_dtype

LOGGER = logging.getLogger(__name__)


def json_data_loader(file_name: str, stock_key: str):
    market_mapping = {"brazilian_stocks": "BR", "us_stocks": "US"}
    dtypes = retrieve_dtype(stock_key)
    df = pd.read_json(file_name, dtype=dtypes)
    df["market"] = market_mapping[stock_key]

    os.remove(file_name)
    return df


def load_data_into_db(df: pd.DataFrame, stock_key: str):
    conn_string = f"postgresql://admin:admin@host.docker.internal:5433/analytics"

    db = create_engine(conn_string)
    conn = db.connect()

    df.to_sql(stock_key, schema="raw_layer", con=conn, if_exists="replace", index=False)

    conn.close()


def get_data_from_bucket(bucket: str, object_path: str, file_name: str):
    minio_client = get_minio_client()
    # Download the file
    minio_client.download_file(bucket, object_path, file_name)


def data_loader(execution_date: str, stock_key: str):
    file_name = f"{stock_key}_data.json"
    object_path = f"si_stocks/{execution_date}/{file_name}"
    get_data_from_bucket("raw-data", object_path, file_name)
    df = json_data_loader(file_name, stock_key)
    load_data_into_db(df, stock_key)
