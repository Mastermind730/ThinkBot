import random
import pyttsx3
import smtplib
import webbrowser
import datetime
import speech_recognition as sr
import os
import sys
import pywhatkit as kit
import wikipedia
import time
import json
import wikipedia
import datetime
#import psutil
# import PyDictionary
import pyjokes
import pyautogui
from sys import platform
import geocoder
import requests
from bs4 import BeautifulSoup

email_id={'sourav':'sourav.97032@gmail.com','tushar':'bhandetushar123@gmail.com'}
g = geocoder.ip('me')
phone_no={'sourav':'+919834144155','vivek':'+919850310343'}
engine=pyttsx3.init()
voice=engine.getProperty("voices")
def speak(string):
    engine=pyttsx3.init()
    voice=engine.getProperty("voices")
    engine.setProperty("voice",voice[1].id)
    #engine.setProperty('rate',150)
    engine.say(string)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>0 and hour<12:

        speak('Good Morning')
    elif hour>12 and hour<6:

        speak('Good Afternoon')
    else:
        speak('Good Evening')
    speak('Hello I am ThinkBot,what  can i do for you Mastermind')



def sendemail(to,messg):
    server=smtplib.SMTP('smtp.gmail.com',587)
    passwd =''  #--->type your password here
    sender = ''  #----->type your gmail id
    server.starttls()
    server.login(sender,passwd)
    print('Logged in succesfully')
    print('Sending email..')
    speak('Sending email..')
    server.sendmail(sender,to,messg)
    print('Your mail has been sent succesfully')

def command():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold=1.1
        audio=r.listen(source)

    try:
        print('Reccgnizing...')
        query=r.recognize_google(audio,language='en-in')
        print(f'User said: {query}')
    except Exception as e:
        print('Cant hear please say it again.')
        return 'None'
    return query

def speak_news():
    url = 'http://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey=407a4f60fa8a4114a9d9c5e56962a929'
    news = requests.get(url).text
    news_dict = json.loads(news)
    arts = news_dict['articles']
    speak('Source: The Times Of India')
    speak('Todays Headlines are..')
    for index, articles in enumerate(arts):
        speak(articles['title'])
        if index == len(arts)-1:
            break
        speak('Moving on the next news headline..')
    speak('These were the top headlines, Have a nice day Sir!!..')

def weather():

    api_url = "https://fcc-weather-api.glitch.me/api/current?lat=" + \
        str(g.latlng[0]) + "&lon=" + str(g.latlng[1])

    data = requests.get(api_url)
    data_json = data.json()
    if data_json['cod'] == 200:
        main = data_json['main']
        wind = data_json['wind']
        weather_desc = data_json['weather'][0]
        speak(str(data_json['coord']['lat']) + 'latitude' + str(data_json['coord']['lon']) + 'longitude')
        speak('Current location is ' + data_json['name'] + data_json['sys']['country'] + 'dia')
        speak('weather type ' + weather_desc['main'])
        speak('Wind speed is ' + str(wind['speed']) + ' metre per second')
        speak('Temperature: ' + str(main['temp']) + 'degree celcius')
        speak('Humidity is ' + str(main['humidity']))
#
# def meaning(str):
#     diction=PyDictionary(str)
#
#     speak(f'meaning of {str} is {result}')

# def cpu():
#     usage = str(psutil.cpu_percent())
#     speak("CPU is at"+usage)
#
#     battery = psutil.sensors_battery()
#     speak("battery is at")
#     speak(battery.percent)



def joke():
    for i in range(5):
        speak(pyjokes.get_jokes()[i])

