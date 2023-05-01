from prefect import flow, task


@flow
def pipe():
    print("hi")
    return None
