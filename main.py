import wikipedia
import win32com.client
import speech_recognition as sr
import webbrowser
import pywhatkit
import datetime
import requests
from bs4 import BeautifulSoup
def say(script):
    '''This fucntion says out loud whatever string is given to it'''
    speaker = win32com.client.Dispatch('SAPI.SpVoice')
    return speaker.Speak(script)
def take_command():
    '''This function takes voice input from the user'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.7
        r.energy_threshold = 400
        audio = r.listen(source)
        try:
            say('Recognizing')
            query = r.recognize_google(audio, language= 'en-in')
            print(f'User said: {query}\n')
            return query
        except Exception as e:
            return 'Some Error Occurred. Sorry from Jarvis'
def Greet_Me():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour <= 12:
        say('Good morning,Boss')
    if hour > 12 and hour <= 15:
        say('Good Afternoon,Boss')
    if hour > 15 and hour <= 19:
        say('Good Evening,Boss')
    say('Hope you are having a good day,How can I help you?')
Greet_Me()
def Search_Google(query):
    import wikipedia as googleScrap
    query = query.replace('jarvis','')
    query = query.replace('search google for','')
    query = query.replace('google','')
    say('Boss ,this is what I found on Google')
    try:
        pywhatkit.search(query)
        result = googleScrap.summary(query,5)
        say(result)
    except :
        say('Sorry Boss there is no speakable output available')
def Search_Youtube(query):
    say('Boss this is what I found for your search on Youtube!')
    query = query.replace('jarvis','')
    query = query.replace('search youtube for','')
    query = query.replace('youtube','')
    try:
        web = 'https://www.youtube.com/results?search_query=' + query
        webbrowser.open(web)
        say('Boss these are the related videos I found Give me a minute I am going to play the most popular one')
        pywhatkit.playonyt(query)
        say('Done Boss')
    except:
        say('Sorry Boss Some error occured I was not able to complete your request')
def Search_Wikipedia(query):
    say('Searching from Wikipedia......')
    query = query.replace('jarvis','')
    query = query.replace('search wikipedia for', '')
    query = query.replace('wikipedia', '')
    results = wikipedia.summary(query,sentences = 5)
    say('According to Wikipedia ......')
    say(results)
    print(results)
while True:
    print('Listening')
    say('Listening')
    query = take_command().lower()
    say('Command accepted')
    sites = [['youtube','https://www.youtube.com'],['wikipedia','https://www.wikipedia.com'],['google','https://www.google.com'],['quora','https://www.quora.com'],['facebook','https://www.facebook.com'],['Github','https://www.github.com'],['Reddit','https://www.reddit.com'],['Discord','https://www.discord.com'],['Instagram','https://www.instagram.com'],['Netflix','https://www.Netflix.com'],['Spotify','https://www.spotify.com']]
    for site in sites:
        if  f'Open {site[0]}'.lower() in query:
            say(f'Opening {site[0]}')
            webbrowser.open(site[1])
    if 'stop'.lower() in query or 'shutdown'.lower() in query or 'shut down'.lower() in query  or 'shut '.lower() in query:
        say('Okay Boss,Jarvis is turning off')
        quit()
    if 'the time'.lower() in query:
        Time = datetime.datetime.now().strftime('%H:%M:%S')
        say(f'Boss,the time is {Time}')
    if 'introduce yourself'.lower() in query:
        say('Boss , I am a virtual voice assistant developed by Mr Shivam Jha and Mr Ishan Tiwari from 10 december 2023 uptill 2024 ,I can help you with almost anything,I can help you with your school work,I can even quiz you,I am capable of face and object recognition,I can tell you the news,predict the weather and do almost everthing models like Siri or Chat Gpt can do')
    if 'Hello'.lower() in query or 'how are you'.lower() in query:
        say('Hi Boss,I am fine,how are you doing?')
    if 'I am fine'.lower() in query:
        say('That is great Boss')
    if 'Thank you'.lower() in query:
        say('You are welcome ,Boss')
    if 'Search Google'.lower() in query:
        Search_Google(query)
    if 'Search Youtube'.lower() in query:
        Search_Youtube(query)
    if 'Search Wikipedia'.lower() in query:
        Search_Wikipedia(query)
    if 'temperature'.lower() in query:
        search = 'temperature in Kolkata'
        url = f'https://search.google.com/search?q={search}'
        r = requests.get(url)
        data = BeautifulSoup(r.text,'html.parser')
        temp = getattr(data.find('div', class_ = "BNeawe"), 'text', None)
        say(f'Boss the current {search} is {temp}')