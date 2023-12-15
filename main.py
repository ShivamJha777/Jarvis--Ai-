import os
import pywhatkit
import webbrowser
import requests
from bs4 import BeautifulSoup
import win32com.client
import speech_recognition as sr
import wikipedia
import datetime
def say(script):
    '''This function says out loud whatever string is given to it'''
    speaker = win32com.client.Dispatch('SAPI.SpVoice')
    return speaker.Speak(script)
def take_command():
    '''This function takes voice input from the user'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.7
        r.energy_threshold = 450
        audio = r.listen(source)
        try:
            say('Recognizing')
            query = r.recognize_google(audio, language= 'en-in')
            print(f'User said: {query}\n')
            return query
        except Exception as e:
            return 'Some Error Occurred. Sorry from Jarvis'
def Greet_Me():
    '''This function greets the user'''
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour <= 12:
        say('Good morning,Boss')
    elif hour > 12 and hour <= 15:
        say('Good Afternoon,Boss')
    else:
        say('Good Evening,Boss')
    say('Hope you are having a good day,How can I help you?')
def Search_Google(query):
    '''This function searches google for "query" and shows the results.It also speaks out loud a summary of the results'''
    import wikipedia as googleScrap
    query = query.replace('jarvis','')
    query = query.replace('search google for','')
    query = query.replace('google','')
    say('Boss ,this is what I found on Google')
    try:
        pywhatkit.search(query)
        result = googleScrap.summary(query,3)
        say(result)
    except :
        say('Sorry Boss there is no speakable output available')
def Search_Youtube(query):
    '''This function searches YouTube for "query" and plays the most popular video/short that it finds.'''
    say('Boss this is what I found for your search on Youtube!')
    query = query.replace('jarvis','')
    query = query.replace('search youtube for','')
    query = query.replace('youtube','')
    try:
        web = 'https://www.youtube.com/results?search_query=' + query
        webbrowser.open(web)
        say('Boss these are the related videos I found ,Give me a minute I am going to play the most popular one')
        pywhatkit.playonyt(query)
        say('Done Boss')
    except:
        say('Sorry Boss .Some error occurred I was not able to complete your request')
def Search_Wikipedia(query):
    '''This function searches wikipedia for "query" and speaks out loud the summary that it finds'''
    say('Searching from Wikipedia......')
    query = query.replace('jarvis','')
    query = query.replace('search wikipedia for', '')
    query = query.replace('wikipedia', '')
    try:
        results = wikipedia.summary(query,sentences = 3)
        say('According to Wikipedia ......')
        say(results)
        print(results)
    except:
        say(f'I am sorry,Boss Either I heard you wrong or there was no information for {query} on wikipedia')
Greet_Me()
while True:
    say('Listening')
    print('Listening')
    query = take_command().lower()
    if 'the time'.lower() in query:
        Time = datetime.datetime.now().strftime('%H:%M:%S')
        say(f'Boss,the time is {Time}')
    elif 'introduce yourself'.lower() in query:
        say('I am a virtual voice assistant developed by Mr Shivam Jha and Mr Ishan Tiwari from 10 december 2023 uptill 2024 ,I can help you with almost anything,I can help you with your school work,I can even quiz you,I am capable of face and object recognition,I can tell you the news,predict the weather and do almost everything models like Siri or Chat Gpt can do')
    elif 'go offline' in query or 'shut off' in query or 'shutdown' in query  or 'shut down' in query:
        say('Okay Boss.Jarvis is going offline')
        quit()
    elif 'I am fine'.lower() in query:
        say('That is great Boss')
    elif 'Thank you'.lower() in query:
        say('You are welcome ,Boss')
    elif 'open' in query:
        from Dictapp import openappweb
        openappweb(query)
    elif 'close' in query:
        from Dictapp import closeappweb
        closeappweb(query)
    elif 'Search Google'.lower() in query:
        Search_Google(query)
    elif 'Search Youtube'.lower() in query:
        Search_Youtube(query)
    elif 'Search Wikipedia'.lower() in query:
        Search_Wikipedia(query)
    elif 'temperature'.lower() in query:
        search = 'temperature in Kolkata'
        url = f'https://search.google.com/search?q={search}'
        r = requests.get(url)
        data = BeautifulSoup(r.text,'html.parser')
        temp = getattr(data.find('div', class_ = "BNeawe"), 'text', None)
        say(f'Boss the current {search} is {temp}')
    elif 'Hello'.lower() or 'how are you'.lower() in query:
        say('Hi Boss,I am fine,how are you doing?')
