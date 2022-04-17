import importlib
import sys
import time
from discord import Embed
from discord.ext import commands
from utils.permissions import is_owner


class Owner(commands.Cog):
    def __init__(self, client) -> None:
        self.client = client

    @commands.check(is_owner)
    @commands.command()
    async def load(self, ctx, directory: str) -> None:
        """Load a Cog extension"""
        self.client.load_extension(f"cogs.{directory}")
        await ctx.send(embed=Embed(title=f"Cog has loaded the {directory}"))

    @commands.check(is_owner)
    @commands.command()
    async def unload(self, ctx, directory: str) -> None:
        """Unload a Cog extension"""
        self.client.unload_extension(f"cogs.{directory}")
        await ctx.send(embed=Embed(title=f"Cog has unloaded the {directory}"))

    @commands.check(is_owner)
    @commands.command()
    async def reload(self, ctx, directory: str) -> None:
        """Reload a Cog extension"""
        self.client.reload_extension(f"cogs.{directory}")
        await ctx.send(embed=Embed(title=f"Cog has reloaded the {directory}"))

    @commands.check(is_owner)
    @commands.command()
    async def reloadUtils(self, ctx, name: str) -> None:
        """Reload a Utils module"""
        module_name = importlib.import_module(f"utils.{name}")
        importlib.reload(module_name)
        await ctx.send(f"Module Reloaded {name}")

    @commands.check(is_owner)
    @commands.command(
        help=" - logging off", aliases=["close", "poweroff", "turnoff, logoff"]
    )
    async def logout(self, ctx):
        """client-bot is logging off"""
        await ctx.send("Bye")
        time.sleep(1)
        sys.exit(0)


def setup(client):
    client.add_cog(Owner(client))
