import asyncio

from telethon import events
from telethon.tl.functions.channels import EditAdminRequest
from telethon.tl.types import ChatAdminRights, MessageEntityMentionName

from userbot.cmdhelp import CmdHelp
from userbot.plugins.sql_helper import gmute_sql as gsql
from userbot.plugins.sql_helper.gban_sql import (
    all_gbanned,
    gbaner,
    is_gbanned,
    ungbaner,
)
from userbot.plugins.sql_helper.gvar_sql import *

from . import *

gbpic = Config.ALIVE_PIC or LEGEND_logo3


async def get_full_user(event):
    args = event.pattern_match.group(1).split(":", 1)
    extra = None
    if event.reply_to_msg_id and not len(args) == 2:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.sender_id)
        extra = event.pattern_match.group(1)
    elif len(args[0]) > 0:
        user = args[0]
        if len(args) == 2:
            extra = args[1]
        if user.isnumeric():
            user = int(user)
        if not user:
            await eor(event, "Need a user to do this...")
            return
        if event.message.entities is not None:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        try:
            user_obj = await event.client.get_entity(user)
        except Exception as err:
            return await eor(event, f"**ERROR !!**\n\n`{str(err)}`")
    return user_obj, extra


async def get_user_from_id(user, event):
    if isinstance(user, str):
        user = int(user)
    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None
    return user_obj


@bot.on(admin_cmd(pattern="gpromote ?(.*)"))
@bot.on(sudo_cmd(pattern="gpromote ?(.*)", allow_sudo=True))
async def _(legendevent):
    i = 0
    await legendevent.get_sender()
    me = await legendevent.client.get_me()
    legend = await eor(legendevent, "`Promoting globally...`")
    my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id)
    f"@{me.username}" if me.username else my_mention
    await legendevent.get_chat()
    if legendevent.is_private:
        user = legendevent.chat
        rank = legendevent.pattern_match.group(1)
    else:
        legendevent.chat.title
    try:
        user, rank = await get_full_user(legendevent)
    except:
        pass
    if me == user:
        await legend.edit("You can't promote yourself...")
        return
    try:
        if not rank:
            rank = "ℓεɠεɳ∂"
    except:
        return await legend.edit("**ERROR !!**")
    if user:
        telchanel = [
            d.entity.id
            for d in await legendevent.client.get_dialogs()
            if (d.is_group or d.is_channel)
        ]
        rgt = ChatAdminRights(
            add_admins=False,
            invite_users=True,
            change_info=False,
            ban_users=True,
            delete_messages=True,
            pin_messages=True,
        )
        for x in telchanel:
            try:
                await legendevent.client(EditAdminRequest(x, user, rgt, rank))
                i += 1
                await legend.edit(f"**Promoting User in :**  `{i}` Chats...")
            except:
                pass
    else:
        await legend.edit(f"**Reply to a user !!**")
    await legend.edit(
        f"[{user.first_name}](tg://user?id={user.id}) **Was Promoted Globally In** `{i}` **Chats !!**"
    )
    await bot.send_message(
        Config.LOGGER_ID,
        f"#GPROMOTE \n\n**Globally Promoted User :** [{user.first_name}](tg://user?id={user.id}) \n\n**Total Chats :** `{i}`",
    )


