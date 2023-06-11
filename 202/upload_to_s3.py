from pathlib import Path
from prefect import flow
from prefect_aws.s3 import S3Bucket


@flow()
def upload_to_s3(color: str, year: int, month: int) -> None:
    """The main flow function to upload taxi data"""
    path = Path(f"data/{color}/{year}/{color}_tripdata_{year}-{month:02}.parquet")
    s3_block = S3Bucket.load("s3-bucket-block")
    s3_block.upload_from_path(from_path=path, to_path=path)


if __name__ == "__main__":
    upload_to_s3(color="green", year=2020, month=1)
