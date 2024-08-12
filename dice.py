from configparser import ConfigParser
from time import sleep
from pyrogram import Client, filters

config=ConfigParser()

config.read('config.ini')

#читаем
api_id = config.get('pyrogram','api_id')
api_hash = config.get('pyrogram','api_hash')

app = Client(name='my_account',api_id=api_id,api_hash=api_hash)

@app.on_message(filters=filters.dice)
def dice(client, message):
    player_1=message
    player_2=app.send_dice(message.chat.id)

    sleep(3.5)
    if player_1.dice.value > player_2.dice.value:
        app.send_message(message.chat.id, 'you win')
    elif player_1.dice.value < player_2.dice.value:
        app.send_message(message.chat.id, 'you dont win')
    else:
        app.send_message(message.chat.id, 'draw')
    print(player_1)
#
app.run()