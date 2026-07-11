import aiosqlite

async def is_whitelisted(guild_id: int, user_id: int):

    db = await aiosqlite.connect("data/guard.db")

    cursor = await db.execute(
        "SELECT * FROM whitelist WHERE guild=? AND user=?",
        (guild_id, user_id)
    )

    row = await cursor.fetchone()

    return row is not None
