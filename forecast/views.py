from django.shortcuts import render
from django.http import HttpResponse

import requests

latitude = 40.7128  # Example: New York City
longitude = -74.0060

open_meteo_url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": latitude,
    "longitude": longitude,
    "current_weather": True
}

open_meteo_response = requests.get(open_meteo_url, params=params)
weather_data = open_meteo_response.json()


def index(request):
    return render(request, "index.html")