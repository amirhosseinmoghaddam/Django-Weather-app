from unicodedata import name
import requests

def WeatherStatus(cities):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={YOUR_API_KEY}'
    all_data = []

    for city in cities:
        r = requests.get(url.format(city)).json()
        temp = r['main']['temp']
        temp = round(temp)

        city_weather = {
            'name': city,
            'temp': temp,
            'desc': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
        }
        all_data.append(city_weather)
    return all_data     
