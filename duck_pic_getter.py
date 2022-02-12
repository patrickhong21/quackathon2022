from serpapi import GoogleSearch
from random import randint


def get_link() -> str:
    '''
    Gives link of random duck picture
    '''
    images_results = scrape_image()

    rand_int = randint(0, len(images_results) - 1)
    image_link = images_results[rand_int]['original']

    print(image_link)

    return image_link


def scrape_image() -> str:
    '''
    Get JSON in dict format from API
    '''
    params = {
        "q": "Duck Animal",
        "tbm": "isch",
        "ijn": "0",
        "api_key": "e191c33349d3ba314d5edd332fc577df540a383576e967f15a45f83a3d2be231"
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    images_results = results['images_results']

    return images_results
