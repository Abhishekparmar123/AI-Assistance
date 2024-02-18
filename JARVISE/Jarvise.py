import datetime
import json
import os
import requests
import smtplib
import webbrowser as wb
from email.mime.text import MIMEText
from urllib.request import urlopen

import psutil
import pyautogui
import pyjokes
import pyttsx3
import speech_recognition as sr
import wikipedia
import wolframalpha
import time

from JARVISE import months

engine = pyttsx3.init()
app_id = 'V337EY-5649662JTQ'

api_key = '64acaeb2f13cc138a7ed309905dc358a'
base_url = 'api.openweathermap.org/data/2.5/weather?q='
city_name = 'bhopal'
complete_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&appid=' + api_key

voice = engine.getProperty('voices')
engine.setProperty('voice', voice[0].id)
voiceRate = 180
engine.setProperty('rate', voiceRate)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def voice(text):
    engine.say(text)
    engine.runAndWait()


def day():
    speak("today is " + datetime.datetime.now().strftime('%A'))


def timeCurr():
    hour = datetime.datetime.now().hour
    minute = datetime.datetime.now().minute
    second = datetime.datetime.now().second
    speak("the current time is {} o clock {} minutes {} seconds".format(hour, minute, second))


def date():
    year = datetime.datetime.now().year
    day = datetime.datetime.now().day
    speak("the current date is ")
    speak(str(day) + months.month() + str(year))


def wishMe():
    hour = datetime.datetime.now().hour
    greet = ''
    if 6 <= hour < 12:
        greet = "Good Morning sir"
    elif 12 <= hour < 18:
        greet = "Good Afternoon sir"
    elif 18 <= hour <= 24:
        greet = "Good Evening sir"
    else:
        greet = "Good night sir"

    speak(greet + ", welcome back, i am jarvis how i can help you")


def bye():
    speak("thank you sir, see you soon")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
    except Exception as e:
        print(e)
        speak("i am waiting for your command")
        return "None"
    return query


def sendmail(to, content, subject):
    msg = MIMEText(content, 'html')
    msg['Subject'] = subject
    msg['To'] = to
    msg['From'] = "abhihitparmar123@gmail.com"
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("abhihitparmar123@gmail.com", "8435057182")
    server.send_message(msg)
    server.close()


def play():
    songs_dir = r'C:\Users\abhis\Music\new music'
    songs = os.listdir(songs_dir)
    os.startfile(os.path.join(songs_dir, songs[0]))


def screenShot():
    img = pyautogui.screenshot()
    img.save(r"photo\ss.png")


def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU use is " + usage + "percent")

    battery = psutil.sensors_battery()
    speak("battery is at " + str(battery[0]) + "percent")
    speak("computer run around" + str(round(battery[1] / 3600)) + ", hours")
    if battery[2]:
        speak("your system is charging")
    else:
        speak("your system is not charging")


def temp():
    response = requests.get(complete_url)
    x = response.json()

    if x['cod'] != "401":
        y = x["main"]
        temp_current = y["temp"] - 273.15
        text = f"the current temperature is {temp_current} degree celsius."
        speak(text)
    else:
        speak("Error occurred")


def weather():
    response = requests.get(complete_url)
    x = response.json()

    if x['cod'] != "404":
        y = x["main"]
        pressure_current = y["pressure"]
        humidity_current = y['humidity']
        y = x["wind"]
        wind_speed = y['speed']
        wind_degree = y['deg']
        z = x['weather']
        weather_desc = z[0]['description']
        text = f"The current weather is {weather_desc}, And The current pressure is {pressure_current} pascal, and " \
               f"the current humidity is {humidity_current} ions. the wind speed is {wind_speed} kilo meter per hours " \
               f"and the wind degree is {wind_degree} "
        speak(text)

    else:
        speak("error occurred")


def jokes():
    speak(pyjokes.get_joke())


