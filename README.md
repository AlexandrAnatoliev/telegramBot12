# telegramBot11

[Ru] Бот обрабатывает команды /start и /help, команду /description (выводит описание бота), команду /count (выводит
число собственных предыдущих вызовов). Бот отвечает на сообщение пользователя рандомным символом алфавита. Бот отвечает
YES, если сообщение содержит число 0 и NO - в противном случае

Взят https://www.youtube.com/watch?v=VWjCv_IDuyQ&list=PLe-iIMbo5JOJm6DRTjhleHojroS-Bbocr&index=4

## Замечания:

* message.reply - ответить на сообщение. Выводится в чате вопрос и ответ на него
* message.answer - послать сообщение. Вопрос не дублируется.
* message.delete - удалить сообщение пользователя из чата
* Хендлеры типа @dp.message_handler() должны ставиться ПОСЛЕ хендлеров типа @dp.message_handler(commands='count'), т.к
  они срабатывают при любой команде

## Требования:

* $ pip install -r requirements.txt
* создать файл config.py, в котором будут храниться токен для доступа к боту в виде

```python 
TOKEN_API = "1234567890:ASDFGHH..."
```

## Где взять token?

* https://xakep.ru/2021/11/28/python-telegram-bots/

## Примеры использования

#### ПРАКТИКА:

* Напишите бота, который будет отвечать на сообщение пользователя рандомным символом алфавита.
* Модифицируйте бота, добавив функцию обработки команды /description, которая будет выводить описание бот.
* Добавить в бот команду /count, которая будет выводить число собственных предыдущих вызовов.
* Сделайте так, чтобы бот отвечал YES, если сообщение содержит число 0 и NO - в противном случае

#### Добавляем библиотеки

```python
import random
from aiogram import Bot, Dispatcher, types, executor
from config import TOKEN_API
```

#### Создаем экземпляр класса Bot

```python
bot = Bot(TOKEN_API)
```

#### Создаем экземпляр класса Dispatcher

```python
dp = Dispatcher(bot)
```

#### Запуск бота

```python
if __name__ == '__main__':
    executor.start_polling(dp)
```

#### Обрабатываем входящие сообщения, срабатывает на команды /start, /help, /description, /count

```python
@dp.message_handler(commands='help')
async def command(message: types.Message):
    await message.reply(text=HELP_COMMAND)
```

#### Входящие сообщения без команд обрабатывает согласно включеной логике

```python
@dp.message_handler()  # обрабатываем входящие сообщения
async def command(message: types.Message):  # объект message класса message
    """
    Бот отвечает на сообщение пользователя рандомным символом алфавита
    :param message: сообщение
    :return: случайная буква из текстового сообщения
    """
    answ = message.text  # сообщение пользователя
    await message.reply(random.choice(answ))  # случайная буква из текстового сообщения


# @dp.message_handler()  # обрабатываем входящие сообщения
async def command(message: types.Message):  # объект message класса message
    """
    Бот отвечает YES, если сообщение содержит число 0 и NO - в противном случае
    :param message: сообщение
    :return: текст YES или NO
    """
    answ = 'NO'  # сообщение пользователя
    if '0' in message.text:
        answ = 'YES'
    await message.answer(answ)  # случайная буква из текстового сообщения
```