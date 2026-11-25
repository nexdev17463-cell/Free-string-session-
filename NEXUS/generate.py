"""
NEXUS String Generator — Core Session Logic
Supports: Pyrogram v2 (user/bot) · Telethon (user/bot)
"""

import asyncio
from asyncio import TimeoutError

import config
from NEXUS import ui

from pyromod import Client                          # pyromod>=1.5
from pyrogram import filters
from pyrogram.types import Message
from pyrogram.errors import (
    ApiIdInvalid, PhoneNumberInvalid, PhoneCodeInvalid,
    PhoneCodeExpired, SessionPasswordNeeded, PasswordHashInvalid,
)

from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.errors import (
    ApiIdInvalidError, PhoneNumberInvalidError, PhoneCodeInvalidError,
    PhoneCodeExpiredError, SessionPasswordNeededError, PasswordHashInvalidError,
)


# ── Helpers ─────────────────────────────────────────────────

SUPPORT_LINK = "[ɴᴇxᴜꜱ ꜱᴜᴘᴘᴏʀᴛ](https://t.me/PURVI_SUPPORT)"

async def _ask(bot: Client, uid: int, text: str, timeout: int = 300) -> Message:
    """Send a prompt and wait for the user's reply via pyromod listen."""
    await bot.send_message(uid, text)
    return await bot.listen(uid, filters=filters.text, timeout=timeout)

async def _cancelled(msg: Message, bot: Client) -> bool:
    """Returns True and notifies if user sent /cancel or any other command."""
    txt = msg.text or ""
    if txt.startswith("/cancel") or txt.startswith("/restart"):
        await msg.reply(ui.MSG_CANCELLED, reply_markup=ui.RETRY_BUTTON)
        return True
    if txt.startswith("/") and txt != "/skip":
        await msg.reply(ui.MSG_CANCELLED, reply_markup=ui.RETRY_BUTTON)
        return True
    return False


# ── Main generation function ────────────────────────────────

