import boto3
from botocore.client import Config


def get_minio_client():
    minio_client = boto3.client(
        "s3",
        endpoint_url="http://host.docker.internal:9000",  # MinIO endpoint from within Docker
        aws_access_key_id="minioadmin",  # MinIO access key
        aws_secret_access_key="minioadmin",  # MinIO secret key
        config=Config(signature_version="s3v4"),
        region_name="us-east-1",  # Default region for S3/MinIO
    )

    return minio_client
