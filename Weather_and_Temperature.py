import requests
from bs4 import BeautifulSoup
import win32com.client
def say(Script):
    '''This function says out loud whatever string is given to it'''
    speaker = win32com.client.Dispatch('SAPI.SpVoice')
    return speaker.Speak(Script)
def find_weather(city):

    # creating url and requests instance
    url = "https://www.google.com/search?q=" + "weather" + city
    html = requests.get(url).content

    # getting raw data
    soup = BeautifulSoup(html, 'html.parser')
    temp = getattr(soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}),"text",None)
    str = getattr(soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}),"text",None)
    data = str.split('\n')
    time = data[0]
    sky = data[1]
    if 'y' not in sky:
        sky = sky+'y'
    # printing all data
    print("Temperature is", temp)
    print("Time: ", time)
    print("Sky Description: ", sky)
    say(f"Temperature is {temp}")
    say(f"Time forecasted is {time} ")
    say(f"Sky Description is {sky}")
def Temperature_finder(Query):
    url = 'https://www.google.com/search?q=' + Query
    html = requests.get(url).content
    soup = BeautifulSoup(html, 'html.parser')
    temp = getattr(soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}), 'text', None)
    print(f'Boss the {Query} is {temp}')
    say(f'Boss the {Query} is {temp}')