import config
import time
import logging
import asyncio
from pyrogram import Client, idle
from pyromod import listen
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s — %(name)s — %(levelname)s — %(message)s"
)
logging.getLogger("pymongo").setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

StartTime = time.time()


# ── pyromod KeyError patch ───────────────────────────────────
def _patch_pyromod():
    try:
        from pyromod.listen import client as pyromod_client
        from pyromod.listen.client import Client as PyromodClient
        from pyromod.utils.types import ListenerTypes

        _orig = PyromodClient.get_listener_matching_with_data

        async def _safe_get_listener(self, data, listener_type):
            if listener_type not in self.listeners:
                return None
            return await _orig(self, data, listener_type)

        PyromodClient.get_listener_matching_with_data = _safe_get_listener
    except Exception:
        pass

_patch_pyromod()
# ─────────────────────────────────────────────────────────────
app = Client(
    "NexusStringGen",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
    in_memory=True,
    plugins=dict(root="NEXUS"),
)

if __name__ == "__main__":
    print(config.BANNER)
    try:
        app.start()
    except ApiIdInvalid:
        raise Exception("❌ API_ID is invalid.")
    except ApiIdPublishedFlood:
        raise Exception("❌ API_ID/API_HASH is flood-banned.")
    except AccessTokenInvalid:
        raise Exception("❌ BOT_TOKEN is invalid.")
    except Exception as e:
        logging.error(f"Startup error: {e}")
        raise

    me = app.get_me()
    print(f"\n✅  @{me.username} is online and ready.\n")

    idle()
    app.stop()
    print("⛔  Bot stopped.")
