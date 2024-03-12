import pywhatkit
import win32com.client
import speech_recognition as sr
from datetime import timedelta
from datetime import datetime
import pyautogui
from time import sleep
contact_list = [['sonu','+919674298550'],['harsh','+918820017190'],['ishan','+917003065311'],['shreyan','+919874314434'],['mummy','+918017233852']]

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
    say('Boss Who do you want to message?')
    person = take_command()
    found = False
    for contact in contact_list:
        if contact[0] in person:
            number = contact[1]
            found = True
            break
    if found == False:
        say('Sorry,Boss I could not find the person you just messaged')
        exit()
    say('What is the message?Only say the message whatever you say next will be sent.')
    message = take_command()
    pywhatkit.sendwhatmsg_instantly(number, '', 5, tab_close=False)
    sleep(45)
    pyautogui.typewrite(message)
    sleep(3)
    pyautogui.press('enter')
    say('Done')
