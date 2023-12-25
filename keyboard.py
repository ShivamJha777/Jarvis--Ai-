from time import sleep
from pynput.keyboard import Key,Controller
import win32com.client
keyboard = Controller()
def say(script):
    '''This function says out loud whatever string is given to it'''
    speaker = win32com.client.Dispatch('SAPI.SpVoice')
    return speaker.Speak(script)
def volumeup(percentage):
    number_of_times = percentage/2
    try:
        number_of_times = int(number_of_times)
        for i in range(number_of_times):
            keyboard.press(Key.media_volume_up)
            keyboard.release(Key.media_volume_up)
            sleep(0.1)
    except:
        say('Sorry Boss,Some error occured ,Please try again')
def volumedown(percentage):
    number_of_times = percentage/2
    try:
        number_of_times = int(number_of_times)
        for i in range(number_of_times):
            keyboard.press(Key.media_volume_down)
            keyboard.release(Key.media_volume_down)
            sleep(0.1)
    except:
        say('Sorry Boss,Some error occurred,Please try again')