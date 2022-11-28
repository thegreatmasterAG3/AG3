import speech_recognition as sr
import os

def Listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,8) # Listening Mode...

        try:
            print("Recognizing...")
            query = r.recognize_google(audio,language="en")

        except:
            return ""

        query = str(query).lower()
        print(query)
        return query


def WakeupDetected():
   

    while True:

        queery = Listen().lower()  

        if "wake up" in queery:
            # os.startfile(r"D:\python project\AI using python\AG3.py")
            from AG3 import MainExecution
            MainExecution()
            

        else:
            pass


# WakeupDetected()

    