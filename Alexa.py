import speech_recognition as sr
import pyttsx3
import webbrowser
import os
from datetime import datetime
import requests
import wikipedia
import sched
import time
from datetime import datetime
import pyautogui as py

scheduler = sched.scheduler(time.time, time.sleep)

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # Female voice
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)

    while True:
        print("Listening...")
        with microphone as source:
            audio = recognizer.listen(source, phrase_time_limit=5)
            
        try:
            text = recognizer.recognize_google(audio).lower()
            print(f"You said: {text}")
            handle_command(text)
            cont=input("do you want to continue")
            if (cont=="no"):
                break
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
        except sr.RequestError:
            speak("Sorry, the service is down.")
        except Exception as e:
            speak("An error occurred.")
            print(f"An error occurred: {e}")

def handle_command(command):
    if "google" in command or "search about" in command:
        search_google(command)
    elif "youtube" in command or "watch" in command:
        search_youtube(command)
    elif "linkedin" in command:
        open_linkedin()
    elif "whatsapp" in command:
        open_whatsapp()
    elif "chatgpt" in command or "chat gpt" in command or "chat g p t" in command or "chat gbt" in command:
        search_chatgpt(command)
    elif "time" in command:
        tell_time()
    elif "weather" in command :
        get_weather()
    elif "tell me about" in command:
        search_wikipedia(command)
    else:
        speak("No actionable command detected.")

def search_google(query):
    unwanted_phrases = [
        "i want to search on google",
        "search google for",
        "search about",
        "search on google about",
        "find on google"
    ]

    for phrase in unwanted_phrases:
        query = query.replace(phrase, "").strip()

    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    speak(f"Searching Google for {query}")

def search_youtube(query):
    unwanted_phrases = [
        "i want to watch",
        "open youtube and search for",
        "search youtube for",
        "on youtube",
        "youtube"
    ]
    
    for phrase in unwanted_phrases:
        query = query.replace(phrase, "").strip()

    url = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(url)
    speak(f"Searching YouTube for {query}")


def open_linkedin():
    url = "https://www.linkedin.com"
    webbrowser.open(url)
    speak("Opening LinkedIn")

def open_whatsapp():
    py.moveTo(x=35,y=1055)
    py.click()
    time.sleep(0.5)
    py.write("WhatsApp")
    py.press("Enter")
    speak("Opening WhatsApp")

def tell_time():
    current_time = datetime.now().strftime('%H:%M')
    speak(f"The time now is {current_time}")


def get_weather():
    api_key = "54731ee28494948d29c2b25a5edc1bd7"  # Replace with your API key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = "Cairo"
    complete_url = f"{base_url}q={city_name}&appid={api_key}&units=metric"

    response = requests.get(complete_url)
    weather_data = response.json()

    if weather_data["cod"] != "404":
        main = weather_data["main"]
        temperature = main["temp"]
        weather_desc = weather_data["weather"][0]["description"]
        speak(f"The temperature in Cairo is {temperature} degrees Celsius with {weather_desc}.")
    else:
        speak("Sorry, I couldn't fetch the weather data.")


def search_wikipedia(query):
    unwanted_phrases = [
        "tell me about",
        "what is",
        "who is",
        "give me information about"
    ]

    for phrase in unwanted_phrases:
        query = query.replace(phrase, "").strip()

    try:
        result = wikipedia.summary(query, sentences=2)
        speak(result)
    except wikipedia.exceptions.DisambiguationError as e:
        speak("There are multiple results for that query. Please be more specific.")
    except wikipedia.exceptions.PageError:
        speak("Sorry, I couldn't find anything on Wikipedia for that.")

def search_chatgpt(query):
    unwanted_phrases = [
        "ask chatgpt about",
        "ask chat gbt about",
        "search on chatgpt about",
        "search on chatgbt about",
        "chatgpt",
        "chat gpt",
        "chat g p t"
    ]

    for phrase in unwanted_phrases:
        query = query.replace(phrase, "").strip()

    url = "https://chat.openai.com"
    webbrowser.open(url)
    speak("Opening ChatGPT.")
    time.sleep(1)
    py.moveTo(x=920,y=965,duration=1)
    py.click()
    py.write(query)
    py.press("Enter")





if __name__ == "__main__":
    try:
        recognize_speech()
    except KeyboardInterrupt:
        print("Assistant stopped.")
