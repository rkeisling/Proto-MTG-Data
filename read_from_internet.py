from requests import get

url_file = {
    'https://www.mtggoldfish.com/prices/paper/standard': 'standard.txt',
    'https://www.mtggoldfish.com/prices/paper/modern_two': 'modern_two.txt',
    'https://www.mtggoldfish.com/prices/paper/modern_one': 'modern_one.txt',
    'https://deckbox.org/sets/1029760/export?s=&f=&o=': 'inventory.txt'
}


def readFromInternet(url, filename):
    r = get(url)
    the_file = open(filename, 'w')
    the_file.write(r.text)


if __name__ == '__main__':
    for url, filename in url_file.items():
        readFromInternet(url, filename)
