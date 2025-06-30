import speech_recognition as sr
import webbrowser
import pyttsx3


recognizer=sr.Recognizer()
ttsx= pyttsx3.init()


def speak(text):
  engine = pyttsx3.init()
  engine.say(text)
  engine.runAndWait()
if __name__ == "__main__":
    speak("Hello sir how may i help you.........")