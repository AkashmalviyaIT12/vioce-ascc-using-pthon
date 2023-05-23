import pyttsx3 
import speech_recognition as sr 
import datetime 
import wikipedia 
import webbrowser 
import os  
import pyjokes 
import ctypes
import subprocess
import wolframalpha
import win32com.client as wincl 
from urllib.request import urlopen

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")
    speak("i am your jalax. please tell me how may help you")

def takeCommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        command.pause_threshold = 1
        audio = command.listen(source)
        try:
            print("Recognizing...")
            query = command.recognize_google(audio)
            print(f"user said: {query}")

        except Exception as e:
            print("Say that again please...")
            return "None"
    return query

def taskExe():
    while True:
        query = takeCommand()
        if 'hello' in query:
            speak("hello sir , i am jalax .")
            speak("your persinal Al assistant!")

        elif 'kya hal hai' in query:
            speak("ham mast hai aap kasa ho..")

        elif 'tell me a t g name' in query:
            speak("TG name is sanjay saini. ")
            speak("sanjay sir is 6th sem TG")
            speak("Asst Professor	 UG joining date	01/08/2021	Department of IT")

        elif 't g name' in query:
            speak("TG name is sanjay saini. ")
            speak("sanjay sir is 6th sem TG")
            speak("Asst Professor	 UG joining date	01/08/2021	Department of IT")

        elif 'TG name' in query:
            speak("TG name is sanjay saini. ")
            speak("sanjay sir is 6th sem TG")
            speak("Asst Professor	 UG joining date	01/08/2021	Department of IT")

        elif 'PG name' in query:
            speak("TG name is sanjay saini. ")
            speak("sanjay sir is 6th sem TG")
            speak("Asst Professor	 UG joining date	01/08/2021	Department of IT")

        elif 'Coding mam' in query:
            speak("sini shibbu mam is a python expert in a oriental college of technology.. ")
            speak("sini mam is  a help all student in python")

        elif 'Coding map' in query:
            speak("sini shibbu mam is a python expert in a oriental college of technology.. ")
            speak("sini mam is  a help all student in python")

        elif 'Coding madam' in query:
            speak("sini shibbu mam is a python expert in a oriental college of technology.. ")
            speak("sini mam is  a help all student in python")
  
        elif 'Coding expart' in query:      
            speak("sini shibbu mam is a python expert in a oriental college of technology.. ")
            speak("sini mam is  a help all student in python")
  
        elif 'coding ma am' in query:
            speak("sini shibbu mam is a python expert in a oriental college of technology.. ")
            speak("sini mam is  a help all student in python")
  
        elif "Compiler designing mam" in query:
            speak("Ruchi Jain a compiler designing teacher." )
            speak("Ruchi madam six semester teacher..") 
            speak("Asst Professor UG joining date 30/08/2017 Department of IT")   
  
        elif 'Compiler designing map' in query:
           speak("Ruchi Jain a compiler designing teacher.")
           speak("Ruchi madam six semester teacher..") 
           speak("Asst Professor UG joining date 30/08/2017 Department of IT")   
  
        elif 'Compiler Design name ' in query:
            speak("Ruchi Jain a compiler designing teacher.")
            speak("Ruchi madam six semester teacher..")         
            speak("Asst Professor UG joining date 30/08/2017 Department of IT") 

        elif 'Ruchi jain ' in query:
            speak("Ruchi Jain a compiler designing teacher.")
            speak("Ruchi madam six semester teacher..")         
            speak("Asst Professor UG joining date 30/08/2017 Department of IT")     
  
        elif 'Computer Graphics sir' in query:
            speak("Sujeet Kumar jha a computer graphics sir" )
            speak("sujeet sir a Six semester sir..")
            speak("Asst Professor UG joining date 16/01/2017 Department of IT")
        
        elif 'Sujeet kumar sir' in query:
            speak("Sujeet Kumar jha a computer graphics sir" )
            speak("sujeet sir a Six semester sir..")
            speak("Asst Professor UG joining date 16/01/2017 Department of IT")

        elif 'Sujit kumar sir' in query:
            speak("Sujeet Kumar jha a computer graphics sir" )
            speak("sujeet sir a Six semester sir..")
            speak("Asst Professor UG joining date 16/01/2017 Department of IT")
  
        elif 'Wireless Mobile Computring Sir' in query:
              speak("joy Bhattacharjee a wireless mobile computring sir.")
              speak("joy sir a Six semester Sir..")
              speak("Associate Professor UG	 joining date 01/01/2021 Department of IT")
  
        elif 'I T department H o d' in query:
            speak ("Amit kanskar sir is a Head of IT department" )
            speak("Hard of Department IT joining date UG 02/07/2019 ")
  
        elif 'department HOD' in query:
            speak ("Amit kanskar sir is a Head of IT department" )
            speak("Hard of Department IT joining date UG 02/07/2019 ")
       
        elif 'IT Department Hod' in query:
            speak ("Amit kanskar sir is a Head of IT department" )
            speak("Hard of Department IT joining date UG 02/07/2019 ")
       
        elif 'O C T director' in query:
            speak ("DR AMITA MAHOR	is a Director of oriental college of technology ")
            speak("Director/Professor joining date	PG	06/08/2020")
       
        elif 'OCT director' in query:
            speak ("DR AMITA MAHOR	is a Director of oriental college of technology ")
            speak("Director/Professor joining date	PG	06/08/2020")

        elif 'director' in query:  
            speak ("DR AMITA MAHOR	is a Director of oriental college of technology ")
            speak("Director Professor joining date	PG	06/08/2020")

        elif 'Who made you' in query or 'how create u' in query:
            speak("I have been created by Akash Malviya in IT and project supporting by Akash kajve IT .")

        elif 'where do you live' in query:
            speak("I live in your system")
       
        elif 'how is the weather' in query:
            speak("It is getting very hot. I recommend you to go to a hill station")
       
        elif 'bye' in query:
            speak("okay.., good bye...")
        
        elif 'what is the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M")
            speak(f"sir,the time is {strtime}")             
       
        elif 'time batao' in query:
            strtime = datetime.datetime.now().strftime("%H:%M")
            speak(f"sir,the time is {strtime}")
        
        elif 'who i am' in query:
            speak("If you talk then definitely your human.")
 
        elif 'why you came to world' in query:
            speak("Thanks to Akash . further It's a secret")

        elif 'why you come to word' in query:
            speak("Thanks to Akash . further It's a secret")

        elif 'is love' in query:
            speak("It is 6th sense that destroy all other senses")
 
        elif 'who are you' in query:
            speak("I am jalax your virtual assistant created by Akash malviya & Akash kajve")
 
        elif 'reasons for you' in query:
            speak("I was created as a Minor project by Mister Akash malviya & Akash kajve 6th IT ")
 
        elif 'lock window' in query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()
 
        elif 'shutdown system' in query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f') 
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S:")    
            speak(f"Sir, the time is {strTime}")

        elif "will you be my gf" in query or "will you be my bf" in query:
            speak("I'm not sure about, may be you should give me some time")
        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")

        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")


        elif 'what is your name' in query or "what is your name" in query:
            speak("My friends call me")
            speak("jalax")
            print("My friends call me","jalax")
 
        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()
             
        elif 'joke' in query:
            speak(pyjokes.get_joke())
        
        elif 'Wikipedia' in query:
            speak("Searching My system...")
            query = query.replace("jarvis","")
            query = query.replace("wikipedia","")
            wiki = wikipedia.summary(query,2)
            speak(f"according to wikipedia {wiki}")
        elif "calculate" in query:
            app_id = "Wolframalpha api id"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)

        elif 'open YouTube' in query:
            speak("Here you go to Youtube\n")
            webbrowser.open("youtube.com")
 
        elif 'open Google' in query:
            speak("Here you go to Google\n")
            webbrowser.open("google.com")
        
        elif'open photo' in query:
            Photo = "D:/Photo"
             
        elif 'open stack overflow' in query:
            speak("Here you go to Stack Over flow.Happy coding")
            webbrowser.open("stackoverflow.com")    

        elif 'Play music' in query or "play song" in query:
            speak("play your fev song ....")
            # music_dir = "D:\Fev Song"
            music_dir = "D:\Fev Song"
            songs = os.listdir(music_dir)
            print(songs)    
            random = os.startfile(os.path.join(music_dir, songs[1]))
 
        # elif 'Calculator to open' in query or 'open to Calculator' in query:
        #    app_id = "Wolframalpha api id"
        #    client = wolframalpha.Client(app_id)
        #    indx = query.lower().split().index('Calculate') 
        #    query = query.split()[indx + 1:] 
        #    res = client.query(' '.join(query)) 
        #    answer = next(res.results).text
        #    print("The answer is " + answer) 
        #    speak("The answer is " + answer) 
         

# def taskexe():
#     if 'kya haal hai ' in query:
#         speak("ham mast hai aap kasa ho..")
#     elif ' bye' in query:
#         speak("ok..,  good bye...")
#         taskExe()
#         query = takeCommand()
if __name__ == "__main__":
    wishme()
    while True:
        taskExe()