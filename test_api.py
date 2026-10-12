import requests
import json
from config import get_google_api_key

API_KEY = get_google_api_key()

# 2. The official Google direct URL for the gemini-1.5-flash model
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"

headers = {
    'Content-Type': 'application/json'
}

# 3. The test message
data = {
    "contents": [{
        "parts":[{"text": "Hi, are you working?"}]
    }]
}

print("Connecting directly to Google servers...\n")
response = requests.post(url, headers=headers, json=data)

# 4. Handling the response
if response.status_code == 200:
    print("✅ Connection successful! The API key works perfectly.")
    
    # Extracting the response text from the JSON structure
    reply = response.json()['candidates'][0]['content']['parts'][0]['text']
    print("Google's reply:", reply)
    print("\n💡 Conclusion: The issue is with the LangChain library settings, and we will fix it next.")
else:
    print(f"❌ Connection failed. Error code: {response.status_code}")
    print("Error details from Google:", response.text)