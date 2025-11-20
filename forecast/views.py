from django.shortcuts import render
from django.http import HttpResponse

from data import get_weather


async def main() -> None:
    from pprint import pprint
    pprint(await get_weather())


def index(request):
    return render(request, "index.html")


if __name__ == "__main__":
    from asyncio import run
    run(main())