import pyttsx3

engine = pyttsx3.init()
voice = engine.getProperty('voices')
print(voice)
engine.setProperty('voice', voice[1].id)
rate = 150
engine.setProperty('rate', rate)
engine.say("hello, please write something in console, i can try to speak that")
engine.runAndWait()

choice = 'y'
while choice.lower() == 'y':
    text = str(input("Enter something : "))
    engine.say(text)
    engine.runAndWait()
    engine.say("Do you want to write more")
    engine.runAndWait()
    choice = input("Do you want to write more [y/n] : ")

