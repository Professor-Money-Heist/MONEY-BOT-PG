import time

from telethon import version

from LEGENDBOT.utils import admin_cmd, edit_or_reply, sudo_cmd
from userbot import LEGENDversion, StartTime
from userbot.cmdhelp import CmdHelp

from . import *


async def reply_id(event):
    reply_to_id = None
    if event.sender_id in Config.SUDO_USERS:
        reply_to_id = event.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    return reply_to_id


LEGEND_IMG = Config.AWAKE_PIC
CUSTOM_ALIVE_TEXT = Config.ALIVE_MSG or "PROFESSOR AGORA"
CUSTOM_YOUR_GROUP = Config.YOUR_GROUP or "@MM_Userbot"


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


@bot.on(admin_cmd(outgoing=True, pattern="awake$"))
@bot.on(sudo_cmd(pattern="awake$", allow_sudo=True))
async def amireallyalive(event):
    if event.fwd_from:
        return
    reply_to_id = await reply_id(event)

    if LEGEND_IMG:
        LEGEND_caption = f"**{legend_mention}**\n"

        LEGEND_caption += f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
        LEGEND_caption += f"     💰𝙼𝙾𝙽𝙴𝚈 𝙷𝙴𝙸𝚂𝚃 𝙸𝚂 𝙰𝚆𝙰𝙺𝙴💰\n"
        LEGEND_caption += f"•🔥• 𝙼𝙾𝙽𝙴𝚈 𝙷𝙴𝙸𝚂𝚃 𝙱𝙾𝚃 : ν3.0\n"
        LEGEND_caption += f"•🔥• 𝚃𝙴𝙻𝙴𝚃𝙷𝙾𝙽: `{version.__version__}`\n"
        LEGEND_caption += f"•🔥• 𝚄𝙿𝚃𝙸𝙼𝙴: `{uptime}`\n" 
        LEGEND_caption += f"•🔥• 𝚂𝚄𝙿𝙿𝙾𝚁𝚃: `[𝙼𝙷𝚄𝙱](https://t.me/MM_USERBOT)\n"

        await event.client.send_file(
            event.chat_id, LEGEND_IMG, caption=LEGEND_caption, reply_to=reply_to_id
        )
        await event.delete()
    else:
        await edit_or_reply(
            awake,
            f"**{CUSTOM_ALIVE_TEXT}**\n\n"
            f"~~~~~~~~~~~~~~~~~~~~~~~ \n"
            f"       𝙼𝙾𝙽𝙴𝚈 𝙷𝙴𝙸𝚂𝚃 𝙱𝙾𝚃 𝚂𝚃𝙰𝚃𝚄𝚂\n"
            f"•⚡• 𝚃𝙴𝙻𝙴𝚃𝙷𝙾𝙽       : `{version.__version__}`\n"
            f"•💰• 𝙼𝙾𝙽𝙴𝚈𝙷𝙴𝙸𝚂𝚃𝙱𝙾𝚃  : `{LEGENDversion}`\n"
            f"•💥• 𝚄𝙿𝚃𝙸𝙼𝙴         : `{uptime}`\n"
            f"•💰• 𝙼𝙰𝚂𝚃𝙴𝚁         : `{mention}\n"
            f"•👨‍🏫• 𝙾𝚆𝙽𝙴𝚁          : `[𝙿𝚁𝙾𝙵𝙴𝚂𝚂𝙾𝚁](t.me/PROFESSOR_AGORA)\n",
        )


CmdHelp("awake").add_command("awake", None, "υѕє αи∂ ѕєє").add_info(
    "Same Like Alive"
).add_type("Official").add()
