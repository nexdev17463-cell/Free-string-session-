from pyrogram import Client, filters
from pyrogram.types import Message

import config
from NEXUS.db.users import add_user, total_users
from NEXUS.ui import LINE, STAR


@Client.on_message(filters.private & ~filters.service, group=1)
async def _track(_, msg: Message):
    if msg.from_user:
        await add_user(msg.from_user.id)


@Client.on_message(filters.user(config.OWNER_ID) & filters.command("stats"))
async def _stats(bot: Client, msg: Message):
    count = await total_users()
    await msg.reply(
        f"**{LINE}**\n"
        f"**{STAR} ꜱᴛᴀᴛꜱ**\n"
        f"**{LINE}**\n\n"
        f"**ᴛᴏᴛᴀʟ ᴜꜱᴇʀꜱ:** `{count}`\n\n"
        f"**{LINE}**",
        quote=True
    )
