# Wake on LAN by Discord

import discord
from wakeonlan import send_magic_packet

TOKEN = "ThisIsYourTOKEN"
CHANNEL_ID = 123456789123456789
MAC_ADDRESS = "A0-B1-C2-D3-E4-F5"

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

def Send_Magic_Packet():
    send_magic_packet( MAC_ADDRESS )
    print( "Send a magic packet." )


# 起動時の動作
# @client.event
# async def on_ready():
#     channel = client.get_channel( CHANNEL_ID )
#     await channel.send( "hello" )

# メッセージ受信時のイベント
@client.event
async def on_message(message):
    # テキスト削除アクション
    if message.content == '!cls':
        await message.channel.purge()

    # マジックパケット送信
    if message.content == "!wol":
        Send_Magic_Packet()
        Send_Magic_Packet()
        send_text = "Sent a magic packet."
        await message.channel.send( send_text )



client.run( TOKEN )

