from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup
import requests

from SprotifyMusic import app
from pyrogram.enums import ChatAction
from MukeshAPI import api

@app.on_message(filters.command(["chatgpt", "ask", "gpt", "ai"]))
async def gpt_bot(m, message):
    if len(message.command) < 2:
            await message.reply_text(
            "Example:**\n\n`/chatgpt write simple website code using html css ,js?`")
    else:
        a = message.text.split(' ', 1)[1]

    try:
        response = api.gemini(a)
        await m.send_chat_action(message.chat.id, ChatAction.TYPING)
        x=response["results"]
        
        await message.reply_text(f"{x}\n😎Powered by @SprotifyMusicBot ", quote=True)  
        
            
    except requests.exceptions.RequestException as e:
        pass