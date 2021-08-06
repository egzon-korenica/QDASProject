apikey = "KobRgKpaAwmvjjOmKoZIxPZcQ33f0Y3ap1Y_Rz3tX4e7"
url = "https://api.eu-gb.tone-analyzer.watson.cloud.ibm.com/instances/372cbdb1-3eb7-4948-8390-c99205593cb7"

from ibm_watson import ToneAnalyzerV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import json

authenticator = IAMAuthenticator(apikey)
ta = ToneAnalyzerV3(version='2021-08-02', authenticator = authenticator)
ta.set_service_url(url)

#res = ta.tone("This sucks, i wish i wasnt here").get_result()

'''
with open("interviews/interview_1/output.txt", "r") as file:
    first_line = file.readline()
    for last_line in file:
        pass
'''

def getToneAnalysis(dir):
    with open(dir, "r") as file:
        first_line = file.readline()
        for last_line in file:
            pass
    res = ta.tone(first_line).get_result()
    enc = json.dumps(res)
    dec = json.loads(enc)

    #print(dec)
    count = 1
    text = []
    for i in dec['document_tone']['tones']:
        print("Tone " + str(count) + ": " + i['tone_name'])
        text.append("Tone in response " + str(count) + ": " + i['tone_name'] + '\n')
        count +=1
    with open(dir.replace("output", "toneanalysis"), 'w') as out:
        out.writelines(text)

#getToneAnalysis("interviews/interview_2/output.txt")
