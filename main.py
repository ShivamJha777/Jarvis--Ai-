import win32com.client
import speech_recognition as sr
import os
def say(script):
    '''This fucntion says out loud whatever string is given to it'''
    speaker = win32com.client.Dispatch('SAPI.SpVoice')
    return speaker.Speak(script)
say('Hello! Welcome to Jarvis AI')
def take_command():
    '''This function takes voice input from the user'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        say('Listening')
        print('Listening')
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language= 'en-in')
            print(f'User said: {query}')
            return query
        except Exception as e:
            return 'Some Error Occured. Sorry from Jarvis'
while True:
    print('Listening')
    say('Listening')
    query = take_command()
    say(query)
    if  'Open Youtube'.lower() in query.lower():
        webbrowser.open('https://youtube.com')
        say('Opening youtube')
