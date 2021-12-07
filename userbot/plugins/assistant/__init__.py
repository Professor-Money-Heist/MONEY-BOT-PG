# LEGENDBOT Assistant
from telethon import Button, custom

from userbot import ALIVE_NAME, bot

from . import *

OWNER_NAME = ALIVE_NAME
OWNER_ID = bot.uid


PROFAGORA_USER = bot.me.first_name
PROF_AGORA = bot.uid

AGORA_mention = f"[{PROFAGORA_USER}](tg://user?id={PROF_AGORA})"
AGORA_logo = "./userbot/resources/pics/-6163428037589314866_121.jpg"
AGORA_logo1 = "./userbot/resources/pics/-4965507108355287505_121.jpg"
AGORA_logo2 = "./userbot/resources/pics/-4965507108355287505_121.jpg"
AGORA_logo4 = "./userbot/resources/pics/-4965507108355287505_121.jpg"
AGORA_logo3 = "./userbot/resources/pics/-4965507108355287505_121.jpg"
AGORAversion = "𝚅10.1"

perf = "[ MONEY HEIST BOT FULL ADVANCED]"


DEVLIST = ["2082798662"]


async def setit(event, name, value):
    try:
        event.set(name, value)
    except BaseException:
        return await event.edit("`Something Went Wrong`")


def get_back_button(name):
    button = [Button.inline("« Bᴀᴄᴋ", data=f"{name}")]
    return button
