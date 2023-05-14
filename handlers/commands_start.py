from aiogram import types
from misc import dp,bot
from .sqlit import reg_user
from .generate_markup import subscription_markup,check_subscription

content = -1001987248829

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    if len(message.text) == 6:
        reg_user(message.chat.id,'default')
    else:
        reg_user(message.chat.id,(message.text[7:]))

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text='Оформление + посты', callback_data=f'test2'))
    markup.add(types.InlineKeyboardButton(text='Закупаем рекламу', callback_data=f'false'))
    markup.add(types.InlineKeyboardButton(text='Продаем рекламу', callback_data=f'false'))

    await bot.copy_message(from_chat_id=content,chat_id=message.chat.id,message_id=27,reply_markup=markup)