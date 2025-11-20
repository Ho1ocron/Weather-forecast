from datetime import datetime
from dataclasses import dataclass


@dataclass
class Weather:
    interval: float
    is_day: float
    temperature: float
    time: datetime
    weathercode: str # Wether code will be translated in string name instead of code
    winddirection: float
    windspeed: float
