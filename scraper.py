import requests
from bs4 import BeautifulSoup
import os


def imageDownload(url, folder):
    try:
        os.mkdir(os.path.join(os.getcwd(), folder))
    except:
        pass
    
    os.chdir(os.path.join(os.getcwd(), folder))
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    images = soup.find_all('img')

    for image in images:
        name = image['alt']
        link = image['src']
        with open(name.replace(' ', '-').replace('/', '').replace('!', '') + '.jpg', 'wb') as f:
            im = requests.get(link)
            f.write(im.content)
            print("Writing: {}".format(name))

a = input("Enter url: ")
b = input("Enter folder name: ")

imageDownload(a, b)




