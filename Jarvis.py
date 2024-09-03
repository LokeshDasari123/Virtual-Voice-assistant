import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import psutil
import pywhatkit as kit
from selenium import webdriver
from selenium.webdriver import chrome
import ctypes
import requests



engine=pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    speak("hello")
    hour=datetime.datetime.now().hour
    if hour>=6 and hour<12:
        speak("good morning")
    elif hour>=12 and hour<18:
        speak("good afternoon")
    elif hour>=18 and hour<21:
        speak("good evening")
    else:
        speak("good night")
    time()
    date()

def time():
    Time=datetime.datetime.now().strftime("%H:%M")

def date():
    year=int(datetime.datetime.now().year)
    month=int(datetime.datetime.now().month)
    date=int(datetime.datetime.now().day)
    now = datetime.datetime.now()
    print(now.strftime("today is " +"%A"))
    speak(now.strftime("today is " +"%A"))
    if now.strftime("%A")=='Monday':
        speak("classes are Python, C plus plus, design and analysis of algorithms")
    elif now.strftime("%A")=='Tuesday':
        speak("classes are Python, C plus plus, design and analysis of algorithms")
    elif now.strftime("%A")=='wednesday':
        speak("classes are Python, C plus plus, design and analysis of algorithms")
    elif now.strftime("%A")=='Thursday':
        speak("classes are Python, C plus plus, design and analysis of algorithms")
    elif now.strftime("%A")=='Friday':
        speak("classes are Python, C plus plus, design and analysis of algorithms")
    elif now.strftime("%A Python, C plus plus, design and analysis of algorithms")=='Saturday':
        speak("classes are Python, C plus plus, design and analysis of algorithms")
    elif now.strftime("%A")=='Sunday':
        speak("Today you are freebird")
    print("iam jarvis. How can i help you")
    speak("iam jarvis. How can i help you")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold=1.2
        audio=r.listen(source)
    
    try:
        print("recognizing...")
        query=r.recognize_google(audio, language='en-in')
        print(query)
    
    except Exception as e:
        print(e)
        speak("say that again")
        return "None"
    
    return query

def location():
    ip_add=requests.get('https://api.ipify.org').text
    url='https://get.geojs.io/v1/ip/geo/'+ip_add+'.json'
    geo_q=requests.get(url)
    geo_d=geo_q.json()
    state=geo_d['city']
    country=geo_d['country']
    speak(f"sir,you are now in {state,country}.")
    print(f"sir,you are now in {state,country}.")

def battery():
    battery=psutil.sensors_battery()
    speak("battery is")
    speak(battery.percent)



if __name__=="__main__":
    wishme()
    while True:
        query=takeCommand().lower()
        
        if 'time' in query:
            time()

        elif 'good morning' in query:
            now = datetime.datetime.now()
            print(now.strftime("today is" +"%A"))
            speak(now.strftime("today is" +"%A"))

        elif 'date' in query:
            date()

        elif 'wikipedia' in query:
            speak("searching...")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=2)
            print(result)
            speak(result)

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")
 
        elif 'fine' in query:
            speak("It's good to know that your fine")
 
        elif "change name" in query:
            speak("What would you like to call me, Sir ")
            assistantname = takeCommand()
            speak("Thanks for naming me")
 
        elif "what's your name" in query or "What is your name" in query:
            speak("My friends call me")
            speak(assistantname)
            print("My friends call me", assistantname)

        elif 'open youtube' in query:
            wb.register('chrome', None)
            wb.open('https://www.youtube.com')

        elif 'open whatsapp' in query:
            wb.register('chrome', None)
            wb.open('https://web.whatsapp.com')

        elif 'search in chrome' in query:
            speak("what should i search")
            search=takeCommand().lower()
            wb.open(f"{search}")
            
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")

        elif 'restart' in query:
            os.system("shutdown /r /t 1")

        elif 'lock my window' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif 'battery usage' in query:
            battery()

        elif 'search on youtube' in query:
            speak("what should i search")
            search=takeCommand()
            kit.playonyt("https://www.youtube.com/results?search_query=" +search)
        
        elif 'play music' in query.lower():
            songs_dir="D:\\music"
            songs=os.listdir(songs_dir)
            print(songs)
            os.startfile(os.path.join(songs_dir,songs[0]))

        elif "location" in query:
            location()

        elif 'offline' in query:
            speak("good bye... Have a nice day")
            quit()
        
        