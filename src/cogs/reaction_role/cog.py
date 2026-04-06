import discord
from discord.ext import commands

import src.cogs.reaction_role.reaction_role_service as rrs

class ReactionRole(discord.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.rrs = rrs.ReactionRoleService(self.bot)
    
    @commands.command(name='reactionrole')
    @commands.guild_only()
    @commands.has_permissions(administrator=True)

    async def reactionrole(self, ctx: commands.Context, message_id: int, role_id: int, emoji: str):
        await self.rrs.add_reaction(ctx, message_id, role_id, emoji)
    
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload:discord.RawReactionActionEvent):
        if self.bot.user and payload.user_id == self.bot.user.id:
            return
        await self.rrs.give_role(payload)
    
    @commands.Cog.listener()
    async def on_message_delete(self, message:discord.Message):
        await self.rrs.remove_reaction(message)

def setup(bot: commands.Bot):
    bot.add_cog(ReactionRole(bot))