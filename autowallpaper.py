import requests as req
import urllib.request as url
import os
import ctypes
import random
from datetime import date

def download_wallpaper(collection, count, client_id):
    get_request = req.get('https://api.unsplash.com/search/photos?query={}&orientation=landscape&page=1&per_page={}&client_id={}'.format(collection,count,client_id))
    data = get_request.json()
    try:
        image_number=random.randint(0, len(data['results'])-1)
        img_data = data['results'][image_number]
        img_url = img_data['urls']['raw']

        file_name = str(date.today())+'.jpg'
        dynamic_resize='&q=100&fm=jpg&crop=edges&fit=max'
        retrieval_url = img_url + dynamic_resize

        url.urlretrieve(retrieval_url, file_name)
        return file_name
    except:
        print("exception occured")
        return 0

def set_wallpaper(file_name):
    try:
        pathToImage=os.path.normpath(os.getcwd()+"\\"+file_name)
        SPI_SETDESKTOPWALLPAPER=20
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKTOPWALLPAPER, 0, pathToImage, 0)
        return pathToImage
    except:
        print("Exception occured")
        return False

def auto_wallpaper():
    filters=["mountains", "nature", "citylights", "lights", "campfire"]
    per_page=20
    client_id='snUZSN9SsbFP-tko3vJotEIjdX60iaumYPx55UrVGE4'

    file_name = download_wallpaper(random.choice(filters), per_page, client_id)
    if not file_name==0:
        set_wallpaper(file_name)
    else:
        print("not successful")


auto_wallpaper()
