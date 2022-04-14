import discord
import os

from discord.ext import commands

client = commands.Bot(command_prefix = "*",intents=discord.Intents.all(),
    allowed_mentions=discord.AllowedMentions(roles=False, users=True, everyone=False),)


for filename in os.listdir("cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")



client.run("OTY0MDcxOTc0NzUyMDkyMTgy.YlfT_g.wjXCRWiv-zaKnDWw2QJGvRrRE8o")



