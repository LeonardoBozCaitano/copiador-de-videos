from gtts import gTTS
from io import BytesIO
import base64
import requests
import json
import os
from dotenv import load_dotenv
import hashlib 
from datetime import datetime

def makeHashName():
    dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    string_to_hash = dt_string + "prompt_response"
    hasher = hashlib.md5()
    hasher.update(string_to_hash.encode('utf-8'))
    hex_hash = hasher.hexdigest()
    return hex_hash

def get_audio_bytes_from(text):
    url = "https://api.elevenlabs.io/v1/text-to-speech/" + "INSERT YOUR KEY"

    payload = json.dumps({
    "text": text, 
    "voice_settings": {
        "stability":  0.5,
        "similarity_boost": 0.33
    }
    })
    headers = {
    'xi-api-key': os.getenv('SEVENELABS_API_KEY'),
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    hashName = makeHashName()

    with open(hashName+'.mp3', 'wb') as f:
        f.write(response.content)

    with open(hashName+'.mp3', 'rb') as f:
        audio_base64 = base64.b64encode(f.read())

    return audio_base64.decode('utf-8')
