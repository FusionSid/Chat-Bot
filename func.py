import random
import speech_recognition
import pyttsx3 as tts
import sys
import datetime
import roast_list
import json
import requests
import math

# write to json files
def write_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f)

recognizer = speech_recognition.Recognizer()
s = tts.init()

# Short answer questions

def age():
    print("I am 42 years old")
    
def name():
    print("My name is Rick")
    
def favsong():
    print("My favourite song is Never gonna give you up")
    
def favfood():
    print("Pizza, Pizza is my favourite food")
    
def favanimal():
    print("The duck is my favourite animal")
    
def favcolor():
    print("My favourite color is blue")
    
def roast():
    roast = random.choice(roast_list.roastlist)
    print(roast)
    
def hello():
    hellores = ["Hello", "Hi there", "Wassup", "Hello there, What can I do for you"]
    print(random.choice(hellores))
    
def quit():
    quitchoices = ["Goodbye Sir", "Goodbye", "Bye", "See ya later", "See ya later alligator"]
    print(random.choice(quitchoices))
    sys.exit(0)

def date():
    print(f"The date today is: {datetime.date.today()}")
    
def time():
    now = datetime.datetime.now()
    timern = now.strftime("%I:%M %p")
    print(f'The time right now is: {timern}')
    

# Bigger functions

def create_note():
    print("What would you like to write on the note?")

    done = False

    while not done:
        print("\nWhat would you like to write to the note!")
        note = input("> ")
        print(note)
                
        print("What would you like to call the note")
        filename = input("> ")
        print(filename)
        filename = filename.lower()

        with open(filename, 'w') as f:
            f.write(note)
            done = True
            print("Your note has been created")


def add_todo():
    print("What would you like to add to you todo list?")

    filename = 'todo_list.json'
    done = False

    while not done:
        print("\nWhat would you like to add to your todo list!")
        item = input("> ")
        filename = 'todo_list.json'

        with open(filename) as json_file:
            data = json.load(json_file)
            data.append(item)
            write_json(data, filename)
            done = True
            print(f"{item} Has been added to the todo list")

def show_todos():
    print("The items in your todo list are the following")

    filename = 'todo_list.json'
    with open(filename) as json_file:
        data = json.load(json_file)

    for item in data:
        print(item)

# Weather

apikey = "6f9aa23390668e72710bd5a33e3d575c"
city = "Auckland"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}"
weather_response = requests.get(url).json()

class Weather():
    def temp():
        temp = weather_response['main']['temp']
        temp = math.floor(temp-273.15)
        print(f"The temperature is {temp} degrees celsius")
        

    def feels_like():
        feelslike = weather_response['main']['feels_like']
        feelslike = math.floor(feelslike-273.15)
        print(f"It feels like {feelslike} degrees celsius")
        

    def min_max():
        min = weather_response['main']['temp_min']
        min = math.floor(min-273.15)
        max = weather_response['main']['temp_max']
        max = math.floor(max-273.15)
        print(f"Minimum Temperature today is {min} And the max will be {max}")
        
    
    def description():
        desc = weather_response['main'][0]["description"]
        main = weather_response['main'][0]['main']
        print(f"Weather description {main}, {desc}")
        

    def sunset():
        stime = weather_response['sys']['sunset']
        sunset = datetime.datetime.fromtimestamp(stime).strftime("%I:%M %p")
        print(f"Sunset is at {sunset}")
        
    
    def sunrise():
        stime = weather_response['sys']['sunrise']
        sunrise = datetime.datetime.fromtimestamp(stime).strftime("%I:%M %p")
        print(f"Sunrise is at {sunrise}")
        


def weather_report():
    Weather.feels_like()
    Weather.min_max()
    Weather.sunrise()
    Weather.sunset()
    Weather.temp()


# Calculator

def calculator(n1, op, n2):
    if op == "+":
        return n1 + n2
    if op == "x":
        return n1 * n2
    if op == "-":
        return n1 - n2
    if op == "/":
        return n1 / n2
    else:
        return "invalid"


def calculate():
    global recognizer
    try:
        with speech_recognition.Microphone() as mic:
            print("What would you like to calculate")
            
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            print("\nWhat would you like to calculate")
            audio = recognizer.listen(mic)
            n2calc = recognizer.recognize_google(audio)
            print(n2calc)
            n2calc = n2calc.split()
            n1 = int(n2calc[0])
            op = n2calc[1]
            n2 = int(n2calc[2])
            ans = calculator(n1, op, n2)
            if ans == 'invalid':
                print("Invalid input")
                
            else:
                print(str(ans))
                
    except speech_recognition.UnknownValueError:
        recognizer = speech_recognition.Recognizer()


