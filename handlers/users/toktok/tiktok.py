



from aiogram import types
from aiogram.dispatcher.filters import Text

from handlers.users.toktok.send import tikotk
from loader import dp


@dp.message_handler(Text(startswith="https://vt.tiktok.com/"))
async def tikiki(message: types.Message):
    link = message.text
    url = tikotk(link=link)

    await message.answer_video(video=url['data']['hdplay'],
                               caption=url['data']['title'])


