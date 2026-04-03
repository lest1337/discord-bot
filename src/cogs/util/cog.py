import discord
from discord.ext import commands

import src.cogs.util.util_service as us

class Utils(discord.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.us = us.UtilService()
        
    @commands.command(name='clear')
    async def clear(self, ctx: commands.Context, num: int):
        await self.us.clear(ctx, num)

def setup(bot: commands.Bot):
    bot.add_cog(Utils(bot))