import pyttsx3 #this is the text to speech conversion library
import datetime # this library is used to get date and time
import speech_recognition as sr # this library allows computer to understand human language
import pyaudio #allows computer to understand human language
import wikipedia # to fetch data from wikipedia
import webbrowser # to open urls on the webbrowser
import os #for playing music and performing your personal system related tasks
import random #used to play any random song from the list

engine = pyttsx3.init('sapi5') #Sapi5 is the technology for voice recognition and synthesis provided by Microsoft
voices = engine.getProperty('voices')
# setting female voice
#print(voices[1].id) # used to see which voice we have set for our speaking assistant
engine.setProperty('voice',voices[1].id)
#for male voice type in 0

def speak(audio):
    engine.say(audio) # say function is used to say the text computer speaks and the one we hear
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >=12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("I am Jarvis, your speaking assistant. Please tell me how may I help you")


def takeCommand(): # used to listen to the user
    # this function takes microphone input from the user and returns string output
    r = sr.Recognizer() # this function helps the computer to recognize the audio spoken by us
    with sr.Microphone() as source:
        print("Listening...") #from this the user will get to know that the computer is listening
        r.pause_threshold = 1 #seconds of non-speaking audio before a phrase is considered complete
        #taki agar hum kuch bol rahe ho to computer usko khatam na karde islie seconds badhaye
        audio = r.listen(source) #computer listens to voice of us

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said : {query}")

    except Exception as e:
        #print(e)
        print("I didn'understand, Please say again!")
        return "None"

    return query


if __name__ == '__main__':
    #speak("Kush Bhatia is the best programmer in the world!")
    wishMe()
    while True:
    #if 1:
        query = takeCommand().lower()
    #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")# now query becomes for wikipedia instead of takeCommand
            results = wikipedia.summary(query, sentences=2) #the 1st 2 sentences will be displayed from the searched wikipedia
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = "E:\\My Music"
            songs = os.listdir(music_dir) # this will list all the songs present in the written location
            print(songs)
            os.startfile(os.path.join(music_dir, random.choice(songs)))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"The time is : {strTime}")
        elif 'open pycharm' in query:
            code_path = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.3.2\\bin\\pycharm64.exe"
            os.startfile(code_path)

        elif 'quit' in query:
            exit()


