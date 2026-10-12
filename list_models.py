import requests
import json
from config import get_google_api_key

API_KEY = get_google_api_key()

# The URL to ask Google for all available models
url = f"https://generativelanguage.googleapis.com/v1beta/models?key={API_KEY}"

print("Asking Google for the list of available models...\n")

# Sending a GET request to read the models
response = requests.get(url)

if response.status_code == 200:
    print("✅ Success! Here are the models you can use:")
    print("-" * 40)
    
    data = response.json()
    for model in data.get('models', []):
        # Print only models that generate text
        if 'generateContent' in model.get('supportedGenerationMethods', []):
            print(f"👉 {model['name']}")
            
    print("-" * 40)
else:
    print(f"❌ Failed. Error code: {response.status_code}")
    print("Error details:", response.text)