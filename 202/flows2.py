from prefect import flow, task


@flow
def pipe2():
    print("hi")
    return None
