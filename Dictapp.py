import os
import pyautogui
import webbrowser
import win32com.client
from time import sleep
def say(script):
    '''This function says out loud whatever string is given to it'''
    speaker = win32com.client.Dispatch('SAPI.SpVoice')
    return speaker.Speak(script)
dictapp = {'commandprompt':'cmd','paint':'paint','word':'winword',"excel":'excel',"chrome":'chrome','vscode':'code','powerpoint':'powerpnt','brave':'brave','pycharm':'pycharm','Whatsapp':'Whatsapp','webstorm':'webstorm'}
def openappweb(query):
    say('Launching ,Sir')
    if '.com' in query or 'co.in'in query or '.org' in query:
        query = query.replace('open','')
        query = query.replace('jarvis','')
        query = query.replace('launch','')
        query = query.replace(' ','')
        webbrowser.open(f'https://www.{query}')
    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f'start {dictapp[app]}')
def closeappweb(query):
    say('Closing,Sir')
    if 'one tab' in query or '1 tab' in query:
        pyautogui.hotkey('ctrl','w')
        say('All tabs closed boss')
    elif 'two tab' in query or '2 tab' in query:
        pyautogui.hotkey('ctrl', 'w')
        sleep(0.5)
        pyautogui.hotkey('ctrl', 'w')
        say('All tabs closed,Boss')
    elif 'three tab' in query or '3 tab' in query:
        pyautogui.hotkey('ctrl', 'w')
        sleep(0.5)
        pyautogui.hotkey('ctrl', 'w')
        sleep(0.5)
        pyautogui.hotkey('ctrl', 'w')
        say('All tabs closed,Boss')
    elif 'four tab' in query or '4 tab' in query:
        pyautogui.hotkey('ctrl', 'w')
        sleep(0.5)
        pyautogui.hotkey('ctrl', 'w')
        sleep(0.5)
        pyautogui.hotkey('ctrl', 'w')
        sleep(0.5)
        pyautogui.hotkey('ctrl', 'w')
        say('All tabs closed,Boss')
    elif 'five tab' in query or '5 tab' in query:
        pyautogui.hotkey('ctrl', 'w')
        sleep(0.5)
        pyautogui.hotkey('ctrl', 'w')
        sleep(0.5)
        pyautogui.hotkey('ctrl', 'w')
        sleep(0.5)
        pyautogui.hotkey('ctrl', 'w')
        sleep(0.5)
        pyautogui.hotkey('ctrl', 'w')
        say('All tabs closed,Boss')
    elif 'six tab' in query or '5 tab' in query:
        pyautogui.hotkey('ctrl', 'w')
        sleep(0.5)
        pyautogui.hotkey('ctrl', 'w')
        sleep(0.5)
        pyautogui.hotkey('ctrl', 'w')
        sleep(0.5)
        pyautogui.hotkey('ctrl', 'w')
        sleep(0.5)
        pyautogui.hotkey('ctrl', 'w')
        sleep(0.5)
        pyautogui.hotkey('ctrl', 'w')
        say('All tabs closed,Boss')
    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f'taskkill /f /in {dictapp[app]}.exe')