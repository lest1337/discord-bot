import discord
from discord.ext import commands

import src.cogs.util.util_service as us

class Utils(discord.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.us = us.UtilService()
        
    @commands.command(name='clear')
    @commands.guild_only()
    
    async def clear(self, ctx: commands.Context, num=100):
        await self.us.clear(ctx, num)

def setup(bot: commands.Bot):
    bot.add_cog(Utils(bot))