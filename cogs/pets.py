import discord
from discord.ext import commands
from discord import Embed
import requests

async def get(session: object, url: object) -> object:
        async with session.get(url) as response:
            return await response.text()

class Pets(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    #comands
    @commands.command()
    async def cat(self, ctx):
      response = requests.get('https://aws.random.cat/meow')
      data = response.json()
      embed = discord.Embed(
          title = 'Kitty Cat 🐈',
          description = 'Cats :star_struck:',
          colour = discord.Colour.purple()
          )
      embed.set_image(url=data['file'])            
      embed.set_footer(text="")
      await ctx.send(embed=embed)

    @commands.command()
    async def dog(self, ctx):
      response = requests.get('https://some-random-api.ml/img/dog')
      data = response.json()
      embed = discord.Embed(
          title = 'Doggy dog 🐕‍🦺',
          description = 'Dogs :star_struck:',
          colour = discord.Colour.purple()
          )
      embed.set_image(url=data['link'])            
      embed.set_footer(text="")
      await ctx.send(embed=embed)

    #events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is online')


def setup(bot):
    bot.add_cog(Pets(bot))