# discord
from tokens import get_discord_token
from dotenv import load_dotenv
import discord
from discord.ext import commands

# getters
from duck_news_getter import get_news
from duck_pic_getter import get_link

load_dotenv()

bot = commands.Bot(command_prefix="~")
bot.remove_command("help")


@bot.event
async def on_ready():
    print('Bot ready')
    await bot.change_presence(activity=discord.Game(name="~info for help"))


@bot.command(aliases=['info'])
async def help(ctx):
    await ctx.send("Instructions: \n~ducknews - for duck related news!")


@bot.command(name="ducknews")
async def _ducknews(ctx):

    news = get_news()
    pic = get_link()
    print(news)
    print(pic)

    embed = discord.Embed(
        title="Duck News!",
        description=news[0],
        color=discord.Colour.random()
    )

    embed.add_field(name='Source', value=news[1], inline=False)
    embed.set_image(url=pic)

    await ctx.send(embed=embed)


bot.run(get_discord_token())
