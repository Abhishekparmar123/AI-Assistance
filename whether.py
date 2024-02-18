import requests
import pyttsx3

engine = pyttsx3.init()
engine.say("Enter the name of city :")
engine.runAndWait()

api_key = '64acaeb2f13cc138a7ed309905dc358a'

base_url = 'api.openweathermap.org/data/2.5/weather?q='

city_name = 'bhopal'

complete_url = 'http://api.openweathermap.org/data/2.5/weather?q='+ city_name+'&appid='+api_key

response = requests.get(complete_url)
x = response.json()
print(x)

if x['cod'] != "404":
    y = x["main"]
    temp_current = y["temp"] - 273.15
    pressure_current = y["pressure"]
    humidity_current = y['humidity']
    y = x["wind"]
    wind_speed = y['speed']
    wind_degree = y['deg']
    z = x['weather']
    weather_desc = z[0]['description']
    engine.say(f"the current temperature is {temp_current} degree celsius. The current pressure is"
               f" {pressure_current} pascal, and the current humidity is {humidity_current} ions."
               f" the wind speed is {wind_speed} kilo meter per hours and the wind degree is {wind_degree}")
    engine.runAndWait()
else:
    print("bye")
