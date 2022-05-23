from django.shortcuts import render, redirect, get_object_or_404
from .forms import CityForm
from .models import Locations
from django.contrib import messages
from .request_weather import WeatherStatus

def index(request):
    cities = Locations.objects.all()

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            new_city = request.POST.get('location')
            if new_city not in cities:
               weather_test = WeatherStatus([new_city])
               if weather_test:  
                  form.save()
                  city_list = Locations.objects.all()
               else:
                  messages.success(request, ("Location Wasn't Found"))    

               weather_datas = WeatherStatus(city_list)
               messages.success(request, ("Location Has Been Added Successfuly"))
               return render(request, 'index.html', {'weather_datas': weather_datas})

            else:
               messages.success(request, ("Location has been exsists"))

    weather_datas = WeatherStatus(cities)
    return render(request, 'index.html', {'weather_datas': weather_datas})


def delete(request, loc):
    get_object_or_404(Locations, location=loc).delete()
    messages.success(request, ("Weather Location Has Been Deleted"))
    return redirect('index')