import discord
from discord.ext import commands
from utils.checks import is_whitelisted

class Guard(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_channel_delete(self, channel):

        guild = channel.guild

        async for entry in guild.audit_logs(limit=1, action=discord.AuditLogAction.channel_delete):

            # Sunucu sahibini koru
            if entry.user.id == guild.owner_id:
                return

            # Whitelist kontrolü
            if await is_whitelisted(guild.id, entry.user.id):
                return

            member = guild.get_member(entry.user.id)

            if member is None:
                return

            try:
                # Tüm rollerini kaldır (varsayılan @everyone hariç)
                await member.edit(
                    roles=[],
                    reason="Guard: İzinsiz kanal silme"
                )

                print(f"{member} yetkileri kaldırıldı.")

            except discord.Forbidden:
                print("Yetki yetersiz.")
