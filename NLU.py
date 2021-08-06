import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, KeywordsOptions, EntitiesOptions

apikey = "XJX6gQPMRUfkx0USfzHIHrrPHnH5PEPycxZkIE6xAazh"

url = "https://api.eu-gb.natural-language-understanding.watson.cloud.ibm.com/instances/1ba469e8-195f-429f-a646-588c2d5dc3ef"

authenticator = IAMAuthenticator(apikey)
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2021-03-25',
    authenticator=authenticator
)

natural_language_understanding.set_service_url(url)

def getKeywords(dir):
    with open(dir, "r") as file:
        first_line = file.readline()
        for last_line in file:
            pass

    response = natural_language_understanding.analyze(
        #text='IBM is an American multinational technology company headquartered in Armonk, New York, United States with operations in over 170 countries.',
        text = first_line,
        features=Features(
            #entities=EntitiesOptions(emotion=True, sentiment=True, limit=2),
            keywords=KeywordsOptions(emotion=True, sentiment=True,
                                     limit=50))).get_result()

    enc = json.dumps(response, indent=2)
    dec = json.loads(enc)

    text = []
    count = 1
    for keyword in dec['keywords']:
            if keyword['relevance'] > 0.5:
                text.append("Keyword " + str(count) + ": " + keyword['text'] + '\n')
                print("Keyword " + str(count) + keyword['text'])
                count += 1
    with open(dir.replace("output", "keywords"), 'w') as out:
        out.writelines(text)
