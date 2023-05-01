from prefect.filesystems import S3

block = S3(
    bucket_path="my-bucket",
    aws_access_key_id="abc don't check me in to public repo",
    aws_secret_access_key="123 don't check me in to public repo",
)
block.save("my_example-block")
