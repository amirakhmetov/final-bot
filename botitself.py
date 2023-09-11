import logging
from aiogram.types import ReplyKeyboardRemove
from aiogram import Bot, types, Dispatcher, executor
from finalbot.keyboards import kb, kb2
from games import ACTION, MMO, RPG
from shipping import PICKUP_FAST_SHIPPING, POST_FAST_SHIPPING, POST_REGULAR_SHIPPING

Token = '6074717490:AAEwQ9gvMjnlh3qMZGB08FwTOymayIKNfbc'
bot = Bot(token=Token)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer(f'Привет, {message.from_user.first_name}!\nЭто бот, который позволяет тебе купить игры\nХочешь ли ты купить одну из игр?', reply_markup=kb)

@dp.callback_query_handler(text='no')
async def yes(callback:types.CallbackQuery):
    await bot.send_message(callback.from_user.id, 'Ок, хорошего дня!')

@dp.callback_query_handler(text='yes')
async def yes(callback:types.CallbackQuery):
    await bot.send_message(callback.from_user.id, 'Какой жанр игры вы предпочитаете?', reply_markup=kb2)

@dp.message_handler(text='Action')
async def action(message:types.Message):
    await message.answer('Вуаля',reply_markup=ReplyKeyboardRemove())
    await bot.send_invoice(message.from_user.id, **ACTION.generate_invoices(), payload=123)

@dp.message_handler(text='MMO')
async def action(message:types.Message):
    await message.answer('Вуаля', reply_markup=ReplyKeyboardRemove())
    await bot.send_invoice(message.from_user.id, **MMO.generate_invoices(), payload=456)

@dp.message_handler(text='RPG')
async def action(message:types.Message):
    await message.answer('Вуаля', reply_markup=ReplyKeyboardRemove())
    await bot.send_invoice(message.from_user.id, **RPG.generate_invoices(), payload=789)


@dp.shipping_query_handler()
async def chose_shipping(query:types.ShippingQuery):
    if query.shipping_address.country_code == 'RU':
        await bot.answer_shipping_query(shipping_query_id=query.id,shipping_options=[
            POST_REGULAR_SHIPPING, POST_FAST_SHIPPING, PICKUP_FAST_SHIPPING], ok=True)
    else:
        await bot.answer_shipping_query(shipping_query_id=query.id, ok=False, error_message='Сюда не доставляем')


@dp.pre_checkout_query_handler()
async def proccess_pre_checkout_query(query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query_id=query.id, ok=True)
    await bot.send_message(chat_id=query.from_user.id, text='Спасибо за покупку')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)