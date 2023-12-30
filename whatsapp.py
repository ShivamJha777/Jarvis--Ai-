import pywhatkit
import win32com.client
import speech_recognition as sr
from datetime import timedelta
from datetime import datetime
import pyautogui
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
            return query.lower()
        except Exception as e:
            return 'Some Error Occurred. Sorry from Jarvis'
update = int((datetime.now() + timedelta(minutes = 2)).strftime('%M'))
strTime = int(datetime.now().strftime('%H'))
def sendMessage():
    say('Who do you want to message Boss?')
    say('To message Sonu say 1 to Message Harsh say 2 to Message Shreyan say 3 to Message Kutta say 4')
    a = int(input())
    if a == 1:
        say('What is the message?Only say the message whatever you say next will be sent.')
        message = str(input())
        number = 'Enter your number here'
        pywhatkit.sendwhatmsg_instantly(number,message,10, tab_close=False)
        pyautogui.press('enter')

