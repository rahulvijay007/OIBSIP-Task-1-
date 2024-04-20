import speech_recognition as sr
import pyttsx3
import datetime

eng = pyttsx3.init()
rec = sr.Recognizer()
def speak(text):
    eng.say(text)
    eng.runAndWait()
def greet():
    speak("Hello! How can I assist you today?")
def get_command():
    with sr.Microphone() as source:
        print("Listening...")
        aud = rec.listen(source)
    
    try:
        command = rec.recognize_google(aud)
        print("User:", command)
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I couldn't understand that.")
        return ""
    except sr.RequestError:
        speak("Sorry, I'm unable to process your request at the moment.")
        return ""
def main():
    greet()
    while True:
        command = get_command()
        
        if "hello" in command:
            speak("Hello there!")
        elif "time" in command:
            now = datetime.datetime.now().strftime("%H:%M")
            speak(f"The current time is {now}.")
        elif "date" in command:
            today = datetime.datetime.now().strftime("%Y-%m-%d")
            speak(f"Today's date is {today}.")
        elif "quit" in command:
            speak("Goodbye!")
            break
        else:
            speak("I'm not sure how to help with that.")
if __name__ == "__main__":
    main()