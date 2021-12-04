
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
                webhook = DiscordWebhook(url='https://discord.com/api/webhooks/916496092064010270/hzklfBh8Q4l89jAzZ5pvaYVaSYbW3J569OUahTi2x2rijG6FDeYCUkSKxQGuLrSrFamH')
                embed = DiscordEmbed(title='', description= 'Name - ' + str(nft_data['results']['title']) + '\nAmount - ' + str(sale_price) + ' SOL\n', color=00000)
                embed.set_image(url=nft_data['results']['img'])
                embed.set_timestamp()

                embed.set_author(name='SolBot Sales')
                if str('solanart') in str(source):
                    embed.set_footer(text='Sale on Solanart', icon_url='https://cdn.discordapp.com/attachments/902716564963467326/902944236050214952/logoonly.png%27')
                if str('magiceden') in str(source):
                    embed.set_footer(text='Sale on Magic Eden', icon_url='https://i.postimg.cc/j2TbqJ3x/favicon.png')
                if str('digitaleyes') in str(source):
                    embed.set_footer(text='Sale on Digital Eyes', icon_url='https://pbs.twimg.com/profile_images/1430306224713740292/q4termyJ.jpg%27')
                if str('alphaart') in str(source):
                    embed.set_footer(text='Sale on Alpha Art', icon_url='https://pbs.twimg.com/profile_images/1446936065051353094/WHXnvPkd_400x400.jpg%27')
                if str('ftx') in str(source):
                    embed.set_footer(text='Sale on FTX US', icon_url='https://cdn.discordapp.com/attachments/902716564963467326/903722456181784596/ftx-logo.png%27')
                webhook.add_embed(embed)
                webhook.execute()
                break
sales()