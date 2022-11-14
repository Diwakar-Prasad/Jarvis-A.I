import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import psutil
import pyjokes  
import requests


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty("rate", 145)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"
    return query

def wishMe():
    timehome = datetime.datetime.now().strftime("%H:%M:%S")
    hour = int(datetime.datetime.now().hour)
    datenow = datetime.date.today().strftime("%B %d, %Y")
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")
    
    speak(f"Today date is {datenow}")
    speak("AND")
    speak(f"The time is {timehome}")
    speak("AND")
    speak(f"The hour is {hour}")
    

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('birkuwarprasad1@gmail.com', 'B8877005518')
    server.sendmail('birkuwarprasad@gmail.com', to, content)
    server.close()

#date function
def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current")
    speak("date is",date)
    speak("month is",month)
    speak("year is",year)

#joke function
def jokes():
    j = pyjokes.get_joke()
    print(j)
    speak(j)

#weather condition
def weather():
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    CITY = "Garhwa"
    API_KEY = "688b3c1c8c5ad7ab54643f49e9cd17c4"
    # upadting the URL
    URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
    # HTTP request
    response = requests.get(URL)
    # checking the status code of the request
    if response.status_code == 200:
       # getting data in the json format
       data = response.json()
       # getting the main dict block
       main = data['main']
       # getting temperature
       temperature = main['temp']
       # getting the humidity
       humidity = main['humidity']
       # getting the pressure
       pressure = main['pressure']
       # weather report
       report = data['weather']
       print("In " + CITY + " Temperature is " +
             str(int(temperature - 273.15)) + " degree celsius ")
       print(f"Humidity is {humidity}")
       print(f"Pressure is {pressure}")
       print(f"Weather Report is {report[0]['description']}")
       speak("In " + CITY + " Temperature is " +
             str(int(temperature - 273.15)) + " degree celsius ")
       speak(f"Humidity is {humidity}")
       speak(f"Pressure is {pressure}")
       speak(f"Weather Report is {report[0]['description']}")
    else:
       # showing the error message
       speak("Error in the HTTP request")

#battery and cpu usage
def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU usage is at ' + usage)
    print('CPU usage is at ' + usage)
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)
    print("battery is at:" + str(battery.percent))

#wishme end
def wishme_end():
    speak("signing off")
    hour = datetime.datetime.now().hour
    if (hour >= 6 and hour < 12):
        speak("Good Morning")
    elif (hour >= 12 and hour < 18):
        speak("Good afternoon")
    elif (hour >= 18 and hour < 24):
        speak("Good Evening")
    else:
        speak("Goodnight.. Sweet dreams")
    quit()

def NewsFromBBC():
	
	# BBC news api
	# following query parameters are used
	# source, sortBy and apiKey
	query_params = {
	"source": "bbc-news",
	"sortBy": "top",
	"apiKey": "32db616595a147a5931dd2f9436e6ca6"
	}
	main_url = "https://newsapi.org/v2/top-headlines?country=in"

	# fetching data in json format
	res = requests.get(main_url, params=query_params)
	open_bbc_page = res.json()

	# getting all articles in a string article
	article = open_bbc_page["articles"]

	# empty list which will
	# contain all trending news
	results = []
	
	for ar in article:
		results.append(ar["title"])
		
	for i in range(len(results)):
		
		# printing all trending news
		print(i + 1, results[i])

	#to read the news out loud for us

	speak(results)



if __name__ == "__main__":
    wishMe()
    while True:
      #if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'who' in query:
            speak('Searching...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'what' in query:
            speak('Searching...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'why' in query:
            speak('Searching...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'where' in query:
            speak('Searching...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'when' in query:
            speak('Searching...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'which' in query:
            speak('Searching...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'whome' in query:
            speak('Searching...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'how' in query:
            speak('Searching...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

          # simple query start

        elif 'hello' in query:
            speak("Hello sir")

        elif 'tell me about you' in query:
            speak(
                "I am your Virtual Assistant. I am Created On TWO OCTOBER TWO THOUSAND TWENTY TWO. By DIWAKAR.")

        elif 'will you kill human' in query:
            speak("No, I like Human I also want to be like human.")

        elif 'what is your IQ' in query:
            speak("Sir, My IQ level is ZERO")

        elif 'who created you' in query:
            speak("DIWAKAR PRASAD!!!")

        elif 'tell me about your creator' in query:
            speak("DIWAKAR CREATED ME ON TWO OCTOBER TWO THOUSAND TWENTY TWO.")

            # simple query end

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            chromePath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
            speak("OPENING GOOGLE")
            os.startfile(chromePath)

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'emergency' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "heerasoni990@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry. I am not able to send this email")

        elif 'date' in query:
            date()
            
        elif 'tell me a joke' in query or 'joke' in query:
            jokes()


        elif 'weather' in query or 'temperature' in query:
            weather()

        elif ("create a reminder list" in query or "reminder" in query):
            speak("What is the reminder?")
            data = takeCommand()
            speak("You said to remember that" + data)
            reminder_file = open("data.txt", 'a')
            reminder_file.write('\n')
            reminder_file.write(data)
            reminder_file.close()

        elif ("do you know anything" in query or "remember" in query):
            reminder_file = open("data.txt", 'r')
            speak("You said me to remember that: " + reminder_file.read())

        elif ("cpu and battery" in query or "battery" in query
              or "cpu" in query):
            cpu()

        elif ("news" in query or "top news" in query):
            NewsFromBBC()

        elif ('i am done' in query or 'power off' in query
              or 'go offline' in query or 'bye' in query
              or 'sleep' in query):
            wishme_end()

else:
    speak("Please come online i cannot heare you")