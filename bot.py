import discord
from discord.ext import commands
from discord.ext import tasks 
import yaml

bot = commands.Bot(command_prefix='.', intents=discord.Intents.default())

with open('config.yaml', 'rb') as f:
    config = yaml.safe_load(f)

@bot.event
async  def on_ready():
    change_status.start()
    print('bot in active')

@tasks.loop(seconds=60)#time
async def change_status():
    channel = bot.get_channel(config["CHANNEL_ID"])
    await channel.send(config["DISCORD_MESSAGE"])
bot.run(config["BOT_TOKEN"])