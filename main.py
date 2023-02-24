# telegramBot12

# Бот на aiogram
# Использование функции on_startup, параметра parse_mode="HTML", отправка emoji и stickers
# При включении бота выполняется функция on_startup
# По команде /start бот пишет сообщение жирным курсивом
# По команде /give бот посылает сообщение и стикер в чат, удаляет сообщение пользователя.
# Бот отвечает на сообщение пользователя его же сообщением, добавляя к нему emoji 🤪. На '❤️' отвечает '🖤'
# Бот подсчитывает количество ✅ в сообщении пользователя и отправляет их количество
# Бот отправляет ID стикера в ответ пользователю
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
# @dp.message_handler(content_types=['sticker']) тип входящего контента в хендлер - стикер
# await message.answer(message.sticker.file_id)  # посылаем id стикера

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

HELP_COMMAND = """
<b>/help</b> - <em>список команд</em>
<b>/start</b> - <em>начать работу с ботом</em>
<b>/give</b> - <em>посылает сообщение и стикер в чат, удаляет сообщение пользователя</em>
"""
# <em> курсив </em>
# <b> жирный шрифт </b>

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


async def on_startup(_):  # функция принимает (_) аргумент!
    """Выполняется при включении бота"""
    print("Я запустился!")


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


@dp.message_handler(content_types=['sticker'])  # тип контента - стикер
async def get_sticker_id(message: types.Message):
    """Бот отправляет ID стикера в ответ пользователю"""
    await message.answer(f"ID этого стикера: {message.sticker.file_id}")  # посылаем id стикера


@dp.message_handler(commands=['give'])
async def give_command(message: types.Message):
    """
    По команде /give посылает сообщение и стикер в чат, удаляет сообщение пользователя
    :param message: /give
    :return: сообщение и sticker
    """
    await bot.send_message(message.from_user.id, text="Смотри какой смешной кот ❤️")
    await bot.send_sticker(message.from_user.id,
                           sticker="CAACAgIAAxkBAAEH305j97F6tGFBLsiXYpArYZ88f6d8wAACUwADrWW8FKPXOfaLMFQULgQ")
    # sticker_id берем у бота "get sticker id" (@idstickerbot)
    await message.delete()


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    """
    Возвращает список существующих команд, текст отформатирован т.о,
    чтобы имена команд были жирным шрифтом, а описание - курсивом.
    :param message: /help
    :return: список существующих команд
    """
    await message.reply(text=HELP_COMMAND, parse_mode="HTML")


@dp.message_handler()
async def send_emoji(message: types.Message):
    """
    Отвечает на сообщение пользователя его же сообщением, добавляя к нему emoji 🤪
    На '❤️' отвечает '🖤'
    Подсчитывает количество ✅ в сообщении пользователя и отправляет их количество
    :param message: сообщение пользователя
    :return: сообщение пользователя + 🤪
    """
    if message.text == '❤️':
        return await message.reply('🖤')
    count = 0
    if '✅' in message.text:
        count = message.text.count('✅')
        return await message.answer(f"В Вашем тексте {count}  ✅")
    await message.reply(message.text + '🤪')  # emoji 🤪 просто копируем из телеграмм


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup)
    # прописываем аргумент on_startup=on_startup, чтобы функция on_startup(_) выполнялась при включении бота
