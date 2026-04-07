import discord
from discord.ext import commands

import src.cogs.util.util_service as us

class Utils(discord.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.us = us.UtilService()
        
    @commands.command(name='clear')
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    
    async def clear(self, ctx: commands.Context, num=100):
        await self.us.clear(ctx, num)

    @commands.command(name='embed')
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def embed(self, ctx: commands.Context):
        await self.us.embed(ctx)

def setup(bot: commands.Bot):
    bot.add_cog(Utils(bot))