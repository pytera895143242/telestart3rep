import logging
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

TOKEN = '6183811659:AAGZrjHdxAn0uiseHPB4jp82ccy8Yni8Hx0'
memory_storage = MemoryStorage()

bot = Bot(token=TOKEN, parse_mode='html')
dp = Dispatcher(bot,storage=memory_storage)
logging.basicConfig(level=logging.INFO)