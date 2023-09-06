import time
from prefect import flow, serve


@flow
def slow_flow(sleep: int = 60):
    "Sleepy flow - sleeps the provided amount of time (in seconds)."
    time.sleep(sleep)


@flow
def fast_flow():
    "Fastest flow this side of the Atlantic."
    return


if __name__ == "__main__":
    slow_deploy = slow_flow.to_deployment(name="sleeper")
    fast_deploy = fast_flow.to_deployment(name="fast")
    serve(slow_deploy, fast_deploy)
