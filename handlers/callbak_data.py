from aiogram import types
from misc import dp, bot
import asyncio
from .sqlit import delit_trafik,update_status,update_activity_status
from .generate_markup import check_subscription,subscription_markup,open_markup

content = -1001987248829


@dp.callback_query_handler(text_startswith='write_')
async def write_watch(call: types.callback_query):
    id = call.data[6:]
    print(update_activity_status(id,1))

    if update_activity_status(id,1) == 1:
        await call.message.answer("Пользователю присвоен статус - Написал сообщение 💬")
    else:
        await call.message.answer("Пользователь не найден в боте. Ошибка")


@dp.callback_query_handler(text_startswith='buy_')
async def buy_watch(call: types.callback_query):
    id = call.data[4:]
    if update_activity_status(id,2) == 1:
        await call.message.answer("Пользователю присвоен статус - Купил курс 💰")
    else:
        await call.message.answer("Пользователь не найден в боте. Ошибка")


@dp.callback_query_handler(text_startswith='nul_')
async def nul_watch(call: types.callback_query):
    id = call.data[4:]
    if update_activity_status(id, 0) == 1:
        await call.message.answer("Пользователю присвоен обычный статус")
    else:
        await call.message.answer("Пользователь не найден в боте. Ошибка")








@dp.callback_query_handler(lambda call: True, state = '*')
async def answer_push_inline_button(call):


    if call.data == 'false':
        await call.message.answer("Неа) Попробуй еще раз")


    if call.data == 'test2':
        update_status(call.message.chat.id, 1)
        await call.message.answer("Правильно! Едем дальше👇🏻")
        await asyncio.sleep(1)
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton(text='Закупаем рекламу', callback_data=f'test3'))
        markup.add(types.InlineKeyboardButton(text='Продаем рекламу', callback_data=f'false'))

        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=31, reply_markup=markup)




    if call.data == 'test3':
        update_status(call.message.chat.id, 2)
        await call.message.answer("Правильно! Едем дальше👇🏻")
        await asyncio.sleep(1)
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton(text='У Евгения отличный канал!', callback_data=f'false'))
        markup.add(types.InlineKeyboardButton(text='Евгений - Мудила', callback_data=f'test4'))

        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=32, reply_markup=markup)


    if call.data == 'test4':
        update_status(call.message.chat.id, 3)
        await call.message.answer("Абсолютно верно!")
        await asyncio.sleep(1)
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton(text='Забрать подарок 🎁', url = 'https://t.me/SteveDuck2'))
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=34, reply_markup=markup)
