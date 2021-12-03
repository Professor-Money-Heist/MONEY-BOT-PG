from telethon.errors import ChatSendInlineForbiddenError as noin
from telethon.errors.rpcerrorlist import BotInlineDisabledError as noinline
from telethon.errors.rpcerrorlist import BotMethodInvalidError as dedbot
from telethon.errors.rpcerrorlist import YouBlockedUserError

from LEGENDBOT.utils import admin_cmd, sudo_cmd
from userbot import CMD_LIST, bot
from userbot.Config import Config

from . import *

perf = "[ †hê Lêɠêɳ̃dẞø† ]"

onbot = "start - Check if I am Alive \nhack - Hack Anyone Through String Session\nping - Pong! \ntr - <lang-code> \nbroadcast - Sends Message To all Users In Bot \nid - Shows ID of User And Media. \naddnote - Add Note \nnotes - Shows Notes \nspam - spam value text (value < 100)\nbigsam - spam value text (value > 100) \nraid - Raid value Reply to Anyone \nreplyraid - Reply To Anyone \ndreplyraid - Reply To Anyone \nrmnote - Remove Note \nalive - Am I Alive? \nbun - Works In Group , Bans A User. \nunbun - Unbans A User in Group \nprumote - Promotes A User \ndemute - Demotes A User \npin - Pins A Message \nstats - Shows Total Users In Bot \npurge - Reply It From The Message u Want to Delete (Your Bot Should be Admin to Execute It) \ndel - Reply a Message Tht Should Be Deleted (Your Bot Should be Admin to Execute It)"

name = f"{legend_mention}'s Assistant"

file = "https://te.legra.ph/file/0a1fa23cbb1e6520f6550.jpg"
description = (
    f"I am Assistant Of {legend_mention}.This Bot Can Help U To Chat With My Master"
)
bot_father = "@BotFather"
mybot = Config.BOT_USERNAME
if mybot.startswith("@"):
    botname = mybot
else:
    botname = f"@{mybot}"


msg = f"""
**⚜ 𝙻𝚎𝚐𝚎𝚗𝚍𝚊𝚛𝚢 𝙰𝚏 𝙻𝚎𝚐𝚎𝚗𝚍𝙱𝚘𝚝 ⚜**

  •        [♥️ 𝚁𝚎𝚙𝚘 ♥️](https://github.com/LEGEND-OS/LEGENDBOT)
  •        [♦️ Deploy ♦️](https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FLEGEND-OS%2FLEGENDBOT&template=https%3A%2F%2Fgithub.com%2FLEGEND-OS%2FLEGENDBOT)

  •  ©️ {Legend_channel} ™
"""


@bot.on(admin_cmd(pattern="repo$"))
@bot.on(sudo_cmd(pattern="repo$", allow_sudo=True))
async def repo(event):
    try:
        legend = await bot.inline_query(botname, "repo")
        await legend[0].click(event.chat_id)
        if event.sender_id == The_LegendBoy:
            await event.delete()
    except (noin, dedbot):
        await eor(event, msg)


