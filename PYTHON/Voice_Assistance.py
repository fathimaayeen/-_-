import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os

def speak(text):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)
    voices = engine.getProperty('voices')
    engine.setProperty("voice", voices[1].id)
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.energy_threshold = 10000
        recognizer.adjust_for_ambient_noise(source, 1.2)
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=5)
            print("Recognizing...")
            query = recognizer.recognize_google(audio, language="en-US")
            print(f"User: {query}")
            return query.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that. Can you please repeat?")
            return listen()
        except sr.RequestError as e:
            speak("There was an error with the speech recognition service. Please check your internet connection.")
            return None

def execute_command(command):
    if "what is your name" in command:
        speak("I am your custom voice assistant.")
    elif "what is the time" in command:
        current_time = datetime.datetime.now().strftime("%H:%M")
        speak(f"what is the time now{current_time}")
    elif "open Google" in command:
        webbrowser.open("https://www.google.com")
    elif "open YouTube" in command:
        webbrowser.open("https://www.youtube.com")
    elif "search" in command:
        search_query = command.replace("search", "")
        webbrowser.open(f"https://www.google.com/search?q={search_query}")
    elif "exit" in command:
        speak("Goodbye!")
        exit()
    else:
        speak("I'm sorry, I don't understand that command.")

if __name__ == "__main__":
    speak("Hello! I'm your voice assistant. How can I help you today?")

    while True:
        command = listen()

        if command:
            execute_command(command)
