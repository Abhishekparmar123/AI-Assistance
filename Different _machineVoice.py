import pyttsx3

engine = pyttsx3.init()
voice = engine.getProperty('voices')
print(voice)

for i in range(0, 3, 1):
    engine.setProperty('voice', voice[i].id)
    rate = 150
    engine.setProperty('rate', rate)
    engine.say("hello, how i can help you")
    engine.runAndWait()
