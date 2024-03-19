from bs4 import BeautifulSoup
import requests
from Jarvis_version_2.speech_say_commands import speak
def synonym(word):
    try:
        url = 'https://www.thesaurus.com/browse/'+ word
        html = requests.get(url).content
        soup = BeautifulSoup(html, 'html.parser')

        synonyms = []
        ul_tag = soup.find('ul', class_='LhpJmDktqk95S2vWg1JZ')
        if ul_tag:
            for li_tag in ul_tag.find_all('li'):
                synonyms.append(li_tag.get_text(strip=True))
        list_of_s = ''
        for synonym in synonyms:
            list_of_s += synonym
            list_of_s += ','
        speak(f'The synonym of {word} are {list_of_s}')
    except:
        speak('Sorry Boss some error occurred')