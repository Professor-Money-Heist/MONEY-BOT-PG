import io
import re

from telethon import Button, custom, events

from userbot import bot

tgbot = bot.tgbot


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"rules")))
async def help(event):
    await event.delete()
    if event.query.user_id is not bot.uid:
        await tgbot.send_message(
            event.chat_id,
            message="🔰Rᴇᴀᴅ Tʜᴇ Rᴜʟᴇꜱ Tᴏᴏ🔰\n\n🔹 Dᴏɴ'ᴛ Sᴩᴀᴍ\n🔹 ᴛᴀʟᴋ Fʀɪᴇɴᴅʟy\n🔹 Dᴏɴ'ᴛ Bᴇ Rᴜᴅᴇ\n🔹 Sᴇɴᴅ Uʀ Mᴇꜱꜱᴀɢᴇꜱ Hᴇʀᴇ\n🔹 Nᴏ Pᴏʀɴᴏɢʀᴀᴘʜʏ\n🔹 Dᴏɴ'ᴛ Wʀɪᴛᴇ Bᴀᴅ Wᴏʀᴅs.\n\nWʜᴇɴ I Gᴇᴛ Fʀᴇᴇ Tɪᴍᴇ , I'ʟʟ Rᴇᴩʟy U 💯✅",
            buttons=[
                [
                    custom.Button.inline(
                        "🚫 Cʟᴏsᴇ 🚫",
                        data="close_vcc",
                    )
                ],
            ],
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"close_vcc")))
async def users(event):
    if event.query.user_id == bot.uid:
        await event.delete()


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"close")))
async def users(event):
    if event.query.user_id == bot.uid:
        await event.delete()


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"users")))
async def users(event):
    if event.query.user_id == bot.uid:
        await event.delete()
        total_users = get_all_users()
        users_list = "⚜List Of Total Users In Bot.⚜ \n\n"
        for starked in total_users:
            users_list += ("==> {} \n").format(int(starked.chat_id))
        with io.BytesIO(str.encode(users_list)) as tedt_file:
            tedt_file.name = "userlist.txt"
            await tgbot.send_file(
                event.chat_id,
                tedt_file,
                force_document=True,
                caption="Total Users In Your Bot.",
                allow_cache=False,
            )
    else:
        pass


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"alive")))
async def help(event):
    await event.delete()
    if event.query.user_id == bot.uid:
        await tgbot.send_message(
            event.chat_id,
            message=f"**Wʜᴀᴛ Dᴏ Yᴏᴜ Wᴀɴᴛ Yᴏ Eᴅɪᴛ Iɴ Aʟɪᴠᴇ?\nFᴏʀ Aɴʏ Kɪɴᴅ Oғ Hᴇʟᴘ Dᴏ Jᴏɪɴ [Đ₳Ɽ₭ Ƒմʂʂìօղ](https://t.me/Dark_Fussion_chat)**",
            buttons=[
                [
                    Button.inline("✘ Aʟɪᴠᴇ Nᴀᴍᴇ ✘", data="name"),
                    Button.inline("✘ Aʟɪᴠᴇ Pɪᴄ ✘", data="img"),
                ],
                [Button.inline("🚫 Cᴀɴᴄᴇʟ 🚫", data="settings")],
            ],
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"img")))
async def help(event):
    await event.delete()
    if event.query.user_id == bot.uid:
        await tgbot.send_message(
            event.chat_id,
            message=f"**Wʜɪᴄʜ Aʟɪᴠᴇ Pɪᴄ Dᴏ Yᴏᴜ Wᴀɴᴛ Tᴏ Cʜᴀɴɢᴇ?\nFᴏʀ Aɴʏ Kɪɴᴅ Oғ Hᴇʟᴘ Dᴏ Jᴏɪɴ [Lêɠêɳ̃dẞø†](https://t.me/Official_LegendBot)**",
            buttons=[
                [Button.inline("✘ Dᴇғᴀᴜʟᴛ Aʟɪᴠᴇ ✘", data="aimg")],
                [Button.inline("✘ Bᴀᴄᴋ ✘", data="alive")],
                [Button.inline("🚫 Cᴀɴᴄᴇʟ 🚫", data="settings")],
            ],
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"name")))
async def help(event):
    await event.delete()
    if event.query.user_id == bot.uid:
        await tgbot.send_message(
            event.chat_id,
            message=f"**Yᴏᴜ Cᴀɴ Cʜᴀɴɢᴇ Aʟɪᴠᴇ Nᴀᴍᴇ..!!\nJᴜsᴛ Fᴏʟʟᴏᴡ Tʜᴇ Sᴛᴇᴘs.! \n\nFᴏʀ Aɴʏ Kɪɴᴅ Oғ Pʀᴏʙʟᴇᴍ Oʀ Dᴏᴜʙᴛ Dᴏ Jᴏɪɴ [Lêɠêɳ̃dẞø†](http://t.me/Official_LegendBot)\n\nJᴜsᴛ Tʏᴘᴇ\n\n`.set var ALIVE_NAME <Name>`\n\nRᴇᴍᴏᴠᴇ `<>` Tʜɪs.**",
            buttons=[
                [Button.inline("✘ Bᴀᴄᴋ ✘", data="alive")],
                [Button.inline("🚫 Cᴀɴᴄᴇʟ 🚫", data="settings")],
            ],
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"aimg")))
async def help(event):
    await event.delete()
    if event.query.user_id == bot.uid:
        await tgbot.send_message(
            event.chat_id,
            message=f"**You can change Alive Pic for `.alive`\nJust follow the steps.!\nAny kind of Problem or doubt do join [Lêɠêɳ̃dẞø†](t.me/Official_LegendBot)\n\nJust type\n\n`.set var ALIVE_PIC <Telegraph Link>`\n\nRemove `<>` this**",
            buttons=[
                [Button.inline("✘ Bᴀᴄᴋ ✘", data="img")],
                [Button.inline("🚫 Cᴀɴᴄᴇʟ 🚫", data="settings")],
            ],
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"dalive")))
async def help(event):
    await event.delete()
    if event.query.user_id == bot.uid:
        await tgbot.send_message(
            event.chat_id,
            message=f"**You can change Alive Pic for `.dalive` \nJust follow the steps.!\nAny kind of Problem or doubt do join [Lêɠêɳ̃dẞø†](t.me/Official_LegendBot)\n\nJust type\n\n`.set var AWAKE_PIC <Telegraph Link>`\n\nRemove `<>` this.**",
            buttons=[
                [Button.inline("✘ Bᴀᴄᴋ ✘", data="img")],
                [Button.inline("🚫 Cᴀɴᴄᴇʟ 🚫", data="settings")],
            ],
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"permit")))
async def help(event):
    await event.delete()
    if event.query.user_id == bot.uid:
        await tgbot.send_message(
            event.chat_id,
            message=f"**What do you want to edit in Pm Permit?\nFor Any kind of Problem or doubt do join [Lêɠêɳ̃dẞø†](t.me/Official_LegendBot)**",
            buttons=[
                [
                    Button.inline("✘ Pᴍ Pᴇʀᴍɪᴛ Tᴇxᴛ ✘", data="text"),
                    Button.inline("✘ Pᴍ Pᴇʀᴍɪᴛ Mᴇᴅɪᴀ ✘", data="media"),
                ],
                [Button.inline("🚫 Cᴀɴᴄᴇʟ 🚫", data="settings")],
            ],
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"media")))
async def help(event):
    await event.delete()
    if event.query.user_id == bot.uid:
        await tgbot.send_message(
            event.chat_id,
            message=f"**You can change Pic permit Pic..!! \nJust follow the steps.!\nAny kind of Problem or doubt do join [Lêɠêɳ̃dẞø†](t.me/Official_LegendBot) type\n\n`.set var PM_PIC <Telegraph Link>`\n\nRemove `<>` this.**",
            buttons=[
                [Button.inline("✘ Bᴀᴄᴋ ✘", data="permit")],
                [Button.inline("🚫 Cᴀɴᴄᴇʟ 🚫", data="settings")],
            ],
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"text")))
async def help(event):
    await event.delete()
    if event.query.user_id == bot.uid:
        await tgbot.send_message(
            event.chat_id,
            message=f"**You can change Pic permit message..!! \nJust follow the steps.!\nAny kind of Problem or doubt do join [Lêɠêɳ̃dẞø†](t.me/Official_LegendBot)\n\nJust type\n\n`.set var PM_MSG <Text>`\n\nRemove `<>` this.**",
            buttons=[
                [Button.inline("✘ Bᴀᴄᴋ ✘", data="permit")],
                [Button.inline("🚫 Cᴀɴᴄᴇʟ 🚫", data="settings")],
            ],
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"settings")))
async def help(event):
    await event.delete()
    if event.query.user_id == bot.uid:
        await tgbot.send_message(
            event.chat_id,
            message=f"**Which type of setting do you want to edit?\nYou can change anything from these..!!\nAny kind for help do join [Lêɠêɳ̃dẞø†](t.me/Official_LegendBot)**",
            buttons=[
                [
                    Button.inline("✘ Aʟɪᴠᴇ ✘", data="alive"),
                    Button.inline("✘ Pᴍ Pᴇʀᴍɪᴛ ✘", data="permit"),
                ],
                [
                    Button.inline("✘ Chat Bot ✘", data="chat"),
                    Button.inline("✘ Vc Bot ✘", data="Vc_Bot"),
                ],
                [Button.inline("✘ Cʟᴏsᴇ ✘", data="close")],
            ],
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"gibcmd")))
async def users(event):
    await event.delete()
    grabon = "🇮🇳Hello Here Are Some Commands \n➤ /start - Check if I am Alive \n➤ /ping - Pong! \n➤ /tr <lang-code> \n➤ /broadcast - Sends Message To all Users In Bot \n➤ /id - Shows ID of User And Media. \n➤ /addnote - Add Note \n➤ /notes - Shows Notes \n➤ /rmnote - Remove Note \n➤ /alive - Am I Alive? \n➤ /bun - Works In Group , Bans A User. \n➤ /unbun - Unbans A User in Group \n➤ /prumote - Promotes A User \n➤ /demute - Demotes A User \n➤ /pin - Pins A Message \n➤ /stats - Shows Total Users In Bot \n➤ /purge - Reply It From The Message u Want to Delete (Your Bot Should be Admin to Execute It) \n➤ /del - Reply a Message Tht Should Be Deleted (Your Bot Should be Admin to Execute It)"
    await tgbot.send_message(event.chat_id, grabon)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"hack")))
async def users(event):
    await event.delete()
    grabon = "I am Giving U Full Power To Hack Anyone Through String session\nClick Here 👉/hack."
    await tgbot.send_message(event.chat_id, grabon)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"v_hack")))
async def users(event):
    await event.delete()
    grabon = "Sorry, Only My Owner Can Acess This Button. If U Want To Use Then Deploy Ur Own Lêɠêɳ̃dẞø†"
    await tgbot.send_message(event.chat_id, grabon)
