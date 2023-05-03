from prefect import flow


@flow(log_prints=True)
def sell():
    """Sell securities"""
    print("Sold securities!")
