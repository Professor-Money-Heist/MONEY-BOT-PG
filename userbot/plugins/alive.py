import time

from telethon import version
from telethon.errors import ChatSendInlineForbiddenError as noin
from telethon.errors.rpcerrorlist import BotMethodInvalidError as dedbot

from LEGENDBOT.utils import admin_cmd, edit_or_reply, sudo_cmd
from userbot import ALIVE_NAME, LEGENDversion
from userbot.cmdhelp import CmdHelp
from userbot.Config import Config

from . import *


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


uptime = get_readable_time((time.time() - StartTime))
DEFAULTUSER = ALIVE_NAME or "MONEY-HEIST-BOT 🇮🇳"
LEGEND_IMG = "https://te.legra.ph/file/919cfc634851f56370872.mp4"
CUSTOM_ALIVE_TEXT = Config.ALIVE_MSG or "𝙼𝙾𝙽𝙴𝚈 Choice 𝙼𝙾𝙽𝙴𝚈-𝙷𝙴𝙸𝚂𝚃-𝙱𝙾𝚃"
CUSTOM_YOUR_GROUP = Config.YOUR_GROUP or "@MM_USERBOT"

Legend = bot.uid
mention = f"[{DEFAULTUSER}](tg://user?id={Legend})"


@bot.on(admin_cmd(outgoing=True, pattern="legend$"))
@bot.on(sudo_cmd(pattern="legend$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = await reply_id(alive)

    if LEGEND_IMG:
        LEGEND_caption = f"**{CUSTOM_ALIVE_TEXT}**\n"

        LEGEND_caption += f"~~~~~~~~~~~~~~~~~~~~~~~\n"
        LEGEND_caption += f"        ** 𝙱𝙾𝚃 𝚂𝚃𝙰𝚃𝚄𝚂 ** \n"
        LEGEND_caption += f"•🔥• **𝙾𝚆𝙽𝙴𝚁**          ~ {ALIVE_NAME}\n\n"
        LEGEND_caption += f"•🌟• **𝙼𝙾𝙽𝙴𝚈 𝙷𝙴𝙸𝚂𝚃 𝙱𝙾𝚃  ~ {LEGENDversion}\n"
        LEGEND_caption += f"•🌟• **𝚃𝙴𝙻𝙴𝚃𝙷𝙾𝙽**     ~ `{version.__version__}`\n"
        LEGEND_caption += f"•🌟• **𝚄𝙿𝚃𝙸𝙼𝙴**         ~ `{uptime}`\n"
        LEGEND_caption += f"•🌟• **𝙶𝚁𝙾𝚄𝙿**           ~ [𝙶𝚁𝙾𝚄𝙿](t.me/MM_Userbot)\n"
        LEGEND_caption += f"•🌟• **𝙼𝚈 𝙶𝚁𝙾𝚄𝙿**  ~ {CUSTOM_YOUR_GROUP}\n"

        await alive.client.send_file(
            alive.chat_id, LEGEND_IMG, caption=LEGEND_caption, reply_to=reply_to_id
        )
        await alive.delete()
    else:
        await edit_or_reply(
            alive,
            f"**{CUSTOM_ALIVE_TEXT}**\n\n"
            f"~~~~~~~~~~~~~~~~~~~~~~~ \n"
            f"         \n"
            f"•⚡• 𝚃𝙴𝙻𝙴𝚃𝙷𝙾𝙽    : `{version.__version__}`\n"
            f"🇮🇳 𝙼𝙾𝙽𝙴𝚈-𝙷𝙴𝙸𝚂𝚃-𝙱𝙾𝚈: `{LEGENDversion}`\n"
            f"🇮🇳 𝚄𝙿𝚃𝙸𝙼𝙴        : `{uptime}`\n"
            f"🔱 𝙼𝙰𝚂𝚃𝙴𝚁        : {mention}\n"
            f"🔱 𝙾𝚆𝙽𝙴𝚁         : [𝙿𝚁𝙾𝙵𝙴𝚂𝚂𝙾𝚁](t.me/Prof_Agora)\n",
        )


msg = f"""
**  ⚜️ 𝙼𝙾𝙽𝙴𝚈-𝙷𝙴𝙸𝚂𝚃-𝙱𝙾𝚃 𝙸𝚂 𝙰𝙻𝙸𝚅𝙴 ⚜️**

       {Config.ALIVE_MSG}
    **  𝙱𝙾𝚃 𝚂𝚃𝙰𝚃𝚄𝚂 **
**•⚜️•𝙾𝚆𝙽𝙴𝚁     :** **[PROFESSOR](https://t.me/Prof_Agora)**
**•🌹•𝙼𝙾𝙽𝙴𝚈-𝙷𝙴𝙸𝚂𝚃-𝙱𝙾𝚃  :** {LEGENDversion}
**•🌹•𝚃𝙴𝙻𝙴𝚃𝙷𝙾𝙽  :** {version.__version__}
**•🌹•𝙰𝙱𝚄𝚂𝙴     :**  {abuse_m}
**•🌹•𝚂𝚄𝙳𝙾      :**  {is_sudo}
**•🌹•𝙱𝙾𝚃.      :** {Config.BOY_OR_GIRL}
"""
botname = Config.BOT_USERNAME


@bot.on(admin_cmd(pattern="alive$"))
@bot.on(admin_cmd(pattern="alive$", allow_sudo=True))
async def legend_a(event):
    try:
        legend = await bot.inline_query(botname, "alive")
        await legend[0].click(event.chat_id)
        if event.sender_id == The_LegendBoy:
            await event.delete()
    except (noin, dedbot):
        await eor(event, msg)


CmdHelp("alive").add_command("bot", None, "υѕє αи∂ ѕєє").add_command(
    "legend", None, "Its Same Like Alive"
).add_command("alive", None, "Its Show ur Alive Template").add_warning(
    "Harmless Module✅"
).add_info(
    "Checking Alive"
).add_type(
    "Official"
).add()
