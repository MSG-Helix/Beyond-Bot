# Beyond-Bot by R3A2

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import time
import os

Client = discord.Client()
bot = commands.Bot(command_prefix='#')

@bot.event
async def on_ready():
    print ("Ready when you are XD")
    print ("I am running on " + bot.user.name)
    print ("With the ID: " + bot.user.id)

@bot.command(pass_context=True)
async def Ping(ctx):
    await bot.say(":ping_pong: Pong!!")
    print ("user has pinged.")

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say(":ping_pong: Pong!!")
    print ("user has pinged.")

@bot.command(pass_context=True)
async def Pong(ctx):
    await bot.say(":ping_pong: Ping!!")
    print ("user has ponged.")

@bot.command(pass_context=True)
async def pong(ctx):
    await bot.say(":ping_pong: Ping!!")
    print ("user has ponged.")

@bot.command(pass_context=True)
async def Info(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color=0xFFFB00)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color=0xFFFB00)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
@commands.has_role("OFFICIALS")
async def Kick(ctx, user: discord.Member):
    await bot.say("I do apollogize, its just orders {}.".format(user.name))
    await bot.kick(user)

@bot.command(pass_context=True)
@commands.has_role("OFFICIALS")
async def kick(ctx, user: discord.Member):
    await bot.say("I do apollogize, its just orders {}.".format(user.name))
    await bot.kick(user)

@bot.command(pass_context=True)
@commands.has_role("OFFICIALS")
async def Ban(ctx, user: discord.Member):
    await bot.say("Sorry but you have been let go {}.".format(user.name))
    await bot.ban(user)

@bot.command(pass_context=True)
@commands.has_role("OFFICIALS")
async def ban(ctx, user: discord.Member):
    await bot.say("Sorry but you have been let go {}.".format(user.name))
    await bot.ban(user)

@bot.command(pass_context=True)
@commands.has_role("OFFICIALS")
async def Unban(ctx, user: discord.Member):
    await bot.say("Welcome back {}!".format(user.name))
    await bot.unban

@bot.command(pass_context=True)
@commands.has_role("OFFICIALS")
async def unban(ctx, user: discord.Member):
    await bot.say("Welcome back {}!".format(user.name))
    await bot.unban

@bot.command(pass_context=True)
async def GO_BEYOND(ctx):
    await bot.say("**PLUS ULTRA!!!**")
    print ("GO BEYOND, PLUS ULTRA!!!")

@bot.command(pass_context=True)
async def News(ctx):
    embed = discord.Embed(title="Holy Mantra", description=" One of the main things I do for the game is create original characters for the Story Mode, and write those characters stories. I have been working with a few artists in the Helping Hand to draw these characters, and give them more life. So, thanks to @ILOforma, I can show sketches she has made for one of my pro heroes. A Buddhist monk living in peace with his mind; kind and gentle, yet hard as steel when called for. Here is the Enlightened Hero; Holy Mantra.", color=0x00ff00)
    embed.set_footer(text="By Loki")
    embed.set_author(name="New Character")
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(name="{}'s info".format(ctx.message.server.name), description="Here's what I could find.", color=0x00ff00)
    embed.set_author(name="Server information")
    embed.add_field(name="Name", value=ctx.message.server.name, inline=True)
    embed.add_field(name="ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Roles", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Members", value=len(ctx.message.server.members))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def Serverinfo(ctx):
    embed = discord.Embed(name="{}'s info".format(ctx.message.server.name), description="Here's what I could find.", color=0x00ff00)
    embed.set_author(name="Server information")
    embed.add_field(name="Name", value=ctx.message.server.name, inline=True)
    embed.add_field(name="ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Roles", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Members", value=len(ctx.message.server.members))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def ServerInfo(ctx):
    embed = discord.Embed(name="{}'s info".format(ctx.message.server.name), description="Here's what I could find.", color=0x00ff00)
    embed.set_author(name="Server information")
    embed.add_field(name="Name", value=ctx.message.server.name, inline=True)
    embed.add_field(name="ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Roles", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Members", value=len(ctx.message.server.members))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=embed)


bot.run(os.getenv('TOKEN'))
