from django.shortcuts import render
from django.http import HttpResponse

from data import get_weather


async def main() -> None:
    from pprint import pprint
    pprint(await get_weather())


async def index(request):
    cities = ["Moscow", "Saint Petersburg", "Novosibirsk", "Yekaterinburg", "Kazan", "Kursk", "Nordvik", "Perm", "Nizhnevartovsk", "Murmansk", "Magadan", "Vladivostok", "Chelyabinsk", "Pervouralsk", "Krasnoufimsk"]
    weather_data = None
    selected_city = request.POST.get('city', '')

    if request.method == 'POST' and selected_city:
        # Await the asynchronous function from data.py
        weather_data = await get_weather(selected_city)
            
    context = {
        'cities': cities,
        'weather_data': weather_data,
        'selected_city': selected_city
    }
    return render(request, "index.html", context)



if __name__ == "__main__":
    from asyncio import run
    run(main())