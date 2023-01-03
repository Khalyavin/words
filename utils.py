import json
import random
import requests

from classes import BasicWord


def load_random_word() -> BasicWord:
    """Loads word list from url (json format), select random word,
    create BasicWord instance, return it"""
    url = 'https://www.jsonkeeper.com/b/51AN'

    global words

    responce = requests.get(url)

    if responce.status_code == 200:
        words = responce.json()

    word = words[random.randint(0, len(words) - 1)]

    subj = BasicWord(word.get('word'), word.get('subwords'))

    return subj


if __name__ == '__main__':
    words = []

    load_random_word()

    assert words[0].get('word') == 'питон'
    assert words[0].get('subwords')[1] == 'тон'