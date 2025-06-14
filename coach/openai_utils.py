from openai import OpenAI
import os


client = OpenAI(api_key="OPENAI_API_KEY")

def get_brief_test_response():
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo", # this can be changed to gpt-4 or other model
            messages=[
                {"role": "user", "content": "Say hello and confirm that the API is working."}
            ]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"API Error: {str(e)}"
