import discord
from discord.ext import commands

class ModerationService:
    def __init__(self):
        pass

    async def change_lock(self, ctx: commands.Context, status: bool):
        guild = ctx.guild
        if guild is None: return

        channel = ctx.channel
        if not isinstance(channel, discord.TextChannel): return

        await channel.set_permissions(guild.default_role, send_messages=status)
        message = await channel.send(embed=discord.Embed(
            title='Channel access status changed',
            description=f'Channel {'unlocked' if status else 'locked'} by {ctx.author.mention}',
            color=discord.Color(0x010101)
        ).set_footer(text='Zane Bot, moderation services', icon_url=ctx.author.avatar))
        
        await message.delete(delay=2.0)