from serpapi import GoogleSearch
from random import randint
from typing import List
from tokens import get_api_token


def get_news() -> List[str]:
    '''
    Produces a few sentences of news with url appended at the end.
    '''

    news_results = scrape_news()

    rand_int = randint(0, len(news_results) - 1)
    news_snippet = news_results[rand_int]["snippet"].replace("\n", "")
    news_url = news_results[rand_int]["link"]

    return [news_snippet, news_url]


def scrape_news() -> dict:
    '''
    Get JSON in dict format from API
    '''
    params = {
    "q": "duck animal",
    "tbm": "nws",
    "api_key": get_api_token()
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    news_results = results['news_results']

    return news_results
