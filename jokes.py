import win32com.client
import json
import requests
def say(script):
    """This function says out loud whatever string is given to it"""
    speaker = win32com.client.Dispatch('SAPI.SpVoice')
    return speaker.Speak(script)

def present_joke(no_of_jokes):
    if 'one' in no_of_jokes:
        def jokes(f):
            data = requests.get(f)
            tt = json.loads(data.text)
            return tt
        f = r"https://official-joke-api.appspot.com/random_joke"
        a = jokes(f)
        try:
            for i in (a):
                say(i["type"])
                print(i["type"])
                say(i["setup"])
                print(i["setup"])
                say(i["punchline"])
                print(i["punchline"], "\n")
        except:
            say('Sorry Boss Due to some errors I cannot recite out the jokes so i will have to write them down')
    else:
        def jokes(f):
            data = requests.get(f)
            tt = json.loads(data.text)
            return tt
        f = r"https://official-joke-api.appspot.com/random_ten"
        a = jokes(f)
        try:
            for i in (a):
                say(i["type"])
                print(i["type"])
                say(i["setup"])
                print(i["setup"])
                say(i["punchline"])
                print(i["punchline"], "\n")
        except:
            say('Sorry Boss Due to some errors I cannot recite out the jokes so i will have to write them down')