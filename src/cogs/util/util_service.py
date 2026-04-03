import discord
import src.cfg.embed as embed_cfg
from discord.ext import commands

class UtilService:
    def __init__(self) -> None:
        pass

    async def clear(self, ctx: commands.Context, num: int) -> None:
        channel = ctx.channel
        author = ctx.author

        if not isinstance(channel, discord.TextChannel) or not isinstance(author, discord.Member):
            return
        
        if not channel.permissions_for(author).manage_messages:
            return
        
        await channel.purge(limit=num+1)
        message = await channel.send(embed=discord.Embed(
            title="Messages supprimés",
            description=f"{author.mention} Vous avez supprimé `{num}` messages.",
            color=embed_cfg.embed_color
        ).set_footer(text=f"Supprimé par {author.display_name}", icon_url=author.display_avatar.url)
        )

        await message.delete(delay=3)