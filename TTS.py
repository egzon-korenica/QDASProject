# Install dependencies
# authenticate
# convert a string
# convert fromm a file
# using new language models

url = 'https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/58f23641-330d-4584-a281-1fa87ff5431a'
apikey = 'EWtDUdU2pOw1TCVwiQtSPX7uSva3QSg8QBXzJpFX9Tbx'

from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# setup service
authenticator = IAMAuthenticator(apikey)
#new tts service
tts = TextToSpeechV1(authenticator=authenticator)
# set service url
tts.set_service_url(url)

with open('./speech.mp3', 'wb') as audio_file:
    res = tts.synthesize("Hello WORLD WORLD WORLD WORLD", accept='audio/mp3', voice='en-US_LisaV3Voice').get_result()
    audio_file.write(res.content)


# read from file
with open("covid.txt", 'r') as f:
    text = f.readlines()

text = [line.replace('\n', '') for line in text]
#text = ''.join(str(line) for line in text)

counter = 0
for sentence in text:
    with open('./audio/{counter:04d}.mp3'.format(counter=counter), 'wb') as audio_file:
        res = tts.synthesize(sentence, accept='audio/mp3', voice='en-GB_JamesV3Voice').get_result()
        audio_file.write(res.content)
        counter +=1

#with open('./covid.mp3', 'wb') as audio_file:
#    res = tts.synthesize(text, accept='audio/mp3', voice='en-US_LisaV3Voice').get_result()
#    audio_file.write(res.content)
