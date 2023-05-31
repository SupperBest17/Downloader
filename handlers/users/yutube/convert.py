



import requests
from aiogram.utils.json import json


def youtub(link):
    url = "https://ytstream-download-youtube-videos.p.rapidapi.com/dl"
    link1 = link[17:]
    querystring = {"id":link1}

    headers = {
    	"X-RapidAPI-Key": "c15eae257dmshe2a302492098711p1c8bedjsnfc3ddb27f70d",
    	"X-RapidAPI-Host": "ytstream-download-youtube-videos.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    print(response.json())
    rest = json.loads(response.text)
    return rest
