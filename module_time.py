import time
from pyrogram import Client, filters
from datetime import datetime, timedelta

with open("userbot.info", "r") as file:
    lines = file.readlines()
    prefix_userbot = lines[2].strip()
last_command_time = {}
cinfo = f"⌛`{prefix_userbot}time`"
ccomand = " Показывает время пользователя юб."


def command_time(app):
    @app.on_message(filters.command(["time"], prefixes=prefix_userbot))
    def send_time(_, message):
        user_id = message.from_user.id
        current_time = datetime.now().strftime("%H:%M:%S")
        if user_id in last_command_time and time.time() - last_command_time[user_id] < 1:
            message.reply_text("Не так часто!")
        else:
            message.reply_text(f"**⌛Время пользователя: {current_time}**")
            last_command_time[user_id] = time.time()

print("Модуль time загружен!")
