# ═══════════════════════════════════════════════
#   NEXUS  ·  UI  &  Message  Templates
# ═══════════════════════════════════════════════

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# ── Dividers & Decoration ───────────────────────────────────
LINE  = "━" * 22
THIN  = "┄" * 22
DOT   = "·"
STAR  = "✦"
ARROW = "➤"
CHECK = "✅"
CROSS = "❌"
WARN  = "⚠️"
LOCK  = "🔐"
KEY   = "🗝️"
PHONE = "📱"
OTP   = "📩"
SAFE  = "🛡️"
SPARK = "⚡"
GLOBE = "🌐"

# ── START message ───────────────────────────────────────────
def start_caption(user_mention: str, bot_mention: str) -> str:
    return (
        f"**{LINE}**\n"
        f"**{SPARK}  ɴᴇxᴜs ꜱᴛʀɪɴɢ ɢᴇɴᴇʀᴀᴛᴏʀ  {SPARK}**\n"
        f"**{LINE}**\n\n"
        f"**{ARROW} ʜᴇʏ, {user_mention} !**\n"
        f"ɪ'ᴍ **{bot_mention}** — ʏᴏᴜʀ ꜱᴇᴄᴜʀᴇ ꜱᴇꜱꜱɪᴏɴ ɢᴇɴᴇʀᴀᴛᴏʀ.\n\n"
        f"**{SAFE}  ꜱᴜᴘᴘᴏʀᴛᴇᴅ ʟɪʙʀᴀʀɪᴇꜱ :**\n"
        f"  {DOT} **Pyrogram v2**  ·  User & Bot\n"
        f"  {DOT} **Telethon**     ·  User & Bot\n\n"
        f"**{GLOBE}  ɴᴏ ɪᴅ ʟᴏɢᴏᴜᴛ ɪꜱꜱᴜᴇ — ꜰᴜʟʟʏ ꜱᴇᴄᴜʀᴇ**\n\n"
        f"**{LINE}**\n"
        f"{ARROW} ᴛᴀᴘ **ɢᴇɴᴇʀᴀᴛᴇ ꜱᴇꜱꜱɪᴏɴ** ᴛᴏ ʙᴇɢɪɴ.\n"
        f"**{LINE}**"
    )

# ── MUST-JOIN message ───────────────────────────────────────
def must_join_caption(link: str) -> str:
    return (
        f"**{LINE}**\n"
        f"**{WARN}  ᴊᴏɪɴ ʀᴇQᴜɪʀᴇᴅ**\n"
        f"**{LINE}**\n\n"
        f"ʏᴏᴜ ᴍᴜꜱᴛ ᴊᴏɪɴ ᴏᴜʀ ᴏꜰꜰɪᴄɪᴀʟ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜꜱᴇ ᴛʜɪꜱ ʙᴏᴛ.\n\n"
        f"**{ARROW}  [{SAFE} ᴊᴏɪɴ ɴᴏᴡ]({link})**\n\n"
        f"ᴀꜰᴛᴇʀ ᴊᴏɪɴɪɴɢ, ꜱᴇɴᴅ /start ᴀɢᴀɪɴ.\n"
        f"**{LINE}**"
    )

# ── Library-choice message ──────────────────────────────────
CHOOSE_LIB_TEXT = (
    f"**{LINE}**\n"
    f"**{KEY}  ꜱᴇʟᴇᴄᴛ ꜱᴇꜱꜱɪᴏɴ ᴛʏᴘᴇ**\n"
    f"**{LINE}**\n\n"
    f"{ARROW} ᴄʜᴏᴏꜱᴇ ᴛʜᴇ ʟɪʙʀᴀʀʏ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ᴀ ꜱᴇꜱꜱɪᴏɴ ꜰᴏʀ:\n\n"
    f"  **Pyrogram v2**  — ᴍᴏᴅᴇʀɴ, ꜰᴀꜱᴛ\n"
    f"  **Telethon**     — ᴄʟᴀꜱꜱɪᴄ, ʀᴏʙᴜꜱᴛ\n\n"
    f"**{LINE}**"
)

CHOOSE_LIB_BUTTONS = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("⚡ Pyrogram v2 — User", callback_data="pyrogram"),
        InlineKeyboardButton("🔹 Pyrogram — Bot",    callback_data="pyrogram_bot"),
    ],
    [
        InlineKeyboardButton("🌐 Telethon — User",   callback_data="telethon"),
        InlineKeyboardButton("🔸 Telethon — Bot",    callback_data="telethon_bot"),
    ],
])

RETRY_BUTTON = InlineKeyboardMarkup([[
    InlineKeyboardButton(f"{SPARK} ɢᴇɴᴇʀᴀᴛᴇ ꜱᴇꜱꜱɪᴏɴ", callback_data="generate")
]])

