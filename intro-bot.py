import discord
from discord.ext import commands
import asyncio

desc = 'A bot to test some commands'

bot = commands.Bot(command_prefix='$', description=desc)

default_role = ''

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.send_message(ctx.message.channel, 'Pong!')

@bot.event
async def on_member_join(member):
    global default_role
    print('New user joined')
    await bot.add_roles(member, default_role)

@bot.command(pass_context=True)
async def setdefaultrole(ctx, def_role: discord.Role):
    global default_role
    roles = ctx.message.server.roles
    print('Role name given: ' + def_role.name)
    for role in roles:
        print(role.name)
        if def_role == role:
            default_role = role
            await bot.say('Default role set to ' + default_role.mention)
            print('Role set')
            break
    if default_role == '':
        await bot.say('No role named ' + def_role.name + ' found')
    print('Loop exit')

@bot.event
async def on_voice_state_update(before, after):
    if before.voice.voice_channel is not None:
        if after.voice.voice_channel is None:
            await bot.send_message(bot.get_channel('340994800595763200'), after.name + ' left channel ' + before.voice.voice_channel.name)

bot.run('MzQxMjg3NDQ3Njc1NTM1MzYx.DF-8sw.9dDv-6vqTKvJ07gUNE_TdtOtEkU')