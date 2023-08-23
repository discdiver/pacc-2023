from prefect import flow


@flow(log_prints=True)
def person(name: str = "Jeff", height: int = 6):
    print(name, height)
