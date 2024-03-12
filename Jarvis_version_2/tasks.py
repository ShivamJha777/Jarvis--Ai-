from wikipedia import wikipedia
import time
from speech_say_commands import *
import webbrowser
import pyautogui
import pywhatkit
import pyjokes
from nltk.corpus import wordnet
import datetime
from Jarvis_version_2.pdfreader import pdfreader
from Jarvis_version_2.location import get_location
def greet():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('Good Morning,Boss!How can I help you today?')
    elif hour >= 12 and hour < 21:
        if hour <= 18:
            speak('Good Evening,Boss!What would you like me to do?')
        else:
            speak('Looks like it is already night time!Time goes quite fast anyways what would you like me to do?')
    else:
        speak('It is quite late but anyways how would you like me to assist you?')
def task_completeion():
    greet()
    while True:
        #query = input("What would you like to do? ").lower()
        query = takeCommand()
        if 'youtube' in query and 'play' not in query:
            query = query.replace('jarvis', '')
            query = query.replace('for', '')
            query = query.replace('in youtube', '')
            query = query.replace('search','')
            try:
                web = 'https://www.youtube.com/results?search_query=' + query
                webbrowser.open(web)
                speak('Boss this is what I found on youtube do want me to open the video which I think is the most relative to the topic?')
                choice = takeCommand().lower()
                if 'y' in choice or 'sure' in choice or 'why not' in choice or 'would love to' in choice:
                    speak('Ok Boss Give me a few seconds I will play the video most relevant to the topic')
                    pywhatkit.playonyt(query)
                speak('Done Boss')
            except:
                speak('Sorry Boss .Some error occurred I was not able to complete your request')
        elif 'google' in query:
            query = query.replace('jarvis', '')
            query = query.replace('search', '')
            query = query.replace('for', '')
            query = query.replace('in', '')
            query = query.replace('google', '')
            speak('Boss ,this is what I found on Google')
            try:
                pywhatkit.search(query)
                result = wikipedia.summary(query, 3)
                speak(result)
            except:
                speak('Sorry Boss there is no speakable output available')
        elif 'play' in query:
            query = query.replace('jarvis','')
            query = query.replace('play','')
            query = query.replace('can you','')
            query = query.replace('on youtube','')
            query = query.replace('i want you to play','')
            query = query.replace('please','')
            try:
                web = 'https://www.youtube.com/results?search_query=' + query
                webbrowser.open(web)
                speak('Boss this is what I found on Youtube ,am playing what I think is the most relevant video')
                pywhatkit.playonyt(query)
            except:
                speak('Sorry Boss,Some error occurred')
        elif 'whatsapp' in query:
            query = query.replace('jarvis','')
            query = query.replace('whatsapp','')
            query = query.replace('send a','')
            query = query.replace('to','')
            query = query.replace('message','')
            speak('On it boss')
            pyautogui.press('super')
            time.sleep(0.9)
            pyautogui.write('whatsapp')
            time.sleep(0.9)
            pyautogui.press('enter')
            time.sleep(4.98)
            pyautogui.write(query)
            time.sleep(1.98)
            pyautogui.press('down')
            time.sleep(0.7)
            pyautogui.press('enter')
            speak(f'Boss what message would you like to send to {query}?')
            message = takeCommand().lower()
            message = message.replace('i','he')
            message = message.replace('want him to know','')
            pyautogui.write(f'Hello {query}!I am J.A.R.V.I.S and my boss  wants you to know that {message}')
            time.sleep(0.6)
            pyautogui.press('enter')
            time.sleep(0.2)
            speak('Message sent successfully')
            pyautogui.hotkey('alt','f4')
        elif 'screenshot' in query:
            pywhatkit.take_screenshot('screenshot')
            speak('Screenshot taken')
        elif 'tab' in query:
            if 'open' in query:
                pyautogui.hotkey('ctrl','t')
                speak('Tab opened')
            else:
                pyautogui.hotkey('ctrl', 'w')
                speak('Tab closed')
        elif 'close' in query:
            speak('On it Boss')
            query = query.replace('close','')
            query = query.replace('jarvis','')
            pyautogui.press('super')
            time.sleep(0.3)
            pyautogui.write(query)
            time.sleep(0.2)
            pyautogui.press('enter')
            speak('Please wait for a few seconds dont switch the window')
            time.sleep(7)
            pyautogui.hotkey('alt','f4')
            speak('Done boss')
        elif 'pdf' in query or 'read' in query:
            speak('Sure Boss Can you please enter the pdf path?')
            file = input('Enter file path:')
            a = pdfreader(file,start_file=False)
            speak('Since there is too much data thus  I think I should print it')
            print(a)
        elif 'location' in query or 'where am i' in query:
            speak('Collecting required data')
            a = get_location()
            speak(f'Boss the {a}')
        elif 'new window' in query:
            pyautogui.hotkey('ctrl', 'n')
            condition = False
            speak('Should I open more windows,Boss?')
            choice = takeCommand()
            if 'y' in choice or 'sure' in choice:
                condition = True
            while condition:
                pyautogui.hotkey('ctrl', 'n')
                condition = False
                speak('Should I open more windows,Boss?')
                choice = takeCommand()
                if 'y' in choice or 'sure' in choice:
                    condition = True
        elif 'history' in query:
            if 'show' in query or 'open' in query:
                time.sleep(3)
                pyautogui.hotkey('ctrl', 'h')
                speak('Done boss')
            else:
                speak('Come on Boss, use icognito mode ,man,anyways I will delete it')
                pyautogui.keyDown('ctrl')
                time.sleep(0.8)
                pyautogui.keyDown('shift')
                time.sleep(0.9)
                pyautogui.press('delete')
                time.sleep(1)
                pyautogui.keyUp('ctrl')
                time.sleep(0.9)
                pyautogui.keyUp('shift')
                time.sleep(0.8)
                pyautogui.press('enter')
                speak('done boss , but, use icognito from next time onwards')
        elif 'joke' in query:
            speak('Sure boss,one Joke coming right up')
            speak(pyjokes.get_joke())
        elif 'temperature' in query:
            default_city = 'Kolkata'
            if 'in' in query:
                query = query.replace('jarvis','')
                query = query.replace('what is the','')
                query = query.replace('how much is the','')
                query = query.replace('temperature in','')
                default_city = query
            from jarvis_version_1.features.Weather_and_Temperature import Temperature_finder
            temperature = Temperature_finder(default_city)
            speak(f'The temperature of {default_city} is {temperature}')
        elif 'weather' in query:
            default_city = 'Kolkata'
            if 'in' in query:
                query = query.replace('jarvis', '')
                query = query.replace('tell me the', '')
                query = query.replace('how is the', '')
                query = query.replace('weather', '')
                query = query.replace('of','')
                query = query.replace('in','')
                default_city = query
            speak(f'Okay boss Presenting a table of weather forecast for {default_city} over the next 3 days')
            from jarvis_version_1.features.Weather_and_Temperature import find_weather
            forecast = find_weather(default_city)
            print(forecast)
        elif 'what is' in query and 'synonym' not in query:
            query = query.replace('what is','')
            query = query.replace('jarvis','')
            try:
                syns = wordnet.synsets(word)
                meaning = syns[0].definition()
                speak(f'The meaning of {word} is {meaning}')
            except:
                result = wikipedia.summary(query, 2)
                speak(f'According to Wikipedia.....{result}')
        elif 'who is' in query:
            query = query.replace('who is', '')
            query = query.replace('jarvis', '')
            result = wikipedia.summary(query, 2)
            speak(f'According to Wikipedia.....{result}')
        elif 'meaning' in query:
            query = query.replace('jarvis','')
            query = query.replace('meaning', '')
            query = query.replace('meanings', '')
            query = query.replace('jarvis', '')
            query = query.replace('what is the', '')
            query = query.replace('of', '')
            query = query.replace('tell me the','')
            query = query.replace(' ','')
            word = query
            syns = wordnet.synsets(word)
            try:
                meaning = syns[0].definition()
                speak(f'The meaning of {word} is {meaning}')
            except IndexError:
                speak("No meanings found")
            try:
                a = syns[0].examples()
                example = a[0]
                speak(f"Examples of {word} in use::")
                speak(example)
            except:
                speak("No examples found")
        elif 'terminate' in query:
            speak('Okay boss,Jarvis is going offline')
            exit()
        elif 'synonym' in query:
            from test2 import synonym
            query = query.replace('jarvis', '')
            query = query.replace('synonym', '')
            query = query.replace('synonyms', '')
            query = query.replace('jarvis', '')
            query = query.replace('what is the', '')
            query = query.replace('of', '')
            query = query.replace('tell me the', '')
            query = query.replace(' ','')
            from test2 import synonym
            synonym(query)
        else:
            speak('Outta my limits')
task_completeion()
