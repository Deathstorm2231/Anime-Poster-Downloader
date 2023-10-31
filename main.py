# Import Required Module
import requests
from bs4 import BeautifulSoup
import re
import os

#url='https://aniwatch.to/most-popular'
folder_name=input(print('Name the folder you want to download in:'))
def imagedown(url,folder):
    try:
        os.mkdir(os.path.join(os.getcwd(),folder))
    except:
        pass
    os.chdir(os.path.join(os.getcwd(),folder))
    r = requests.get(url)

    soup = BeautifulSoup(r.content, 'lxml')
    images=soup.find_all('img')

    for image in images:
        name = re.search("alt.*?\".*?\"",str(image))
        if name is None:
            continue
        link = re.search("src.*?\".*?\"",str(image))
        if link is None:
            continue
        #print(name.group()[5:-1])
        #print(link.group()[5:-1])
        #print(" ")
        with open(name.group()[5:-1] + '.jpg', 'wb') as f:
            try: 
                img = requests.get(link.group()[5:-1])
                f.write(img.content)
            except requests.exceptions.MissingSchema:
                print("Invalid url")
        
            print('Downloading: ', name.group()[5:-1])


imagedown('https://aniwatch.to/most-popular',folder_name)