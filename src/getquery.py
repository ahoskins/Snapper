import json, urllib
import random

def offset():
	return random.randint(0, 10)

def getindex(maxindex):
    return random.randint(0, maxindex)

def thechosenone(results):
    length = len(results)
    while True:
        index = getindex(length - 1)
        result = results[index]
        if result['medium'] == 'SCULPTURE' or result['medium'] == 'MURAL':
            return result

def getsearchquery():
    url = 'http://api.namara.io/v0/data_sets/51b6af69-fcd9-4517-ac6b-39e89310c1eb/data/en-1?api_key=a4a9c51c599083326fc49989d6b8b0ce8f107183525404677898a5c851f70989&offset=' + str(offset())
    print url
    search_response = urllib.urlopen(url)
    search_results = search_response.read()
    results = json.loads(search_results)

    chosen = thechosenone(results)
    return dict({ 'title': chosen['title'], 'artist': chosen['artist_name'] })
