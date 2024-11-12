from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

kb1 = KeyboardButton(text='Расчитать')
kb2 = KeyboardButton(text='Информация')
kb3 = KeyboardButton(text='Купить')

start_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(kb1, kb2, kb3)

in_kb1 = InlineKeyboardButton(text='Product1', callback_data='product_buying')
in_kb2 = InlineKeyboardButton(text='Product2', callback_data='product_buying')
in_kb3 = InlineKeyboardButton(text='Product3', callback_data='product_buying')
in_kb4 = InlineKeyboardButton(text='Product4', callback_data='product_buying')

catalog_kb = InlineKeyboardMarkup(row_width=4).add(in_kb1,in_kb2,in_kb3,in_kb4)


buy_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Назад', callback_data='back_to_catalog')],
    ]
)
