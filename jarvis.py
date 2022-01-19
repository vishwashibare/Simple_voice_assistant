import pyttsx3  # this is module by which the computer can recognise our sound
import datetime # this is for giving time
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
from pygame import mixer



engine = pyttsx3.init('sapi5') # it is to initiliaze the module or voice system
voices = engine.getProperty('voices')  # here we are giving the voice
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def sound():
    mixer.init()
    mixer.music.load("google_sound.mpeg")
    mixer.music.play()

def wishme():
    hour = int(datetime.datetime.now().hour) # it will provide us the time in hours
    if hour>=0 and hour<12:
        speak("Good morning")
    elif hour>=12 and hour<18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    
    speak("I am Jarvis sir . How can I help You")

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com,587')
    server.ehlo()
    server.starttls()
    server.login('vishwashibare29@gmail.com','vishuprem615')
    server.sendmail('vishwashibare29@gmail.com',to,content)
    server.close()
    
def takeCommand():# it takes the command from user as audio format
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        sound()
        r.pause_threshold = 1 
        audio = r.listen(source) # this is the command by which the AI is listening
    try:
        print("Recognizing..")
        query = r.recognize_google(audio,language='en-in') # here our {audio} is getting recognized by google engine
        print(f"user said: {query}\\n")
    
    except Exception as e:
       # print(e)
        speak("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower() # Here we have converted the command ie our voice 
        
        #Logic for excuting the programme
        if 'wikipedia' in query:
            speak('searching wikipedia....')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentence = 2) # here that much sentence will be spoken by the AI
            speak("According to wikipedia")
            speak(results)
            
        elif 'hello jarvis' in query:
            speak("Hello sir")
            
        elif 'how are you' in query:
            speak("fine sir...")
            
        # for opening Youtube
        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")
            
        # for opening google
        elif 'open google' in query:
            webbrowser.open("www.google.com")
            
        # for opening Stackoverflow website
        elif 'open stackoverflow' in query:
            webbrowser.open("www.stackoverflow.com")
            
        # to open the github repo
        elif 'open GitHub repository' in query:
            webbrowser.open("www.github.com")
        
        elif 'whatsapp' in query:
             speak("Where do  you want to open it. In website or system software ")
             query = takeCommand().lower()
             if 'website' in query:
                webbrowser.open('www.whatsapp.com')
             elif 'system software' and 'system'and 'software' in query:
              try:
                os.startfile('C:\\Users\\LEGION\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\WhatsApp')
                speak("Sorry sir I am a learning ROBO please do the further task by yourself ")
              except Exception as e:
                  speak("Sorry sir as I am a learning robo i could not open it please do it by yourself")
               
               
        elif 'play music' in query:
          #  music_dir = "" # here is the directory of songs which present in the our system
          #  songs = os.listdir(music_dir) # this command gives the all the list of files inside the folder
          #  print(songs)
          #  os.startfile(os.path.join(music_dir,songs[0])) #here it will open the 1st file as {song[0]} is given
             webbrowser.open("www.spotify.com")
             
            
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime} ")
            
        elif 'open code' in query:
            code_path = "C:\\Users\\LEGION\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)
            
        elif 'email to vishwas' in query:
            try:
                speak("What should I say.?")
                content = takeCommand() # here we are sharing the content
                to = "vishwashibare29@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry my friend harry bhai. I am not able to send this email")
        
        elif 'quit' and 'stop' and 'exit' in query:
           speak("Thanks you")
           break
    
            
            


            
        
        
    
