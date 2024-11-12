import logging
import asyncio
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import text
from config import *
from keyboards import *
import dbm
from crud_functions import *

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_API)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(f'Добро пожалованть {message.from_user.username} ' + text.start, reply_markup=start_kb)

@dp.message_handler(text='Расчитать')
async def calculate(message: types.Message):
    await message.reply(message.text)


@dp.message_handler(text='Информация')
async def info(message: types.Message):
    await message.answer(text=text.info)


@dp.message_handler(text='Купить')
async def get_buying_list(message: types.Message):
    db_list = dbm.dbOpen()
    it = get_all_products()
    size = len(it)
    for i in range(size):
        with open(it[i][4], 'rb') as img:
            await message.answer_photo(img, f'Название: {it[i][1]} | Описание: {it[i][2]} | Цена: {it[i][3]}')
    await message.answer(text=text.choice, reply_markup=catalog_kb)
    dbm.dbClose(db_list[0])


@dp.callback_query_handler(text='product_buying')
async def answer(call: types.callback_query):
    await  call.message.answer(text=text.answer, reply_markup=buy_kb)
    await call.answer()


# @dp.callback_query_handler(text='checker')
# async def buyCheker(call: types.callback_query):
#     with open('checker.jpg', 'rb') as img:
#         await call.message.answer_photo(img, text.checker_game, reply_markup=buy_kb)
#     await call.answer()
#
#
# @dp.callback_query_handler(text='cards')
# async def buyCards(call):
#     with open('cards.png', 'rb') as img:
#         await call.message.answer_photo(img, text.cards_Lgame, reply_markup=buy_kb)
#     await call.answer()
#
#
# @dp.callback_query_handler(text='other')
# async def buy_other(call: types.callback_query):
#     await call.message.answer(text.other, reply_markup=buy_kb)
#     await call.answer()


@dp.callback_query_handler(text='back_to_catalog')
async def back(call):
    await call.message.answer(text=text.choice, reply_markup=catalog_kb)
    await call.answer()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
