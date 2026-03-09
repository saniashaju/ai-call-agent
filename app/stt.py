import speech_recognition as sr

recognizer = sr.Recognizer()

def listen():

    with sr.Microphone() as source:
        print("\nListening... Speak now")

        audio = recognizer.listen(source, phrase_time_limit=3)

        try:
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            return text

        except:
            print("Could not understand audio")
            return ""