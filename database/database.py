import aiosqlite

class Database:

    def __init__(self):
        self.db = "data/guard.db"

    async def connect(self):
        self.conn = await aiosqlite.connect(self.db)

        await self.conn.execute("""
        CREATE TABLE IF NOT EXISTS whitelist(
            guild INTEGER,
            user INTEGER
        )
        """)

        await self.conn.execute("""
        CREATE TABLE IF NOT EXISTS settings(
            guild INTEGER PRIMARY KEY,
            log_channel INTEGER,
            enabled INTEGER
        )
        """)

        await self.conn.commit()

db = Database()
