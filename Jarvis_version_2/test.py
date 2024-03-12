from bs4 import BeautifulSoup
import requests
query = 'bad'
url = 'https://www.thesaurus.com/browse/'+ query
html = requests.get(url).content
soup = BeautifulSoup(html, 'html.parser')
synoym = getattr(soup.find('ul', attrs={'class': 'LhpJmDktqk95S2vWg1JZ'}), 'text', None)
synoym = str(synoym)
import re

def separate_words(words):
    # Use regular expression to find all words
    word = re.findall('[A-Z]?[a-z]+', words)
    return word

# Example usage
separated_words = separate_words(synoym)
print(separated_words)
