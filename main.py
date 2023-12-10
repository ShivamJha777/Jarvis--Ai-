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
        audio = r.listen(source)
        query = r.recognize_google(audio, language= 'en-in')
        print(f'User said: {query}')
        return query
command = take_command()
say(command)
