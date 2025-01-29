import requests

endpoint = "https://api.openweathermap.org/data/2.5/forecast"
apikey = "8db68b6f43c28d3274be30c466bfe03b"
weather_params = {
    "lat" :46.065552,
    "lon":-118.333641,
    "appid":apikey
}

response = requests.get(endpoint,params=weather_params)

weather_data = response.json()
will_rain = False
for hour_data in weather_data["list"]:
   condition_code = hour_data['weather'][0]["id"]
   if int(condition_code) < 700:
       will_rain = True

   if will_rain:
       print("Bring an umbrella")


