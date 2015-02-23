from argparse import ArgumentParser
from snapchat_bots import SnapchatBot, Snap
import requests
import tempfile
import urlparse
import os
import json, urllib

from getquery import getsearchquery

def get_url_extension(url):
    path = urlparse.urlparse(url).path
    return os.path.splitext(path)[1]

def download_file(url):
    resp = requests.get(url)
    local_file = tempfile.NamedTemporaryFile(suffix = get_url_extension(url), delete=False)
    local_file.write(resp.content)
    return local_file.name

def search(query):
    query = urllib.urlencode({'q': query})
    url = 'http://ajax.googleapis.com/ajax/services/search/images?v=1.0&%s' % query
    search_response = urllib.urlopen(url)
    search_results = search_response.read()
    results = json.loads(search_results)
    
    data = results['responseData']
    hits = data['results']

    return hits[0]['url']

class ReflectorBot(SnapchatBot):
    def on_snap(self, sender, snap):
        query = getsearchquery()
        local_filename = download_file(search(query))
        snap = Snap.from_file(local_filename, query)
        self.send_snap([sender], snap)

    def on_friend_add(self, friend):
        self.add_friend(friend)

    def on_friend_delete(self, friend):
        self.delete_friend(friend)

if __name__ == '__main__':
    parser = ArgumentParser("Reflector Bot")
    parser.add_argument('-u', '--username', required=True, type=str, help="Username of the account to run the bot on")
    parser.add_argument('-p', '--password', required=True, type=str, help="Password of the account to run the bot on")

    args = parser.parse_args()

    bot = ReflectorBot(args.username, args.password)
    bot.listen(timeout=5)
