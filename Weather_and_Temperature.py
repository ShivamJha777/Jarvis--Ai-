import requests
from bs4 import BeautifulSoup
import win32com.client
def say(Script):
    '''This function says out loud whatever string is given to it'''
    speaker = win32com.client.Dispatch('SAPI.SpVoice')
    return speaker.Speak(Script)
def find_weather(city):
    say(f'Okay Boss presenting a table of the weather of the next 3 days for  {city} ')
    print(city)
    url = 'https://wttr.in/{}'.format(city)
    # Getting the Weather Data of the City
    res = requests.get(url)
    # Printing the results!
    print(res.text)
def Temperature_finder(Query):
    url = 'https://www.google.com/search?q=' + Query
    html = requests.get(url).content
    soup = BeautifulSoup(html, 'html.parser')
    temp = getattr(soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}), 'text', None)
    print(f'Boss the {Query} is {temp}')
    say(f'Boss the {Query} is {temp}')