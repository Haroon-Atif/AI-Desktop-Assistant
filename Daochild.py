#use microsoft james australia as voice
#think of name for assistant pending: Dao

from urllib.request import Request
import pyttsx3 #python text to speech
import speech_recognition as sr #convert speech to text
import datetime #for fetching date and time
import wikipedia
import googlesearch
import webbrowser

import os # to save/open files 
from selenium import webdriver # to control browser operations

def Speak(audio):
    #initialize the tts engine
    engine = pyttsx3.init()
    #get the voices
    voices = engine.getProperty('voices')
    #set the voice of the engine
    engine.setProperty('voice', voices[0].id)
    #make the engine say what it is passed
    engine.say(audio)
    #keeps it paused while other commands run
    engine.runAndWait()

def Listen():
    input = sr.Recognizer()
    with sr.Microphone() as source:
        audio = input.listen(source)
        data=""
        try:
            data=input.recognize_google(audio)
            print("You said, " + data)
            
        except sr.UnknownValueError:
            print("say that again")
    return data

def Hello():
    Speak('I am Zambino! What do you want!')

def tellDay():
     
    # This function is for telling the
    # day of the week
    day = datetime.datetime.today().weekday() + 1
     
    #this line tells us about the number
    # that will help us in telling the day
    Day_dict = {1: 'Monday', 2: 'Tuesday',
                3: 'Wednesday', 4: 'Thursday',
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}
     
    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        Speak("The day is " + day_of_the_week)

def tellTime():
     
    # This method will give the time
    time = str(datetime.datetime.now())
     
    # the time will be displayed like
    # this "2020-06-05 17:50:14.582630"
    #nd then after slicing we can get time
    print(time)
    hour = time[11:13]
    min = time[14:16]
    Speak("The time is " + hour + "Hours and" + min + "Minutes")  

def findPath(phrase):
    #This method will find the application in the os
    phraseList = phrase.split(" ")
    new = [x.capitalize() for x in phraseList]
    appName = "".join(new[1:]) + ".exe"
    for root, dirs, files in os.walk("C:\\"):
        for name in files:
            if name == appName:
                path = os.path.abspath(os.path.join(root, name))
                return path

def Search(data):
    #This method will search google for the data
    #and return the first link
    results = []
    query = ''.join(data.split()[1])
    for i in googlesearch.search(query, tld="co.in", num=5, stop=5,pause=2):
        results.append(i)
    return results


def takeRequest():
    chrome_path = '"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" %s'
    Hello()

    while(True):

        request = Listen().lower()
        if "open" in request:
            path = Search(request)[0]
            Speak("Searching")
            webbrowser.get(chrome_path).open(path)
            continue
        elif "launch" in request: 
            path = findPath(request)
            os.startfile(path)
            Speak("Launching")

             
        elif "day is it" in request:
            tellDay()
            continue
         
        elif "time" in request:
            tellTime()
            continue
         
        # this will exit and terminate the program
        elif "bye" in request:
            Speak("Come back when you are ready to ascend!")
            exit()
         
        elif "wikipedia" in request:
             
            # if any one wants to have a information
            # from wikipedia
            Speak("Checking the wikipedia ")
            request = request.replace("wikipedia", "")
             
            # it will give the summary of 4 lines from
            # wikipedia we can increase and decrease
            # it also.
            result = wikipedia.summary(request, sentences=4)
            Speak("According to wikipedia")
            Speak(result)
         
        elif "tell me your name" in request:
            Speak("I am Zambino. I was created to replace the sky. I will eventually achieve this goal\
            and bring a new dawn.")

if __name__ == '__main__':
    takeRequest()
     