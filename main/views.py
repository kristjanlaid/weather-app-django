from django.shortcuts import render
import json
import urllib.request


def index(request):
    if request.method == "POST":
        city = request.POST["city"]
        API_key = "e2443024e19455b9de481a7c49e1f81d"

        source = urllib.request.urlopen(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"
        ).read()

        list_of_data = json.loads(source)

        data = {
            "country_code": str(list_of_data["sys"]["country"]),
            "coordinate": str(list_of_data["coord"]["lon"])
            + " "
            + str(list_of_data["coord"]["lat"]),
            "temp": str(list_of_data["main"]["temp"]) + "k",
            "pressure": str(list_of_data["main"]["pressure"]),
            "humidity": str(list_of_data["main"]["humidity"]),
        }
        print(data)
    else:
        data = {}
    return render(request, "main/index.html", data)
