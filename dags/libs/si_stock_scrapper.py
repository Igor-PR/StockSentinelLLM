import os
import json
import logging
from datetime import datetime

import requests
import boto3
from botocore.client import Config
from botocore.exceptions import ClientError


URLS_TO_SCRAP = {
    "brazilian_stocks": "https://statusinvest.com.br/category/advancedsearchresultpaginated?search=%7B%22Sector%22%3A%22%22%2C%22SubSector%22%3A%22%22%2C%22Segment%22%3A%22%22%2C%22my_range%22%3A%22-20%3B100%22%2C%22forecast%22%3A%7B%22upsidedownside%22%3A%7B%22Item1%22%3Anull%2C%22Item2%22%3Anull%7D%2C%22estimatesnumber%22%3A%7B%22Item1%22%3Anull%2C%22Item2%22%3Anull%7D%2C%22revisedup%22%3Atrue%2C%22reviseddown%22%3Atrue%2C%22consensus%22%3A%5B%5D%7D%2C%22dy%22%3A%7B%22Item1%22%3Anull%2C%22Item2%22%3Anull%7D%2C%22p_l%22%3A%7B%22Item1%22%3Anull%2C%22Item2%22%3Anull%7D%2C%22peg_ratio%22%3A%7B%22Item1%22%3Anull%2C%22Item2%22%3Anull%7D%2C%22p_vp%22%3A%7B%22Item1%22%3Anull%2C%22Item2%22%3Anull%7D%2C%22p_ativo%22%3A%7B%22Item1%22%3Anull%2C%22Item2%22%3Anull%7D%2C%22margembruta%22%3A%7B%22Item1%22%3Anull%2C%22Item2%22%3Anull%7D%2C%22margemebit%22%3A%7B%22Item1%22%3Anull%2C%22Item2%22%3Anull%7D%2C%22margemliquida%22%3A%7B%22Item1%22%3Anull%2C%22Item2%22%3Anull%7D%2C%22p_ebit%22%3A%7B%22Item1%22%3Anull%2C%22Item2%22%3Anull%7D%2C%22ev_ebit%22%3A%7B%22Item1%22%3Anull%2C%22Item2%22%3Anull%7D%2C%22dividaliquidaebit%22%3A%7B%22Item1%22%3Anull%2C%22Item2%22%3Anull%7D%2C%22dividaliquidapatrimonioliquido%22%3A%7B%22Item1%22%3Anull%2C%22Item2%22%3Anull%7D%2C%22p_sr%22%3A%7B%22Item1%22%3Anull%2C%22Item2%22%3Anull%7D%2C%22p_capitalgiro%22%3A%7B%22Item1%22%3Anull%2C%22Item2%22%3Anull%7D%2C%22p_ativocirculante%22%3A%7B%22Item1%22%3Anull%2C%22Item2%22%3Anull%7D%2C%22roe%22%3A%7B%22Item1%22%3Anull%2C%22Item2%22%3Anull%7D%2C%22roic%22%3A%7B%22Item1%22%3Anull%2C%22Item2%22%3Anull%7D%2C%22roa%22%3A%7B%22Item1%22%3Anull%2C%22Item2%22%3Anull%7D%2C%22liquidezcorrente%22%3A%7B%22Item1%22%3Anull%2C%22Item2%22%3Anull%7D%2C%22pl_ativo%22%3A%7B%22Item1%22%3Anull%2C%22Item2%22%3Anull%7D%2C%22passivo_ativo%22%3A%7B%22Item1%22%3Anull%2C%22Item2%22%3Anull%7D%2C%22giroativos%22%3A%7B%22Item1%22%3Anull%2C%22Item2%22%3Anull%7D%2C%22receitas_cagr5%22%3A%7B%22Item1%22%3Anull%2C%22Item2%22%3Anull%7D%2C%22lucros_cagr5%22%3A%7B%22Item1%22%3Anull%2C%22Item2%22%3Anull%7D%2C%22liquidezmediadiaria%22%3A%7B%22Item1%22%3Anull%2C%22Item2%22%3Anull%7D%2C%22vpa%22%3A%7B%22Item1%22%3Anull%2C%22Item2%22%3Anull%7D%2C%22lpa%22%3A%7B%22Item1%22%3Anull%2C%22Item2%22%3Anull%7D%2C%22valormercado%22%3A%7B%22Item1%22%3Anull%2C%22Item2%22%3Anull%7D%7D&orderColumn=&isAsc=&page=0&take=607&CategoryType=1",
    "us_stocks": 'https://statusinvest.com.br/category/advancedsearchresultpaginated?search={"Sector":"","SubSector":"","Segment":"","my_range":"-20;100","forecast":{"upsidedownside":{"Item1":null,"Item2":null},"estimatesnumber":{"Item1":null,"Item2":null},"revisedup":true,"reviseddown":true,"consensus":[]},"dy":{"Item1":null,"Item2":null},"p_l":{"Item1":null,"Item2":null},"peg_ratio":{"Item1":null,"Item2":null},"p_vp":{"Item1":null,"Item2":null},"p_ativo":{"Item1":null,"Item2":null},"margembruta":{"Item1":null,"Item2":null},"margemebit":{"Item1":null,"Item2":null},"margemliquida":{"Item1":null,"Item2":null},"p_ebit":{"Item1":null,"Item2":null},"ev_ebit":{"Item1":null,"Item2":null},"dividaliquidaebit":{"Item1":null,"Item2":null},"dividaliquidapatrimonioliquido":{"Item1":null,"Item2":null},"p_sr":{"Item1":null,"Item2":null},"p_capitalgiro":{"Item1":null,"Item2":null},"p_ativocirculante":{"Item1":null,"Item2":null},"roe":{"Item1":null,"Item2":null},"roic":{"Item1":null,"Item2":null},"roa":{"Item1":null,"Item2":null},"liquidezcorrente":{"Item1":null,"Item2":null},"pl_ativo":{"Item1":null,"Item2":null},"passivo_ativo":{"Item1":null,"Item2":null},"giroativos":{"Item1":null,"Item2":null},"receitas_cagr5":{"Item1":null,"Item2":null},"lucros_cagr5":{"Item1":null,"Item2":null},"liquidezmediadiaria":{"Item1":null,"Item2":null},"vpa":{"Item1":null,"Item2":null},"lpa":{"Item1":null,"Item2":null},"valormercado":{"Item1":null,"Item2":null}}&orderColumn=&isAsc=&page=0&take=5238&CategoryType=12',
}

