import requests
import json


def instagram_download(link):
	url = "https://instagram-downloader-download-instagram-videos-stories.p.rapidapi.com/index"

	querystring = {"url":link}

	headers = {
		"X-RapidAPI-Key": "28d0d114c8msh5b9ad1427ffbd16p1c86a9jsn15d5cd9c4ddc",
		"X-RapidAPI-Host": "instagram-downloader-download-instagram-videos-stories.p.rapidapi.com"
	}

	response = requests.request("GET", url, headers=headers, params=querystring)
	rest = json.loads(response.text)
	if 'error' in rest:
		return 'Bad'
	else:
		dict = {}
		if rest['Type'] == "Post-Image":
			dict['type'] = 'image'
			dict['media'] = rest['media']
			return dict
		elif rest['Type'] == "Post-Video":
			dict['type'] = 'video'
			dict['media'] = rest['media']
			return dict
		elif rest['Type'] == 'Carousel':
			dict['type'] = 'carousel'
			dict['media'] = rest['media']
			return dict
		else:
			return 'Bad'