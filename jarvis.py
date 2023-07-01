import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=20 and hour<4 :
        speak('Good Night')

    elif hour>=4 and hour<12 :  
        speak("Good Morning")

    elif hour>=12 and hour<18 :
        speak('Good Afternoon')

    else : speak('Good Evening')

    speak("Hello Akant Sir... I am Jarvis.... Your Desktop Assistant")
    speak("How may i help you sir")

def takeCommand():
    #it takes microphone input from the user and returns String output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print("User Said: ", query )

    except Exception as e:
        print(e)

        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()
        #logic for Executing task based on query
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace('wikipedia',"")
            results = wikipedia.summary(query,sentences=2)
            speak('According to wikipedia')
            speak(results)

        elif 'quit' in query:
            speak('goodbye Akant... i quit')
            exit()

    