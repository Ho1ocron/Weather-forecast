from httpx import AsyncClient
from asyncio import run, gather
from pprint import pprint

from processor import get_citys_coords
from models import Weather


async def get_weather(
    name: str= "Yekaterinburg", 
    url: str = "https://api.open-meteo.com/v1/forecast"
) -> Weather | None:
    lantitude, longitude = await get_citys_coords("Moscow")
    params = {
        "latitude": lantitude,
        "longitude": longitude,
        "current_weather": True
    }
    async with AsyncClient() as client:
        response = await client.get(url, params=params)
        weather = response.json()
        pprint(weather["current_weather"])


if __name__ == "__main__": 
    run(get_weather())
# async def fetch_url(url, client=None):
#     """Fetch a single URL asynchronously"""
#     if client is None:
#         client = httpx.AsyncClient()

#     response = await client.get(url, timeout=5)

#     if response.status_code != 200:
#         return None

#     return response.json()


# async def fetch_multiple_urls(urls):
#     """Fetch multiple URLs concurrently"""
#     async with httpx.AsyncClient() as client:
#         tasks = [fetch_url(url, client) for url in urls]
#         return [x for x in await asyncio.gather(*tasks) if x]
