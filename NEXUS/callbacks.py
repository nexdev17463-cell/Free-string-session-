import traceback
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup

from NEXUS.ui import CHOOSE_LIB_TEXT, CHOOSE_LIB_BUTTONS, RETRY_BUTTON
from NEXUS.generate import generate_session


@Client.on_callback_query(
    filters.regex(r"^(generate|pyrogram|pyrogram_bot|telethon|telethon_bot)$")
)
async def _cb(bot: Client, cq: CallbackQuery):
    q = cq.matches[0].group(1)
    try:
        if q == "generate":
            await cq.answer()
            await cq.message.reply(CHOOSE_LIB_TEXT, reply_markup=CHOOSE_LIB_BUTTONS)

        elif q == "pyrogram":
            await cq.answer("Pyrogram v2 — User session")
            await generate_session(bot, cq.message, telethon=False, is_bot=False)

        elif q == "pyrogram_bot":
            await cq.answer("Pyrogram v2 — Bot session")
            await generate_session(bot, cq.message, telethon=False, is_bot=True)

        elif q == "telethon":
            await cq.answer("Telethon — User session")
            await generate_session(bot, cq.message, telethon=True, is_bot=False)

        elif q == "telethon_bot":
            await cq.answer("Telethon — Bot session")
            await generate_session(bot, cq.message, telethon=True, is_bot=True)

    except Exception as e:
        traceback.print_exc()
        await cq.message.reply(
            f"**❌ ᴀɴ ᴇʀʀᴏʀ ᴏᴄᴄᴜʀʀᴇᴅ:**\n`{e}`\n\nᴘʟᴇᴀꜱᴇ ᴛʀʏ ᴀɢᴀɪɴ.",
            reply_markup=RETRY_BUTTON
        )
