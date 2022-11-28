
import datetime
import os
from Body.Speak import Speak



def time():
    Time=datetime.datetime.now().strftime('%I:%M: %p')
    Speak('It Is')
    Speak(Time)

def date():
    today=datetime.datetime.now().strftime('The date today is %d %m %Y, please note that the format is day, month, year')
    Speak(today)

def welcome():
    hour=datetime.datetime.now().hour
    if hour >=3 and hour <12:
        Speak("Good morning sir")
    if hour >=12 and hour <18:
        Speak("Good afternoon sir")
    if hour >=18 and hour <21:
        Speak("Good evening sir")
    if hour >=21 and hour <24:
        Speak("Good night and have a nice deram sir")
    if hour >=0 and hour <3:
        Speak("It is late sir, let us take a nap")
