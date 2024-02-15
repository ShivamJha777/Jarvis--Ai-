import os
import win32com.client
import datetime
from time import sleep


def say(script):
    '''This function says out loud whatever string is given to it'''
    speaker = win32com.client.Dispatch('SAPI.SpVoice')
    return speaker.Speak(script)
def ring(alarm_time):
    alarm_hour = alarm_time[0:2]
    alarm_min = alarm_time[3:5]
    while True:
        now = datetime.datetime.now()
        current_hour = now.strftime("%H")
        current_min = now.strftime("%M")
        if alarm_hour == current_hour:
            if alarm_min == current_min:
                    say('Boss,The alarm is ringing')
                    os.startfile('../../carol_of_the_bells-alarm.wav')
                    sleep(30)
                    break
ring('21:38')
