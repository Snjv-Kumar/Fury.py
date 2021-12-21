import datetime
import os


import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser




engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[1].id)
engine.setProperty("voice",voices[1].id)









def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good afternoon")
    else:
        speak("Good evening")

    speak("I am taniya, please tell me how may i help you")

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("recognizing..")
        query=r.recognize_google(audio,language='en-in')
        print("user said : ",query)
    except Exception as e:
        print(e)
        print("say that again..")
        return "None"
    return query



if __name__=="__main__":
    wishme()
    while True:
        query=takecommand().lower()

        if "wikipedia" in query:
            speak("searching wikipedia...")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=1)
            speak("according to wikipedia")
            print("results")
            speak(results)
        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")
        elif "the time" in query:
            strtime=datetime.datetime.now().strftime("%H,%M,%S")
            speak("time is :",strtime)
        elif "open pycharm" in query:
            pycharm= "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\JetBrains"
            os.startfile(pycharm)


