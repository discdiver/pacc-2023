import httpx
from prefect import flow, task


@task(retries=4, retry_delay_seconds=0.1)
def fetch_cat_fact():
    cat_fact = httpx.get("https://httpstat.us/Random/200,500")
    if cat_fact.status_code >= 400:
        raise Exception()
    print(cat_fact.text)


@flow
def fetch():
    fetch_cat_fact()


if __name__ == "__main__":
    fetch()
