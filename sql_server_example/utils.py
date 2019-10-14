import requests


def get_first_google_result(query):
    search_results = requests.get(f"http://google.com/search?q={query}")
    first_url = search_results.text.split('/url')[1].split('BNeawe UPmit AP7Wnd')[1].split('<')[0][2:].split(' ')[0]
    return first_url
