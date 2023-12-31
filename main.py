import os
import pywhatkit
import webbrowser
import win32com.client
import speech_recognition as sr
import wikipedia
import datetime
import pyautogui
from keyboard import volumeup, volumedown
import random
from time import sleep
import speedtest
def say(script):
    """This function says out loud whatever string is given to it"""
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
            query = r.recognize_google(audio, language='en-in')
            print(f'User said: {query}\n')
            return query.lower()
        except Exception as e:
            return 'Boss I am Sorry Some error occurred I could not understand or hear you'
def Greet_Me():
    '''This function greets the user'''
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        say('Good morning,Boss')
    elif hour > 12 and hour <= 15:
        say('Good Afternoon,Boss')
    else:
        say('Good Evening,Boss')
    say('Hope you are having a good day,How can I help you?')


def Search_Google(query):
    '''This function searches google for "query" and shows the results.It also speaks out loud a summary of the results'''
    import wikipedia as googleScrap
    query = query.replace('jarvis', '')
    query = query.replace('search google for', '')
    query = query.replace('google', '')
    say('Boss ,this is what I found on Google')
    try:
        pywhatkit.search(query)
        result = googleScrap.summary(query, 3)
        say(result)
    except:
        say('Sorry Boss there is no speakable output available')


def Search_Youtube(query):
    '''This function searches YouTube for "query" and plays the most popular video/short that it finds.'''
    say('Boss this is what I found for your search on Youtube!')
    query = query.replace('jarvis', '')
    query = query.replace('search youtube for', '')
    query = query.replace('youtube', '')
    try:
        web = 'https://www.youtube.com/results?search_query=' + query
        webbrowser.open(web)
        say('Boss these are the related videos I found ,Give me a minute I am going to play the most popular one')
        pywhatkit.playonyt(query)
        say('Done Boss')
    except:
        say('Sorry Boss .Some error occurred I was not able to complete your request')


def Search_Wikipedia(query):
    '''This function searches wikipedia for "query" and speaks out loud the summary that it finds'''
    say('Searching from Wikipedia......')
    query = query.replace('jarvis', '')
    query = query.replace('search wikipedia for', '')
    query = query.replace('wikipedia', '')
    try:
        results = wikipedia.summary(query, sentences=3)
        say('According to Wikipedia ......')
        say(results)
        print(results)
    except:
        say(f'I am sorry,Boss Either I heard you wrong or there was no information for {query} on wikipedia')
password = 'jarvis approval'
lives = 5
for i in range(5):
    say('To Start say the Password')
    user_input = take_command()
    if password in user_input:
        say('Access Granted')
        Greet_Me()
        break
    else:
        say('Wrong password entered')
        lives -= 1
        say(f'You have {lives} attempts left')
if lives <= 0:
    say('Access Denied,Jarvis is going offline')
    exit()