LOGGER = logging.getLogger(__name__)


def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Configure MinIO Client
    minio_client = boto3.client(
        "s3",
        endpoint_url="http://host.docker.internal:9000",  # MinIO endpoint from within Docker
        aws_access_key_id="minioadmin",  # MinIO access key
        aws_secret_access_key="minioadmin",  # MinIO secret key
        config=Config(signature_version="s3v4"),
        region_name="us-east-1",  # Default region for S3/MinIO
    )

    # Ensure that bucket exists before attempting upload
    try:
        minio_client.create_bucket(Bucket=bucket)
    except Exception:
        pass

    # Upload the file
    try:
        response = minio_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        LOGGER.error(e)
        return False
    return True


def si_web_scrapper(execution_date: str, stock_key: str):

    headers = {"user-agent": "Mozilla/5.0"}
    url_to_scrap = URLS_TO_SCRAP[stock_key]
    request = requests.get(url_to_scrap, headers=headers)
    if request.status_code == 200:
        response_json = request.json()
        file_name = f"{stock_key}_data.json"
        stock_list = response_json.get("list")
        with open(file_name, mode="w") as file:
            file.write(json.dumps(stock_list, ensure_ascii=False))

        object_path = f"si_stocks/{execution_date}/{file_name}"
        upload_file(file_name, "raw-data", object_path)

        os.remove(file_name)