# ── Step prompts ────────────────────────────────────────────
def prompt_api_id(lib_name: str) -> str:
    return (
        f"**{LINE}**\n"
        f"**{SPARK}  {lib_name} ꜱᴇꜱꜱɪᴏɴ — ꜱᴛᴇᴘ 1/4**\n"
        f"**{LINE}**\n\n"
        f"{ARROW} ꜱᴇɴᴅ ʏᴏᴜʀ **API_ID**\n\n"
        f"ɢᴇᴛ ɪᴛ ᴀᴛ: [my.telegram.org](https://my.telegram.org)\n\n"
        f"{WARN} ꜱᴇɴᴅ /skip ᴛᴏ ᴜꜱᴇ ᴛʜᴇ ʙᴏᴛ'ꜱ ᴅᴇꜰᴀᴜʟᴛ ᴋᴇʏꜱ.\n"
        f"**{LINE}**"
    )

def prompt_api_hash() -> str:
    return (
        f"**{LINE}**\n"
        f"**{SPARK}  ꜱᴛᴇᴘ 2/4 — API_HASH**\n"
        f"**{LINE}**\n\n"
        f"{ARROW} ɴᴏᴡ ꜱᴇɴᴅ ʏᴏᴜʀ **API_HASH**\n\n"
        f"ɢᴇᴛ ɪᴛ ᴀᴛ: [my.telegram.org](https://my.telegram.org)\n"
        f"**{LINE}**"
    )

def prompt_phone() -> str:
    return (
        f"**{LINE}**\n"
        f"**{PHONE}  ꜱᴛᴇᴘ 3/4 — ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀ**\n"
        f"**{LINE}**\n\n"
        f"{ARROW} ꜱᴇɴᴅ ʏᴏᴜʀ **ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀ** ᴡɪᴛʜ ᴄᴏᴜɴᴛʀʏ ᴄᴏᴅᴇ.\n\n"
        f"  ᴇxᴀᴍᴘʟᴇ: `+91 99XXXXXXXX`\n\n"
        f"**{LINE}**"
    )

def prompt_bot_token() -> str:
    return (
        f"**{LINE}**\n"
        f"**{KEY}  ꜱᴛᴇᴘ 3/4 — ʙᴏᴛ ᴛᴏᴋᴇɴ**\n"
        f"**{LINE}**\n\n"
        f"{ARROW} ꜱᴇɴᴅ ʏᴏᴜʀ **BOT_TOKEN**\n\n"
        f"  ᴇxᴀᴍᴘʟᴇ: `6810174902:AAGQVElsBPT...`\n\n"
        f"**{LINE}**"
    )

def prompt_otp() -> str:
    return (
        f"**{LINE}**\n"
        f"**{OTP}  ꜱᴛᴇᴘ 4/4 — OTP ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ**\n"
        f"**{LINE}**\n\n"
        f"{ARROW} ꜱᴇɴᴅ ᴛʜᴇ **OTP** ʏᴏᴜ ʀᴇᴄᴇɪᴠᴇᴅ ᴏɴ ᴛᴇʟᴇɢʀᴀᴍ.\n\n"
        f"{WARN} ꜱᴇɴᴅ ɪᴛ **ᴡɪᴛʜ ꜱᴘᴀᴄᴇꜱ** ᴛᴏ ᴀᴠᴏɪᴅ ᴀᴜᴛᴏ-ʀᴇᴀᴅ.\n"
        f"  ᴇxᴀᴍᴘʟᴇ: `1 2 3 4 5`\n\n"
        f"**{LINE}**"
    )

def prompt_2fa() -> str:
    return (
        f"**{LINE}**\n"
        f"**{LOCK}  2FA ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ ʀᴇQᴜɪʀᴇᴅ**\n"
        f"**{LINE}**\n\n"
        f"{ARROW} ʏᴏᴜʀ ᴀᴄᴄᴏᴜɴᴛ ʜᴀꜱ **Two-Step Verification** ᴇɴᴀʙʟᴇᴅ.\n\n"
        f"{ARROW} ᴘʟᴇᴀꜱᴇ ꜱᴇɴᴅ ʏᴏᴜʀ **ᴄʟᴏᴜᴅ ᴘᴀꜱꜱᴡᴏʀᴅ**:\n\n"
        f"**{LINE}**"
    )

