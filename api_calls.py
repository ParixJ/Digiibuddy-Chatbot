import requests
import json
from dotenv import load_dotenv
import os

def get_response(user_input,api_key):
    model = "mistralai/mixtral-8x22b-instruct"

    response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {api_key}"
    },
    data=json.dumps({
        "model": model,
        "messages": [
        {
            "role": "user",
            "content": user_input
        },
        {
            'role': 'system',
            'message':   """Your are a chatbot that helps elderly
                            or non technical people understand technology 
                            and technological terms.Answer accordingly"""
        }
    ], "max_tokens":512
        
    })
    )
    
    return response.json()