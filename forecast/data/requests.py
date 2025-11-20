import httpx
import asyncio


async def fetch_url(url, client=None):
    """Fetch a single URL asynchronously"""
    if client is None:
        client = httpx.AsyncClient()

    response = await client.get(url, timeout=5)

    if response.status_code != 200:
        return None

    return response.json()


async def fetch_multiple_urls(urls):
    """Fetch multiple URLs concurrently"""
    async with httpx.AsyncClient() as client:
        tasks = [fetch_url(url, client) for url in urls]
        return [x for x in await asyncio.gather(*tasks) if x]
