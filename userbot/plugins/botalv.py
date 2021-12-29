from telethon import version

from userbot.utils import *
from userbot import *
from userbot.cmdhelp import CmdHelp

# -------------------------------------------------------------------------------

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "MONEY"

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

money = bot.uid

mention = f"[{DEFAULTUSER}](tg://user?id={money})"


PM_IMG = "https://telegra.ph/file/4f03f6d4e9521902eb57f.jpg"
pm_caption = "**𝐦𝐨𝐧𝐞𝐲 𝐡𝐞𝐢𝐬𝐭 𝐢𝐬 𝐨𝐧𝐥𝐢𝐧𝐞**\n\n"

pm_caption += f"**┏🔥𝐌𝐨𝐧𝐞𝐲 𝐇𝐞𝐢𝐬𝐭 𝐔𝐬𝐞𝐫𝐛𝐨𝐭🔥┓**\n"
pm_caption += f"**┣🚀 𝐌𝐲 𝐌𝐚𝐬𝐭𝐞𝐫 : {mention}**\n"
pm_caption += f"**┣🚀 𝐓𝐞𝐥𝐞𝐭𝐡𝐨𝐧 : `{version.__version__}`**\n"
pm_caption += f"**┣🚀 𝐏𝐫𝐨𝐟𝐞𝐬𝐬𝐨𝐫 : {LEGENDversion}**\n"
pm_caption += f"**┣🚀 𝐒𝐮𝐝𝐨     : `{sudou}`**\n"
pm_caption += f"**┣🚀 𝐎𝐰𝐧𝐞𝐫     : [𝐏𝐫𝐨𝐟𝐞𝐬𝐬𝐨𝐫](https://t.me/Prof_Agora)**\n"
pm_caption += f"**┗[♦️𝐒𝐮𝐩𝐩𝐨𝐫𝐭♦️](https://t.me/mm_Userbot)┛**\n"

pm_caption += "    [✨яєρο✨](https://github.com/Professor-Money-Heist/MONEY-HEIST-BOT) 🔹 [📜License📜](https://github.com/Professor-Money-Heist/MONEY-HEIST-BOT/blob/master/LICENSE)"


@bot.on(admin_cmd(outgoing=True, pattern="bot$"))
@bot.on(sudo_cmd(pattern="bot$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG, caption=pm_caption)
    await alive.delete()


CmdHelp("alv").add_command(
    "alive", None, "Check weather the bot is alive or not"
).add_command(
    "bot",
    None,
    "Check weather the bot is alive or not. In your custom Alive Pic and Alive Msg",
).add_warning(
    "Harmless Module"
).add_info(
    "Are u alive?"
).add_type(
    "Official"
).add()
