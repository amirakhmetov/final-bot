from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

kb = InlineKeyboardMarkup()
btn1 = InlineKeyboardButton('Да', callback_data='yes')
btn2 = InlineKeyboardButton('Нет', callback_data='no')
kb.add(btn1, btn2)

kb2 = ReplyKeyboardMarkup(resize_keyboard=True)
btn3 = KeyboardButton('Action')
btn4 = KeyboardButton('MMO')
btn5 = KeyboardButton('RPG')
kb2.add(btn3, btn4, btn5)