@bot.on(admin_cmd(pattern="gdemote ?(.*)"))
@bot.on(sudo_cmd(pattern="gdemote ?(.*)", allow_sudo=True))
async def _(legendevent):
    i = 0
    await legendevent.get_sender()
    me = await legendevent.client.get_me()
    legend = await eor(legendevent, "`Demoting Globally...`")
    my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id)
    f"@{me.username}" if me.username else my_mention
    await legendevent.get_chat()
    if legendevent.is_private:
        user = legendevent.chat
        rank = legendevent.pattern_match.group(1)
    else:
        legendevent.chat.title
    try:
        user, rank = await get_full_user(legendevent)
    except:
        pass
    if me == user:
        await legend.edit("You can't Demote yourself !!")
        return
    try:
        if not rank:
            rank = "legend"
    except:
        return await legend.edit("**ERROR !!**")
    if user:
        telchanel = [
            d.entity.id
            for d in await legendevent.client.get_dialogs()
            if (d.is_group or d.is_channel)
        ]
        rgt = ChatAdminRights(
            add_admins=None,
            invite_users=None,
            change_info=None,
            ban_users=None,
            delete_messages=None,
            pin_messages=None,
        )
        for x in telchanel:
            try:
                await legendevent.client(EditAdminRequest(x, user, rgt, rank))
                i += 1
                await legend.edit(f"**Demoting Globally In Chats :** `{i}`")
            except:
                pass
    else:
        await legend.edit(f"**Reply to a user !!**")
    await legend.edit(
        f"[{user.first_name}](tg://user?id={user.id}) **Was Demoted Globally In** `{i}` **Chats !!**"
    )
    await bot.send_message(
        Config.LOGGER_ID,
        f"#GDEMOTE \n\n**Globally Demoted :** [{user.first_name}](tg://user?id={user.id}) \n\n**Total Chats :** `{i}`",
    )


@bot.on(admin_cmd(pattern=r"gban ?(.*)"))
@bot.on(sudo_cmd(pattern=r"gban ?(.*)", allow_sudo=True))
async def _(event):
    legend = await eor(event, "`Gbanning...`")
    reason = ""
    await event.get_reply_message()
    if event.reply_to_msg_id:
        userid = (await event.get_reply_message()).sender_id
        try:
            reason = event.text.split(" ", maxsplit=1)[1]
        except IndexError:
            reason = ""
    elif event.pattern_match.group(1):
        usr = event.text.split(" ", maxsplit=2)[1]
        userid = await get_user_id(usr)
        try:
            reason = event.text.split(" ", maxsplit=2)[2]
        except IndexError:
            reason = ""
    elif event.is_private:
        userid = (await event.get_chat()).id
        try:
            reason = event.text.split(" ", maxsplit=1)[1]
        except IndexError:
            reason = ""
    else:
        return await eod(
            legend, "**To gban a user i need a userid or reply to his/her message!!**"
        )
    name = (await event.client.get_entity(userid)).first_name
    chats = 0
    if userid == The_LegendBoy:
        return await eod(legend, "🥴 **Nashe me hai kya lawde ‽**")
    if str(userid) in DEVLIST:
        return await eod(legend, "😑 **GBan my creator ?¿ Really‽**")
    if is_gbanned(userid):
        return await eor(
            legend,
            "This kid is already gbanned and added to my **Gban Watch!!**",
        )
    async for gfuck in event.client.iter_dialogs():
        if gfuck.is_group or gfuck.is_channel:
            try:
                await event.client.edit_permissions(
                    gfuck.id, userid, view_messages=False
                )
                chats += 1
                await legend.edit(f"**Gbanning...** \n**Chats :** __{chats}__")
            except BaseException:
                pass
    gbaner(userid)
    a = gvarstat("ALIVE_PIC")
    if a is not None:
        b = a.split(" ")
        c = [LEGEND_logo2]
        for d in b:
            c.append(d)
        gbpic = random.choice(c)
    else:
        gbpic = LEGEND_logo2
    gmsg = f"🥴 [{name}](tg://user?id={userid}) **Gbanned** By {legend_mention} **Reason = Not Mentioned 😏**\n\n📍 Added to Gban Watch!!\n**🔰 Total Chats :**  `{chats}`"
    if reason != "":
        gmsg += f"\n**🔰 Reason :**  `{reason}`"
    ogmsg = f"[{name}](tg://user?id={userid}) **Is now GBanned by** {legend_mention} **in**  `{chats}`  **Chats!! 😏**\n\n**📍 Also Added to Gban Watch!!**"
    if reason != "":
        ogmsg += f"\n**🔰 Reason :**  `{reason}`"
    if Config.ABUSE == "ON":
        await bot.send_file(event.chat_id, gbpic, caption=gmsg)
        await legend.delete()
    else:
        await legend.edit(ogmsg)


