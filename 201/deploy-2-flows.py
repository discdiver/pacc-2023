import requests
from prefect import flow, deploy, serve


@flow(log_prints=True)
def hi():
    print("hello")


@flow(log_prints=True)
def fetch_weather(lat: float = 3, lon: float = -30):
    base_url = "https://api.open-meteo.com/v1/forecast/"
    weather = requests.get(
        base_url,
        params=dict(latitude=lat, longitude=lon, hourly="temperature_2m"),
    )
    most_recent_temp = float(weather.json()["hourly"]["temperature_2m"][0])
    print(f"Most recent temp C: {most_recent_temp} degrees")


if __name__ == "__main__":
    dep1 = fetch_weather.to_deployment(name="weather-deploy")
    dep2 = hi.to_deployment(name="hey")
    deploy(
        dep1,
        dep2,
        work_pool_name="dock1",
        image="discdiver/whatevs-image:1.0",
        push=False,
    )
