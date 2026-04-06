import discord
from discord.ext import commands

import src.cogs.util.util_service as us
import src.cogs.util.reaction_role_service as rrs

class Utils(discord.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.us = us.UtilService()
        self.rrs = rrs.ReactionRoleService(self.bot)
        
    @commands.command(name='clear')
    @commands.guild_only()
    
    async def clear(self, ctx: commands.Context, num: int):
        await self.us.clear(ctx, num)

    @commands.command(name='reactionrole')
    @commands.guild_only()
    @commands.has_permissions(administrator=True)

    async def reactionrole(self, ctx: commands.Context, message_id: int, role_id: int, emoji: str):
        await self.rrs.add_reaction(ctx, message_id, role_id, emoji)
    
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload:discord.RawReactionActionEvent):
        if payload.user_id == self.bot.user.id:
            return
        await self.rrs.give_role(payload)
    
    @commands.Cog.listener()
    async def on_message_delete(self, message:discord.Message):


def setup(bot: commands.Bot):
    bot.add_cog(Utils(bot))