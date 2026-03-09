import speech_recognition as sr

recognizer = sr.Recognizer()

def listen():
    try:
        with sr.Microphone() as source:
            print("\nListening... Speak now")

            audio = recognizer.listen(source, phrase_time_limit=3)

            text = recognizer.recognize_google(audio)
            print("You said:", text)
            return text

    except Exception:
        # fallback if microphone fails
        text = input("\nCustomer (type if mic not working): ")
        return text