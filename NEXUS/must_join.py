import config
from NEXUS.ui import must_join_caption, RETRY_BUTTON

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import UserNotParticipant, ChatAdminRequired, ChatWriteForbidden


@Client.on_message(filters.incoming & filters.private, group=-1)
async def _must_join(bot: Client, msg: Message):
    if not config.MUST_JOIN:
        return

    try:
        try:
            await bot.get_chat_member(config.MUST_JOIN, msg.from_user.id)
        except UserNotParticipant:
            if config.MUST_JOIN.lstrip("-").isdigit():
                chat_info = await bot.get_chat(config.MUST_JOIN)
                url = chat_info.invite_link
            else:
                url = f"https://t.me/{config.MUST_JOIN}"

            try:
                await msg.reply_photo(
                    photo="https://files.catbox.moe/k6jrxc.jpg",
                    caption=must_join_caption(url),
                    reply_markup=InlineKeyboardMarkup([[
                        InlineKeyboardButton("🔶 ᴊᴏɪɴ ɴᴏᴡ", url=url)
                    ]])
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"[must_join] Make me admin in: {config.MUST_JOIN}")
