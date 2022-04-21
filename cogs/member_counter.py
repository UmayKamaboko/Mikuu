#Imports

import discord
from discord.ext import commands

#Member Counter Class

class MemberCounter(commands.Cog):
  def __init__(self, client):
      self.client = client

  # When someone Joins
  
  @commands.Cog.listener()
  async def on_member_join(self, member):
    channel = self.client.get_channel(954761642967707710)
    await channel.edit(name = f"Members : {len(member.guild.members)}")
    

  # When someone Leaves
  
  @commands.Cog.listener()
  async def on_member_remove(self, member):
    channel = self.client.get_channel(954761642967707710)
    await channel.edit(name = f"Members : {len(member.guild.members)}")

# Adding the Cog to Client

async def setup(client):
    await client.add_cog(MemberCounter(client))
