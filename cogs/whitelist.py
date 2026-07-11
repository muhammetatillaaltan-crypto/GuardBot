import discord
from discord.ext import commands
from discord import app_commands
import aiosqlite

class Whitelist(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="whitelist_add", description="Kullanıcıyı whitelist'e ekler.")
    @app_commands.default_permissions(administrator=True)
    async def whitelist_add(self, interaction: discord.Interaction, user: discord.Member):

        db = await aiosqlite.connect("data/guard.db")

        await db.execute(
            "INSERT INTO whitelist(guild,user) VALUES(?,?)",
            (interaction.guild.id, user.id)
        )

        await db.commit()

        await interaction.response.send_message(
            f"✅ {user.mention} whitelist'e eklendi.",
            ephemeral=True
        )

    @app_commands.command(name="whitelist_remove", description="Whitelist'ten kaldırır.")
    @app_commands.default_permissions(administrator=True)
    async def whitelist_remove(self, interaction: discord.Interaction, user: discord.Member):

        db = await aiosqlite.connect("data/guard.db")

        await db.execute(
            "DELETE FROM whitelist WHERE guild=? AND user=?",
            (interaction.guild.id, user.id)
        )

        await db.commit()

        await interaction.response.send_message(
            f"🗑️ {user.mention} whitelist'ten kaldırıldı.",
            ephemeral=True
        )

async def setup(bot):
    await bot.add_cog(Whitelist(bot))
