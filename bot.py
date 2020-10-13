from aiogram import Bot, Dispatcher, executor, try:

from config import BOT_TOKEN

bot = Bot (token=BOT_TOKEN)
dp = Dispatcher (bot)

@dp.massage_handler (commands=('start'))
async def start_cmd (massege: types.Massage):
    await massage.reply ('привет то то тото')
dp.massage_handler ()
async def start_cmd (massege: types.Massage):  
    await massage.reply (massage.text)

if __name__ == '__main__':
    executor.start_pollng (dp, skip_updates=True)