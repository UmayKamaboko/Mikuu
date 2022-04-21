#Imports

import discord
from discord.ui import Button, View
from discord.ext import commands
#Defining client + Intents
intents = discord.Intents.all()
client = commands.Bot(command_prefix=">",case_insensitive = True , intents = intents)



# Ticket Button

class TicketView(View):
  @discord.ui.button(label="Create a Ticket",style=discord.ButtonStyle.green,emoji = "🎫")
  async def button_callback(self,interaction,button):
    
    # Renaming Interaction items
    guild = interaction.guild
    user = interaction.user
    #Checking if ticket is already open
    channels = []
    for channel in guild.channels :
      if str(channel.type) == "text":
        channels.append(channel.name)
    text = f"ticket-{user.name}".lower()
    text = text.replace(" ","-")
    if text in channels :  
      await interaction.response.send_message(f":x: Shoma ham aknon yek Ticket Baze digar Darid.",ephemeral=True)  
      return
    #Creating the ticket

    # Overwrites Dict
    overwrites = {
      guild.default_role: discord.PermissionOverwrite(read_messages=False),
      user : discord.PermissionOverwrite(read_messages=True)
   }
    channels = []
    channel  = await guild.create_text_channel(name=f"ticket-{user.name}", reason="Opened Ticket",overwrites = overwrites)
    await interaction.response.send_message(f"Ticket Sakhte Shod - {channel.mention}",ephemeral=True)
    await channel.send(f"Salam {user.mention} ! In Ticket Shoma Mibashad. Shoma Mitavanid dar Har Zaman Ba Command `>close` Ticket ra Bebandid !")


#Function that sends Claim ticket Message
async def sendticket(channel:discord.TextChannel):
  view = TicketView()
  ticketch = channel
  await ticketch.purge(limit=None)
  await ticketch.send("✉️ Baraye Baz Kardan Ticket Roye Dokme Zir Bezanid.",view=view)


class Ticket(commands.Cog):

  def __init__(self,client):
    self.client = client

  #Command to send the Ticket message
  @commands.command()
  async def ticket(self,ctx):
    view = TicketView()
    ticketch = self.client.get_channel(966566872109682738)
    await ticketch.purge(limit=None)
    await ticketch.send("✉️ Baraye Baz Kardan Ticket Roye Dokme Zir Bezanid.",view=view)

  #Close command
  @commands.command()
  async def close(self,ctx):
    if ctx.channel.name.startswith("ticket"):
      await ctx.channel.delete()
    else :
      await ctx.reply(":x: Inja yek Channel Ticket Nist!")

async def setup(client):
    await client.add_cog(Ticket(client))     