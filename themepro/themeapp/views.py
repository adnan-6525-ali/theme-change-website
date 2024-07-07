from django.shortcuts import render , redirect
from django.http import JsonResponse
from .models import ExampleModel
from datetime import datetime
import geocoder
import requests

# to fetch hour
now = datetime.now()
hour = now.hour

# to fetch the temprature using coordinate of user
g = geocoder.ip('me')
api_key = 'e93d7dcbb7809b2415b8503f567188dd'  
if g.ok:
    latitude = g.latlng[0]
    longitude = g.latlng[1]

    url = f'http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        city_name = data['name']
        curr_temp = data['main']['temp']
else:
    curr_temp = 25
    city_name = None

# condition for the colour according to curr_temp
# curr_temp = -5
if curr_temp >= 40:
    navCol = "#FE9900"  #orange
elif 30<= curr_temp <40:
    navCol = "#F8E21C"  #yellow
elif 20<= curr_temp <30:
    navCol = "#1BC4E1"  #skyblue
elif 10<= curr_temp <20:
    navCol = "#376B6D"  #blue and black shade
elif 0<= curr_temp < 10:
    navCol = "#88A1A2"  #grey and blue shade
elif curr_temp < 0:
    navCol = "#6C6C6A"  #grey shade


# -----> MAIN <-------

def index(request):
    # hour=20
    if (6<= hour <19):
        # print("--------------light theme--------------")   
        # print(f"NAVCOLOR IS :--{navCol}")   
        # print(f"current temprature is {curr_temp} and city name is {city_name} ")
        themecolor = "light"
        colNav = navCol
        return render(request, 'index.html', {'theme': themecolor , "colorNav":colNav})

    else:
        # print("--------------dark theme--------------")
        # print(f"NAVCOLOR IS :--{navCol}") 
        # print(f"current temprature is {curr_temp} and city name is {city_name} ")
        themecolor = "dark"
        colNav = navCol
        return render(request, 'index.html', {'theme': themecolor , "colorNav":colNav})




def location(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        desc = request.POST.get("des")
        data = ExampleModel(name=name , age=age , description=desc)
        data.save()
        return redirect("/")

    return render(request,"location.html")

# def formData(request):
#     if request.method == "POST":
#         name = request.POst.get("name")
#         age = request.POST.get("age")
#         desc = request.POST.get("des")
        
#         print("name is:-----",name)
#         print("age  is:-----",age )
#         print("desc is:-----",desc)
#         return redirect("/location")

 