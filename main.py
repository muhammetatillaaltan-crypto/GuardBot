import discord
from discord.ext import commands
import asyncio
import os

intents = discord.Intents.all()

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)

@bot.event
async def on_ready():
    print("=" * 40)
    print(f"Bot giriş yaptı")
    print(bot.user)
    print("=" * 40)

    try:
        synced = await bot.tree.sync()
        print(f"{len(synced)} Slash komutu senkronize edildi.")
    except Exception as e:
        print(e)

async def load_extensions():
    for file in os.listdir("./cogs"):
        if file.endswith(".py"):
            await bot.load_extension(f"cogs.{file[:-3]}")
            print(f"{file} yüklendi.")

async def main():
    async with bot:
        await load_extensions()
        from config import TOKEN
        await bot.start(TOKEN)

asyncio.run(main())
