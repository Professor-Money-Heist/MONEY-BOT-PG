from faker import Faker
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from MONEY-HEIST-BOT import CmdHelp
from MONEY-HEIST-BOT import bot as MONEY-HEIST-BOT
from MONEY-HEIST-BOT.utils import admin_cmd, edit_or_reply, sudo_cmd


@MONEY_HEIST_BOT.on(admin_cmd("gencc$"))
@MONEY_HEIST_BOT.on(sudo_cmd("gencc$", allow_sudo=True))
async def _(MONEYevent):
    if MONEYevent.fwd_from:
        return
    MONEYcc = Faker()
    MONEYname = MONEYcc.name()
    MONEYadre = MONEYcc.address()
    MONEYcard = MOBEYcc.credit_card_full()

    await edit_or_reply(
        MONEYevent,
        f"__**👤 NAME :- **__\n`{MONEYname}`\n\n__**🏡 ADDRESS :- **__\n`{MONEYadre}`\n\n__**💸 CARD :- **__\n`{MONEYcard}`",
    )


@MONEY_HEIST_BOT.on(admin_cmd(pattern="bin ?(.*)"))
@MONEY_HEIST_BOT.on(sudo_cmd(pattern="bin ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    MONEY_input = event.pattern_match.group(1)
    chat = "@szbinscheckerbot"
    await event.edit("Checking...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=2143004427)
            )
            await event.client.send_message(chat, f"/bin {MONEY_input}")
            response = await response
        except YouBlockedUserError:
            await event.reply("Please Unblock @szbinscheckerbot")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


@MONEY_HEIST_BOT.on(admin_cmd(pattern="register ?(.*)"))
@MONEY_HEIST_BOT.on(sudo_cmd(pattern="register ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    MONEY_input = event.pattern_match.group(1)
    chat = "@carol5_bot"
    await event.edit("Checking...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1247032902)
            )
            await event.client.send_message(chat, f"/register {LEGEND_input}")
            response = await response
        except YouBlockedUserError:
            await event.reply("Please Unblock @carol5_bot")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


@MONEY_HEIST_BOT.on(admin_cmd(pattern="password ?(.*)"))
@MONEY_HEIST_BOT.on(sudo_cmd(pattern="password ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    MONEY_input = event.pattern_match.group(1)
    chat = "@carol5_bot"
    await event.edit("Checking...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1247032902)
            )
            await event.client.send_message(chat, f"/password {LEGEND_input}")
            response = await response
        except YouBlockedUserError:
            await event.reply("Please Unblock @carol5_bot")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


CmdHelp("carder").add_command("gencc", None, "Generates fake cc...").add_command(
    "register", None, "Register Ur Account Here"
).add_command("password", "<enter>", "Set ur Account Password On CXM.CARDS").add()
