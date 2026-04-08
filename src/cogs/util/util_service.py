import discord
from discord.ext import commands

class UtilService:
    def __init__(self) -> None:
        pass

    async def clear(self, ctx: commands.Context, num: int) -> None:
        channel = ctx.channel
        if not isinstance(channel, discord.TextChannel):
            return
        await channel.purge(limit=num+1)
    
    async def embed(self, ctx: commands.Context) -> None:
        channel = ctx.channel
        if not isinstance(channel, discord.TextChannel):
            return
        
        async for message in channel.history(limit=2):
            if message.id == ctx.message.id:
                continue
            await ctx.send(embed=discord.Embed(description=message.content, color=discord.Color(0x010101)))
        return