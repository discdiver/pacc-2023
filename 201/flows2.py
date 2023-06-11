from prefect import flow


@flow
def pipe2():
    print("hi")
    return None
