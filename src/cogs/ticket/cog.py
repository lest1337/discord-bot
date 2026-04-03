import discord
from discord.ext import commands

import src.cogs.ticket.ticket_service as ts

class Tickets(discord.Cog):
    def __init__(self, bot) -> None:
        self.bot: discord.Bot = bot
        self.ts = ts.TicketService(bot)
    
    @commands.command(name='create-ticket-panel')
    @commands.has_permissions(manage_channels=True)
    async def create_ticket_panel(self, ctx: commands.Context):
        await self.ts.create_ticket_panel(ctx=ctx)

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload: discord.RawReactionActionEvent):
        await self.ts.create_ticket_channel(payload)
        


def setup(bot: commands.Bot):
    bot.add_cog(Tickets(bot))