from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

import speech_recognition as sr
import pyttsx3


class TranslatorApp(MDApp):
    def build(self):
        return

    # This function is called from Speaker Button to speak the written text
    def speak(self):
        engine = pyttsx3.init()
        engine.say(self.root.ids.usertext2.text)
        engine.runAndWait()

    # This function is called from MIC Button and it starts recording. It will listen for only given amount of Seconds
    def listen(self):
        r = sr.Recognizer()

        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            audio = r.record(source, duration=3)

        try:
            self.root.ids.usertext1.text = "You Said: " + r.recognize_google(audio)

        except:
            self.root.ids.usertext1.text = "Could not understand audio"


TranslatorApp().run()
