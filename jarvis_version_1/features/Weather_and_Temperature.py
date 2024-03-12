import requests
from bs4 import BeautifulSoup
import win32com.client
def say(Script):
    '''This function says out loud whatever string is given to it'''
    speaker = win32com.client.Dispatch('SAPI.SpVoice')
    return speaker.Speak(Script)
def find_weather(city):
    print(city)
    url = 'https://wttr.in/{}'.format(city)
    # Getting the Weather Data of the City
    res = requests.get(url)
    # Printing the results!
    return res.text
def Temperature_finder(Query):
    url = 'https://www.google.com/search?q=' + Query
    html = requests.get(url).content
    soup = BeautifulSoup(html, 'html.parser')
    temp = getattr(soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}), 'text', None)
    return f'Boss the {Query} is {temp}'