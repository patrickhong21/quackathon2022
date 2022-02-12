from serpapi import GoogleSearch
from random import randint
from typing import List

def get_news() -> List[str]:
    '''
    Produces a few sentences of news with url appended at the end.
    ''' 
    print(scrape_news())
    return scrape_news()


def scrape_news() -> List[str]:
    '''
    api get json
    '''
    params = {
    "q": "duck animal",
    "tbm": "nws",
    "api_key": "7babd63756f443d283ecd3fd67e39fe3af581203b500dec3e42b47ba6b1e2ca8"
    }


    search = GoogleSearch(params)
    results = search.get_dict()
    news_results = results['news_results']

    rand_Integer = randint(0,len(news_results)-1)

    news_snippet = news_results[rand_Integer]["snippet"]
    news_url = news_results[rand_Integer]["link"]



    return [news_snippet,news_url]
    
get_news()


