import os

from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from telegraph import upload_file

from SprotifyMusic import app


@app.on_message(filters.command(["tgm", "tgt", "telegraph", "tl"]))
async def get_link_group(client, message):
    if not message.reply_to_message:
        return await message.reply_text(
            "ᴘʟᴇᴀsᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇᴅɪᴀ ᴛᴏ ᴜᴘʟᴏᴀᴅ ᴏɴ ᴛᴇʟᴇɢʀᴀᴘʜ"
        )
    try:
        text = await message.reply("Processing...")

        async def progress(current, total):
            await text.edit_text(f"📥 Downloading... {current * 100 / total:.1f}%")

        try:
            local_path = await message.reply_to_message.download( progress=progress
            )
            await text.edit_text("📤 Uploading to Telegraph...")
            upload_path = upload_file(local_path)
            await text.edit_text(
                f"🌐 | [Telegraph Link](https://telegra.ph{upload_path[0]})",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "Telegraph Link",
                                url=f"https://telegra.ph{upload_path[0]}",
                            )
                        ]
                    ]
                ),
            )
            try:
                os.remove(local_path)
            except Exception:
               pass
        except Exception as e:
            await text.edit_text(f"❌ |File Upload Failed \n\n<i>Reason: {e}</i>")
            try:
                os.remove(local_path)
            except Exception:
               pass
            return
    except Exception:
        pass