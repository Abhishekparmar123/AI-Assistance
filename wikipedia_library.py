# importing the module
import wikipedia
import pyttsx3

engine = pyttsx3.init()


def summary():
    result = wikipedia.summary('India', sentences=2)
    print(result)


def search():
    result = wikipedia.search("Python", results=5)
    print(result)


def pageData():
    page = wikipedia.page("india")
    print(page.html)
    print(page.original_title)
    print(page.links[0:10])
    print(page.images)
    print("Content of this page : \n")
    print(page.content)
    print("Summary of this page : \n")
    print(page.summary)


def language():
    wikipedia.set_lang("hi")
    print(wikipedia.summary("India"))


# summary()
# search()
# pageData()
language()
