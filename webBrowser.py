import webbrowser as wb


def Open():
    wb.open('http://www.google.com')
    wb.open_new('http://www.python.org')
    wb.open_new_tab('http://www.python.org')


def openBrowser():
    path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
    wb.get(path).open_new_tab('http://cricket.org')


# Open()
# openBrowser()
