# Imports

import discord
import random
import traceback
import time
import os
import json
import asyncio
from keep_alive import keep_alive
from discord.ext import commands
from cogs.ticket import sendticket
from cogs.reactionrole import sendreaction
#Defining the Client

TOKEN = os.environ['BOT_TOKEN']
intents = discord.Intents.all()
client = commands.Bot(help_command=None,
                      command_prefix=">",
                      case_insensitive=True,
                      intents=intents)

client.remove_command("help")

# Loading Cogs
async def loadcogs():
  for filename in os.listdir("./cogs"):
      if filename.endswith(".py"):
          try:
              await client.load_extension(f"cogs.{filename[:-3]}")
              print(f"{filename} Loaded.")
          except:
              traceback.print_exc()
              pass

#=====Main Code=====

@client.event
async def on_ready():
  print(f"Logged in as {client.user}")
  await client.change_presence(activity=discord.Activity(
        type=discord.ActivityType.listening, name="Prefix : >"),
                                 status=discord.Status.online)
  channel = client.get_channel(954761642967707710)
  await channel.edit(name = f"Members : {len(channel.guild.members)}")
  await loadcogs()
  channel = client.get_channel(966566872109682738)
  await sendticket(channel)
  reactionchannel = client.get_channel(966582534047662130)
  await sendreaction(reactionchannel)

  

# Running the Bot

keep_alive()
client.run(TOKEN)