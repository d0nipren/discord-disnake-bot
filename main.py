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

bot.run("") #токен
