import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui 
import psutil
import pyjokes

engine = pyttsx3.init(driverName='espeak')
engine.setProperty('rate', 160)
engine.setProperty('volume', 8)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The Current time is ")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("Today's Date is ")

    speak(date)
    speak(month)
    speak(year)

def wishMe():
    speak("Welcome")
    hour = datetime.datetime.now().hour
    if hour >=6 and hour<12:
        speak("Good Morning Sir")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir")

    else:
        speak("Good Evening Sir")

    time()
    date()
    speak("Jarvis At your Service. Please tell me how can i help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising....")
        query = r.recognize_google(audio, language='en-in')
        print(query)

    except Exception as e:
        print(e)
        speak("Say that Again Please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('xyz@gmail.com', '1234567890')
    server.sendmail('xyz@gmail.com', to, content)
    server.close()

def screenShot():
    img = pyautogui.screenshot()
    img.save()

def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at ' + usage)
    battery = psutil.sensors_battery()
    speak('Battery is at ')
    speak(battery.percentage)

def jokes():
    speak(pyjokes.get_joke())

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if "time" in query:
            time()

        elif "date" in query:
            date()

        elif "wikipedia" in query:
            speak("searching..")
            query = query.replace('wikipedia', '')
            result = wikipedia.summary(query, sentence = 2)
            print(result)
            speak(result)
        
        elif 'send email' in query:
            try:
                speak("What Should i say")
                content = takeCommand()
                to = 'qwert@gmail.com'
                sendEmail(to, content)
                speak("Email has been Sent")

            except Exception as e:
                print(e)
                speak("unable to send Email")

        elif 'search in chrome' in query:
            speak("What Should i Search?")
            chromePath = 'Enter Your Chrome Path'
            search = takeCommand().lower()
            wb.get(chromePath).open_new_tab(search + '.com')

        elif 'logout' in query:
            os.system('shutdown -l')

        elif 'shutdown' in query:
            os.system('shutdown /s /t 1')

        elif 'restart' in query:
            os.system('shutdown /r /t 1')

        elif 'play songs' in query:
            songs_dir = 'Enter Your Song Directory Path'
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))

        elif 'remember that' in query:
            speak("What should i remember")
            data = takeCommand()
            speak("You Said me to remember that " + data)
            remember = open('data.txt', 'w')
            remember.write(data)
            remember.close()

        elif 'do you know anything' in query:
            remember = open('data.txt', 'r')
            speak('you said me to remember that ' + remember.read())

        elif 'screenshot' in query:
            screenShot()
            speak("Done!")

        elif 'cpu' in query:
            cpu()

        elif 'joke' in query:
            jokes()
        
        elif "offline" in query:
            speak("Going Offline")
            quit 

        
