from motor.motor_asyncio import AsyncIOMotorClient
import config

_client = AsyncIOMotorClient(config.MONGO_DB_URI)
db = _client.NexusStringGen
