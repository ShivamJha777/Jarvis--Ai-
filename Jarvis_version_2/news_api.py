import json
import requests as re


def news_company_name(original_string, i):
    last_dash_index = original_string.rfind('-')
    source_name = original_string[last_dash_index+ 2:]
    final_string = f'News{i+1}: from {source_name},it says {original_string[11:last_dash_index]}'
    return final_string
def news(no_of_news):
    r = re.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=29dbe0ac800e42af9b4cc38677b0d9e0')
    data = json.loads(r.content)
    total_news = ''
    for i in range(no_of_news):
        news_title = f'News title: {data["articles"][i]["title"]}'
        formatted_news_title = news_company_name(news_title,i)
        print(formatted_news_title)
        total_news += f'{formatted_news_title}\n'
    return total_news
news(20)