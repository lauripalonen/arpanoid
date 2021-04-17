import os
import logging
from discord.ext import commands
from dotenv import load_dotenv
from logics import roll as cast, info_msg

logging.basicConfig(level=logging.INFO)
load_dotenv()

def start():
    bot = commands.Bot(command_prefix='!', help_command=None)

    @bot.event
    async def on_ready():
        print('Bot logged in as {0.user.name}.'.format(bot))

    @bot.command()
    async def roll(ctx, dice):
        result = cast(dice)
        await ctx.send(result)

    @bot.command()
    async def help(ctx):
        await ctx.send(info_msg())
   
    token = os.getenv('BOT_TOKEN')
    bot.run(token)

start()
