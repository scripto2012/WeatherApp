from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm

def index(request):
    app_id = 'dbe6392a42183d78bf44aed0c9ad722a'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + app_id


    if(request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    all_cities = []
    for city in cities:
        response = requests.get(url.format(city.name)).json()
        print(response)
        city_info = {
            'city': city.name,
            'temp': response["main"]["temp"],
            'temp_min': response["main"]["temp_min"],
            'temp_feel': response["main"]["feels_like"],
            'icon': response["weather"][0]["icon"]
        }
        all_cities.append(city_info)

    context = {
        'all_info': all_cities,
        'form': form
    }

    return render(request, 'weather/index.html', context)
