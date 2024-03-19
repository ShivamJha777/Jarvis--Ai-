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
        if 'google' in query:
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
        elif 'disney' in query:
            query = query.replace('jarvis','')
            query = query.replace('play','')
            query = query.replace('start','')
            query = query.replace('on disney','')
            query = query.replace('hotstar','')
            query = query.replace('plus','')
            query = query.replace('+', '')
            webbrowser.open('https://www.hotstar.com/in/explore')
            time.sleep(3)
            pyautogui.moveTo(683, 554)
            time.sleep(2)
            pyautogui.click()
            time.sleep(8.5)
            pyautogui.write(query)
            time.sleep(2)
            pyautogui.press('enter')
            time.sleep(0.9)
            pyautogui.moveTo((296, 657))
            time.sleep(2.1)
            pyautogui.click()
            time.sleep(0.5)
            pyautogui.moveTo(456, 948)
            time.sleep(1)
            pyautogui.click()
            keep_continuing = True
            while keep_continuing:
                time.sleep(10)
                a = takeCommand()
                if 'wake up' in a:
                    keep_continuing = False
                    greet()
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
        elif 'homework mode' in query:
            speak('Turning on homework mode.Please include your homework pdf in the folder of this program and then enter its name.')
            name = input('Enter pdf name:')
            speak('Now please enter the start and end page')
            start = int(input('Enter start page:'))
            end = int(input('Ending page:'))
            speak('Homework mode initiated.')
            from rag_agent import agent
            while True:
                speak('What is your request?')
                request = takeCommand()
                if 'quit' in request:
                    break
                response = agent(pdf_name=name,start_page=start,end_page=end,question=request)
                response = response.replace('#','')
                speak(response)
        elif 'whatsapp' in query and 'close' not in query:
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
        elif 'horoscope' in query:
            speak("Sure boss which sign's horoscope would you like?")
            sign = takeCommand()
            sign = sign.replace('i would like','')
            sign = sign.replace('jarvis','')
            sign.replace('a','')
            sign = sign.replace('horoscope of','')
            sign = sign.replace(' ','')
            from horoscope import get_horoscope
            result = get_horoscope(sign)
            speak(f'Your horoscope says: {result}')
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
            time.sleep(4)
            pyautogui.hotkey('alt','f4')
            speak('Done boss')
        elif 'pdf' in query or 'read' in query:
            speak('Sure Boss Can you please enter the pdf path and start page?')
            name = input('Enter pdf name pls(ignore the.pdf extension):')
            start = int(input('Enter Start page:'))
            end = int(input('Enter end page:'))
            a = pdfreader(pdf_name=name,start_page=start,limit=end)
            speak('Since there is too much data thus  I think I should print it')
            print(a)
        elif 'wallpaper' in query:
            speak('Changing Wallpaper...')
            from wallpaper_changer import wallpaper_changer
            wallpaper_changer(r"C:\Users\Dell\Pictures\wallpaper_folder")
        elif 'notes' in query:
            speak('Sure Boss.Please enter the required parameters for generating the notes')
            pdf = input('Enter pdf name(Include it in the folder of this program and ignore the.pdf extension)')
            start = int(input('Enter start page:'))
            end_num = int(input('Enter the ending page:'))
            words = input('How many words per point would you like?:')
            from notes_generator import pdf_notes
            speak('Please wait a few seconds.Generating notes....')
            pdf_notes(pdf_name=pdf,start_page=start,end_page=end_num,word_per_point=words)
            speak('Notes have been typed in the word document save it where you like.')
        elif 'sleep' in query:
            keep_continuing = True
            while keep_continuing:
                time.sleep(10)
                a = takeCommand()
                if 'jarvis' in a or 'wake up':
                    keep_continuing = False
                    greet()
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
                pyautogui.press('super')
                time.sleep(0.4)
                pyautogui.write('brave')
                time.sleep(0.4)
                pyautogui.press('enter')
                time.sleep(3)
                pyautogui.hotkey('ctrl','t')
                pyautogui.click(x=1883, y=90)
                time.sleep(1)
                pyautogui.click(x=1498, y=796)
                time.sleep(1.5)
                pyautogui.click(x=366, y=522)
                time.sleep(0.9)
                pyautogui.click(x=754, y=904)
                time.sleep(0.6)
                pyautogui.click(x=1253, y=908)
                time.sleep(0.9987356)
                pyautogui.hotkey('alt','f4')
                speak('done boss , but,use icognito from next time onwards')
        elif 'joke' in query:
            speak('Sure boss,one Joke coming right up')
            speak(pyjokes.get_joke())
        elif 'open' in query:
            if '.com' in query or '.in' in query or '.org' in query:
                query = query.replace('open', '')
                query = query.replace('jarvis', '')
                query = query.replace('launch', '')
                query = query.replace(' ', '')
                speak(f'Launching {query},Boss')
                webbrowser.open(f'https://www.{query}')
            else:
                query = query.replace('open', '')
                query = query.replace('jarvis', '')
                query = query.replace('launch', '')
                query = query.replace(' ', '')
                speak(f'Ok Boss,Launching {query}')
                pyautogui.press('super')
                time.sleep(0.3)
                pyautogui.write(query)
                time.sleep(0.8)
                pyautogui.press('enter')
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
        elif 'news' in query:
            speak('Sure Boss How many News would you like?')
            news_no = int(input('Enter the number of news you would like to hear about:'))
            from news_api import news
            total_news = news(news_no)
            speak(total_news)
        elif 'quote' in query:
            from random_qoute import random_qoute
            if 'regarding' not in query and 'about' not in query:
                a = random_qoute('')
                speak(a)
            else:
                query = query.replace('jarvis','')
                query = query.replace('tell me a','')
                query = query.replace('lets hear a','')
                query = query.replace('quote','')
                query = query.replace('about','')
                query = query.replace('regarding','')
                query = query.replace(' ','')
                nigga = random_qoute(query)
                speak(nigga)
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
