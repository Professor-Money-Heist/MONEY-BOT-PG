import os

from telethon import TelegramClient

try:
    from userbot import bot
except:
    pass

API_ID = os.environ.get("APP_ID", None)
API_HASH = os.environ.get("API_HASH", None)
token = os.environ.get("BOT_TOKEN", None)
lnbot = TelegramClient("legendboy", API_ID, API_HASH).start(bot_token=token)

if __name__ == "__main__":
    bot.start()
    bot.run_until_disconnected()
    lnbot.run_until_disconnected()
