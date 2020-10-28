import speech_recognition as sr
import pyttsx3

rec = sr.Recognizer()

while(1):
    with sr.Microphone() as source:
        rec.adjust_for_ambient_noise(source, duration=0.2)
        audio = rec.listen(source)
        text = rec.recognize_google(audio)
        print(text)
