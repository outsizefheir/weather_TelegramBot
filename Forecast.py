import requests
from config import W_TOKEN

def get_forecast(city: str) -> dict | None:
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,
        'appid': W_TOKEN,
        'units': 'metric',
        'lang': 'ru'
    }
    try:
        with requests.get(url, params=params) as r:
            data = r.json()
            weather_data = {
                'city': data['name'],
                'temp': data['main']['temp'],
                'pressure': data['main']['pressure'],
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind']['speed'],
                'description': data['weather'][0]['description']
            }
            return weather_data
    except:
        return None

