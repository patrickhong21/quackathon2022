from serpapi import GoogleSearch
from random import randint
from tokens import get_api_token


def get_link() -> str:
    '''
    Gives link of random duck picture
    '''
    images_results = scrape_image()

    rand_int = randint(0, len(images_results) - 1)
    image_link = images_results[rand_int]['original']

    return image_link


def scrape_image() -> dict:
    '''
    Get JSON in dict format from API
    '''
    params = {
        "q": "Duck Animal",
        "tbm": "isch",
        "ijn": "0",
        "api_key": get_api_token()
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    images_results = results['images_results']

    return images_results
