import os

from aiogram import Bot, Dispatcher, types, executor
from asyncio import sleep
from dotenv import load_dotenv
load_dotenv()

bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot)
# Dispatcher. То, что работает с событиями.


@dp.message_handler(commands=['start'])
async def on_message(message: types.Message):
    await bot.send_message(message.from_user.id, f'Привет, { message.from_user.username }. Начинаем игру..')
    await sleep(1)

    await bot.send_message(message.from_user.id, 'Бот кидает кубик')
    bot_data = await bot.send_dice(message.from_user.id)
    bot_data = bot_data['dice']['value']
    await sleep(4)

    await bot.send_message(message.from_user.id, f'{ message.from_user.username } кидает кубик')
    user_data = await bot.send_dice(message.from_user.id)
    user_data = user_data['dice']['value']
    await sleep(4)

    if bot_data > user_data:
        await bot.send_message(message.from_user.id, 'Вы проиграли')
    elif bot_data < user_data:
        await bot.send_message(message.from_user.id, 'Вы победили')
    else:
        await bot.send_message(message.from_user.id, 'Ничья')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    # запускаем бота для ожидания сообщений


