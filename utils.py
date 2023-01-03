import json
import requests

from classes import BasicWord

def load_random_word():
    """Loads word list from url (json format), select random word,
    create BasicWord instance, return it"""
    url = 'https://www.jsonkeeper.com/b/51AN'

    responce = requests.get(url)
    print(f'responce.status_code = {responce.status_code}')
    if responce.status_code == 200:
        words = responce.json()

    print(words[0])
    print(words[1])
    print(words[2])


if __name__ == '__main__':
    load_random_word()