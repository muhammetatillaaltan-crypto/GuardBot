from discord.ext import commands
from discord import app_commands
import discord
import aiosqlite

class Setup(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="setup",
        description="Guard sistemini kur."
    )
    async def setup_guard(
        self,
        interaction: discord.Interaction,
        log_channel: discord.TextChannel
    ):

        await interaction.response.defer(ephemeral=True)

        db = await aiosqlite.connect("data/guard.db")

        await db.execute(
            "INSERT OR REPLACE INTO settings VALUES(?,?,?)",
            (
                interaction.guild.id,
                log_channel.id,
                1
            )
        )

        await db.commit()

        embed = discord.Embed(
            title="✅ Guard Aktif",
            description=f"Log kanalı: {log_channel.mention}",
            color=0x2ecc71
        )

        await interaction.followup.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Setup(bot))
