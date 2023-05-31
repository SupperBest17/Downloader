

import requests
from aiogram.utils.json import json


def tikotk(link):
	url = "https://tiktok-video-no-watermark2.p.rapidapi.com/"

	querystring = {"url":link,"hd":"1"}

	headers = {
		"X-RapidAPI-Key": "c15eae257dmshe2a302492098711p1c8bedjsnfc3ddb27f70d",
		"X-RapidAPI-Host": "tiktok-video-no-watermark2.p.rapidapi.com"
	}

	response = requests.get(url, headers=headers, params=querystring)
	rest = json.loads(response.text)
	return rest