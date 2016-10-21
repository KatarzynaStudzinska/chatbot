from watson_developer_cloud import SpeechToTextV1
import json


import requests
import json
import os

url = "https://stream.watsonplatform.net/speech-to-text/api"
username = "734cad41-7f47-46da-869a-bcd63a42ed98"
password = "rlz2M6qjaDux"

filepath = 'file.wav'  # path to file
filename = os.path.basename(filepath)

audio = open(filepath ,'rb')

files_input = {
 "audioFile":(filename,audio,'audio/wav')
}

response = requests.post(url, auth=(username, password), headers={"Content-Type": "audio/wav"},files=files_input)

print('stauts_code: {} (reason: {})'.format(response.status_code, response.reason))

print response.text

stt = SpeechToTextV1(username=username, password=password)
print(stt)
audio_file = open("file.wav", "rb")

print json.dumps(stt.recognize(audio_file, content_type="audio/wav"), indent=2)