@bot.on(admin_cmd(pattern="help ?(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="help ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    tgbotusername = botname
    chat = "@Botfather"
    if tgbotusername is not None:
        try:
            results = await event.client.inline_query(tgbotusername, "legendbot_help")
            await results[0].click(
                event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True
            )
            await event.delete()
        except noinline:
            legend = await eor(
                event,
                "**Inline Mode is disabled.** \n__Turning it on, please wait for a minute...__",
            )
            async with bot.conversation(chat) as conv:
                try:
                    first = await conv.send_message("/setinline")
                    second = await conv.get_response()
                    third = await conv.send_message(tgbotusername)
                    fourth = await conv.get_response()
                    fifth = await conv.send_message(perf)
                    sixth = await conv.get_response()
                    await bot.send_read_acknowledge(conv.chat_id)
                except YouBlockedUserError:
                    return await legend.edit("Unblock @Botfather first.")
                await legend.edit(
                    f"**Turned On Inline Mode Successfully.** \n\nDo `{l1}op` again to get the help menu."
                )
            await bot.delete_messages(
                conv.chat_id,
                [first.id, second.id, third.id, fourth.id, fifth.id, sixth.id],
            )
    else:
        await eor(
            event,
            "**⚠️ 𝙴𝚁𝚁𝙾𝚁 !!** \n𝙿𝚕𝚎𝚊𝚜𝚎 𝚁𝚎-𝙲𝚑𝚎𝚌𝚔 BOT_TOKEN & BOT_USERNAME on Heroku.",
        )


@bot.on(admin_cmd(pattern="op ?(.*)", outgoing=True))
async def yardim(event):
    if event.fwd_from:
        return
    tgbotusername = botname
    input_str = event.pattern_match.group(1)
    if tgbotusername is not None or LEGEND_input == "text":
        results = await event.client.inline_query(tgbotusername, "legendbot_help")
        await results[0].click(
            event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True
        )
        await event.delete()
    else:
        await eor(event, "**Check Bot Token And Bot Username In Reveal Var*")

        if input_str in CMD_LIST:
            string = "Commands found in {}:\n".format(input_str)
            for i in CMD_LIST[input_str]:
                string += "  " + i
                string += "\n"
            await event.edit(string)
        else:
            await event.edit(input_str + " is not a valid plugin!")


@bot.on(admin_cmd(pattern="plinfo(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="plinfo(?: |$)(.*)", allow_sudo=True))
async def legendbott(event):
    if event.fwd_from:
        return
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await eor(event, str(CMD_HELP[args]))
        else:
            await eor(event, "**⚠️ 𝙴𝚛𝚛𝚘𝚛 !** \n𝙽𝚎𝚎𝚍 𝚊 Plugin 𝚗𝚊𝚖𝚎 𝚝𝚘 𝚜𝚑𝚘𝚠 𝚙𝚕𝚞𝚐𝚒𝚗 𝚒𝚗𝚏𝚘")
    else:
        string = ""
        sayfa = [
            sorted(list(CMD_HELP))[i : i + 5]
            for i in range(0, len(sorted(list(CMD_HELP))), 5)
        ]

        for i in sayfa:
            string += f"`♦️`"
            for sira, a in enumerate(i):
                string += "`" + str(a)
                if sira == i.index(i[-1]):
                    string += "`"
                else:
                    string += "`, "
            string += "\n"
        await eor(
            event,
            "Please Specify A Module Name Of Which You Want Info" + "\n\n" + string,
        )


assist = os.environ.get("ASSISTANT", None)


@bot.on(admin_cmd("on ?(.*)"))
@bot.on(sudo_cmd("on ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if Config.ASSISTANT == "ON":
        async with event.client.conversation(bot_father) as conv:
            try:
                first = await conv.send_message("/setcommands")
                second = await conv.get_response()
                third = await conv.send_message(botname)
                fourth = await conv.get_response()
                fifth = await conv.send_message(onbot)
                sixth = await conv.get_response()
                seventh = await conv.send_message("/setname")
                eighth = await conv.get_response()
                nineth = await conv.send_message(botname)
                tenth = await conv.get_response()
                eleventh = await conv.send_message(name)
                twelveth = await conv.get_response()
                thirdteen = await conv.send_message("/setdescription")
                fourthteen = await conv.get_response()
                fiveteen = await conv.send_message(botname)
                sixteen = await conv.get_response()
                seventeen = await conv.send_message(description)
                eightteen = await conv.get_response()
                await bot.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                return await legend.edit("Unblock @Botfather first.")
            await event.edit(
                f"**Turned On Assistance Successfully.\nClick Here 👉{botname} & Add To Any Group**"
            )
            await bot.delete_messages(
                conv.chat_id,
                [
                    first.id,
                    second.id,
                    third.id,
                    fourth.id,
                    fifth.id,
                    sixth.id,
                    seventh.id,
                    eighth.id,
                    nineth.id,
                    tenth.id,
                    eleventh.id,
                    twelveth.id,
                    thirdteen.id,
                    fourthteen.id,
                    fiveteen.id,
                    sixteen.id,
                    seventeen.id,
                    eightteen.id,
                ],
            )
    else:
        return await event.edit(
            "**Plz First Turn On Assistant.** Click Here👉 `.set var ASSISTANT ON` Anf send"
        )
    
@borg.on(admin_cmd(pattern="config"))  # pylint:disable=E0602

async def _(event):

    if event.fwd_from:

        return

    result = await borg(functions.help.GetConfigRequest())  # pylint:disable=E0602

    result = result.stringify()

    logger.info(result)  # pylint:disable=E0602

    await event.edit("тєℓєтнση  вαѕє∂ υѕєявσт ρσωєяє∂ ву **Lêɠêɳ̃dẞø†** вσт")
    
    
