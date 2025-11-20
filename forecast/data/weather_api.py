from httpx import AsyncClient
from asyncio import run, gather
from datetime import datetime

from .processor import get_citys_coords
from .models import Weather


async def serializer(key: str, value: str) -> datetime | float | str:
    weather_codes = {
        0: "Clear sky",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast",
        45: "Fog",
        48: "Depositing rime fog",
        51: "Drizzle: Light",
        53: "Drizzle: Moderate",
        55: "Drizzle: Dense intensity",
        56: "Freezing Drizzle: Light",
        57: "Freezing Drizzle: Dense intensity",
        61: "Rain: Light",
        63: "Rain: Moderate",
        65: "Rain: Heavy intensity",
        66: "Freezing Rain: Light",
        67: "Freezing Rain: Heavy intensity",
        71: "Snow fall: Light",
        73: "Snow fall: Moderate",
        75: "Snow fall: Heavy intensity",
        77: "Snow grains",
        80: "Rain showers: Light",
        81: "Rain showers: Moderate",
        82: "Rain showers: Violent",
        85: "Snow showers: Light",
        86: "Snow showers: Heavy",
        95: "Thunderstorm: Slight or moderate",
        96: "Thunderstorm with slight hail",
        99: "Thunderstorm with heavy hail"
    }

    if key == "time":
        return datetime.fromisoformat(value)
    elif key == "weathercode":
        return weather_codes[int(value)]
    else:
        try:
            return float(value)
        except Exception as e:
            print(e)
            print(key, value)
            return 0.0


async def get_weather(
    name: str = "Yekaterinburg",
    url: str = "https://api.open-meteo.com/v1/forecast"
) -> Weather | None:
    if name == "":
        return None

    lantitude, longitude = await get_citys_coords(name)

    params = {
        "latitude": lantitude,
        "longitude": longitude,
        "current_weather": True
    }

    async with AsyncClient() as client:
        response = await client.get(url, params=params)
        if response.status_code != 200:
            return None

        forecast: dict[str, dict[str, str]] = response.json()
        
        # weather = Weather(*[await serializer(key, value) for key, value in forecast["current_weather"].items()])
        # Open-Meteo no longer returns "interval", so set fallback
        
        cw = forecast["current_weather"]
        weather = Weather(
            interval=0.0,  
            is_day=await serializer("is_day", cw["is_day"]),
            temperature=await serializer("temperature", cw["temperature"]),
            time=await serializer("time", cw["time"]),
            weathercode=await serializer("weathercode", cw["weathercode"]),
            winddirection=await serializer("winddirection", cw["winddirection"]),
            windspeed=await serializer("windspeed", cw["windspeed"]),
        )
        return weather


if __name__ == "__main__":
    from pprint import pprint
    pprint(run(get_weather()))
