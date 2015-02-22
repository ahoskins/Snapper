import json, urllib
import random

# SCULPTURE
# MURAL
# 

def offset():
	return random.randint(0, 10)

def limit():
	return random.randint(10, 20)

def thechosenone(results):
	for result in results:
		if result['medium'] == 'SCULPTURE' or result['medium'] == 'MURAL':
			return result

def getsearchquery():
    url = 'http://api.namara.io/v0/data_sets/51b6af69-fcd9-4517-ac6b-39e89310c1eb/data/en-1?api_key=a4a9c51c599083326fc49989d6b8b0ce8f107183525404677898a5c851f70989&offset=' + str(offset()) + '&limit=' + str(limit())
    search_response = urllib.urlopen(url)
    search_results = search_response.read()
    results = json.loads(search_results)

    chosen = thechosenone(results)
    return chosen['title'] + ' ' + chosen['artist_name']

# if __name__ == '__main__':
# 	getsearchquery()