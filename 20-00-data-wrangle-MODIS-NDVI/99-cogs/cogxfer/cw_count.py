import requests

def cw_count_words_at_url(url):
    resp = requests.get(url)
    return len(resp.text.split())
