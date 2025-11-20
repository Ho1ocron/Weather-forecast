from datetime import datetime
from dataclasses import dataclass


@dataclass
class Weather:
    interval: float
    is_day: str
    temperature: float
    time: datetime
    weathercode: str # Wether code will be translated into string name instead of code
    winddirection: float
    windspeed: float
