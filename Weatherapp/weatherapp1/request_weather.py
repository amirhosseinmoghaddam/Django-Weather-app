from unicodedata import name
import requests

def WeatherStatus(cities):
    #Use API
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={ENTER_YOUR_API_KEY}'
    all_data = []
    
    #Get cities live weather
    for city in cities:
        r = requests.get(url.format(city)).json()
        #Get temperature
        temp = r['main']['temp']
        #Round to a Integer
        temp = round(temp)
        
        #Save all city weather datas in dict
        city_weather = {
            'name': city,
            'temp': temp,
            'desc': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
        }
        all_data.append(city_weather)
    return all_data     
