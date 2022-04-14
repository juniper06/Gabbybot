from asyncio import events
import discord

from discord.ext import commands

class User(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @commands.command(aliases=["send", "dm", "pm"])
    async def message(self, ctx, user: discord.User, *, message: str):
        """ Sending a message to Specific User"""
        await user.send(message)
        await ctx.reply(f"Message send to {user}", mention_author=False)

    @commands.command()
    async def ping(self,ctx):
        await ctx.send('Pong! {0}ms'.format(round(self.client.latency, 1)))

def setup(client):
    client.add_cog(User(client))