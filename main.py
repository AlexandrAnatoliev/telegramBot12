# telegramBot12

# Использование функции on_startup, параметра parse_mode="HTML", отправка emoji и stickers
# При включении бота выполняется функция on_startup
# По команде /start бот пишет сообщение жирным курсивом
# По команде /give бот посылает стикер в чат, удаляет сообщение пользователя.
# Бот отвечает на сообщение пользователя его же сообщением, добавляя к нему emoji 🤪
#
# https://www.youtube.com/watch?v=lbLzGfshtaY&list=PLe-iIMbo5JOJm6DRTjhleHojroS-Bbocr&index=6

# ЗАМЕЧАНИЯ:
# Параметр parse_mode="HTML" определяет метод чтения сообщения, в данном случае - как HTML-сообщение
# <em> курсив </em>
# <b> жирный шрифт </b>
# В executor.start_polling(dp, on_startup=on_startup), прописываем аргумент on_startup=on_startup,
# чтобы функция on_startup(_) выполнялась при включении бота
# Функция on_startup(_) принимает '_' аргумент!
# sticker_id берем у бота "get sticker id" (@idstickerbot)
# emoji 🤪 просто копируем из телеграмм

# ПРАКТИКА:
# Реализуйте бота, который будет отправлять стикер с котиком в ответ на команду /give.
# Но перед отправкой стикера отправьте сообщение "Смотри какой смешной кот ❤️"
# Модифицируйте бота, добавив возможность отправлять обычное сердечко, а в ответ получать черное.
# Реализуйте бота, который будет подсчитывать количество ✅ в сообщении пользователя и отправлять их количество.
# Напишите функцию /help, которая будет возвращать список существующих команд, отформатируйте текст т.о,
# чтобы имена команд были жирным шрифтом, а описание - курсивом.
# Напишите функцию on_startup(), которая будет выводить в терминал "Я запустился!"
# Напишите бота, который будет отправлять ID стикера в ответ пользователю

from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


async def on_startup(_):  # функция принимает (_) аргумент!
    """Выполняется при включении бота"""
    print("Бот успешно запущен")


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    """
    По команде /start пишет приветственное сообщение в чат
    :param message: /start
    :return: сообщение в чат
    """
    await message.answer("<em>Добро <b>пожаловать</b> в наш бот</em>", parse_mode="HTML")
    # параметр parse_mode="HTML" определяет метод чтения сообщения, в данном случае - как HTML-сообщение
    # <em> курсив </em>
    # <b> жирный шрифт </b>


@dp.message_handler(commands=['give'])
async def give_command(message: types.Message):
    """
    По команде /give посылает стикер в чат, удаляет сообщение пользователя
    :param message: /give
    :return: sticker
    """
    await bot.send_sticker(message.from_user.id,
                           sticker="CAACAgIAAxkBAAEH3t5j95ShMzv012IKJIc2ojsFtZBmAgACHhQAAqkCuUqNRYHXFO-0Oi4E")
    # sticker_id берем у бота "get sticker id" (@idstickerbot)
    await message.delete()


@dp.message_handler()
async def send_emoji(message: types.Message):
    """
    Отвечает на сообщение пользователя его же сообщением, добавляя к нему emoji 🤪
    :param message: сообщение пользователя
    :return: сообщение пользователя + 🤪
    """
    await message.reply(message.text + '🤪')  # emoji 🤪 просто копируем из телеграмм


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup)
    # прописываем аргумент on_startup=on_startup, чтобы функция on_startup(_) выполнялась при включении бота
