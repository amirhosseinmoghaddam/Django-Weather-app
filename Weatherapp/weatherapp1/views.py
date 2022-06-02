from django.shortcuts import render, redirect, get_object_or_404
from .forms import CityForm
from .models import Locations
from django.contrib import messages
from .request_weather import WeatherStatus

def index(request):
    #Get all datas
    cities = Locations.objects.all()
    
    #User submit a POST method
    if request.method == 'POST':
        form = CityForm(request.POST)
        
        #Form validation and get location from user input
        if form.is_valid():
            new_city = request.POST.get('location')
            
            #Don't add a city multiple times
            if new_city not in cities:
               weather_test = WeatherStatus([new_city])
               
               #Save form if everythings go well
               if weather_test:  
                  form.save()
                  city_list = Locations.objects.all()
               else:
                  messages.success(request, ("Location Wasn't Found"))    
               
               #Response clean weather datas to user
               weather_datas = WeatherStatus(city_list)
               messages.success(request, ("Location Has Been Added Successfuly"))
               return render(request, 'index.html', {'weather_datas': weather_datas})

            else:
               messages.success(request, ("Location has been exsists"))
    
    #Render First page
    weather_datas = WeatherStatus(cities)
    return render(request, 'index.html', {'weather_datas': weather_datas})

#Delete a location when user click on delete
def delete(request, loc):
    get_object_or_404(Locations, location=loc).delete()
    messages.success(request, ("Weather Location Has Been Deleted"))
    return redirect('index')
