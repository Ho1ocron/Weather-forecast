from httpx import AsyncClient
from datetime import datetime

from .processor import get_citys_coords
from .models import Weather
from forecast.settings import API_URL, WEATHER_CODES


async def serializer(key: str, value: str) -> datetime | float | str:
    if key == "time":
        return datetime.fromisoformat(value)
    elif key == "weathercode":
        return WEATHER_CODES[int(value)]
    else:
        try:
            return float(value)
        except Exception as e:
            print(e)
            print(key, value)
            return 0.0


async def get_weather(
    name: str = "Yekaterinburg",
    url: str = API_URL
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
    from asyncio import run
    from pprint import pprint

    pprint(run(get_weather()))
