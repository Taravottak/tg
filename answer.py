from configparser import ConfigParser
from asyncio import sleep
import pathlib
from pyrogram import Client, filters
import aiofiles
config=ConfigParser()

config.read('config.ini')

#читаем
api_id = config.get('pyrogram','api_id')
api_hash = config.get('pyrogram','api_hash')

#создание файла юзерс если его нет
pathlib.Path('users.txt').touch(exist_ok=True)

text='привет'

app = Client(name='my_account',api_id=api_id,api_hash=api_hash)

@app.on_message(filters=filters.private)
async def auto_answer(event, message): 
    #получение всех пользователей из файла users.txt
    #получение именно тех с кем было взаимодействие
    async with aiofiles.open(file='users.txt', mode='r', encoding='utf-8') as file:
        users = (await file.read()).split('\n')
    #если пользователя нет в чатах
    if str(message.chat.id) not in users:
        async with aiofiles.open(file='users.txt',mode='a+', encoding='utf-8') as file:
            #запись айди пользователя в файл
            await file.write(f'{message.chat.id}\n')
            if message.from_user.id == (await app.get_me()).id:
                pass
            else:
                #отправка сообщения пользователю
                await app.send_message(chat_id=message.chat.id, text=text)
    
#
app.run()