if __name__ == '__main__':
    wishme()

    while True:
        query = command().lower()
        # query=input('Enter command:')
        if 'hello' in query or 'hii' in query:
            speak('Hello Sir How are you??')

        elif 'voice' in query:
            if 'female' in query:
                engine.setProperty('voice', voice[1].id)
            else:
                engine.setProperty('voice', voice[0].id)
            speak("Hello Sir, I have switched my voice. How is it?")

        elif 'wikipedia' in query:
            speak('Searching Wikipedia..')
            query=query.replace('wikipedia','')
            results=wikipedia.summary(query,sentences=2)
            speak('According to wikipedia.')
            speak(results)
            print(results)

        # elif 'cpu' in query:
        #     cpu()

        elif 'joke' in query:
            joke()

        elif 'screenshot' in query:
            speak("taking screenshot")
            screenshot()

        elif 'send email' in query:
            for i in email_id:
                if i in query:
                    to=email_id[i]
                    msg=command().lower()
                    sendemail(to=to,messg=msg)
                    speak(f'Email has been sent successfully to {to}')
        elif 'search' in query:
            speak('What do you want to search for?')
            search = command().lower()
            url = 'https://google.com/search?q=' + search
            webbrowser.get('chrome').open_new_tab(
                url)
            speak('Here is What I found for' + search)
        elif 'shutdown' in query:
            kit.shutdown(datetime.datetime.now())
            speak('Windows is shutting down')

        elif 'weather' in query:
            speak('Todays weather forecast is :')
            weather()

        elif 'news' in query:
            speak('Ofcourse sir..')
            speak_news()
            speak('Do you want to read the full news...')
            test = command().lower()
            if 'yes' in test:
                speak('Ok Sir, Opening browser...')
                webbrowser.open(getNewsUrl())
                speak('You can now read the full news from this website.')
            else:
                speak('No Problem Sir')

        elif 'dictionary' in query:
            speak('What you want to search in your intelligent dictionary?')
            meaning(command().lower())

        elif 'location' in query:
            speak('What is the location?')
            location = command().lower()
            url = 'https://google.nl/maps/place/' + location + '/&amp;'
            webbrowser.get('chrome').open_new_tab(url)
            speak('Here is the location ' + location)
        elif 'open google' in query:
            speak('Opening Google...')
            webbrowser.open('www.google.com')

        elif 'set alarm' in query:
            speak('At what time should I set the alarm for ex say ,set alarm to 3:30')
            Timing=command()
            Timing.replace('set alarm to','')
            Timing.replace(':','')
            import resource
            resource.Alarm(Timing)
            speak('Wake Up Fast!!!')

        elif 'open youtube' in query:
            speak('Opening Youtube..')
            webbrowser.open('youtube.com')
        elif 'open stackoverflow' in query:
            speak('Opening StackOverflow')
            webbrowser.open('stackoverflow.com')
        elif 'open cmd' in query:
            os.startfile('cmd')
        elif 'open pycharm' in query:
            pycharm_path= "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.3.3\\bin\\pycharm64.exe"
            os.startfile(pycharm_path)
        elif 'the time' in query:
            strtime=datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'Sir,the time is {strtime}')
        elif 'open zoom' in query:
            zoom_path='"C:\\Users\\Sourav Narvekar\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"'
            os.startfile(zoom_path)

        elif 'open notepad' in query:
            note_path='%windir%\\system32\\notepad.exe'
            os.startfile(note_path)
        elif 'whatsapp message' in query:
            speak('What to say..')
            messg=command().lower()
            for i in phone_no:
                if i in query:
                    kit.sendwhatmsg(phone_no[i],message=messg)
                    speak(f'Sending message to {phone_no[i]}')
                    time.sleep(60)
                    speak('Message sent successfully')
        elif 'on youtube' in query:
            query=query.replace('on youtube','')
            kit.playonyt(query)

        elif 'tell temperature' in query:
            search='temperature in pune'
            url=f'https://www.google.com/search?q={search}'
            r=requests.get(url)
            data=BeautifulSoup(r.text,'html.parser')
            temp=data.find('div',class_='BNeawe').text
            speak(f'The current temperature in pune is {temp}')
        elif 'play music'in query:
            music_dir=''
            songs=os.listdir(music_dir)
            r=random.randint(1,15)
            os.startfile(os.path.join(music_dir),songs[r])


        elif 'quit' in query:
            speak('Quitting Thinkbot..')
            sys.exit()
