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
pm_caption = "**๐ฆ๐จ๐ง๐๐ฒ ๐ก๐๐ข๐ฌ๐ญ ๐ข๐ฌ ๐จ๐ง๐ฅ๐ข๐ง๐**\n\n"

pm_caption += f"**โ๐ฅ๐๐จ๐ง๐๐ฒ ๐๐๐ข๐ฌ๐ญ ๐๐ฌ๐๐ซ๐๐จ๐ญ๐ฅโ**\n"
pm_caption += f"**โฃ๐ ๐๐ฒ ๐๐๐ฌ๐ญ๐๐ซ : {mention}**\n"
pm_caption += f"**โฃ๐ ๐๐๐ฅ๐๐ญ๐ก๐จ๐ง : `{version.__version__}`**\n"
pm_caption += f"**โฃ๐ ๐๐ซ๐จ๐๐๐ฌ๐ฌ๐จ๐ซ : {LEGENDversion}**\n"
pm_caption += f"**โฃ๐ ๐๐ฎ๐๐จ     : `{sudou}`**\n"
pm_caption += f"**โฃ๐ ๐๐ฐ๐ง๐๐ซ     : [๐๐ซ๐จ๐๐๐ฌ๐ฌ๐จ๐ซ](https://t.me/Prof_Agora)**\n"
pm_caption += f"**โ[โฆ๏ธ๐๐ฎ๐ฉ๐ฉ๐จ๐ซ๐ญโฆ๏ธ](https://t.me/mm_Userbot)โ**\n"

pm_caption += "    [โจััฯฮฟโจ](https://github.com/Professor-Money-Heist/MONEY-HEIST-BOT) ๐น [๐License๐](https://github.com/Professor-Money-Heist/MONEY-HEIST-BOT/blob/master/LICENSE)"


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
