import psutil
import pyttsx3
engine = pyttsx3.init()
battery = psutil.sensors_battery()
# fan = psutil.sensors_fans()
# temp = psutil.sensors_temperatures()

print(battery)
print(psutil.cpu_times())

print(battery[1])
print(round(battery[1]/3600, 1))

engine.say(battery[0])
engine.runAndWait()

engine.say(round(battery[1]/3600, 1))
engine.runAndWait()
