import speech_recognition as sr
import random
from num2words import num2words
from subprocess import call
import requests
import os

import sys
# obtain audio from the microphone

def talker(sentence):
    cmd = 'flite -voice kal16 -t "' + sentence + '"'
    os.system(cmd)
    

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

cont = True
while cont:
    try:
        if "hello" in r.recognize_google(audio):
            talker("hello what can i do for you?")
            with sr.Microphone() as source:
                print("Say something!")
                audio = r.listen(source)

    
        elif "start" in r.recognize_google(audio):
            talker("Here are the files in your directory")
            os.system("ls")
            with sr.Microphone() as source:
                print("What next!")
                audio = r.listen(source)
        
        elif "stop" in r.recognize_google(audio):
            talker("Goodbye sir have a nice day")
            cont = False
    
        
        elif "open" in r.recognize_google(audio):
            talker("What website would you like to visit")
            with sr.Microphone() as source:
                print("What next!")
                audio = r.listen(source)
            
            site = r.recognize_google(audio)
            talker("Now launching " + site + " on chrome")
            os.system('ddgr -j "'  + site + '"')
        
    
        else:
            talker(r.recognize_google(audio))
            with sr.Microphone() as source:
                print("Say something!")
                audio = r.listen(source)

    except sr.UnknownValueError:
        talker("could not understand audio")
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)
    
    except sr.RequestError as e:
        talker("Could not request results from Google Speech Recognition service")
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)
