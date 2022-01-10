import discord
import random
from dotenv import dotenv_values

config = dotenv_values(".env")
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return

    if message.channel.name == 'python-bot':
        if user_message.lower() == 'hello':
            await message.channel.send(f'Hello {username}!')
            return
        elif user_message.lower() == 'bye':
            await message.channel.send(f'See you later {username}!')
            return
        elif user_message.lower() == '!random':
            response = f'This is your random number: {random.randrange(10000)}'
            await message.channel.send(response)
            return
    
    if user_message.lower() == '!anywhere':
        await message.channel.send('This can be used anywhere!')
        return

    if user_message.lower() == '!8ball':
        random_responses = ['As I see it, yes.', 'Ask again later.', 'Better not tell you now.', 'Cannot predict now.', 'Concentrate and ask again.',                         'Don’t count on it.', 'It is certain.', 'It is decidedly so.', 'Most likely.', 'My reply is no.', 'My sources say no.',                      'Outlook not so good.', 'Outlook good.', 'Reply hazy, try again.', 'Signs point to yes.', 'Very doubtful.', 'Without a doubt.',                     'Yes.', 'Yes – definitely.', 'You may rely on it.']
        random_response = random.choice(random_responses)

        await message.channel.send(f'This is your 8ball response: {random_response}')
        return

client.run(config["TOKEN"])