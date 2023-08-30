from datetime import datetime
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import wikipedia
import webbrowser
import string
import os
import random
import datetime
import smtplib
import os

def speak(audio):
    myobj=gTTS(text=audio,lang='en',slow=True)
    myobj.save("welcome1.mp3")
    playsound("welcome1.mp3")
    
    
def takeCommand():
    # It takes microphone input and return text....
    
    r=sr.Recognizer()
    with sr.Microphone() as source:
         print("Listening...")
         r.pause_threshold = 1
         audio=r.listen(source)
    try:
        print("Recognising...")
        query=r.recognize_google(audio, language='en-in')
        print(f"User Said : {query.lower()}\n")

    except Exception as e:
        print("Say that Again pls...")
        return "none"

    return query



if __name__ == '__main__':
    speak("Ram Ram Karan.")
    while True:
        query=takeCommand().lower()


        if 'face' or 'who am i' or 'do you know me' or 'do you know who i am' in query:
            path='/media/barryallen/5a4f9633-aaad-4309-a675-d6c7f6aae0e3/face_Recognition_source_code/main_video.py'
            name = os.system(f'python3 {path}')
            
