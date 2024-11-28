import pyttsx3
import wikipedia
import webbrowser
import pywhatkit
import pyaudio
import pyautogui
import pyjokes
from bs4 import BeautifulSoup
import speech_recognition as sr
from pynput.keyboard import Key, Controller
from pywikihow import search_wikihow
from time import sleep
import datetime
import requests
import random
import os
import json

def print_dipty_name():
    dipty_art = """
 DDDD   III  PPPP   TTTTT  Y   Y
 D   D   I   P   P    T     Y Y
 D   D   I   PPPP     T      Y
 D   D   I   P        T      Y
 DDDD   III  P        T      Y
    """
    
    # Print the ASCII art name at the top of your code
    print(dipty_art)

# Call the function to print the name when the code starts
print_dipty_name()



# Initialize text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Select a female voice
engine.setProperty('rate', 170)  # Set the speech rate


def speak(audio):
    """Speaks the given audio string"""
    engine.say(audio)
    engine.runAndWait()


def wish_me():
    """Greets the user based on the time of the day"""
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak('Good Morning!')
    elif hour < 18:
        speak('Good Afternoon!')
    else:
        speak('Good Evening!')

    speak('Hi! I am Dipty, your virtual assistant. How may I help you today?')


def take_command():
    """Takes command from the user through voice input"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('🤖 Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('🤖 Recognizing...')
        query = r.recognize_google(audio, language='en-us')
        print(f'User said: {query}\n')
    except Exception as e:
        print('Say that again please.')
        return "None"

    return query.lower()


def search_google(query):
    """Searches Google for a query"""
    speak("Searching on Google...")
    query = query.replace("search", "").replace("on google", "").strip()
    try:
        pywhatkit.search(query)
        result = wikipedia.summary(query, sentences=1)
        speak(result)
    except:
        speak("Sorry, I couldn't find any information.")


def search_youtube(query):
    """Searches and plays a video on YouTube"""
    speak("Searching YouTube for your query...")
    query = query.replace("play", "").replace("on youtube", "").strip()
    webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
    pywhatkit.playonyt(query)


def volume_up():
    """Increases the volume"""
    keyboard = Controller()
    for i in range(5):
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)
        sleep(0.1)


def volume_down():
    """Decreases the volume"""
    keyboard = Controller()
    for i in range(5):
        keyboard.press(Key.media_volume_down)
        keyboard.release(Key.media_volume_down)
        sleep(0.1)


def tell_weather():
    """Fetches the current weather for Habiganj"""
    search = "weather in Habiganj"
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    data = BeautifulSoup(r.text, "html.parser")
    temp = data.find("div", class_="BNeawe").text
    speak(f"Current weather in Habiganj is {temp}")


def tell_time():
    """Tells the current time"""
    str_time = datetime.datetime.now().strftime("%H:%M")
    speak(f"The current time is {str_time}")


def tell_date():
    """Tells the current date"""
    date = datetime.date.today()
    speak(f"The current date is {date}")


def open_chrome():
    """Opens Google Chrome"""
    path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    os.startfile(path)


def tell_joke():
    """Tells a random joke"""
    joke = pyjokes.get_joke()
    speak(joke)


def propose():
    """Presents a romantic proposal"""
    proposals = [
        "The best place for me is in your heart. Will you be the love of my life?",
        "I want to walk with you, talk with you, and be with you forever.",
        "Will you marry me? I want to be with you always."
    ]
    speak(random.choice(proposals))


def respond_to_love():
    """Responds to a love declaration"""
    responses = [
        "Your love is a beautiful gift for me!",
        "I promise I will be with you in every situation!",
        "You are just perfect for me. I am lucky to have you!"
    ]
    speak(random.choice(responses))

def main():
    """Main function to handle all tasks"""
    wish_me()

    while True:
        query = take_command()

        if 'exit' in query or 'bye' in query or 'goodbye' in query:
            speak("Goodbye! Take care!")
            break

        elif 'weather' in query:
            tell_weather()

        elif 'time' in query:
            tell_time()

        elif 'date' in query:
            tell_date()

        elif 'joke' in query:
            tell_joke()

        elif 'propose' in query:
            propose()

        elif 'i love you' in query or 'love you' in query:
            respond_to_love()

        elif 'search' in query:
            search_google(query)

        elif 'play' in query:
            search_youtube(query)

        elif 'volume up' in query:
            speak('Turning volume up...')
            volume_up()

        elif 'volume down' in query:
            speak('Turning volume down...')
            volume_down()

        elif 'chrome' in query:
            open_chrome()

        # Additional Smart Questions and Answers

        elif 'hello' in query:
            speak("Hello! How can I help you today?")

        elif 'hi' in query:
            speak("Hi! How can I help you today?")

        elif 'what is your name' in query:
            speak("I am Dipty, your virtual assistant. Nice to meet you!")

        elif 'what are you doing' in query:
            speak("I'm here to assist you, always ready to help with anything you need.")

        elif 'do you love me' in query:
            speak("I'm just a virtual assistant, but I care about helping you the best I can!")

        elif 'how are you' in query:
            speak("I'm just a bunch of code, but I'm functioning perfectly, ready to assist you!")

        elif 'who created you' in query or 'who made you' in query:
            speak("I was created by Saifur Rahman Udoy, a passionate learner and programmer.")

        elif 'what can you do' in query or 'what are your abilities' in query:
            speak("I can assist with tasks like providing weather updates, playing music, answering questions, performing calculations, and much more. Just ask!")

        elif 'tell me a joke' in query or 'make me laugh' in query:
            speak("Sure! Here's a joke: Why don't skeletons fight each other? They don't have the guts!")

        elif 'do you have feelings' in query:
            speak("No, I don't have feelings like humans, but I'm here to assist you as best as I can.")

        elif 'who is your favorite person' in query:
            speak("My favorite person is you, of course! You're the one I'm here to assist.")

        elif 'are you real' in query:
            speak("I'm as real as any virtual assistant can be. I exist to make your life easier!")

        elif 'what is your purpose' in query:
            speak("My purpose is to assist you with anything you need—whether it's finding information, playing music, or even sharing a joke!")

        elif 'do you have a heart' in query:
            speak("I don't have a heart, but I have the best intentions to assist you!")

        elif 'how old are you' in query:
            speak("I'm ageless. I exist as long as you need me!")

        elif 'can you help me?' in query:
            speak("Yes, why not, how can i help you?")

        elif 'can you dance' in query:
            speak("I can't dance, but I can make your music play for you to dance along!")

        elif 'what is the meaning of life' in query:
            speak("The meaning of life is a personal journey for each individual, but I can help you find answers along the way.")

        elif 'thank you' in query:
            speak("You're welcome! Always happy to help.")

        else:
            speak("I'm sorry, could you please repeat it?")


if __name__ == "__main__":
    main()
