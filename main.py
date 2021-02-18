import discord
import os

# bobo please help us ;(

client = discord.Client()

@client.event
async def on_ready():
    print('Bobo HIMSELF is among you.\nAVE BOBO OR PERISH'.format(client))
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('with YOUR MOM'))
@client.event
async def on_message(message):
  if (message.author.bot == False):
    if (len(message.content) > 1):
     
      if message.author == client.user:
          return
    
      if ('bobo') in message.content.lower():
          await message.channel.send('WELCOME TO BOBOLAND\nhttps://youtu.be/KCMlSdMjqDQ')
      elif ('drew') in message.content.lower():
          await message.channel.send ('https://preview.redd.it/azltyjsepat01.png?auto=webp&s=b6f14d8165856b2e282ff699d3cc2b191077f941')
      elif ('lepi mica') in message.content.lower():
          await message.channel.send('https://tenor.com/view/lepi-mica-turbofolk-assault-attack-gif-8162881')
      elif ('haraca') in message.content.lower():
          await message.channel.send('https://glowostarnews.com/wp-content/uploads/2020/10/1602678134_maxresdefault.jpg')
      elif ('kiko') in message.content.lower():
          await message.channel.send('https://glowostarnews.com/wp-content/uploads/2020/10/1602678134_maxresdefault.jpg')
      elif 'chicken'in message.content.lower():
          await message.channel.send('EAT SOME BOBO CHICKEN! OOH OOH OOH')
      elif ('stop') in message.content.lower():
          await message.channel.send('Remember: No means yes!')
      elif ('gordian') in message.content.lower():
          await message.channel.send('https://media.discordapp.net/attachments/722208122168410152/811384670737924096/gordian_knot.gif')
      elif ('jersey') in message.content.lower():
          await message.channel.send('https://giphy.com/gifs/rDnondNh8abXqbCTjH')
      elif ('black') in message.content.lower():
          await message.channel.send('https://youtu.be/YN9amfoTdPM')
      elif ('trump') in message.content.lower():
          await message.channel.send('BEST PRESIDENT EVER OOOOH OOH OOOH O')
      elif('srpska') in message.content.lower():
          await message.channel.send('https://media4.giphy.com/media/C4BqyEpolMLpTe4OvP/giphy.gif')
      elif('tsquare') in message.content.lower():
          await message.channel.send('https://tenor.com/view/scaredsim-masato-honda-t-square-ewi-megalith-gif-20222975')
      elif('hindu') in message.content.lower():
          await message.channel.send("https://media2.giphy.com/media/t51EjqRK1Hlje5df5t/giphy.gif")


client.run(os.getenv('TOKEN'))
