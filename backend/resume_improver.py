import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def improve_resume(text):
    prompt = f"Suggest improvements to this resume:\n\n{text}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']
