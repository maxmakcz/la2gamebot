from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

TOKEN = '5676141426:AAF3ewoXeatoRPZKb3IAjDNnn0IFU8u4-Po'
bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot,storage=storage)
DB_URI = "postgres://fosywprygboprb:3392909af75df4902b2a368f3bb557d754528af49b4227fde388ffe71009b0aa@ec2-54-76-43-89.eu-west-1.compute.amazonaws.com:5432/d7ok62das6ks8g"