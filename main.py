import discord
from discord.ext import commands
import os
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

items = {
    'бумага': '2-5 месяцев',
    'кожура': '2-5 недель',
    'бутылка': '400 лет'
}

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def decomposition(ctx, item):
    if item in items:
        time_to_decompose = items[item]
        await ctx.send(f'Предмет {item} разлагается примерно {time_to_decompose}')
    else:
        await ctx.send('Про такой предмет еще нет информации')

@bot.command()
async def sort(ctx, item):
    if item == 'батарейки':
        await ctx.send('отдать на переработку')
    elif item == 'стекло':
        await ctx.send('отдать на переработку, можно выбросить в специальную урну')
    else:
        await ctx.send('пока неизвестно, что делать с этим предметом')

bot.run('MTEzMjI3NzgxNDMyMjc5NDYwNw.Gyrs1z.Qj_hwFBwB9WQ3XMeF5bJIhKzZsY-YKrBgEUk-g')