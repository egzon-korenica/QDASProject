apikey = "KobRgKpaAwmvjjOmKoZIxPZcQ33f0Y3ap1Y_Rz3tX4e7"
url = "https://api.eu-gb.tone-analyzer.watson.cloud.ibm.com/instances/372cbdb1-3eb7-4948-8390-c99205593cb7"

from ibm_watson import ToneAnalyzerV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator(apikey)
ta = ToneAnalyzerV3(version='2021-08-02', authenticator = authenticator)
ta.set_service_url(url)

#res = ta.tone("This sucks, i wish i wasnt here").get_result()

chat = [
    {
    "text": "I feel great, it's sunny outside, and I've got all my work done",
    "user":"He who shall not be named"
    },
    {
    "text":"This sucks, I have like 500 hours more coding to do. This is going to take all weekend",
    "user": "Nick"
    },
]

with open("interviews/interview_1/output.txt", "r") as file:
    first_line = file.readline()
    for last_line in file:
        pass

res = ta.tone(first_line)
print(res)
print(first_line)
