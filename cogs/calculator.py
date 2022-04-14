import math
from discord.ext import commands

class Calculator(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ["+"])
    async def add(self,ctx,int1,int2):
        '''To bring two or more numbers together to make a new total.'''
        int1 = int(int1)
        int2 = int(int2)
        await ctx.send("%d + %d = %d"% (int1,int2,int1 + int2))

    @commands.command(alises = ["-", "subtract"])
    async def minus(self,ctx,int1,int2):
        '''to take away from a group or a number of things.'''
        int1 = int(int1)
        int2 = int(int2)
        await ctx.send("%d - %d = %d"% (int1,int2,int1 - int2))

    @commands.command(aliases = ["multi","*","x"])
    async def multiply(self,ctx,int1,int2):
        '''the process of calculating the result when a number is taken times.'''
        int1 = int(int1)
        int2 = int(int2)
        await ctx.send("%d * %d = %d"% (int1,int2,int1 * int2))

    @commands.command(aliases = ["div","/"])
    async def divide(self,ctx,int1,int2):
        '''the process of breaking a number up into equal parts, and finding out how many equal parts can be made.'''
        int1 = int(int1)
        int2 = int(int2)
        await ctx.send("%d / %d = %d"% (int1,int2,int1 / int2))

    @commands.command(aliases = ["pow"])
    async def power(self,ctx,int1,int2):
        '''represents repeated multiplication of the same factor is called a power.'''
        int1 = int(int1)
        int2 = int(int2)
        await ctx.send("%d ^ %d = %d"% (int1,int2,pow(int1,int2)))

    @commands.command(aliases =  ["sqrt"])
    async def squareroot(self,ctx,base):
        '''when multiplied by itself, gives the original number.'''
        base = int(base)
        await ctx.send("√%d = %d"% (base,math.sqrt(base)))

    @commands.command(aliases = ["mod"])
    async def modulo(self,ctx,int1,int2):
        '''operation that finds the remainder when one integer is divided by another.'''
        int1 = int(int1)
        int2 = int(int2)
        await ctx.send("%d mod %d = %d"% (int1,int2,int1 % int2))

    @commands.command(aliases = ["abs"])
    async def absolute(self,ctx,int1):
        '''| x | of a real number x is the non-negative value of x without regard to its sign.'''
        int1 = int(int1)
        await ctx.send("%d |x| = %d"% (int1,abs(int1)))

    @commands.command(aliases = ["fact"])
    async def factorial(self,ctx,int1):
        '''divides another number or expression evenly with no remainder.'''
        int1 = int(int1)
        await ctx.send("factorial of %d = %d"% (int1,math.factorial(int1)))

    @commands.command()
    async def pi(self,ctx):
        '''π is the ratio of the circumference of any circle to the diameter of that circle.'''
        await ctx.send("3.1415926535897932384626433832795")

def setup(client):
    client.add_cog(Calculator(client))