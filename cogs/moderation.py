#Imports

import discord
from discord.ext import commands

#Defining client + Intents
intents = discord.Intents.all()
client = commands.Bot(command_prefix=">",case_insensitive = True , intents = intents)


class Moderation(commands.Cog):
    
  def __init__(self,client):
      self.client = client

  #Clear Command
  
  @commands.command()
  @commands.guild_only()
  @commands.has_permissions(manage_messages=True)
  async def clear(self,ctx, amount=None):  
    async with ctx.channel.typing():
      if amount == None :
        await ctx.reply(":rolling_eyes: Lotfan yek Adad Sahih Vared konid.")
        return
      try :
        amount = int(amount)
      except :
        await ctx.reply(":rolling_eyes: Lotfan yek Adad Sahih Vared konid.")
        return
      if amount == 0 or amount < 0 :
          await ctx.reply(":x: Meghdar Baiad Az 0 Bozorg Tar Bashe! ")
          return
      else:
          try :  
            await ctx.channel.purge(limit=amount)
            await ctx.reply(f"{amount} Payam pak Shodand.",delete_after = 5)
          except :
            await ctx.reply(":rolling_eyes: Mesl in ke Permission Purge kardan In Channel Ro Nadaram ...")
            return

  #Ban Command

  @commands.command()
  @commands.guild_only()
  @commands.has_permissions(ban_members=True)
  async def ban(self,ctx, member:discord.Member=None, *,reason =None):
          if member == None :
              await ctx.reply(f"Lotfan yek Nafar Ro Mention Kon Ta Kickesh Konam.")
              return
          if member == ctx.author:
                  await ctx.reply("Chera mikhai Khodet ro Ban koni ? :pensive:")
                  return
          
          if reason == None:
                  reason = "Bedone Dalil"
          message = f"Shoma **Ban Shodid** az **{ctx.guild.name}** Bekhatere **{reason}**"
          try : 
            await ctx.guild.ban(member, reason=reason)
            await ctx.reply(f"{member.mention} Ban Shod Be dalile {reason}",delete_after=10)
            try : 
              await member.send(message)
            except : 
              pass
          except : 
            await ctx.reply(":x: Natonestam Oon Member Ro Ban Konam !",delete_after=5)
            return

  #Kick command
  
  @commands.command()
  @commands.guild_only()
  @commands.has_permissions(kick_members=True)
  async def kick(self,ctx ,member:discord.Member=None, *,reason =None):
      if member == self.client.user :
        await ctx.reply(":x: Nemitonam Khodam ro kick konam!")
        return
      if member == ctx.author:
              await ctx.reply(":x: Lotfan Yeki Digaro Kick Kon.")
              return
      if member == None :
              await ctx.reply(f"Lotfan yek Nafar Ro Mention Kon Ta Kickesh Konam.")
              return
      if reason == None:
              reason = "Bedone Dalil"
      message = f"Shoma **Kick Shodid** Az **{ctx.guild.name}** Bekhatere **{reason}**"
      
      try : 
        await ctx.guild.kick(member, reason=reason)
        await ctx.reply(f"{member.mention} Kick Shod Be dalile {reason}",delete_after=10)
        try :
            await member.send(message)
        except : 
            pass
      except : 
        await ctx.reply(f"Nemitonam Oon Fard ro Kick Konam.",delete_after=5)
        return

  #Channel Locker Command
  
  @commands.command()
  @commands.guild_only()
  @commands.has_permissions(manage_messages=True)
  async def lock(self,ctx, channel:discord.TextChannel=None):
    if isinstance(channel,discord.VoiceChannel):
      await ctx.reply(":rolling_eyes: Channel Haye Type Voice ro Nemishe Lock Kard.")
      return
    if channel == None :
      channel = ctx.channel
    try  :
      await channel.set_permissions(ctx.guild.default_role,send_messages=False)
      await ctx.reply(':white_check_mark: Channel lock shod.')
    except :
      await ctx.reply(":x: Natonestam Channel Ro Unlock Konam.")

  #Channel unlocker Command
  @commands.command()
  @commands.guild_only()
  @commands.has_permissions(manage_messages=True)
  async def unlock(self,ctx,channel:discord.TextChannel = None):
    if isinstance(channel,discord.VoiceChannel):
      await ctx.reply(":rolling_eyes: Channel Haye Type Voice ro Nemishe Unlock Kard.")
      return
    if channel == None :
      channel = ctx.channel
    try  :
      await channel.set_permissions(ctx.guild.default_role,send_messages=True)
      await ctx.reply(':white_check_mark: Channel unlock shod.')
    except :
      await ctx.reply(":x: Natonestam Channel Ro Unlock Konam.")

async def setup(client):
    await client.add_cog(Moderation(client))     