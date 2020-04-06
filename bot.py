# bot.py
import discord
import os
token = "Njk0MjQ2NDg2NzYxNzk5Nzky.XoI1cw.MpLeSVe0HuMz-oTjnpEe2QcHi_A"
client = discord.Client()

@client.event
async def on_ready():
    activity = discord.Activity(type=discord.ActivityType.watching, name="skaerf™")
    await client.change_presence(status=discord.Status.do_not_disturb, activity=activity)
    print(f'[skaerf™] skaerfbot is active, linked to bot user {client.user}, author is Lawrence H. Have a good day!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.content == "=faq":
        faqfile = open("text files\\faq.txt")
        faq = faqfile.read()
        await message.channel.send(faq)
    elif message.content == "=about":
        await message.channel.send("skaerfbot developed by Lawrence H.`\nAll plugins seen here are custom, programmed by skaerf#6400\nIf you need support, go to <#693527385819316335> or make a ticket in <#694230953698263131>")
    elif message.content == "=plugins":
        pluginsfile = open("text files\\plugins.txt")
        plugins = pluginsfile.read()
        await message.channel.send(plugins)
    elif message.content == "help":
        await message.channel.send("Please check the FAQ with `=faq` to check if your question has already been answered!\nIf not, please paste your console error on https://hastebin.com and ping skaerf or an online helper for them to look at it!")

@client.event
async def on_member_join(member):
    welcome = client.get_channel("<#693527110672711762>")
    boiThatJoined = member.id
    await welcome.send("Welcome "+boiThatJoined+"to skaerf™'s server! If you need help with a plugin, please go to <#693527385819316335>!")
client.run(token)