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