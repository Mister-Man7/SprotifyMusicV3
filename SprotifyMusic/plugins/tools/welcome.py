from pyrogram.types import Message
from pyrogram import filters
from SprotifyMusic import app

import random

welcomeList = [
    "Bukan burung bukan pesawat! Tapi, {}",
    "{} adalah legenda dan wujud asli dari cahaya!",
    "Gausah join lu, {}! /kickme aja",
    "Plis bang ajak {}",
    "Woi {}! Lu dapet goceng",
    "We don't pray for love, we just pray for {}",
    "Mulut bergetar, {} bergoyang",
    "Sempat dinyatakan meninggal, ternyata {} mengalami mati suri! iiiiiiii",
    "{} dateng woi!!! kabur!",
    "{} said, don't give up! it's a little complicated.",
    "Kiw! Sungkem dulu sini sama {}",
]

@app.on_message(filters.new_chat_members)
async def new(_, m: Message):
    text = random.choice(welcomeList).format(m.from_user.mention())

    await m.reply(text)
