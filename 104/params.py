from prefect import flow
from datetime import date


@flow(log_prints=True)
def person(name: str = "Jeff", height: int = 6):
    print(date, name, height)