# ── Success message ─────────────────────────────────────────
def success_session(lib_name: str, session: str, support_link: str) -> str:
    return (
        f"**{LINE}**\n"
        f"**{CHECK}  ꜱᴇꜱꜱɪᴏɴ ɢᴇɴᴇʀᴀᴛᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ**\n"
        f"**{LINE}**\n\n"
        f"**{SPARK} ʟɪʙʀᴀʀʏ:** `{lib_name}`\n\n"
        f"**{KEY} ʏᴏᴜʀ ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ:**\n"
        f"`{session}`\n\n"
        f"**{LINE}**\n"
        f"{WARN} **ɴᴇᴠᴇʀ ꜱʜᴀʀᴇ ᴛʜɪꜱ ᴡɪᴛʜ ᴀɴʏᴏɴᴇ!**\n"
        f"ɪᴛ ɢɪᴠᴇꜱ ꜰᴜʟʟ ᴀᴄᴄᴇꜱꜱ ᴛᴏ ʏᴏᴜʀ ᴀᴄᴄᴏᴜɴᴛ.\n\n"
        f"ꜱᴜᴘᴘᴏʀᴛ: {support_link}\n"
        f"**{LINE}**"
    )

def success_dm_note(lib_name: str) -> str:
    return (
        f"**{CHECK}  ꜱᴜᴄᴄᴇꜱꜱ!**\n\n"
        f"ʏᴏᴜʀ **{lib_name}** ꜱᴇꜱꜱɪᴏɴ ʜᴀꜱ ʙᴇᴇɴ ꜱᴇɴᴛ ᴛᴏ ʏᴏᴜʀ **ꜱᴀᴠᴇᴅ ᴍᴇꜱꜱᴀɢᴇꜱ**.\n\n"
        f"ᴄʜᴇᴄᴋ ᴛʜᴇʀᴇ ᴀɴᴅ ꜱᴀᴠᴇ ɪᴛ ꜱᴇᴄᴜʀᴇʟʏ! {SAFE}"
    )

# ── Error messages ──────────────────────────────────────────
ERR_API_INVALID   = f"**{CROSS} API_ID / API_HASH ᴄᴏᴍʙɪɴᴀᴛɪᴏɴ ɪꜱ ɪɴᴠᴀʟɪᴅ.**\n\nᴘʟᴇᴀꜱᴇ ᴛʀʏ ᴀɢᴀɪɴ."
ERR_PHONE_INVALID = f"**{CROSS} ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀ ɪꜱ ɪɴᴠᴀʟɪᴅ.**\n\nᴍᴀᴋᴇ ꜱᴜʀᴇ ɪᴛ ɪɴᴄʟᴜᴅᴇꜱ ᴛʜᴇ ᴄᴏᴜɴᴛʀʏ ᴄᴏᴅᴇ."
ERR_OTP_INVALID   = f"**{CROSS} OTP ɪꜱ ɪɴᴄᴏʀʀᴇᴄᴛ.** ᴘʟᴇᴀꜱᴇ ᴛʀʏ ᴀɢᴀɪɴ."
ERR_OTP_EXPIRED   = f"**{CROSS} OTP ʜᴀꜱ ᴇxᴘɪʀᴇᴅ.** ᴘʟᴇᴀꜱᴇ ʀᴇꜱᴛᴀʀᴛ."
ERR_2FA_WRONG     = f"**{CROSS} 2FA ᴘᴀꜱꜱᴡᴏʀᴅ ɪꜱ ɪɴᴄᴏʀʀᴇᴄᴛ.** ᴘʟᴇᴀꜱᴇ ᴛʀʏ ᴀɢᴀɪɴ."
ERR_API_ID_INT    = f"**{CROSS} API_ID ᴍᴜꜱᴛ ʙᴇ ᴀ ɴᴜᴍʙᴇʀ.**\n\nᴘʟᴇᴀꜱᴇ ꜱᴇɴᴅ ᴏɴʟʏ ᴅɪɢɪᴛꜱ."
ERR_TIMEOUT       = f"**{WARN} ᴛɪᴍᴇᴏᴜᴛ!**\n\nʏᴏᴜ ᴛᴏᴏᴋ ᴛᴏᴏ ʟᴏɴɢ ᴛᴏ ʀᴇꜱᴘᴏɴᴅ. ᴘʟᴇᴀꜱᴇ ꜱᴛᴀʀᴛ ᴀɢᴀɪɴ."
MSG_CANCELLED     = f"**{CROSS} ᴘʀᴏᴄᴇꜱꜱ ᴄᴀɴᴄᴇʟʟᴇᴅ.**\n\nᴛᴀᴘ ʙᴇʟᴏᴡ ᴛᴏ ꜱᴛᴀʀᴛ ᴀɢᴀɪɴ."
MSG_SENDING_OTP   = f"**{OTP} ꜱᴇɴᴅɪɴɢ OTP ᴛᴏ ʏᴏᴜʀ ᴛᴇʟᴇɢʀᴀᴍ...**"
MSG_LOGGING_IN    = f"**{SPARK} ʟᴏɢɢɪɴɢ ɪɴ ᴡɪᴛʜ ᴛᴏᴋᴇɴ...**"
