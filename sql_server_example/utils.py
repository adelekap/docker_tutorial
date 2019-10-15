from bs4 import BeautifulSoup
import requests

USER_AGENT = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}


def get_first_google_result(query):
    response = requests.get(f"http://google.com/search?q={query}",headers=USER_AGENT)
    soup = BeautifulSoup(response.text)
    result = soup.find_all('div', attrs={'class': 'g'})[0]
    link = result.find('a', href=True).attrs['href']
    return link
