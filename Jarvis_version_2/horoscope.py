import requests
from bs4 import BeautifulSoup
def get_horoscope(zodiac_symbol,day = 'today'):
    zodiac_signs = {
        'aries': 1,
        'taurus' : 2,
        'gemini' : 3,
        'cancer' : 4,
        'leo' : 5,
        'virgo' : 6,
        'libra' : 7,
        'scorpio' : 8,
        'sagittarius' : 9,
        'capricorn' : 10,
        'aquarius' : 11,
        'pisces' : 12
    }
    url = f'https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-{day}.aspx?sign={zodiac_signs[zodiac_symbol]}'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    data = soup.find('div',attrs={'class':'main-horoscope'})
    print(data.p.text)
    return data.p.text