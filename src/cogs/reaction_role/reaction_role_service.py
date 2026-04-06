import discord
from discord.ext import commands

import cogs.reaction_role.reaction_role_repo as repo

class ReactionRoleService:
    def __init__(self, bot) -> None:
        self.repo = repo.ReactionRoleRepo()
        self.bot: commands.Bot = bot
    
    # Adds the reaction
    async def add_reaction(self, ctx: commands.Context, message_id: int, role_id: int, emoji: str):
        guild = ctx.guild
        if not guild:
            return
        message = await ctx.channel.fetch_message(message_id)
        role = await guild.fetch_role(role_id)

        if not message or not role:
            return
        
        self.repo.add_message(message_id, emoji, role_id)
        await message.add_reaction(emoji)
    
    async def remove_reaction(self, message: discord.Message):
        if not self.repo.get_message(message.id) is None:
            self.repo.remove_message(message.id)

    # Gives the role on reaction
    async def give_role(self, payload: discord.RawReactionActionEvent):
        results = self.repo.get_message(payload.message_id)
        if not results: return
        if not payload.guild_id: return
        
        guild = self.bot.get_guild(payload.guild_id)
        if not guild: return

        for result in results:
            if result[2] != str(payload.emoji):
                continue

            role = guild.get_role(result[1])
            member = payload.member

            if role and member:
                await member.add_roles(role)