import os
from dotenv import load_dotenv

import discord
from discord.ext import commands

import src.db.database as db

db.init_db()

# dotenv loading
load_dotenv()
TOKEN = os.getenv('TOKEN')
DEBUG_GUILD_ID = os.getenv('DEBUG_GUILD_ID')

intents = discord.Intents.default()
intents.message_content = True

# bot setup
bot = commands.Bot(
    command_prefix='+',
    intents=intents,
    debug_guilds=[DEBUG_GUILD_ID],
    status=discord.Status.dnd
    )
modules = {
    "util": True,
    "ticket": False,
    "verif": True,
}

# cogs loadings
for module in os.listdir("./src/cogs"):
    if modules[module]:
        bot.load_extension(f"src.cogs.{module}.cog")

bot.run(TOKEN)