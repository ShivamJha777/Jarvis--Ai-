import os
import pyautogui
import webbrowser
import speech_recognition as sr
from time import sleep
def take_command():
    '''This function takes voice input from the user'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.7
        r.energy_threshold = 500
        audio = r.listen(source)
        try:
            say('Recognizing')
            query = r.recognize_google(audio, language='en-in')
            print(f'User said: {query}\n')
            return query.lower()
        except Exception as e:
            return 'Boss I am Sorry Some error occurred I could not understand or hear you'

import win32com.client
from time import sleep
did_Find_App = False
def say(script):
    '''This function says out loud whatever string is given to it'''
    speaker = win32com.client.Dispatch('SAPI.SpVoice')
    return speaker.Speak(script)
def openappweb(query):
    if '.com' in query or 'co.in'in query or '.org' in query:
        query = query.replace('open','')
        query = query.replace('jarvis','')
        query = query.replace('launch','')
        query = query.replace(' ','')
        say(f'Launching {query},Boss')
        webbrowser.open(f'https://www.{query}')
    elif 'tab' in query:
        say('Boss How many tabs would you like to open?Please only say the number of tabs')
        try:
            tab = int(take_command())
            tab += 1
            for i in range(tab):
                pyautogui.hotkey('ctrl', 'w')
        except:
            say('Sorry Boss Some error occurred you will have to manually enter the number of tabs to be closed')
            tab = int(input('Enter the number of tabs you want to open:'))
            tab += 1
            sleep(4)
            num = 0
            while num != tab:
                pyautogui.hotkey('ctrl', 't')
                num += 1
        say('All Tabs Opened  Boss')
    else:
        query = query.replace('open','')
        query = query.replace('jarvis','')
        pyautogui.press('super')
        pyautogui.typewrite(query)
        pyautogui.press('enter')
def closeappweb(query):
    if 'tab' in query:
        say('Boss How many tabs would you like to close?Please only say the number of tabs')
        try:
            tab = int(take_command())
            tab += 1
            say('Boss Please switch to your browser window so I can add the tabs')
            sleep(3)
            for i in range(tab):
                pyautogui.hotkey('ctrl','w')
        except:
            say('Sorry Boss Some error occurred you will have to manually enter the number of tabs to be closed')
            tab = int(input('Enter the number of tabs you want to close:'))
            tab += 1
            say('Boss PLease switch to the browser window so I can close the tabs')
            num = 0
            sleep(4)
            while num != tab:
                pyautogui.hotkey('ctrl', 'w')
                num += 1
        say('All Tabs Closed Boss')
    elif 'window' in query:
        say('Okay Boss Please switch to the window you would like to close')
        sleep(2)
        say('Closing The current open window')
        pyautogui.hotkey('alt','f4')
    else:
        query = query.replace('jarvis','')
        query = query.replace('close','')
        query = query.replace('please','')
        query = query.replace('i','')
        query = query.replace('for me','')
        query = query.replace('can you','')
        query = query.replace('want you to','')
        os.system(f'taskkill /f /im {query}.exe')