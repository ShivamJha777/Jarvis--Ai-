
import json
import requests


def get_fun_fact(za_hell):
    url = "https://uselessfacts.jsph.pl/random.json?language=en"


    response = requests.request("GET", url)

    data = json.loads(response.text)

    useless_fact = data['text']
    return useless_fact