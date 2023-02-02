# 起動確認

import discord
import datetime
import sys
import pytz

TOKEN = "ThisIsYourTOKEN"
CHANNEL_ID = 123456789123456789

client = discord.Client(intents=discord.Intents.default())

def get_boot_time():
    dt_now = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
    show_dt = dt_now.strftime('%Y/%m/%d %H:%M')
    on_ready_text = "【Started】- Your PC Name -  {}".format( show_dt )
    # print( on_ready_text )

    return str( on_ready_text )

# 起動時の動作
@client.event
async def on_ready():
    channel = client.get_channel( CHANNEL_ID )
    await channel.send( get_boot_time() )
    sys.exit()

client.run( TOKEN )

