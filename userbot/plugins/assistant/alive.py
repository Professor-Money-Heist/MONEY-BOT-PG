from telethon import events

from userbot import *

from . import *

PM_IMG = "https://te.legra.ph/file/6c14ed70a84ea325d82c1.jpg"
pm_caption = f"⚜『MONEYHEIST』Is Ôñĺîne⚜ \n\n"
pm_caption += f"Ôwñêř ~ 『{AGORA_mention}』\n"
pm_caption += f"**╭───────────**\n"
pm_caption += f"┣Ťêlethon ~ `1.15.0` \n"
pm_caption += f"┣『MONEYHESITBOT』~ `{AGORAversion}` \n"
pm_caption += f"┣Çhâññel ~ [Channel](https://t.me/MM_UB_UPDATES)\n"
pm_caption += f"┣**License** ~ [License v3.0](github.com/Professor-Money-Heist/MONEY-HEIST-BOT/blob/master/LICENSE)\n"
pm_caption += f"┣Copyright ~ By [『Professor-Money-Heist』 ](https://t.me/PROF_AGORA)\n"
pm_caption += f"┣Assistant ~ By [『Professor-Monet-Heist』 ](https://t.me/PTOF_AGORA)\n"
pm_caption += f"╰────────────\n"
pm_caption += f"       »        [『M and M USERBOTS』](https://t.me/MM_UB_UPDATES) «««"


@tgbot.on(events.NewMessage(pattern="^/alive"))
async def _(event):
    await tgbot.send_file(event.chat_id, PM_IMG, caption=pm_caption)
