from aiogram import types
from aiogram.dispatcher.filters import Text

from handlers.users.yutube.convert import youtub
from loader import dp


@dp.message_handler(Text(startswith="https://youtu"))
async def linkniki(message: types.Message):
    link = message.text
    url = youtub(link=link)
    await message.answer_video(video=url['formats'][2]['url'],
                               caption=url['title'])












# import requests
#
# url = "https://ytstream-download-youtube-videos.p.rapidapi.com/dl"
#
# querystring = {"id":"UxxajLWwzqY"}
#
# headers = {
# 	"X-RapidAPI-Key": "c15eae257dmshe2a302492098711p1c8bedjsnfc3ddb27f70d",
# 	"X-RapidAPI-Host": "ytstream-download-youtube-videos.p.rapidapi.com"
# }
#
# response = requests.get(url, headers=headers, params=querystring)
#
# print(response.json())