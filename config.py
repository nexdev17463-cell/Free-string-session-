from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID      = int(getenv("API_ID", "0"))
API_HASH    = getenv("API_HASH", "")
BOT_TOKEN   = getenv("BOT_TOKEN", None)
OWNER_ID    = int(getenv("OWNER_ID", "0"))
MONGO_DB_URI = getenv("MONGO_DB_URI", "")
MUST_JOIN   = getenv("MUST_JOIN", "")   # channel/group username without @

# ── Aesthetic ──────────────────────────────────────────────
BANNER = """
╔══════════════════════════════════════╗
║   ɴᴇxᴜs  ꜱᴛʀɪɴɢ  ɢᴇɴᴇʀᴀᴛᴏʀ  ʙᴏᴛ    ║
║        ʙᴏᴏᴛɪɴɢ ᴜᴘ ...              ║
╚══════════════════════════════════════╝
"""

# ── Styled text helpers (Telegram MarkdownV2-safe bold) ────
def hdr(text: str) -> str:
    """Wraps text in Telegram bold."""
    return f"**{text}**"

def mono(text: str) -> str:
    return f"`{text}`"

def link(label: str, url: str) -> str:
    return f"[{label}]({url})"
