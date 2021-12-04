
# discord bot token


###

import requests
import json
from decimal import Decimal
import discord
import time
import tweepy
import urllib.request
import random
import os
import threading
from json.decoder import JSONDecodeError
from discord_webhook import DiscordWebhook, DiscordEmbed
# discord bot token

print("test")
test = ""




def sales():
    url = 'https://api-mainnet.magiceden.io/rpc/getGlobalActivitiesByQuery?q=%7B%22%24match%22%3A%7B%22collection_symbol%22%3A%22solbots%22%7D%2C%22%24sort%22%3A%7B%22blockTime%22%3A-1%7D%2C%22%24skip%22%3A0%7D'
    while True:
        time.sleep(1)
        try:
            data = json.loads(requests.get(url).text)
        except JSONDecodeError:
            threading.Thread(target=sales).start()
            break
        for i in range(100000):
            if str('exchange') in str(data['results'][i]):
                f = open('solbots.txt').read()
                if str(data['results'][i]) != str(f):
                    open('solbots.txt', 'w').write(str(data['results'][i]))
                    print('Sale Found! Sending Info!')
                else:
                    print('No Sales Found')
                    break
                sale = data['results'][i]
                mint = sale['mint']
                nft_data = json.loads(requests.get('https://api-mainnet.magiceden.io/rpc/getNFTByMintAddress/' + mint).text)
                sale_price = str(sale['parsedTransaction']['total_amount']/1000000000)
                source =  sale['source']
                webhook = DiscordWebhook(url='https://discord.com/api/webhooks/916511511030136943/VjICxP0xXV7WlhNas92fSEDsOFFik3xWG4JRnMEZcibWoLa_Kf-jDIDoUK6da4r9lpPs')
                embed = DiscordEmbed(title='', description= 'Name - ' + str(nft_data['results']['title']) + '\nAmount - ' + str(sale_price) + ' SOL\n', color=00000)
                embed.set_image(url=nft_data['results']['img'])
                embed.set_timestamp()

                embed.set_author(name='SolBot Sales')
                if str('magiceden') in str(source):
                    embed.set_footer(text='Sale on Magic Eden', icon_url='https://i.postimg.cc/j2TbqJ3x/favicon.png')
                webhook.add_embed(embed)
                webhook.execute()
                break
sales()