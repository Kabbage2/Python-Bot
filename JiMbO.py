import discord
import config

intents = discord.Intents.default()
intents.members=True
client = discord.Client(intents = intents)



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


@client.event
async def on_member_join(member):
    channel = discord.utils.get(client.get_all_channels(),id = config.channelid)
    await channel.send(content = f"Welcome {member.mention}!")
    

client.run(config.TOKEN)