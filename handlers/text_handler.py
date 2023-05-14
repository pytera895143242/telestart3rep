from aiogram import types
from misc import dp,bot
import asyncio

ADMIN_ID_1 = 6250893291
ADMIN_ID = [ADMIN_ID_1]

@dp.message_handler(content_types='text')
async def all_other_messages(message: types.message):
    if message.chat.id == ADMIN_ID_1:
        try:
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton(text='Написал в личку', callback_data=f'write_{message.forward_from.id}'))
            markup.add(types.InlineKeyboardButton(text='Совершил покупку', callback_data=f'buy_{message.forward_from.id}'))
            markup.add(types.InlineKeyboardButton(text='Cтатус обычного юзера [0]', callback_data=f'nul_{message.forward_from.id}'))

            await bot.send_message(text = f"Что сделал пользователь?", chat_id=message.chat.id,reply_markup=markup)

        except:
            await message.answer("Возможно пользователь запретил пересылку")
