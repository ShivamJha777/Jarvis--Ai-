import requests
import json
import win32com.client
import speech_recognition as sr
def say(script):
    '''This function says out loud whatever string is given to it'''
    speaker = win32com.client.Dispatch('SAPI.SpVoice')
    return speaker.Speak(script)
def take_command():
    '''This function takes voice input from the user'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.7
        r.energy_threshold = 500
        audio = r.listen(source)
        try:
            say('Recognizing')
            query = r.recognize_google(audio, language= 'en-in')
            print(f'User said: {query}\n')
            return query
        except Exception as e:
            return 'Some Error Occurred,Boss. Sorry from Jarvis'
def latestenews(API_KEY):
    api_dict = {'business':f'https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey={API_KEY}',
                'entertainment':f'https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey={API_KEY}',
                "science":f"https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey={API_KEY}",
                "health":f'https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey={API_KEY}',
                'sports':f"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey={API_KEY}",
                'technology':f"https://newsapi.org/v2/top-headlines?country=in&category=TECHNOLOGY&apiKey={API_KEY}"
                }
    content = None
    url = None
    say('Which field of news do you want , business or ,entertainment,or science or health or sports or technology')
    field = take_command()
    for key,value in api_dict.items():
        if key.lower() in field.lower():
            url = value
            print(url)
            print('Url was found')
            break
    news = getattr(requests.get(url),"text",None)
    news = json.loads(news)
    say('Boss Here are the news I found ')
    arts = news['articles']
    for articles in arts:
        article = articles['title']
        print(article)
        say(article)
        news_url = articles['url']
        print(f'For more info visit: {news_url}')
        say('Boss If you would like to stop Say stop')
        choice = take_command()
        if 'stop' in choice:
            break
    say('That is all Boss')
