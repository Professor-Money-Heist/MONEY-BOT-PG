import os

from telethon import Button, events

from userbot import *
from userbot.Config import Config
from userbot.plugins import *

LEGEND_IMG = os.environ.get(
    "BOT_PING_PIC", "https://te.legra.ph/file/e2382264c33ebe6f362cc.jpg"
)
ms = 4
ALIVE = Config.ALIVE_NAME

LegendBoy = f"**꧁•⊹٭Ping٭⊹•꧂**\n\n   ⚜ {ms}\n   ⚜ ❝𝐌𝐲 𝐌𝐚𝐬𝐭𝐞𝐫❞ ~『{ALIVE}』"


@tgbot.on(events.NewMessage(pattern="^/ping"))
async def _(event):
    GOOD = [[Button.url("💰𝙼𝙾𝙽𝙴𝚈 𝙷𝙴𝙸𝚂𝚃 𝙱𝙾𝚃💰", "https://t.me/MM_USERBOT")]]
    await tgbot.send_file(event.chat_id, MONEY_IMG, caption=PROF_AGORA, buttons=GOOD)
