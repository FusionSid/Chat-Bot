from neuralintents import GenericAssistant
import sys
import func
import requests

mappings = {
    "hello": func.hello,
    "create_note": func.create_note,
    "create_todo": func.add_todo,
    "show_todos": func.show_todos,
    "age": func.age,
    "name": func.name,
    "time": func.time,
    "date": func.date,
    "calculate": func.calculate,
    "exit": func.quit,
    "roast": func.roast,
    "favsong": func.favsong,
    "favcolor": func.favcolor,
    "favanimal": func.favanimal,
    "favfood": func.favfood,
    "weather_report": func.weather_report,
    "feels_like": func.Weather.feels_like,
    "min_max": func.Weather.min_max,
    "sunrise": func.Weather.sunrise,
    "sunset": func.Weather.sunset,
    "temp": func.Weather.temp
}

assistant = GenericAssistant('intents.json', intent_methods=mappings)

def ask():
    tm = input("Would you like to train the model or use a saved model? \n")

    if tm == 't':
        saveas = input("\nSave as: ")
        assistant.train_model()
        assistant.save_model(model_name=saveas)
        runasis = input("\nRun assistant? y/n ")
        if runasis == "n":
            sys.exit(0)
    if tm == 's':
        modeln = input("\nModel name: ")
        assistant.load_model(model_name=modeln)

assistant.load_model('model')

print("\nVoice Assistant is ready!")
while True:
    try:
        message = input("> ")
        assistant.request(message)
    except:
        print("ERROR")