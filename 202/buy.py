from prefect import flow


@flow(log_prints=True)
def buy():
    """buy securities"""
    print("Bought securities")
