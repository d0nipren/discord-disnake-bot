from disnake.ext import commands

class PingPong(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='ping', description='Пинг понг!') #слэш-команда пинг
    async def pingpong(interaction):
        await interaction.response.send_message("Понг!")

def setup(bot):
    bot.add_cog(PingPong(bot))