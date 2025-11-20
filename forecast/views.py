from django.shortcuts import render
from django.http import HttpResponse

from models import Weather

import csv
import requests

COUNTRIES = "countries.csv"


def coords(filename: str, search_term: str, column_index=None) -> tuple[float]:
    found_lines = []
    with open(filename, 'r', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        for i, row in enumerate(csv_reader):
            if column_index is not None:
                if len(row) > column_index and search_term in row[column_index]:
                    found_lines.append((i, row))
            else:
                if any(search_term in cell for cell in row):
                    found_lines.append((i, row))
    lantitude, longitude = float(found_lines[0][1][1][1:]), float(found_lines[0][1][2][1:])
    return lantitude, longitude


def get_weather(country: str = "Russia") -> Weather:
    
    lantitude = coords(COUNTRIES, country)[0]
    longitude = coords(COUNTRIES, country)[1]

    open_meteo_url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lantitude,
        "longitude": longitude,
        "current_weather": True
    }

    open_meteo_response = requests.get(open_meteo_url, params=params)
    weather_data = open_meteo_response.json()
    print(weather_data)
    weather = Weather()
    return weather

get_weather()
def index(request):
    return render(request, "index.html")