from pyrogram import filters
from SprotifyMusic import app

# Variabel global
tracked_users = {}

# Fungsi untuk melacak perubahan nama dan username
async def track_user(app, message):
    user = message.from_user
    if user.id in tracked_users:
        tracked_users[user.id]['name'] = user.first_name + ' ' + user.last_name
        tracked_users[user.id]['username'] = user.username
    else:
        tracked_users[user.id] = {
            'name': user.first_name + ' ' + user.last_name,
            'username': user.username
        }

# Fungsi untuk menghandle pesan baru
async def handle_new_message(app, message):
    await track_user(app, message)

    if message.from_user.id in tracked_users and message.from_user.first_name + ' ' + message.from_user.last_name != tracked_users[message.from_user.id]['name']:
        old_name = tracked_users[message.from_user.id]['name']
        new_name = message.from_user.first_name + ' ' + message.from_user.last_name
        await send_name_change_alert(app, message, old_name, new_name)
        tracked_users[message.from_user.id]['name'] = new_name

    if message.from_user.id in tracked_users and message.from_user.username != tracked_users[message.from_user.id]['username']:
        old_username = tracked_users[message.from_user.id]['username']
        new_username = message.from_user.username
        await send_username_change_alert(app, message, old_username, new_username)
        tracked_users[message.from_user.id]['username'] = new_username

# Fungsi untuk mengirim pesan peringatan perubahan nama
@app.on_message(filters.new_chat_members, handle_new_message)
async def send_name_change_alert(app, message, old_name, new_name):
    text = f" Peringatan Perubahan Nama! \n\n"
    text += f"User: {message.from_user.first_name} {message.from_user.last_name} ({message.from_user.id})\n"
    text += f"Nama Lama: {old_name}\n"
    text += f"Nama Baru: {new_name}"
    await app.send_message(chat_id=message.chat.id, text=text)

# Fungsi untuk mengirim pesan peringatan perubahan username
async def send_username_change_alert(app, message, old_username, new_username):
    text = f" Peringatan Perubahan Username! \n\n"
    text += f"User: {message.from_user.first_name} {message.from_user.last_name} ({message.from_user.id})\n"
    text += f"Username Lama: {old_username}\n"
    text += f"Username Baru: {new_username}"
    await app.send_message(chat_id=message.chat.id, text=text)

