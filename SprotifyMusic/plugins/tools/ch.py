from datetime import datetime

from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS, PING_IMG_URL
from SprotifyMusic import app
from SprotifyMusic.utils import bot_sys_stats
from SprotifyMusic.utils.decorators.language import language

from SprotifyMusic.utils.database import get_active_chats, get_active_video_chats

@app.on_message(
    filters.command("respondtostatusbotbaby") & filters.private & ~BANNED_USERS
)
async def respondtobomt(client, message: Message):
    UP, CPU, RAM, DISK = await bot_sys_stats()
    if "%" in CPU:
        CPU = CPU.replace("%", "")
    if "%" in DISK:
        DISK = DISK.replace("%", "")
    active_voice = len(await get_active_chats())
    active_video = len(await get_active_video_chats())
    x = f"<b><u>Bot Status</b></u>\n\nDisk: {DISK}\nCPU: {CPU}\nUptime: {UP}\nStatus: {active_voice} active voice {active_video} active video"
    await message.reply_text(x) 
