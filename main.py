import win32com.client
import speech_recognition as sr
import webbrowser
def say(script):
    '''This fucntion says out loud whatever string is given to it'''
    speaker = win32com.client.Dispatch('SAPI.SpVoice')
    return speaker.Speak(script)
say('Hello! Welcome to Jarvis AI')
def take_command():
    '''This function takes voice input from the user'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.5
        audio = r.listen(source)
        try:
            print('Recognizing')
            query = r.recognize_google(audio, language= 'en-in')
            print(f'User said: {query}')
            return query
        except Exception as e:
            return 'Some Error Occurred. Sorry from Jarvis'
while True:
    print('Listening')
    say('Listening')
    query = take_command()
    say('Command accepted')
    say(query)
    sites = [['youtube','https://www.youtube.com'],['wikipedia','https://www.wikipedia.com'],['google','https://www.google.com'],['quora','https://www.quora.com'],['facebook','https://www.facebook.com'],['Github','https://www.github.com'],['Reddit','https://www.reddit.com'],['Discord','https://www.discord.com'],['Instagram','https://www.instagram.com'],['Netflix','https://www.Netflix.com'],['Spotify','https://www.Spotify.com']]
    for site in sites:
        if  f'Open {site[0]}'.lower() in query.lower():
            say(f'Opening {site[0]}')
            webbrowser.open(site[1])
    if 'stop'.lower() in query.lower():
        say('Okay Sir,Jarvis is turning off')
        quit()