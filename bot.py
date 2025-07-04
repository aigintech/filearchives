import logging
import asyncio
from aiogram import F
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.storage.memory import MemoryStorage


main_token = "7549350686:AAFiK1EeYXVLbyzrUC9xP5tr-x30UQCmwlg"

logging.basicConfig(level=logging.INFO)

bot = Bot(main_token)
dispatcher = Dispatcher(storage=MemoryStorage())

@dispatcher.message(Command('start'))
async def start_handler(message: Message):
    await message.answer("Welcome choose the sport: ")

@dispatcher.message()
async def echo_handler(message: Message):
    await message.answer(message.text)

async def main():
    print("This is sports archives. you can choose the sport and search for the matches in archive!")
    await dispatcher.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())