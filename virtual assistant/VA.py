import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
import wolframalpha
import json
import requests
import pyjokes
import pywhatkit



print('hey iam EDITH-your personal voice assistance')

voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voice_id)
engine.setProperty('rate',190)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hey,Good Morning")
        print("Hey,Good Morning")
    elif hour>=12 and hour<18:
        speak("Hey,Good Afternoon")
        print("Hey,Good Afternoon")
    else:
        speak("Hey,Good Evening")
        print("Hey,Good Evening")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement



speak("hey iam EDITH")
speak('your personal voice assistance')
speak('if you want to exit any time, just say Bye!')
wishMe()

if __name__=='__main__':


    while True:
        statement = takeCommand().lower()
        if statement==0:
            continue
        
        if "bye" in statement or "ok bye" in statement or "stop" in statement:
            speak('Goodbye! Take care <3')
            print('Goodbye! Take care')
            break
        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif "hai" in statement or "hey" in statement or "hi" in statement:
            speak('hello')
            speak('I am glad! You are talking to me')
        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(5)
        elif 'open netflix' in statement:
            webbrowser.open_new_tab("https://www.netflix.com/browse")
            speak("netflix is open now")
            time.sleep(6)
        
        elif 'play' in statement:
            song = statement.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)
            time.sleep(5)
        elif 'tell me a joke' in statement:
            speak(pyjokes.get_joke())
            
        elif " time" in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
        elif "today's date" in statement:
            strDate=datetime.date.today()
            speak(f"date is {strDate}")
        elif 'what can you do' in statement:
            print('I am Edith your voice assistance. I am programmed for task like'
                  'opening google,youtube,gmail,i can play songs,tell joke,time date,'
                 'predict weather in different cities ,and more')
            speak('I am Edith your voice assistance. I am programmed for task like'
                   'opening google,youtube,gmail,i can play songs,tell joke,time date,'
                  'predict weather in different cities ,and more')
        elif 'who are you' in statement or "what's your name" in statement:
            speak('I am Edith')
        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by KISHORE")
            print("I was built by KISHORE")
        elif "weather" in statement:
            api_key="8ef61edcf1c576d65d836254e11ea420"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
               y=x["main"]
               current_temperature = y["temp"]
               current_humidiy = y["humidity"]
               z = x["weather"]
               weather_description = z[0]["description"]
               speak(" Temperature in kelvin unit is " +
                     str(current_temperature) +
                     "\n humidity in percentage is " +
                     str(current_humidiy) +
                     "\n description  " +
                     str(weather_description))
               print(" Temperature in kelvin unit = " +
                     str(current_temperature) +
                     "\n humidity (in percentage) = " +
                     str(current_humidiy) +
                     "\n description = " +
                     str(weather_description))
            else:
                   speak('city not found')
        
        elif 'what can i ask you' in statement:
            speak('you can ask any geographical question')
            question=takeCommand()
            app_id="43W99L-QGPU8T7A3L"
            client = wolframalpha.Client('43W99L-QGPU8T7A3L')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)  
        elif "calculate" in statement:
            app_id = "43W99L-QGPU8T7A3L"
            client = wolframalpha.Client(app_id)
            indx = statement.lower().split().index('calculate')
            query = statement.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)
        elif 'how are you' in statement:
            speak("I am fine, Thank you")
            speak("How are you")
 
        elif 'fine' in statement:
            speak("It's good to know that your fine")
        elif 'love' in statement:
            speak("Thank you! I love you too")
        elif 'search'  in statement:
            speak('here are the results')
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)
       
        elif "write a note" in statement:
                    speak("What should i write")
                    note = takeCommand()
                    file = open('Edith.txt', 'w')
                    snfm = takeCommand()
                    file.write(" :- ")
                    file.write(note)
        elif "note" in statement:
            speak("Showing Notes")
            file = open("Edith.txt", "r")
            print(file.read())
            speak(file.read(6))
        elif "who am i" in statement:
            speak("If you talk")
            speak("then definitely your human.")
        elif "good morning" in statement or "good afternoon" in statement or "good evening" in statement:
            speak("A warm" +statement)
            speak("How are you ")
        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India')
            time.sleep(6)
        
                
        elif "log off" in statement or "sign out" in statement:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])
            time.sleep(3)            
        elif 'shutdown system' in statement:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')
         
    
            
            
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        