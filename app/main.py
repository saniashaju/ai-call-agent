import time
from llm import generate_response
from tts import speak
from stt import listen

def run_agent():

    print("\nHotel AI Receptionist Ready\n")

    while True:

        user_text = listen()

        if not user_text:
            continue

        start = time.time()

        response = generate_response(user_text)

        latency = time.time() - start

        print("\nAssistant:", response)

        speak(response)

        print("\nLatency:", latency, "seconds\n")


if __name__ == "__main__":
    run_agent()