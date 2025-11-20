from datetime import datetime


class Weather:
    interval: int
    is_day: int
    temperature: float
    time: datetime
    weathercode: str # Wether code will be translated in string name instead of code
    winddirection: float
    windspeed: float