@bot.on(admin_cmd(pattern=r"ungban ?(.*)"))
@bot.on(sudo_cmd(pattern=r"ungban ?(.*)", allow_sudo=True))
async def _(event):
    legend = await eor(event, "`Ungban in progress...`")
    if event.reply_to_msg_id:
        userid = (await event.get_reply_message()).sender_id
    elif event.pattern_match.group(1):
        userid = await get_user_id(event.pattern_match.group(1))
    elif event.is_private:
        userid = (await event.get_chat()).id
    else:
        return await eor(legend, "`Reply to a user or give their userid... `")
    name = (await event.client.get_entity(userid)).first_name
    chats = 0
    if not is_gbanned(userid):
        return await eor(legend, "`User is not gbanned.`")
    async for gfuck in event.client.iter_dialogs():
        if gfuck.is_group or gfuck.is_channel:
            try:
                await event.client.edit_permissions(
                    gfuck.id, userid, view_messages=True
                )
                chats += 1
            except BaseException:
                pass
    ungbaner(userid)
    await legend.edit(
        f"📍 [{name}](tg://user?id={userid}) **is now Ungbanned from `{chats}` chats and removed from Gban Watch!!**",
    )


@bot.on(admin_cmd(pattern="listgban$"))
@bot.on(sudo_cmd(pattern="listgban$", allow_sudo=True))
async def already(event):
    hmm = await eor(event, "`Fetching Gbanned users...`")
    gbanned_users = all_gbanned()
    GBANNED_LIST = "**Gbanned Users :**\n"
    if len(gbanned_users) > 0:
        for user in gbanned_users:
            hel = user.chat_id
            legend = int(hel)
            try:
                tity = await event.client.get_entity(legend)
                name = tity.first_name
            except ValueError:
                name = "User"
            GBANNED_LIST += f"📍 [{name}](tg://user?id={legend}) (`{legend}`)\n"
    else:
        GBANNED_LIST = "No Gbanned Users!!"
    await hmm.edit(GBANNED_LIST)


@bot.on(events.ChatAction)
async def _(event):
    if event.user_joined or event.added_by:
        user = await event.get_user()
        chat = await event.get_chat()
        if is_gbanned(str(user.id)):
            if chat.admin_rights:
                try:
                    await event.client.edit_permissions(
                        chat.id,
                        user.id,
                        view_messages=False,
                    )
                    gban_watcher = f"⚠️⚠️**Warning**⚠️⚠️\n\n`Gbanned User Joined the chat!!`\n**⚜️ Victim Id :**  [{user.first_name}](tg://user?id={user.id})\n"
                    gban_watcher += (
                        f"**🔥 Action 🔥**  \n`Banned this piece of shit....` **AGAIN!**"
                    )
                    await event.reply(gban_watcher)
                except BaseException:
                    pass


@bot.on(admin_cmd(pattern=r"gkick ?(.*)"))
@bot.on(sudo_cmd(pattern=r"gkick ?(.*)", allow_sudo=True))
async def gkick(event):
    legend = await eor(event, "`Kicking globally...`")
    if event.reply_to_msg_id:
        userid = (await event.get_reply_message()).sender_id
    elif event.pattern_match.group(1):
        userid = await get_user_id(event.pattern_match.group(1))
    elif event.is_private:
        userid = (await event.get_chat()).id
    else:
        return await eor(legend, "`Reply to some msg or add their id.`")
    name = (await event.client.get_entity(userid)).first_name
    chats = 0
    if userid == The_LegendBoy:
        return await eor(legend, "**🥴 Nashe me hai kya lawde!!**")
    if str(userid) in DEVLIST:
        return await eor(legend, "**😪 I'm not going to gkick my developer!!**")
    async for gkick in event.client.iter_dialogs():
        if gkick.is_group or gkick.is_channel:
            try:
                await bot.kick_participant(gkick.id, userid)
                chats += 1
            except BaseException:
                pass
    gkmsg = f"🏃 **Globally Kicked** [{name}](tg://user?id={userid})'s butts !! \n\n📝 **Chats :**  `{chats}`"
    if Config.ABUSE == "ON":
        await bot.send_file(event.chat_id, gbpic, caption=gkmsg)
        await legend.delete()
    else:
        await legend.edit(gkmsg)


