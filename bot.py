#discord
from dotenv import load_dotenv
import discord
from discord.ext import commands

#getters
from duck_news_getter import get_news
from duck_pic_getter import get_link


load_dotenv()

bot = commands.AutoShardedBot(commands.when_mentioned_or('~'))
bot.remove_command("help")



@bot.event
async def on_ready():
    print('Bot ready')
    await bot.change_presence(activity=discord.Game(name="~info for help"))

@bot.command(aliases=['info'])
async def help(ctx):
    await ctx.send("Instructions")

@bot.command()
async def ducknews(ctx):
    news = get_news()
    pic = get_link()


    embed = discord.Embed(
        title = "Duck News!",
        description = news[0], 
        color = discord.Colour.random
    )
    
    embed.add_field(name = 'Link', value = news[1], inline=False)
    embed.set_image(url=pic)

    await bot.say(embed=embed)


bot.run("xrarbwzDt4go4DgmsTn4w7XWc0KdNnwR")