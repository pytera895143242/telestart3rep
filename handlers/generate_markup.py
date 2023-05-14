from aiogram import types
from .sqlit import update_status,get_channel_info
from aiogram import types
from misc import dp,bot


def subscription_markup():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text='Проверить подписку', callback_data=f'call_check'))
    return markup


async def check_subscription(user_id):

    proverka = (await bot.get_chat_member(chat_id= -1001741398265, user_id=user_id)).status
    if proverka == 'member' or proverka == 'administrator' or proverka == 'creator':
        update_status(user_id,1)
        return True
    else:
        return False

def open_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1_1 = types.KeyboardButton('Поиск фильмов 🔎')
    button_1_2 = types.KeyboardButton('Фильм из ТикТок 🎬')
    button_2_1 = types.KeyboardButton('Новинки 🎊')
    button_2_2 = types.KeyboardButton('Избранное ❤️')
    button_3 = types.KeyboardButton('Информация ⚙️')
    button_4 = types.KeyboardButton('FAQ ?')

    markup.add(button_1_1,button_1_2)
    markup.add(button_2_1,button_2_2)
    markup.add(button_3)
    markup.add(button_4)

    return markup