async def generate_session(
    bot: Client,
    msg: Message,
    *,
    telethon: bool = False,
    is_bot: bool   = False,
):
    uid = msg.chat.id

    # ── Determine library label ──────────────────────────────
    lib = "Telethon" if telethon else "Pyrogram v2"
    if is_bot:
        lib += " Bot"

    await msg.reply(f"**⚡ ꜱᴛᴀʀᴛɪɴɢ {lib.upper()} ꜱᴇꜱꜱɪᴏɴ ɢᴇɴᴇʀᴀᴛᴏʀ...**")

    # ── Step 1 · API_ID ──────────────────────────────────────
    try:
        api_id_msg = await _ask(bot, uid, ui.prompt_api_id(lib), timeout=300)
    except TimeoutError:
        await bot.send_message(uid, ui.ERR_TIMEOUT, reply_markup=ui.RETRY_BUTTON)
        return

    if await _cancelled(api_id_msg, bot):
        return

    if api_id_msg.text.strip() == "/skip":
        api_id    = config.API_ID
        api_hash  = config.API_HASH
        skip_keys = True
    else:
        try:
            api_id = int(api_id_msg.text.strip())
        except ValueError:
            await api_id_msg.reply(ui.ERR_API_ID_INT, reply_markup=ui.RETRY_BUTTON)
            return
        skip_keys = False

    # ── Step 2 · API_HASH ────────────────────────────────────
    if not skip_keys:
        try:
            api_hash_msg = await _ask(bot, uid, ui.prompt_api_hash(), timeout=300)
        except TimeoutError:
            await bot.send_message(uid, ui.ERR_TIMEOUT, reply_markup=ui.RETRY_BUTTON)
            return
        if await _cancelled(api_hash_msg, bot):
            return
        api_hash = api_hash_msg.text.strip()

    # ── Step 3 · Phone / Bot token ──────────────────────────
    prompt = ui.prompt_bot_token() if is_bot else ui.prompt_phone()
    try:
        cred_msg = await _ask(bot, uid, prompt, timeout=300)
    except TimeoutError:
        await bot.send_message(uid, ui.ERR_TIMEOUT, reply_markup=ui.RETRY_BUTTON)
        return
    if await _cancelled(cred_msg, bot):
        return
    credential = cred_msg.text.strip()

    # ── Build client ─────────────────────────────────────────
    if telethon:
        client = TelegramClient(StringSession(), api_id, api_hash)
    elif is_bot:
        client = Client(
            "nexus_bot_session",
            api_id=api_id,
            api_hash=api_hash,
            bot_token=credential,
            in_memory=True,
        )
    else:
        client = Client(
            "nexus_user_session",
            api_id=api_id,
            api_hash=api_hash,
            in_memory=True,
        )

    await client.connect()

    # ── Send OTP / Bot-token login ───────────────────────────
    try:
        if not is_bot:
            await msg.reply(ui.MSG_SENDING_OTP)
            if telethon:
                code_obj = await client.send_code_request(credential)
            else:
                code_obj = await client.send_code(credential)
        else:
            await msg.reply(ui.MSG_LOGGING_IN)
    except (ApiIdInvalid, ApiIdInvalidError):
        await msg.reply(ui.ERR_API_INVALID, reply_markup=ui.RETRY_BUTTON)
        await client.disconnect()
        return
    except (PhoneNumberInvalid, PhoneNumberInvalidError):
        await msg.reply(ui.ERR_PHONE_INVALID, reply_markup=ui.RETRY_BUTTON)
        await client.disconnect()
        return

    # ── OTP ──────────────────────────────────────────────────
    if not is_bot:
        try:
            otp_msg = await _ask(bot, uid, ui.prompt_otp(), timeout=600)
        except TimeoutError:
            await bot.send_message(uid, ui.ERR_TIMEOUT, reply_markup=ui.RETRY_BUTTON)
            await client.disconnect()
            return
        if await _cancelled(otp_msg, bot):
            await client.disconnect()
            return

        otp = otp_msg.text.replace(" ", "").strip()

        try:
            if telethon:
                await client.sign_in(credential, otp, password=None)
            else:
                await client.sign_in(credential, code_obj.phone_code_hash, otp)
        except (PhoneCodeInvalid, PhoneCodeInvalidError):
            await msg.reply(ui.ERR_OTP_INVALID, reply_markup=ui.RETRY_BUTTON)
            await client.disconnect()
            return
        except (PhoneCodeExpired, PhoneCodeExpiredError):
            await msg.reply(ui.ERR_OTP_EXPIRED, reply_markup=ui.RETRY_BUTTON)
            await client.disconnect()
            return
        except (SessionPasswordNeeded, SessionPasswordNeededError):
            # ── 2FA ─────────────────────────────────────────
            try:
                tfa_msg = await _ask(bot, uid, ui.prompt_2fa(), timeout=300)
            except TimeoutError:
                await bot.send_message(uid, ui.ERR_TIMEOUT, reply_markup=ui.RETRY_BUTTON)
                await client.disconnect()
                return
            if await _cancelled(tfa_msg, bot):
                await client.disconnect()
                return
            try:
                if telethon:
                    await client.sign_in(password=tfa_msg.text.strip())
                else:
                    await client.check_password(password=tfa_msg.text.strip())
            except (PasswordHashInvalid, PasswordHashInvalidError):
                await tfa_msg.reply(ui.ERR_2FA_WRONG, reply_markup=ui.RETRY_BUTTON)
                await client.disconnect()
                return
    else:
        # Bot-token login
        if telethon:
            await client.start(bot_token=credential)
        else:
            await client.sign_in_bot(credential)

    # ── Export session ───────────────────────────────────────
    if telethon:
        session_str = client.session.save()
    else:
        session_str = await client.export_session_string()

    # ── Send to Saved Messages (user sessions) ───────────────
    full_msg = ui.success_session(lib, session_str, SUPPORT_LINK)
    try:
        if not is_bot:
            await client.send_message("me", full_msg)
        else:
            await bot.send_message(uid, full_msg)
    except Exception:
        pass

    await client.disconnect()

    # ── Notify user ──────────────────────────────────────────
    await bot.send_message(uid, ui.success_dm_note(lib), reply_markup=ui.RETRY_BUTTON)
