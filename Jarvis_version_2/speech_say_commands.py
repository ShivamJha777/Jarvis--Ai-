import pyttsx3
import speech_recognition as sr
assistant = pyttsx3.init('sapi5')
voices = assistant.getProperty('voices')
for voice in voices:
    print(voice.id)
    assistant.setProperty('voice',voices[0].id)
def speak(text):
    print('')
    assistant.say(text)
    print('')
    assistant.runAndWait()
def takeCommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...',end='',flush=True)
        speak('Listening')
        command.dynamic_energy_threshold = True
        command.adjust_for_ambient_noise(source)
        audio = command.listen(source)
        try:
            print('\r',end='',flush=True)
            print('Recognizing...',end='\n',flush=True)
            query = command.recognize_google(audio,language='en-in')
            print(f'User said: {query}')
            return query.lower()
        except:
            speak('Could not understand audio,redoing operation')
            takeCommand()

