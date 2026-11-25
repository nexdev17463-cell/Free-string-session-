from NEXUS.db import db

_col = db.users


async def add_user(user_id: int) -> None:
    if not await _col.find_one({"uid": user_id}):
        await _col.insert_one({"uid": user_id})


async def all_users() -> list:
    return [u async for u in _col.find({"uid": {"$gt": 0}})]


async def total_users() -> int:
    return await _col.count_documents({})