remember = ''
while True:
    print('Listening')
    query = take_command().lower()
    if 'jarvis' in query:
        if 'the time'.lower() in query:
            Time = datetime.datetime.now().strftime('%H:%M:%S')
            say(f'Boss,the time is {Time}')
        elif 'shutdown the system' in query:
            say('Boss Are You sure You want to shutdown this computer?Reply with a yes  no')
            shutdown = take_command()
            if 'y' in shutdown:
                os.system('shutdown /s /t 1')
        elif 'fun fact' in query:
            try:
                say('Boss how many fun facts would you like?Please only say the number')
                no_of_facts = int(take_command())
                say('Boss due to presence of quotes in the fun fact.I cannot say it out loud,thus I am going to print the fun facts')
                from Fun_fact import get_fun_fact
                for i in range(1,no_of_facts +1):
                    fun_fact = get_fun_fact('')
                    try:
                        say(fun_fact)
                        print(fun_fact)
                    except:
                        say('Boss due to presence of quotes in the fun fact.I cannot say it out loud,thus I am going to print the fun facts')
                        print('fun fact')
            except:
                say('Boss due to some errors you will have to manually type down the number of fun facts you would like to read')
                no_of_facts = int(input('Enter the number of jokes,You would like to hear:'))
                from Fun_fact import get_fun_fact
                for i in range(1, no_of_facts + 1):
                    fun_fact = get_fun_fact('')
                    try:
                        say(fun_fact)
                        print(fun_fact)
                    except:
                        say('Boss due to presence of quotes in the fun fact.I cannot say it out loud,thus I am going to print the fun facts')
                        print('fun fact')
        elif 'shut down the system' in query:
            say('Boss Are You sure You want to shutdown this computer?Reply with a yes and no')
            shutdown = take_command()
            if 'y' in shutdown:
                os.system('shutdown /s /t 1')
        elif 'speed' in query:
            say('Okay Boss performing a Internet speed test')
            wifi = speedtest.Speedtest()
            upload = round(wifi.upload() / 1048576,3)
            download = round(wifi.download() / 1048576,3)
            print(f'The upload speed is {upload} mb/s')
            print(f'The download speed is {download} mb/s')
            say(f'Boss The upload speed is {upload} megabytes per second')
            say(f'and The download speed is {download} megabytes per second')
        elif 'switch window' in query:
            say('Okay Boss Switching the window')
            pyautogui.hotkey('alt','tab')
        elif 'joke' in query:
            say('Boss would like one joke or ten?')
            jokes_told = take_command()
            from jokes import present_joke
            if 'one' in query:
                present_joke('one')
            else:
                say('Ten jokes coming right up boss')
                present_joke('')
        elif 'turn off the system' in query:
            say('Boss Are You sure You want to shutdown this computer?Reply with a yes and no')
            shutdown = take_command()
            if 'y' in shutdown:
                os.system('shutdown /s /t 1')
        elif 'introduce yourself'.lower() in query:
            say('I am a virtual voice assistant developed by Mr Shivam Jha and Mr Ishan Tewari from 10 december 2023 uptill 2024,My Name stands for Just A RATHER VERY INTELLIGENT SYSTEM,I can help you with almost anything,I can help you with your school work,I can even quiz you,I am capable of face and object recognition,I can tell you the news,predict the weather and do almost everything models like Siri or Chat Gpt can do')
        elif 'go offline' in query or 'shut off' in query or 'shutdown' in query or 'shut down' in query:
            say('Okay Boss.Jarvis is going offline')
            quit()
        elif 'Pause'.lower() in query:
            pyautogui.press('k')
            say('Done,Boss.The video has been Paused')
        elif 'Play'.lower() in query:
            pyautogui.press('k')
            say('Done,Boss.The video has been Played')
        elif 'mute'.lower() in query:
            pyautogui.press('m')
            say('Done Boss,The video has been muted')
        elif 'unmute'.lower() in query:
            pyautogui.press('m')
            say('Done Boss,The video has been un-muted')
        elif 'increase the volume' in query:
            say('Boss how much percentage would you like the volume to be increase by?Please tell a even number.Only say the percentage value')
            try:
                increase_percentage = take_command()
                increase_percentage = increase_percentage.replace('percent', '')
                increase_percentage = increase_percentage.replace('percentage', '')
                increase_percentage = increase_percentage.replace('%', '')
                increase_percentage = int(increase_percentage)
                if increase_percentage % 2 != 0:
                    while increase_percentage % 2 != 0:
                        increase_percentage += 0.1
                say('Okay Boss,Turning up the volume')
                volumeup(increase_percentage)
            except:
                say('Sorry Boss ,Some error occurred Please try again')
        elif 'decrease the volume' in query:
            say('Boss how much percentage would you like the volume to be decrease by?Please tell a even number.')
            try:
                decrease_percentage = take_command()
                decrease_percentage = decrease_percentage.replace('percent', '')
                decrease_percentage = decrease_percentage.replace('percentage', '')
                decrease_percentage = decrease_percentage.replace('%', '')
                decrease_percentage = int(decrease_percentage)
                if decrease_percentage % 2 != 0:
                    while decrease_percentage % 2 != 0:
                        decrease_percentage += 1
                say('Okay Boss Turning down the volume')
                volumedown(decrease_percentage)
            except:
                say('Sorry Boss,Some error occurred please try again')
        elif 'whatsapp' in query:
            from whatsapp import sendMessage

            sendMessage()
        elif 'I am fine'.lower() in query:
            say('That is great Boss')
        elif 'tired' in query:
            say('Okay Boss Playing some songs to cheer you up')
            play_songs = True
            while play_songs:
                b = random.randint(1, 10)
                if b == 1:
                    webbrowser.open('https://www.youtube.com/watch?v=kagoEGKHZvU')
                    sleep(210)
                elif b == 2:
                    webbrowser.open('https://www.youtube.com/watch?v=623JGFAYZ3w')
                    sleep(329)
                elif b == 3:
                    webbrowser.open('https://www.youtube.com/watch?v=dawrQnvwMTY')
                    sleep(195)
                elif b == 4:
                    webbrowser.open('https://www.youtube.com/watch?v=2QdPxdcMhFQ')
                    sleep(236)
                elif b == 5:
                    webbrowser.open('https://www.youtube.com/watch?v=YkJvHe3KK2c')
                    sleep(123)
                elif b == 6:
                    webbrowser.open('https://www.youtube.com/watch?v=7aMOurgDB-o')
                    sleep(108)
                elif b == 7:
                    webbrowser.open('https://www.youtube.com/watch?v=fWRPihlt2ho')
                    sleep(90.7)
                elif b == 8:
                    webbrowser.open('https://www.youtube.com/watch?v=MENcEyD0B7w')
                    sleep(177)
                elif b == 9:
                    webbrowser.open('https://www.youtube.com/watch?v=ajIqCULzFJA')
                    sleep(116.9)
                elif b == 10:
                    webbrowser.open('https://www.youtube.com/watch?v=gjkNwuPcl50')
                    sleep(122.5)
                say('Boss Would you like me to keep playing songs?Please reply with a yes or no')
                choice = take_command()
                if 'no' in choice:
                    play_songs = False
        elif 'Thank you'.lower() in query:
            say('You are welcome ,Boss')
        elif 'open' in query:
            from Dictapp import openappweb
            openappweb(query)
        elif 'close' in query:
            from Dictapp import closeappweb
            closeappweb(query)
        elif 'Google'.lower() in query:
            Search_Google(query)
        elif 'Youtube'.lower() in query:
            Search_Youtube(query)
        elif 'Wikipedia'.lower() in query:
            Search_Wikipedia(query)
        elif 'news' in query:
            from NewsRead import latestenews

            api_key = 'Enter your API key here'
            latestenews(api_key)
        elif 'calculation' in query:
            from Calculator import calculator

            calculator()
        elif 'calculate' in query:
            from Calculator import calculator

            calculator()
        elif 'temperature'.lower() in query:
            search = 'temperature in Kolkata'
            if 'in' in query:
                query = query.replace('what is the', '')
                query = query.replace('jarvis', '')
                search = query
            from Weather_and_Temperature import Temperature_finder

            Temperature_finder(search)
        elif 'weather' in query:
            from Weather_and_Temperature import find_weather

            the_city = 'Kolkata'
            if 'in' in query:
                query = query.replace('jarvis', '')
                query = query.replace('how is the weather in', '')
                query = query.replace('what is the weather in', '')
                query = query.replace('tell me ', '')
                query = query.replace('how the weather in', '')
                query = query.replace('is', '')
                the_city = query
            find_weather(the_city)
        elif 'remember that' in query:
            query = query.replace('jarvis', '')
            query = query.replace('i want you to', '')
            query = query.replace('remember that', '')
            query = query.replace('i', 'you')
            remember += query
            say(f'OKay Boss,I wil remember {remember}')
        elif 'What do you remember' in query:
            say(f'Boss,You told me to remember that {remember}')
        elif 'forget' in query:
            say('Okay Boss I am Going to forget whatever you told me')
            remember = ''
        elif 'set an alarm' in query:
            say('Sorry Boss,due to some errors you will have to manually write down the alarm time.')
            a = input('Please give the alarm time in "HH:MM " format:')
            say('Okay Boss setting an alarm')
            from alarm import ring
            ring(a)
        elif 'Ishan' in query:
            say('Ishan is the one of my creator')
        elif 'Shivam' in query:
            say('He is one of my creator')
        elif 'Hello'.lower() or 'how are you'.lower() in query:
            say('Sorry Boss,I could not understand what you just said')