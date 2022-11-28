from Brain.AIBrain import ReplyBrain
from Brain.Qna import QuestionsAnswer
from Body.Listen import MicExecution
print(">> Starting The AG3 : Wait For Some Seconds.")
from Body.Speak import Speak
from Main import MainTaskExecution


def MainExecution():

    # Speak("Hello Sir")
    # Speak("I am AG3, I'm Ready To Assist You Sir.")
    from Features.Feature import welcome
    welcome()

    while True:

        Data = MicExecution()
        Data = str(Data)
        
        ValueReturn = MainTaskExecution(Data)

        if ValueReturn==True:
            pass

        elif len(Data)<=1:
            pass

        elif 'you need a break' in Data:
            Speak("Ok Sir , You can call me anytime !")
            from Features.Wakeup import WakeupDetected
            WakeupDetected()

        elif "time" in Data:
            from Features.Feature import time
            time()

        elif "date" in Data:
            from Features.Feature import date
            date()
            

        elif "turn on the tv" in Data: # Specific Command
            Speak("ok..  Turning On The Android Tv")

        elif "what is" in Data or "where is" in Data or "question" in Data or "answer" in Data:
            Reply = QuestionsAnswer(Data)

        # elif "space news" in Data:
        #     Speak("Tell Me The Date For News Exteacting Process .")
        #     Date = Takecommand()

        #     from Features.DateCon import DateConverter
        #     Value = DateConverter(Date)
        #     from Features.Nasa import NasaNews
        #     NasaNews(Value)

        else:
            Reply = ReplyBrain(Data)
            Speak(Reply)

MainExecution()


# def ClapDetect():
#     query = Tester()

# ClapDetect()

# def WakeUp():
#     query = WakeupDetected()

# WakeUp()


