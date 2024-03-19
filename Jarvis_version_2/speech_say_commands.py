import time

import pyttsx3
import speech_recognition
assistant = pyttsx3.init('sapi5')
voices = assistant.getProperty('voices')
for voice in voices:
    print(voice.id)
    assistant.setProperty('voice',voices[0].id)
    assistant.setProperty('rate',200)
def speak(text):
    print('')
    assistant.say(text)
    print('')
    assistant.runAndWait()
def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.adjust_for_ambient_noise(source)
        r.non_speaking_duration = 0.6
        r.pause_threshold = 1
        audio = r.listen(source,phrase_time_limit= 6.8)
    try:
        print("Understanding..")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return 'None'
    return query.lower()