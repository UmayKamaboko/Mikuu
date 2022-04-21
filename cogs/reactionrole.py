#Imports

import discord
from discord.ui import Button, View
from discord.ext import commands
#Defining client + Intents
intents = discord.Intents.all()
client = commands.Bot(command_prefix=">",case_insensitive = True , intents = intents)


#Function that sends Claim ticket Message
async def sendreaction(channel:discord.TextChannel):
  reactch = channel
  await reactch.purge(limit=None)
  message = await reactch.send("React Below to Claim Your Role!\n🔫 : CSGO\n🎵 : Music")
  await message.add_reaction("🎵")
  await message.add_reaction("🔫")

#Reaction Role Class
class ReactionRole(commands.Cog):

  def __init__(self,client):
    self.client = client

  # Will trigger when someone Reacts to a Message
  @commands.Cog.listener()
  async def on_reaction_add(self,reaction, user):
    if user == self.client.user : 
      return # So bot doesn't give role to itself
    Channel = self.client.get_channel(966582534047662130)
    if reaction.message.channel.id != Channel.id:
        return
    if reaction.emoji == "🔫":
      Role = discord.utils.get(user.guild.roles, name="csgo")
      await user.add_roles(Role)
      try : 
        await user.send(f":white_check_mark: Claimed {Role} in {Channel.guild.name} By Reacting !")
      except : 
        pass
    if reaction.emoji == "🎵":
      Role = discord.utils.get(user.guild.roles, name="music")
      await user.add_roles(Role)
      try : 
        await user.send(f":white_check_mark: Claimed {Role} in {Channel.guild.name} By Reacting !")
      except : 
        pass


  # Command to Send the Reaction message
  @commands.command()
  async def react(self,ctx):
    await ctx.message.delete()
    message = await ctx.send("React Below to Claim Your Role!\n🔫 : CSGO\n🎵 : Music")
    await message.add_reaction("🎵")
    await message.add_reaction("🔫")

# Adding ReactionRole Class to Client
async def setup(client):
    await client.add_cog(ReactionRole(client))     