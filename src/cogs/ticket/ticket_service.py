import discord
from discord.ext import commands

import src.cfg.embed as embed_cfg
import src.cogs.ticket.ticket_repo as repo

class TicketService:
    def __init__(self, bot) -> None:
        self.repo = repo.TicketRepo()
        self.bot: discord.Bot = bot

    # Basic type validity check function
    async def is_valid(self, ctx: commands.Context):
        if (not isinstance(ctx.channel, discord.TextChannel) or
        not isinstance(ctx.author, discord.Member) or
        ctx.guild is None
        or self.bot is None):
            return False
        return True
    
    # Create the base ticket message with a reaction to create a ticket    
    async def create_ticket_panel(self, ctx: commands.Context):

        # Checks
        if not await self.is_valid(ctx):
            return
        
        message = await ctx.channel.send(embed=discord.Embed(
            title="Tickets",
            description="Réagissez pour créer un ticket. Les helpeurs seront notifiés pour vous aider le plus rapidement possible",
            color=embed_cfg.embed_color,
            footer=embed_cfg.footer
        ))

        self.repo.add_ticket_message(message.id)

        await message.add_reaction('🎫')

    # Create the ticket channel
    async def create_ticket_channel(self, payload: discord.RawReactionActionEvent):

        # Checks
        ticket_messages = self.repo.get_ticket_message()
        if payload.guild_id is None or not payload.message_id in ticket_messages:
            return
        
        guild = self.bot.get_guild(payload.guild_id)
        if guild is None:
            guild = self.bot.fetch_guild(payload.guild_id)
        author = self.bot.get_user(payload.user_id)

        if not isinstance(guild, discord.Guild) or not isinstance(author, discord.Member):
            return

        if not self.repo.get_ticket_from_user(payload.user_id) is None:
            return
        
        # Logic
        channel = await guild.create_text_channel(f"ticket-{author.name}", category=None)
        await channel.send(embed=discord.Embed(
            title="Ticket",
            description=f"{author.mention}, ton ticket a été créé.",
            color=embed_cfg.embed_color,
            footer=embed_cfg.footer
        ))