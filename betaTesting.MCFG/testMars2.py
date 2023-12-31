import os
import requests
import importlib
from datetime import datetime
from bs4 import BeautifulSoup

cacheFolder = "catcheMars.MCFG"
if not os.path.exists(cacheFolder):
    os.makedirs(cacheFolder)

def download2(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as file:
        file.write(response.content)

def import2(module_name):
    return importlib.import_module(module_name)

def post2(title, date, description):
    print("Title:", title)
    print("Date:", date)
    print("Description:", description)
    print("\n" + "=" * 50 + "\n")

url = "https://services.www.fuzzythefoxx.site/V10/MARS/@NEWS/MNS-V01.py"
filename = os.path.join(cacheFolder,"nwsSrvrTEST.py")

download2(url, filename)
server = import2("nwsSrvrTEST.py")
serverPosts = server.posts

for post in serverPosts:
    title = serverPosts.get('title', 'No Title')
    date = serverPosts.get('date', datetime.now().strftime('%Y-%m-%d'))
    description = serverPosts.get('description', 'No Description')

    post2(title, date, description)