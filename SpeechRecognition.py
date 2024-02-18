import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[2].id)
rate = 150
engine.setProperty('rate', rate)

engine.say("say something, i will try to recognize that")
engine.runAndWait()

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Listening...")
    r.pause_threshold = 1
    audio = r.listen(source)
    print(audio)
try:
    print("Recognizing...")
    query = r.recognize_google(audio)
    print(query)
    engine.say(query)
    engine.runAndWait()
except Exception as e:
    print(e)
    engine.say("Say that again please")
    engine.runAndWait()
