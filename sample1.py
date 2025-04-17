import pyttsx3
import speech_recognition as sr
import webbrowser
import otp  

# Function to convert text to speech
def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech and convert to text
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"You said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Please try again.")
        return None
    except sr.RequestError:
        print("Network error.")
        return None

# Greet the user
def greet():
    speak("Hello, how can I help you?")

# Main logic
def main():
    greet()
    while True:
        query = take_command()
        if query is None:
            continue

        if "hi how are you" in query:
            speak("I am doing good, how about you?")
        elif "shut down" in query:
            speak("Take care, bye!")
            break
        elif "open web page" in query:
            speak("Opening Codegnan website!")
            webbrowser.open("https://www.codegnan.com")
        elif "open meesho" in query:
            speak("Opening meesho website!")
            webbrowser.open("https://www.meesho.com")
        elif "open zepto" in query:
            speak("Opening zepto website!")
            webbrowser.open("https://www.zeptonow.com")
        elif "send otp" in query:
            speak("Please enter the email address.")
            email = input("Enter email here: ")
            otp.otp(email)
            speak("OTP sent successfully.")

if __name__ == "__main__":
    main()

