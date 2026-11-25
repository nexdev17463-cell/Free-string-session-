from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from NEXUS.ui import start_caption, RETRY_BUTTON
from NEXUS.db.users import add_user

START_PHOTO = "https://files.catbox.moe/ljyrvb.jpg"


@Client.on_message(filters.private & filters.incoming & filters.command("start"))
async def cmd_start(bot: Client, msg: Message):
    await add_user(msg.from_user.id)

    me = await bot.get_me()
    caption = start_caption(
        user_mention=msg.from_user.mention,
        bot_mention=me.mention,
    )

    await bot.send_photo(
        chat_id=msg.chat.id,
        photo=START_PHOTO,
        caption=caption,
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("⚡ ɢᴇɴᴇʀᴀᴛᴇ ꜱᴇꜱꜱɪᴏɴ", callback_data="generate")],
            [
                InlineKeyboardButton("🔸 ꜱᴜᴘᴘᴏʀᴛ",  url="https://t.me/PURVI_SUPPORT"),
                InlineKeyboardButton("📢 ᴜᴘᴅᴀᴛᴇꜱ",  url="https://t.me/PURVI_UPDATES"),
            ],
        ])
    )
