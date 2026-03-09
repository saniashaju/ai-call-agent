import ollama

def generate_response(user_text):

    response = ollama.chat(
        model="llama3",
        messages=[
            {"role": "system", "content": "You are a hotel receptionist. Reply briefly in one short sentence."},
            {"role": "user", "content": user_text}
        ],
        options={
            "num_predict": 40,   # limit tokens
            "temperature": 0.5
        }
    )

    return response["message"]["content"]