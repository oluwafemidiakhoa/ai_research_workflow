# test_openai.py

import os
import logging
from openai import OpenAI

def test_openai():
    openai_api_key = os.getenv('OPENAI_API_KEY')
    if not openai_api_key:
        logging.error("OpenAI API key not found.")
        print("Error: OpenAI API key not found.")
        return

    client = OpenAI(api_key=openai_api_key)
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a test."},
                {"role": "user", "content": "Hello, world!"}
            ],
            max_tokens=10
        )
        print("API Key is valid. Test response:", response.choices[0].message.content)
    except Exception as e:
        logging.error(f"API Key test failed: {e}")
        print(f"API Key test failed: {e}")

if __name__ == "__main__":
    test_openai()
