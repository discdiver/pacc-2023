import httpx
from prefect import flow


@flow(retries=4)
def fetch():
    cat_fact = httpx.get("https://httpstat.us/Random/200,500")
    if cat_fact.status_code >= 400:
        raise Exception()
    print(cat_fact.text)


if __name__ == "__main__":
    fetch()
