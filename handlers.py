from aiogram import F
from aiogram.types import Message
from bot import dp, bot


@dp.message(F.text == "/start")
async def start_cmd(message: Message):
    await message.answer("Бизнес-бот активен. Напиши !hi в ЛС, чтобы получить приветствие.")


@dp.message(F.text == "!hi")
async def hi_cmd(message: Message):
    if message.chat.type == "private":
        await message.answer("Привет! 👋 Это бизнес-бот. Вы успешно подключены.")
    else:
        await message.reply("Команда работает только в личке!")
