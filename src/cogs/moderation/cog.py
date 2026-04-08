import discord
from discord.ext import commands
from src.cogs.moderation import moderation_service as ms

class ModerationCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.ms = ms.ModerationService()

    @commands.command(name='lock')
    @commands.has_permissions(administrator=True)
    @commands.guild_only()

    async def lock(self, ctx: commands.Context):
        await self.ms.change_lock(ctx, False)
    
    @commands.command(name='unlock')
    @commands.has_permissions(administrator=True)
    @commands.guild_only()

    async def unlock(self, ctx: commands.Context):
        await self.ms.change_lock(ctx, True)

def setup(bot):
    bot.add_cog(ModerationCog(bot))