if __name__ == "__main__":
    wishMe()

    while True:
        query = takeCommand().lower()
        print(query)

        if "time" in query:
            timeCurr()
        elif "date" in query:
            date()
        elif "which day is it" in query:
            day()
        elif "how are you" in query:
            speak("I am fine, thanks for asking sir, I hope you are also feet and fine")
        elif "according to you" in query:
            speak('If you can talk then definitely you are human')
        elif 'about your self' in query or "about yourself" in query:
            speak('I am jarvis 1.0, i am personal assistant, i am created by abhishek, i can help you in various '
                  'records, i can search for you on the internet, i can also grab information from wikipedia in limits '
                  'terms, i can try to make your life better where you just have to command me and i will do '
                  'it for you')
        elif 'why you came' in query or 'why you come' in query:
            speak('Thanks to abhishek sir, further this is a secret, without my creator permission i can not able to '
                  'tell you')
        elif 'about your creator' in query:
            speak('My creator is Abhishek and Abhishek is an extra ordinary person he has a passion for robotics, '
                  'artificial intelligence and machine learning, he is very collaborative with you facing any problem '
                  'regarding the jarvis, he will glad to help you')
        elif "thank you" in query:
            speak("don't say like this, this is my work")
        elif "wikipedia" in query:
            try:
                speak("searching...")
                query = query.replace("search on wikipedia ", "")
                print(query)
                result = wikipedia.summary(query, sentences=2)
                speak("According to wikipedia")
                print(result)
                speak(result)
            except Exception as e:
                speak(e)
        elif "send mail" in query:
            try:
                speak("what is subject")
                subject = takeCommand()
                print(subject)
                speak("what should i say")
                content = takeCommand()
                print(content)
                to = "anandmohanmaddy@gmail.com"
                sendmail(to, content, subject)
                speak("the mail send successfully")
            except Exception as e:
                speak(e)
                speak("unable to send the message")
        elif "chrome" in query or "search on chrome" in query:
            speak("what should I search?")
            search = takeCommand().lower()
            print(search)
            wb.open_new_tab('http://' + search + '.com')
        elif "google" in query or "search on google" in query:
            speak("what should I search ?")
            search_term = takeCommand().lower()
            wb.open('https://www.google.com/search?q=' + search_term)
        elif "search in youtube" in query or "search on youtube" in query:
            speak("what should I search?")
            search_term = takeCommand().lower()
            wb.open('https://www.youtube.com/results?search_query=' + search_term)
        elif "chrome tab" in query:
            wb.open_new_tab('http://www.google.com')
        elif "news" in query:
            try:
                jsonObj = urlopen(
                    "http://newsapi.org/v2/top-headlines?country=us&category=entertainment&apiKey=6c2cc42dccb64eaaa35c9f98fdbfd9c6")
                data = json.load(jsonObj)
                i = 1

                speak("Here are some top headlines from the Entertainment Industry")
                print('****************************TOP HEADLINES*************************')
                for item in data["articles"]:
                    print(str(i) + ", " + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(item['title'])
                    if i == 5:
                        break
                    i += 1
            except Exception as e:
                print(str(e))
        elif "where is" in query:
            query = query.replace('where is ', '')
            location = query
            speak("you asked to locate" + location)
            wb.open_new_tab("https://www.google.com/maps/place/" + location)
        elif "calculate" in query:
            try:
                client = wolframalpha.Client(app_id)
                index = query.lower().split().index('calculate')
                query = query.split()[index + 1:]
                res = client.query(''.join(query))
                answer = next(res.results).text
                print('the answer is : ' + answer)
                speak('The answer is ' + answer)
            except Exception as e:
                print(e)
                speak(e)
        elif 'what is' in query or 'who is' in query:
            client = wolframalpha.Client(app_id)
            res = client.query(query)
            try:
                print(next(res.results).text)
                speak(next(res.results).text)
            except StopIteration:
                print('no result')

        elif "log out" in query or "logout" in query:
            os.system("shutdown -l")
        elif "shutdown" in query or "shut down" in query:
            os.system("shutdown /s /t 1")
        elif "restart" in query or "re start" in query:
            os.system("shutdown /r /t 1")
        elif "play songs" in query or "play music" in query:
            play()
        elif "remember that" in query:
            speak("what should i remember?")
            data = takeCommand()
            speak("you said me to remember" + data)
            remember = open("data.txt", "w")
            remember.write(data)
            remember.close()
        elif "do you know anything" in query or "did you know anything" in query:
            remember = open("data.txt", "r")
            speak("you said me to remember that" + remember.read())
        elif "write a note" in query:
            speak("what should I write, sir?")
            notes = takeCommand()
            file = open('notes.txt', 'w')
            speak("Sir should I include Date and Time?")
            ans = takeCommand()
            if 'yes' in ans or 'sure' in ans:
                year = datetime.datetime.now().year
                day = datetime.datetime.now().day
                date1 = str(day) + " " + months.month() + " " + str(year)

                hour = datetime.datetime.now().hour
                minute = datetime.datetime.now().minute
                second = datetime.datetime.now().second
                strTime = "{} o clock {} minutes {} seconds".format(hour, minute, second)

                file.write("Note write on ")
                file.write(date1 + " time " + strTime)
                file.write(':-')
                file.write(notes)
                speak('Done Taking Notes, sir!')
            else:
                file.write(notes)
        elif "read note" in query:
            speak("Reading your notes")
            file = open('notes.txt', 'r')
            read = file.read()
            print(read)
            speak(read)
        elif "take screenshot" in query:
            screenShot()
            speak("done")
        elif 'show screenshot' in query:
            path = r"C:\Users\abhis\PycharmProjects\My Jarvise\photo"
            os.startfile(path)
        elif "word" in query:
            speak("Opening MS Word.....")
            ms_word = r'C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Microsoft Office/MS word'
            os.startfile(ms_word)
        elif "cpu" in query:
            cpu()
        elif "temperature" in query:
            temp()
        elif "weather" in query:
            weather()
        elif "joke" in query or "jokes" in query:
            jokes()
        elif "i love you" in query or 'i love u' in query:
            speak("i love you two, i like to make your work easy")
        elif 'sleep mode' in query:
            speak('For How many second you want to stop my service?')
            ans = int(takeCommand())
            speak('sleep mode activated for ' + str(ans) + 'second')
            print(ans)
            time.sleep(ans)
            speak('hello sir, jarvis in your service again, What i can help you')
        elif "offline" in query:
            bye()
            quit()
