import requests
from prefect import flow
from prefect


@flow()
def fetch_weather(lat: float = 3, lon: float = -30):
    base_url = "https://api.open-meteo.com/v1/forecast/"
    weather = requests.get(
        base_url,
        params=dict(latitude=lat, longitude=lon, hourly="temperature_2m"),
    )
    most_recent_temp = float(weather.json()["hourly"]["temperature_2m"][0])
    print(f"Most recent temp C: {most_recent_temp} degrees")
    return most_recent_temp


if __name__ == "__main__":
    fetch_weather.from_source(
        source="https://github.com/org/repo.git",
        entrypoint="path/to/flow.py:my_flow").serve(name="gh-deploy", interval="300")

