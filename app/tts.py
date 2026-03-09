import pyttsx3

engine = pyttsx3.init()

# Make voice clearer
engine.setProperty('rate', 170)     # speed of speech
engine.setProperty('volume', 1)     # max volume

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()