@bot.on(admin_cmd(pattern=r"gmute ?(\d+)?"))
@bot.on(sudo_cmd(allow_sudo=True, pattern=r"gmute ?(\d+)?"))
async def gm(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await eor(event, "`Trying to gmute user...`")
        await asyncio.sleep(2)
        private = True
    reply = await event.get_reply_message()
    if event.pattern_match.group(1) is not None:
        userid = event.pattern_match.group(1)
    elif reply is not None:
        userid = reply.sender_id
    elif private is True:
        userid = event.chat_id
    else:
        return await eor(
            event, "Need a user to gmute. Reply or give userid to gmute them.."
        )
    event.chat_id
    await event.get_chat()
    if gsql.is_gmuted(userid, "gmute"):
        return await eor(event, "This kid is already Gmuted.")
    try:
        if str(userid) in DEVLIST:
            return await eor(event, "**Sorry I'm not going to gmute them..**")
    except:
        pass
    try:
        gsql.gmute(userid, "gmute")
    except Exception as e:
        await eor(event, "Error occured!\nError is " + str(e))
    else:
        if Config.ABUSE == "ON":
            await bot.send_file(
                event.chat_id, shhh, caption="**Chup Madarcod... Bilkul Chup 🤫**"
            )
            await event.delete()
        else:
            await eor(event, "🤫 Shhh... **Don't speak Now !!**")


@bot.on(admin_cmd(outgoing=True, pattern=r"ungmute ?(\d+)?"))
@bot.on(sudo_cmd(allow_sudo=True, pattern=r"ungmute ?(\d+)?"))
async def endgmute(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await eor(event, "`Trying to ungmute !!`")
        await asyncio.sleep(2)
        private = True
    reply = await event.get_reply_message()
    if event.pattern_match.group(1) is not None:
        userid = event.pattern_match.group(1)
    elif reply is not None:
        userid = reply.sender_id
    elif private is True:
        userid = event.chat_id
    else:
        return await eor(
            event,
            "Please reply to a user or add their into the command to ungmute them.",
        )
    event.chat_id
    if not gsql.is_gmuted(userid, "gmute"):
        return await eor(event, "I don't remember I gmuted him...")
    try:
        gsql.ungmute(userid, "gmute")
    except Exception as e:
        await eor(event, "Error occured!\nError is " + str(e))
    else:
        await eor(event, "Ok!! Speak")


@command(incoming=True)
async def watcher(event):
    try:
        if gsql.is_gmuted(event.sender_id, "gmute"):
            await event.delete()
    except Exception as e:
        LOGS.info(str(e))


CmdHelp("global").add_command(
    "gban",
    "<reply>/<userid>",
    "Globally Bans the mentioned user in 'X' chats you are admin with ban permission.",
).add_command(
    "ungban", "<reply>/<userid>", "Globally Unbans the user in 'X' chats you are admin!"
).add_command(
    "listgban", None, "Gives the list of all GBanned Users."
).add_command(
    "gkick", "<reply>/<userid>", "Globally Kicks the user in 'X' chats you are admin!"
).add_command(
    "gmute", "<reply> or <userid>", "Globally Mutes the User."
).add_command(
    "ungmute", "<reply> or <userid>", "Globally Unmutes the gmutes user."
).add_command(
    "gpromote",
    "<reply> or <username>",
    "Globally Promotes the mentioned user in all the chats you are admin with Add Admins permission.",
).add_command(
    "gdemote",
    "<reply> or <username>",
    "Globally Demotes the mentioned user in all the chats you have rights to demoted that user.",
).add_info(
    "Global Admin Tool."
).add_warning(
    "✅ Harmlesss Module."
).add()
