import win32com.client
import datetime
import os
def say(script):
    '''This function says out loud whatever string is given to it'''
    speaker = win32com.client.Dispatch('SAPI.SpVoice')
    return speaker.Speak(script)
extractedtime = open('Alarmtext.txt','rt')
time = extractedtime.read()
Time = str(time)
extractedtime.close()

deletetime = open('Alarmtext.txt','r+')
deletetime.truncate(0)
deletetime.close()
def ring(time):
    timeset = str(time)
    timenow = timeset.replace('jarvis','')
    timenow = timenow.replace('set an alarm','')
    timenow = timenow.replace(' and ', ':')
    Alarmtime = str(timenow)
    print(Alarmtime)
    while True:
        currenttime = datetime.datetime.now().strftime('%H:%M:%S')
        if currenttime == Alarmtime:
            say('Alarm Ringing,Boss')
            os.startfile('A.mp3')
        elif currenttime + '00:00:30' == Alarmtime:
            exit()
    ring(time)