from ollama import Client

client = Client(host="http://localhost:11434")


def generate_letter(prompt):
    try:
        response = client.chat(
            model="llama3.2:3b",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            options={
                "temperature": 0.5,
                "num_predict": 250,
                "top_p": 0.9,
                "num_ctx": 2048
            }
        )

        return response["message"]["content"]

    except Exception as e:
        return f"Error: {e}"