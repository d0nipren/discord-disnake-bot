import disnake
import os

from disnake.ext import commands

intents=disnake.Intents.all() # подключаем интенты
bot = commands.Bot(command_prefix='!', intents=intents) #создаем префикс и вставляем интенты

@bot.event #создаем оповещение о включении бота
async def on_ready():
    print("Bot is ready!")

for file in os.listdir("./cogs"):
    if file.endswith(".py"):
        bot.load_extension(f"cogs.{file[:-3]}")

bot.run("MTE5MTQ1NzM2NTg1ODQ3MTk5OA.Gn0AXy.NlzMPu0iP4jxjLoUXy5O6MW_JGDEZghCKPCaIQ") #токен