# This example requires the 'message_content' intent.

import discord
import re
from urllib.parse import urlparse
from urlextract import URLExtract


extractor = URLExtract()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    # Ignore messages from ourselves
    if message.author == client.user:
        return

    for link in extractor.gen_urls(message.content):
        # Skip it if embed disabled
        link_idx = message.content.index(link)
        if link_idx > 0:
            if (message.content[link_idx - 1] == "<") and (message.content[link_idx + len(link)] == ">"):
                continue

        parsed = urlparse(link)

        if parsed.netloc in ["www.tiktok.com"]:
            await message.channel.send(parsed._replace(netloc="vxtiktok.com").geturl(), reference=message)
        elif parsed.netloc in ["x.com", "twitter.com"]:
            await message.channel.send(parsed._replace(netloc="fxtwitter.com").geturl(), reference=message)

    # Remove link embed from user
    await message.edit(suppress=True)


client.run("***REMOVED***")
