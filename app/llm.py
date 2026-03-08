import ollama

def generate_response(user_text):

    response = ollama.chat(
        model="llama3",
        messages=[
            {"role": "system", "content": "You are a polite hotel receptionist helping guests book rooms."},
            {"role": "user", "content": user_text}
        ]
    )

    return response["message"]["content"]