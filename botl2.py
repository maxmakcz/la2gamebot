from aiogram import Bot, types, filters
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
from keyboards import shop, dion, rb, skill, buff,giran1,loc,sell,tochka,rbfight,aden,rbfight2,quest
from aiogram.types import ReplyKeyboardRemove
import asyncio
import os, json, string
import aiogram.utils.markdown as fmt
import sqlite3 as sq
import random
import hashlib
import emoji
import logging
from skilsss import *
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.dispatcher import DEFAULT_RATE_LIMIT
from aiogram.dispatcher.handler import CancelHandler, current_handler
from aiogram.utils.exceptions import Throttled
from aiogram.utils.executor import start_polling
from typing import Union
from lock import giran,Aden
from lock import craft_s
from lock import Rb,Rb2
from aiogram.utils.executor import start_webhook
import psycopg2

giran.register_giran(dp)
craft_s.register_craft(dp)
Rb.register_rb(dp)
Aden.register_aden(dp)
Rb.register_rb(dp)

HEROKU_APP_NAME = os.getenv('HEROKU_APP_NAME')

# webhook settings
WEBHOOK_HOST = f'https://{HEROKU_APP_NAME}.herokuapp.com'
WEBHOOK_PATH = f'/webhook/{TOKEN}'
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'

# webserver settings
WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = os.getenv('PORT', default=8000)
async def on_startup(dispatcher):
    await bot.set_webhook(WEBHOOK_URL, drop_pending_updates=True)
async def on_shutdown(dispatcher):
    await bot.delete_webhook()

con = psycopg2.connect(DB_URI, sslmode = "require")
cur = con.cursor()
@dp.message_handler(commands=['start'])
@dp.throttled(rate=1)
async def start(message: types.Message):
    user_id = message.from_user.id
    nick = message.from_user.username
    df = "Demon Fang(D) +"
    bs = "Brigandine Set(D) +"
    rec = "0"
    rec2 = "0"
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is None:
        await message.answer('Вы зарегистрированы')
        cur.execute(f'INSERT INTO players(id ,nick , zat ,Krit ,def  ,atk  ,atkxp ,hp  ,hpxp  ,'
                    f'xp  ,RB1  ,RB2  ,RB3  , tochkab , tochkam , tochkar , minirb  , mob1 ,mob2  , mob3 , minirb2 , Weapon , dion ,'
                    f' giran , aden ,mob4 , mob5, mob6 , minirb3 , mob7 , mob8 , mob9 ,mob10 , armor , gold , defxp ,'
                    f' maxhp , zat2 ,profa ,buff ,srec , Varnish ,rbfight ,mp ,maxmp ,hpbanka ,mpbanka ,mob11 ,mob12 ,dinoq ,'
                    f' nosq ,aliq ,bufq ,lionq ,bearq ,mobr ,mobra)  VALUES (%s,%s,0,1,1,5,0,140,0,0,10000,'
                          f'50000,150000,0,0,0,0,600,2200,12000,200000,'
                          f'%s,0,0,0,2000,3600,5000,400000,6400,10000,11000,13000,'
                          f'%s,0,0,100,0,%s,0,%s,16000,16000,0,0,0,0,0,0,0,0,0,0,0,0,0,0)',(user_id,nick,df,bs,rec,rec2))
        con.commit()
    else:
        await message.answer('Вы уже зарегистрированы')
@dp.message_handler(commands=['buff'])
@dp.throttled(rate=1)
async def buffskil(message: types.Message):
  await message.answer(('<b>ВСЕ БАФЫ ДЕЙСТВУЮТ 5 МИНУТ \nМАКСИМАЛЬНОЕ КОЛЛИЧЕСТОВ: 3</b>'),parse_mode="html", reply_markup = buff)
@dp.message_handler(commands=['shop'])
@dp.throttled(rate=1)
async def shop_pux(message: types.Message):
  await message.answer(('Добро пожаловать в магазин! У нас лучшие цены!'), reply_markup = shop)
@dp.message_handler(commands=['loc'])
@dp.throttled(rate=1)
async def shop_pux(message: types.Message):
  await message.answer(("Выбери куда пойти"), reply_markup = loc)
@dp.message_handler(Text(equals='\U0001F519  Назад'))
@dp.throttled(rate=1)
async def shop_pux(message: types.Message):
  await message.answer(("Ты вернулся обратно"), reply_markup = loc)
@dp.message_handler(Text(equals='\U0001F3E1Town of Dion\U0001F3E1'))
@dp.throttled(rate=1)
async def shop_pux(message: types.Message):
  await message.answer(("Ты Атакуешь"), reply_markup = dion)
@dp.message_handler(Text(equals='\U0001F54DTown of Giran\U0001F54D'))
@dp.throttled(rate=1)
async def giran2(message: types.Message):
  await message.answer(("Ты Атакуешь"), reply_markup = giran1)
@dp.message_handler(Text(equals='\U0001F3F0Town of Aden\U0001F3F0'))
@dp.throttled(rate=1)
async def adentown(message: types.Message):
  await message.answer(("Ты Атакуешь"), reply_markup = aden)
@dp.message_handler(Text(equals="\U0001F3DFRaid Boss's\U0001F3DF"))
@dp.throttled(rate=1)
async def rb1(message: types.Message):
  await message.answer(("Здарова"),parse_mode="html", reply_markup = rb)
@dp.message_handler(commands=['res'])
@dp.throttled(rate=1)
async def craftm(message: types.Message):
    con = sq.connect("game.db")
    con.row_factory = sq.Row
    cur = con.cursor()
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        cur.execute(f"SELECT minirb,dion,giran,aden,srec,Varnish FROM players WHERE id = {user_id}")
        rows = cur.fetchone()
        await message.answer(fmt.text(fmt.text('\n<b>Ресурсы:</b>'
                                               '         \n\U0001F9F1Iron Ore:',fmt.hbold(rows['minirb']),
                                               '         \n\U0001F9FFBlue Gemstone:',fmt.hbold(rows['dion']),
                                                        '\n\U0001F943Varnish:',fmt.hbold(rows['Varnish']),
                                               '\n\n<b>Рецепты:</b>',
                                                         '\n(B)\U0001F4DC',(rows['giran']),
                                                         '\n(A)\U0001F4DC',(rows['aden']),
                                                         '\n(S)\U0001F4DC',(rows['srec'])
                                               )),parse_mode= "html")
@dp.message_handler(Text(equals="\U0001F377ХП банка\U0001F377(300)"))
@dp.throttled(rate=1)
async def hpbanka(message: types.Message):
    con = sq.connect("game.db")
    con.row_factory = sq.Row
    cur = con.cursor()
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        hp = int(cur.execute(f'SELECT hpbanka FROM players WHERE id = {user_id}').fetchone()[0])
        if hp < 5:
            cur.executescript(f"UPDATE players SET hpbanka = hpbanka + 1, gold = gold - 300 WHERE id = {user_id} ")
            await message.answer("Ты купил  ХП банку")
        elif hp >= 5:
            await message.answer("Максимум 5 банок!")



@dp.message_handler(Text(equals="\U0001F9CAМП банка\U0001F9CA(400)"))
@dp.throttled(rate=1)
async def mpbanka(message: types.Message):
    con = sq.connect("game.db")
    con.row_factory = sq.Row
    cur = con.cursor()
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        hp = int(cur.execute(f'SELECT mpbanka FROM players WHERE id = {user_id}').fetchone()[0])
        if hp < 5:
            cur.executescript(f"UPDATE players SET mpbanka = mpbanka + 1, gold = gold - 300 WHERE id = {user_id} ")
            await message.answer("Ты купил МП банку")
        elif hp >= 5:
            await message.answer("Максимум 5 банок!")


@dp.message_handler(Text(equals='\U0001F4B0Продажа материалов\U0001F4B0'))
@dp.throttled(rate=1)
async def sellshop(message: types.Message):
    con = sq.connect("game.db")
    con.row_factory = sq.Row
    cur = con.cursor()
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        cur.execute(f"SELECT minirb,dion,Varnish,gold FROM players WHERE id = {user_id}")
        rows = cur.fetchone()
        await message.answer(fmt.text(fmt.text('У тебя:','\n\U0001F9F1Iron Ore:', fmt.hbold(rows['minirb']),
                                               '\n\U0001F9FFBlue Gemstone:', fmt.hbold(rows['dion']),
                                               '\n\U0001F943Varnish:', fmt.hbold(rows['Varnish']),
                                               '\n\U0001FA99Aden:', fmt.hbold(rows['gold']))), parse_mode="HTML",reply_markup=sell)
@dp.message_handler(Text(equals='\U0001F9F1Iron Ore (100)'))
@dp.throttled(rate=1)
async def sellshop(message: types.Message):
    con = sq.connect("game.db")
    con.row_factory = sq.Row
    cur = con.cursor()
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        gold = cur.execute(f"SELECT minirb FROM players WHERE id = {user_id}").fetchone()
        for i in gold:
            if i >= 1:
                cur.executescript(f"UPDATE players SET minirb = minirb - 1, gold = gold + 100 WHERE id = {user_id} ")
                await message.answer(fmt.text(fmt.text('Ты продал Iron Ore, Adena +', fmt.hbold('100'))),
                                     parse_mode="HTML")
            elif i <= 0:
                await message.answer("У тебя нет Iron Ore")
@dp.message_handler(Text(equals='\U0001F9FFBlue Gemstone (200)'))
@dp.throttled(rate=1)
async def sellshop(message: types.Message):
    con = sq.connect("game.db")
    con.row_factory = sq.Row
    cur = con.cursor()
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        gold = cur.execute(f"SELECT dion FROM players WHERE id = {user_id}").fetchone()
        for i in gold:
            if i >= 1:
                cur.executescript(f"UPDATE players SET dion = dion - 1, gold = gold + 200 WHERE id = {user_id} ")
                await message.answer(fmt.text(fmt.text('Ты продал Blue Gemstone, Adena +', fmt.hbold('200'))),
                                     parse_mode="HTML")
            elif i <= 0:
                await message.answer("У тебя нет Blue Gemstone")
@dp.message_handler(Text(equals='\U0001F943Varnish (300)'))
@dp.throttled(rate=1)
async def sellshop(message: types.Message):
    con = sq.connect("game.db")
    con.row_factory = sq.Row
    cur = con.cursor()
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        gold = cur.execute(f"SELECT Varnish FROM players WHERE id = {user_id}").fetchone()
        for i in gold:
            if i >= 1:
                cur.executescript(f"UPDATE players SET Varnish = Varnish - 1, gold = gold + 300 WHERE id = {user_id} ")
                await message.answer(fmt.text(fmt.text('Ты продал Varnish, Adena +', fmt.hbold('300'))),
                                     parse_mode="HTML")
            elif i <= 0:
                await message.answer("У тебя нет Varnish")
@dp.message_handler(Text(equals='\U0001F4DBВыход\U0001F4DB'))
@dp.throttled(rate=1)
async def exitshop(message: types.Message):
    await message.answer("Скоро увидимся!", reply_markup = ReplyKeyboardRemove())
@dp.message_handler(commands=['tochka'])
@dp.throttled(rate=1)
async def tochka_s(message: types.Message):
  await message.answer(("<b>Точить оружие - 15% шанс что сломается</b>"
                        "\nDemon fang(D) - 10 Adena за 1 точку"
                        "\nHomunkulus sword(C) - 50 Adena за 1 точку"
                        "\nSword of Valhalla(B) - 200 Adena за 1 точку"
                        "\nSword of Miracles(A) - 500 Adena за 1 точку\n\n<b>Точить доспехи - 30% шанс что сломается</b>"
                        "\nBrigandine Set(D) - 20 Adena за 1 точку"
                        "\nComposite Set(C) - 60 Adena за 1 точку"
                        "\nBlue Wolf Armor(B) - 300 Adena за 1 точку"
                        "\nDark Crystal Armor(A) - 600 Adena за 1 точку\n\n<b>Точить Блесс точкой - 15% шанс что не заточится</b>"
                        "\nБлесс точками нельзя точить Demon fang(D) "), reply_markup = tochka,parse_mode="html")
@dp.message_handler(Text(equals='Точить оружие'))
@dp.throttled(rate=1)
async def tochw(message:types.Message):
    con = sq.connect("game.db")
    con.row_factory = sq.Row
    cur = con.cursor()
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        gold = cur.execute(f"SELECT gold FROM players WHERE id = {user_id}").fetchone()
        for i in gold:
            if i >= 10:
                weapon = cur.execute(f"SELECT Weapon FROM players WHERE id = {user_id}").fetchone()
                for i in weapon:
                    if i == "Demon Fang(D) +":
                        a = int(random.randrange(100))
                        if a > 85:
                           cur.executescript(f"UPDATE players SET zat = 1, atk = 5, Krit = krit - zat +1,gold = gold - 10 WHERE id = {user_id} ")
                           await message.answer(fmt.text(fmt.text('\U0000274c Сломал Demon fang(D) +', fmt.hbold('1'))), parse_mode="HTML")
                        elif a < 85:
                           cur.executescript(f"UPDATE players SET zat = zat + 1, atk = zat*5, Krit = krit + 1, gold = gold - 10 WHERE id = {user_id}")
                           cur.execute(f"SELECT zat,atk,Krit FROM players WHERE id = {user_id}")
                           rows = cur.fetchone()
                           await message.answer(fmt.text(fmt.text('\U00002728 Demon fang(D) + ', fmt.hbold(rows['zat']),
                                                           'Крит:', fmt.hbold(rows['krit']),
                                                           'Атака =', fmt.hbold(rows['atk']))), parse_mode="HTML")
                    elif i == "Homunkulus sword(С) +":
                        a = int(random.randrange(100))
                        if a > 85:
                           cur.executescript(f"UPDATE players SET zat = 1, atk = 8, Krit = krit - zat + 1,gold = gold - 50 WHERE id = {user_id} ")
                           await message.answer(fmt.text(fmt.text('\U0000274c Сломал Homunkulus sword(С) +', fmt.hbold('1'))), parse_mode="HTML")
                        elif a < 85:
                           cur.executescript(f"UPDATE players SET zat = zat + 1, atk = zat*8, Krit = krit + 1, gold=gold -50 WHERE id = {user_id}")
                           cur.execute(f"SELECT zat,atk,Krit FROM players WHERE id = {user_id}")
                           rows = cur.fetchone()
                           await message.answer(fmt.text(fmt.text('\U00002728 Homunkulus sword(С) + ', fmt.hbold(rows['zat']),
                                                           'Крит:', fmt.hbold(rows['krit']),
                                                           'Атака =', fmt.hbold(rows['atk']))), parse_mode="HTML")
                    elif i == "Sword of Valhalla(B) +":
                        a = int(random.randrange(100))
                        if a > 85:
                           cur.executescript(f"UPDATE players SET zat = 1, atk = 14, Krit = krit -zat + 1 ,gold = gold - 200 WHERE id = {user_id} ")
                           await message.answer(fmt.text(fmt.text('\U0000274c Сломал Sword of Valhalla(B) +', fmt.hbold('1'))), parse_mode="HTML")
                        elif a < 85:
                           cur.executescript(f"UPDATE players SET zat = zat + 1, atk = zat*14, Krit = krit +1, gold = gold -200  WHERE id = {user_id}")
                           cur.execute(f"SELECT zat,atk,Krit FROM players WHERE id = {user_id}")
                           rows = cur.fetchone()
                           await message.answer(fmt.text(fmt.text('\U00002728 Sword of Valhalla(B) + ', fmt.hbold(rows['zat']),
                                                           'Крит:', fmt.hbold(rows['krit']),
                                                          'Атака =', fmt.hbold(rows['atk']))), parse_mode="HTML")
                    elif i == "Sword of Miracles(A) +":
                        a = int(random.randrange(100))
                        if a > 85:
                           cur.executescript(f"UPDATE players SET zat = 1, atk = 30, Krit = krit - zat + 1 ,gold = gold - 500 WHERE id = {user_id} ")
                           await message.answer(fmt.text(fmt.text('\U0000274c Сломал Sword of Valhalla(B) +', fmt.hbold('1'))), parse_mode="HTML")
                        elif a < 85:
                           cur.executescript(f"UPDATE players SET zat = zat + 1, atk = zat*30, Krit = krit +1, gold = gold -500  WHERE id = {user_id}")
                           cur.execute(f"SELECT zat,atk,Krit FROM players WHERE id = {user_id}")
                           rows = cur.fetchone()
                           await message.answer(fmt.text(fmt.text('\U00002728 Sword of Miracles(A) + ', fmt.hbold(rows['zat']),
                                                           'Крит:', fmt.hbold(rows['krit']),
                                                          'Атака =', fmt.hbold(rows['atk']))), parse_mode="HTML")
            else:
                await message.answer("Не хватает Adena (Надо 10-50-200-500)")
    else:
        await message.answer("Зарегистрируйся!")
@dp.message_handler(Text(equals='Точить доспехи'))
@dp.throttled(rate=1)
async def tocha(message:types.Message):
    con = sq.connect("game.db")
    con.row_factory = sq.Row
    cur = con.cursor()
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        gold = cur.execute(f"SELECT gold FROM players WHERE id = {user_id}").fetchone()
        for i in gold:
            if i >= 20:
                weapon = cur.execute(f"SELECT armor FROM players WHERE id = {user_id}").fetchone()
                for i in weapon:
                    if i == "Brigandine Set(D) +":
                        a = int(random.randrange(100))
                        if a > 70:
                           cur.executescript(f"UPDATE players SET zat2 = 0, def = 1,gold = gold -20 WHERE id = {user_id} ")
                           await message.answer(fmt.text(fmt.text('\U0000274c Сломал Brigandine Set(D) +', fmt.hbold('0'))), parse_mode="HTML")
                        elif a < 70:
                           cur.executescript(f"UPDATE players SET zat2 = zat2 + 1, def = def+1, gold = gold -20 WHERE id = {user_id}")
                           cur.execute(f"SELECT zat2,def FROM players WHERE id = {user_id}")
                           rows = cur.fetchone()
                           await message.answer(fmt.text(fmt.text('\U00002728 Brigandine Set(D) + ', fmt.hbold(rows['zat2']),
                                                           'Защита:', fmt.hbold(rows['def']),
                                                           )), parse_mode="HTML")
                    elif i == "Composite Set(C) +":
                        a = int(random.randrange(100))
                        if a > 85:
                           cur.executescript(f"UPDATE players SET zat2 = 0, def = 2,gold=gold-60 WHERE id = {user_id} ")
                           await message.answer(fmt.text(fmt.text('\U0000274c Сломал Composite Set(C) +', fmt.hbold('0'))), parse_mode="HTML")
                        elif a < 85:
                           cur.executescript(f"UPDATE players SET zat2 = zat2 + 1, def = zat2*2,gold=gold-60 WHERE id = {user_id}")
                           cur.execute(f"SELECT zat2,def FROM players WHERE id = {user_id}")
                           rows = cur.fetchone()
                           await message.answer(fmt.text(fmt.text('\U00002728 Composite Set(C) + ', fmt.hbold(rows['zat2']),
                                                           'Защита:', fmt.hbold(rows['def']),
                                                           )), parse_mode="HTML")
                    elif i == "Blue Wolf Armor(B) +":
                        a = int(random.randrange(100))
                        if a > 85:
                           cur.executescript(f"UPDATE players SET zat2 = 0, def = 3,gold=gold-300 WHERE id = {user_id} ")
                           await message.answer(fmt.text(fmt.text('\U0000274c Сломал Blue Wolf Armor(B) +', fmt.hbold('0'))), parse_mode="HTML")
                        elif a < 85:
                           cur.executescript(f"UPDATE players SET zat2 = zat2 + 1, def = zat2*3,gold=gold-300 WHERE id = {user_id}")
                           cur.execute(f"SELECT zat2,def FROM players WHERE id = {user_id}")
                           rows = cur.fetchone()
                           await message.answer(fmt.text(fmt.text('\U00002728 Blue Wolf Armor(B) +', fmt.hbold(rows['zat2']),
                                                           'Защита:', fmt.hbold(rows['def']),
                                                           )), parse_mode="HTML")
                    elif i == "Dark Crystal Armor(A) +":
                        a = int(random.randrange(100))
                        if a > 85:
                           cur.executescript(f"UPDATE players SET zat2 = 0, def = 4,gold=gold-600 WHERE id = {user_id} ")
                           await message.answer(fmt.text(fmt.text('\U0000274c Сломал Dark Crystal Armor(A) +', fmt.hbold('0'))), parse_mode="HTML")
                        elif a < 85:
                           cur.executescript(f"UPDATE players SET zat2 = zat2 + 1, def = zat2*4,gold=gold-600 WHERE id = {user_id}")
                           cur.execute(f"SELECT zat2,def FROM players WHERE id = {user_id}")
                           rows = cur.fetchone()
                           await message.answer(fmt.text(fmt.text('\U00002728 Dark Crystal Armor(A) +', fmt.hbold(rows['zat2']),
                                                           'Защита:', fmt.hbold(rows['def']),
                                                           )), parse_mode="HTML")
            else:
                await message.answer("Не хватает Adena (Надо 20-60-300-600)")
@dp.message_handler(Text(equals='Точить Блесс точкой'))
@dp.throttled(rate=1)
async def tochb(message:types.Message):
    con = sq.connect("game.db")
    con.row_factory = sq.Row
    cur = con.cursor()
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        weapon = cur.execute(f"SELECT Weapon FROM players WHERE id = {user_id}").fetchone()
        for i in weapon:
            if i == "Homunkulus sword(С) +":
                tochb = cur.execute(f"SELECT tochkab FROM players WHERE id = {user_id}").fetchone()
                for i in tochb:
                    if i >= 1:
                        d = int(random.randrange(100))
                        if d < 85:
                            cur.executescript(f"UPDATE players SET zat = zat + 1 WHERE id = {user_id}")
                            cur.executescript(f"UPDATE players SET atk = zat*8 WHERE id = {user_id}")
                            cur.executescript(f"UPDATE players SET Krit = krit + 1 WHERE id = {user_id}")
                            cur.executescript(f"UPDATE players SET tochkab = tochkab - 1 WHERE id = {user_id}")
                            cur.execute(f"SELECT zat,atk,Krit,tochkab FROM players WHERE id = {user_id}")
                            rows = cur.fetchone()
                            await message.answer(fmt.text(fmt.text('\U00002728 Homunkulus sword(C) + ', fmt.hbold(rows['zat']),
                                                                   'Крит:', fmt.hbold(rows['krit']),
                                                                   'Атака =', fmt.hbold(rows['atk']),
                                                                   'Блесс точек:',fmt.hbold(rows['tochkab'])
                                                                   )), parse_mode="HTML")
                        elif d > 85:
                            cur.executescript(f"UPDATE players SET tochkab = tochkab - 1 WHERE id = {user_id}")
                            await message.answer("Неудача")
                    else:
                        await message.answer("Недостаточно Блесс точек")
            elif i == "Sword of Valhalla(B) +":
                tochb = cur.execute(f"SELECT tochkab FROM players WHERE id = {user_id}").fetchone()
                for i in tochb:
                    if i >= 1:
                        d = int(random.randrange(100))
                        if d < 85:
                            cur.executescript(f"UPDATE players SET zat = zat + 1 WHERE id = {user_id}")
                            cur.executescript(f"UPDATE players SET atk = zat*14 WHERE id = {user_id}")
                            cur.executescript(f"UPDATE players SET Krit = krit + 1 WHERE id = {user_id}")
                            cur.executescript(f"UPDATE players SET tochkab = tochkab - 1 WHERE id = {user_id}")
                            cur.execute(f"SELECT zat,atk,krit,tochkab FROM players WHERE id = {user_id}")
                            rows = cur.fetchone()
                            await message.answer(fmt.text(fmt.text('\U00002728 Sword of Valhalla(B) + ', fmt.hbold(rows['zat']),
                                                                   'Крит:', fmt.hbold(rows['krit']),
                                                                   'Атака =', fmt.hbold(rows['atk']),
                                                                   'Блесс точек:',fmt.hbold(rows['tochkab']))), parse_mode="HTML")
                        elif d > 85:
                            cur.executescript(f"UPDATE players SET tochkab = tochkab - 1 WHERE id = {user_id}")
                            await message.answer("Неудача")
                    else:
                        await message.answer("Недостаточно Блесс точек")
            else:
                await message.answer("Блесс точками нельзя точить Demon fang(D)")
    else:
        await message.answer("Зарегистрируйся!")
@dp.message_handler(Text(equals='\U0000269CКупить Блесс точку\U0000269C(30000)'))
@dp.throttled(rate=1)
async def buy_homa(message:types.Message):
    con = sq.connect("game.db")
    con.row_factory = sq.Row
    cur = con.cursor()
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        weapon = cur.execute(f"SELECT gold FROM players WHERE id = {user_id}").fetchone()
        for i in weapon:
            if i >= 5000:
                cur.executescript(f"UPDATE players SET tochkab = tochkab + 1  WHERE id = {user_id} ")
                cur.executescript(f"UPDATE players SET gold = gold - 30000 WHERE id = {user_id}")
                await message.answer(fmt.text(fmt.text('Вы купили Блесс точку ')))
            else:
                await message.answer(fmt.text(fmt.text('Не хватает Adena. Блесс точка стоит 30000')))
    else:
        await message.answer("Зарегистрируйся!")

@dp.message_handler(Text(equals='\U0001F5E1Купить Homunkulus sword(C)\U0001F5E1(5000)'))
@dp.throttled(rate=1)
async def buy_homa(message:types.Message):
    con = sq.connect("game.db")
    con.row_factory = sq.Row
    cur = con.cursor()
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        weapon = cur.execute(f"SELECT gold FROM players WHERE id = {user_id}").fetchone()
        for i in weapon:
            if i >= 5000:
                cur.executescript(f"UPDATE players SET weapon = 'Homunkulus sword(С) +'  WHERE id = {user_id} ")
                cur.executescript(f"UPDATE players SET gold = gold - 5000 WHERE id = {user_id}")
                cur.executescript(f"UPDATE players SET atk = 8 WHERE id = {user_id}")
                cur.executescript(f"UPDATE players SET zat = 0 WHERE id = {user_id}")
                await message.answer(fmt.text(fmt.text('Вы купили Homunkulus sword(С) ')))
            else:
                await message.answer(fmt.text(fmt.text('Не хватает Adena. Homunkulus sword(С) стоит 5000')))
    else:
        await message.answer("Зарегистрируйся!")
@dp.message_handler(Text(equals='\U0001F5E1Купить Sword of Valhalla(B)\U0001F5E1(16000)'))
@dp.throttled(rate=1)
async def buy_valhala(message:types.Message):
    con = sq.connect("game.db")
    con.row_factory = sq.Row
    cur = con.cursor()
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        weapon = cur.execute(f"SELECT gold FROM players WHERE id = {user_id}").fetchone()
        for i in weapon:
            if i >= 16000:
                cur.executescript(f"UPDATE players SET weapon = 'Sword of Valhalla(B) +'  WHERE id = {user_id} ")
                cur.executescript(f"UPDATE players SET gold = gold - 16000 WHERE id = {user_id}")
                cur.executescript(f"UPDATE players SET atk = 11 WHERE id = {user_id}")
                cur.executescript(f"UPDATE players SET zat = 0 WHERE id = {user_id}")
                await message.answer(fmt.text(fmt.text('Вы купили Sword of Valhalla  ')))
            else:
                await message.answer(fmt.text(fmt.text('Не хватает Adena. Sword of Valhalla(B) стоит 16000')))
    else:
        await message.answer("Зарегистрируйся!")
@dp.message_handler(Text(equals='\U0001F94BКупить Composite Set(С)\U0001F94B(6500)'))
@dp.throttled(rate=1)
async def buy_compset(message:types.Message):
    con = sq.connect("game.db")
    con.row_factory = sq.Row
    cur = con.cursor()
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        weapon = cur.execute(f"SELECT gold FROM players where id = {user_id}").fetchone()
        for i in weapon:
            if i >= 6500:
                cur.executescript(f"UPDATE players SET armor = 'Composite Set(C) +'  WHERE id = {user_id} ")
                cur.executescript(f"UPDATE players SET gold = gold - 6500 WHERE id = {user_id}")
                cur.executescript(f"UPDATE players SET zat2 = 0 WHERE id = {user_id}")
                cur.executescript(f"UPDATE players SET def = 1 WHERE id = {user_id}")
                await message.answer(fmt.text(fmt.text('Вы купили Composite Set ')))
            else:
                await message.answer(fmt.text(fmt.text('Не хватает Adena. Composite Set стоит 6500 ')))
    else:
        await message.answer("Зарегистрируйся!")
@dp.message_handler(Text(equals='\U0001F9A6Гремлин\U0001F9A6'))
@dp.throttled(rate=1)
async def mob1(message:types.Message):
    con = sq.connect("game.db")
    con.row_factory = sq.Row
    cur = con.cursor()
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        r = int(cur.execute(f"SELECT hpxp FROM players where id = {user_id}").fetchone()[0])
        if r < 500:
            h = int(cur.execute(f"SELECT hp FROM players where id = {user_id}").fetchone()[0])
            if h > 0:
                c = int(random.randrange(100))
                if c > 90:
                    cur.executescript(f"UPDATE players SET mob1 = mob1 - atk - krit*4 - atkxp WHERE id = {user_id}")
                    cur.executescript(f"UPDATE players SET hp = hp - (40/(def + defxp)) WHERE id = {user_id}")
                    cur.execute(f"SELECT mob1,atk,krit,hp,atkxp FROM players WHERE id = {user_id}")
                    rows = cur.fetchone()
                    await message.answer(fmt.text(
                       fmt.text('\U0001F4A5\U0001F4A5\U0001F4A5КРИТ!!! Вы отняли у Гремлина :', fmt.hbold(rows['atk']),'-', fmt.hbold(rows['krit']), '*', fmt.hbold('4'),'-', fmt.hbold(rows['atkxp']),
                             '\nГремлин атакует, ваше ХП стало:', fmt.hbold(rows['hp']),
                             '\n\U0001F9A6ХП Гремлина стало:', fmt.hbold(rows['mob1']))), parse_mode="HTML")
                    r = cur.execute(f"SELECT mob1 FROM players WHERE id = {user_id}").fetchone()
                    for i in r:
                        if i <= 0:
                            cur.executescript(f"UPDATE players SET gold = gold+20 WHERE id = {user_id}")
                            cur.executescript(f"UPDATE players SET mob1 = 100 WHERE id = {user_id}")
                            cur.executescript(f"UPDATE players SET xp = xp+1 WHERE id = {user_id}")
                            cur.executescript(f"UPDATE players SET hpxp = hpxp +1 WHERE id = {user_id}")
                            await message.answer(fmt.text(
                                fmt.text(' Поздравляю! Вы убили Гремлина!\nAdena +', fmt.hbold('20'),'\nXp +',fmt.hbold('1'))),parse_mode="HTML")
                elif c < 90:
                    cur.executescript(f"UPDATE players SET mob1 = mob1 - atk - atkxp WHERE id = {user_id}")
                    cur.executescript(f"UPDATE players SET hp = hp - (40/(def + defxp)) WHERE id = {user_id}")
                    cur.execute(f"SELECT mob1,atk,hp,atkxp FROM players WHERE id = {user_id}")
                    rows = cur.fetchone()
                    await message.answer(fmt.text(fmt.text('\U0001F4A5Вы отняли у Гремлина :', fmt.hbold(rows['atk']),'+', fmt.hbold(rows['atkxp']) , '\nГремлин атакует, ваше ХП стало:', fmt.hbold(rows['hp']),
                                               '\n\U0001F9A6ХП Гремлина стало:', fmt.hbold(rows['mob1']))), parse_mode="HTML")
                    r = cur.execute(f"SELECT mob1 FROM players WHERE id = {user_id} ").fetchone()
                    for i in r:
                        if i <= 0:
                            cur.executescript(f"UPDATE players SET gold = gold+20 WHERE id = {user_id}")
                            cur.executescript(f"UPDATE players SET mob1 = 100 where id = {user_id}")
                            cur.executescript(f"UPDATE players SET xp = xp+1 WHERE id = {user_id}")
                            cur.executescript(f"UPDATE players SET hpxp = hpxp +1 WHERE id = {user_id}")
                            await message.answer(fmt.text(
                                fmt.text(' Поздравляю! Вы убили Гремлина!\nAdena +', fmt.hbold('20'),'\nXp +',fmt.hbold('1'))), parse_mode="HTML")
            else:
                cur.executescript(f"UPDATE players SET mob1 = 100 where id = {user_id}")
                cur.executescript(f"UPDATE players SET hp = 0 where id = {user_id}")
                await message.answer('\U0001F3F3Вас убили, хп монстра восстановилось\U0001F3F3')
        else:
            await message.answer("Вы уже достаточно сильны чтобы нападать на Гремлина")
@dp.message_handler(Text(equals='\U0001F9CCТроль\U0001F9CC'))
@dp.throttled(rate=1)
async def mob1(message:types.Message):
    con = sq.connect("game.db")
    con.row_factory = sq.Row
    cur = con.cursor()
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        r = cur.execute(f"SELECT hpxp FROM players where id = {user_id}").fetchone()
        for i in r:
            if i < 800:
                r = cur.execute(f"SELECT hp FROM players where id = {user_id}").fetchone()
                for i in r:
                    if i > 0:
                        c = int(random.randrange(100))
                        if c < 10:
                            cur.executescript(f"UPDATE players SET mob2 = mob2 - atk - krit*4 - atkxp WHERE id = {user_id}")
                            cur.executescript(f"UPDATE players SET hp = hp - (160/(def + defxp)) - 2  WHERE id = {user_id}")
                            cur.execute(f"SELECT mob2,atk,krit,hp,atkxp FROM players WHERE id = {user_id}")
                            rows = cur.fetchone()
                            await message.answer(fmt.text(
                                fmt.text('\U0001F4A5\U0001F4A5\U0001F4A5КРИТ!!! Вы отняли у Троля :', fmt.hbold(rows['atk']),'-', fmt.hbold(rows['krit']), '*', fmt.hbold('4'),'-', fmt.hbold(rows['atkxp']),
                                         '\n\U0001F9CCТроль атакует, ваше ХП стало:', fmt.hbold(rows['hp']),
                                         '\nХП Троля стало:', fmt.hbold(rows['mob2']))), parse_mode="HTML")
                            q = cur.execute(f"SELECT mob2 FROM players WHERE id = {user_id}").fetchone()
                            for x in q:
                                if x <= 0:
                                    cur.executescript(f"UPDATE players SET gold = gold+60 WHERE id = {user_id}")
                                    cur.executescript(f"UPDATE players SET mob2 = 600 WHERE id = {user_id}")
                                    cur.executescript(f"UPDATE players SET xp = xp+2 WHERE id = {user_id}")
                                    cur.executescript(f"UPDATE players SET hpxp = hpxp +1 WHERE id = {user_id}")
                                    await message.answer(fmt.text(
                                        fmt.text(' Поздравляю! Вы убили \U0001F9CCТроля!\n\U0001F4AFВам повезло!!!\nAdena +', fmt.hbold('60'),'\nXp +',fmt.hbold('2'))),parse_mode="HTML")
                        elif c > 10:
                            cur.executescript(f"UPDATE players SET mob2 = mob2 - atk - atkxp WHERE id = {user_id}")
                            cur.executescript(f"UPDATE players SET hp = hp - (160/(def + defxp)) - 2 WHERE id = {user_id}")
                            cur.execute(f"SELECT mob2,atk,hp,atkxp FROM players WHERE id = {user_id}")
                            rows = cur.fetchone()
                            await message.answer(fmt.text(fmt.text('\U0001F4A5 Вы отняли у Троля :', fmt.hbold(rows['atk']),'+', fmt.hbold(rows['atkxp']) , '\nТроль атакует, ваше ХП стало:', fmt.hbold(rows['hp']),
                                                               '\n\U0001F9CCХП Троля:', fmt.hbold(rows['mob2']))), parse_mode="HTML")
                            q = cur.execute(f"SELECT mob2 FROM players WHERE id = {user_id} ").fetchone()
                            for x in q:
                                if x <= 0:
                                    cur.executescript(f"UPDATE players SET gold = gold+45 WHERE id = {user_id}")
                                    cur.executescript(f"UPDATE players SET mob2 = 600 where id = {user_id}")
                                    cur.executescript(f"UPDATE players SET xp = xp+2 WHERE id = {user_id}")
                                    cur.executescript(f"UPDATE players SET hpxp = hpxp +1 WHERE id = {user_id}")
                                    await message.answer(fmt.text(
                                        fmt.text(' Поздравляю! Вы убили \U0001F9CCТроля!\nAdena +', fmt.hbold('45'),'\nXp +',fmt.hbold('2'))), parse_mode="HTML")
                    else:
                        cur.executescript(f"UPDATE players SET mob2 = 600 where id = {user_id}")
                        cur.executescript(f"UPDATE players SET hp = 0 where id = {user_id}")
                        await message.answer('\U0001F3F3Вас убили, хп монстра восстановилось\U0001F3F3')
            else:
                await message.answer("Ты слишком сильный для Троля ищи других")
@dp.message_handler(Text(equals='\U0001F5FFГолем\U0001F5FF'))
@dp.throttled(rate=1)
async def mob1(message:types.Message):
    con = sq.connect("game.db")
    con.row_factory = sq.Row
    cur = con.cursor()
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        r = cur.execute(f"SELECT hpxp FROM players where id = {user_id}").fetchone()
        for i in r:
            if i < 1200:
                h = cur.execute(f"SELECT hp FROM players where id = {user_id}").fetchone()
                for m in h:
                    if m > 0:
                        c = int(random.randrange(100))
                        if c > 90:
                            cur.executescript(f"UPDATE players SET mob3 = mob3 - atk - krit*4 - atkxp, hp = hp - (700/(def + defxp)) WHERE id = {user_id}")
                            cur.execute(f"SELECT mob3,atk,krit,hp,atkxp FROM players WHERE id = {user_id}")
                            rows = cur.fetchone()
                            await message.answer(fmt.text(
                               fmt.text('\U0001F4A5\U0001F4A5\U0001F4A5КРИТ!!! Вы отняли у Голема :', fmt.hbold(rows['atk']), '-', fmt.hbold(rows['krit']), '*', fmt.hbold('4'),'-', fmt.hbold(rows['atkxp']),
                                     '\nГолема атакует, ваше ХП стало:', fmt.hbold(rows['hp']),
                                     '\n\U0001F5FFХП Голема стало:', fmt.hbold(rows['mob3']))), parse_mode="HTML")
                            r = cur.execute(f"SELECT mob3 FROM players WHERE id = {user_id}").fetchone()
                            for i in r:
                                if i <= 0:
                                    drop = random.randrange(100)
                                    if drop < 85:
                                        cur.executescript(f"UPDATE players SET gold = gold+80, mob3 = 1200, xp = xp+3,"
                                                          f" hpxp = hpxp +1 WHERE id = {user_id}")
                                        await message.answer(fmt.text(
                                            fmt.text(' Поздравляю! Вы убили Голема!\nAdena +', fmt.hbold('80'),'\nXp +',fmt.hbold('3'))),parse_mode="HTML")
                                    if drop > 85:
                                        cur.executescript(f"UPDATE players SET gold = gold+80, mob3 = 1200, xp = xp+3,"
                                                          f" hpxp = hpxp+1, minirb = minirb + 1 WHERE id = {user_id}")
                                        await message.answer(fmt.text(
                                            fmt.text(' Поздравляю! Вы убили Голема!\n Удача! Выпал Iron Ore! \nAdena +', fmt.hbold('80'),
                                                     '\nXp +', fmt.hbold('3'))), parse_mode="HTML")
                        elif c < 90:
                            cur.executescript(f"UPDATE players SET mob3 = mob3 - atk - atkxp, hp = hp - (700/(def + defxp)) WHERE id = {user_id}")
                            cur.execute(f"SELECT mob3,atk,hp,atkxp FROM players WHERE id = {user_id}")
                            rows = cur.fetchone()
                            await message.answer(fmt.text(fmt.text('\U0001F4A5 Вы отняли у Голема :', fmt.hbold(rows['atk']),'+', fmt.hbold(rows['atkxp']) ,
                                                                   '\nГолем атакует, ваше ХП стало:', fmt.hbold(rows['hp']),
                                                       '\n\U0001F5FFХП Голема стало:', fmt.hbold(rows['mob3']))), parse_mode="HTML")
                            r = cur.execute(f"SELECT mob3 FROM players WHERE id = {user_id} ").fetchone()
                            for i in r:
                                if i <= 0:
                                    drop = random.randrange(100)
                                    if drop < 85:
                                        cur.executescript(f"UPDATE players SET gold = gold+80, mob3 = 1200,"
                                                      f"xp = xp+3, hpxp = hpxp +1 WHERE id = {user_id}")
                                        await message.answer(fmt.text(
                                            fmt.text(' Поздравляю! Вы убили Голема!\nAdena +', fmt.hbold('80'),'\nXp +',fmt.hbold('3'))), parse_mode="HTML")
                                    if drop > 85:
                                        cur.executescript(f"UPDATE players SET gold = gold+80, mob3 = 1200,"
                                                          f"xp = xp+3, hpxp = hpxp +1, minirb = minirb + 1 WHERE id = {user_id}")
                                        await message.answer(fmt.text(
                                            fmt.text(' Поздравляю! Вы убили Голема!\n Удача! Выпал Iron Ore!\nAdena +', fmt.hbold('80'),
                                                     '\nXp +', fmt.hbold('3'))), parse_mode="HTML")
                    else:
                        cur.executescript(f"UPDATE players SET mob3 = 1200, hp = 0 where id = {user_id}")
                        await message.answer('\U0001F3F3Вас убили, хп монстра восстановилось\U0001F3F3')
            else:
                await message.answer("Вы уже достаточно сильны чтобы нападать на Голема")
    a = int(random.randrange(10))
    if a > 7:
        cur.executescript(f"UPDATE players SET hp = hp - 20 where id = {user_id}")
        await message.answer(fmt.text(fmt.text('Голем использовал Stone wall -', fmt.hbold('20'), 'ХП')),
                             parse_mode="HTML")
@dp.message_handler(Text(equals='\U0001F40AАллигатор\U0001F40A'))
@dp.throttled(rate=1)
async def mob1(message:types.Message):
    con = sq.connect("game.db")
    con.row_factory = sq.Row
    cur = con.cursor()
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id}")
    data = cur.fetchone()
    if data is not None:
        h = int(cur.execute(f"SELECT hp FROM players where id = {user_id}").fetchone()[0])
        r = int(cur.execute(f"SELECT mob4 FROM players WHERE id = {user_id} ").fetchone()[0])
        if h > 0:
            c = int(random.randrange(100))
            if c > 90:
                r = int(cur.execute(f"SELECT mob4 FROM players WHERE id = {user_id} ").fetchone()[0])
                if r > 0:
                    cur.executescript(f"UPDATE players SET mob4 = mob4 - atk - krit*4 - atkxp, hp = hp - (1100/(def + defxp)) WHERE id = {user_id}")
                    cur.execute(f"SELECT mob4,atk,krit,hp,atkxp FROM players WHERE id = {user_id}")
                    rows = cur.fetchone()
                    await message.answer(fmt.text(
                       fmt.text('\U0001F4A5\U0001F4A5\U0001F4A5КРИТ!!! Вы отняли у Аллигатора :', fmt.hbold(rows['atk']), '-', fmt.hbold(rows['krit']), '*', fmt.hbold('4'),'-', fmt.hbold(rows['atkxp']),
                             '\nАллигатор атакует, ваше ХП стало:', fmt.hbold(rows['hp']),
                             '\n\U0001F40AХП Аллигатора стало:', fmt.hbold(rows['mob4']))), parse_mode="HTML")
                elif r <= 0:
                    drop = random.randrange(100)
                    if drop > 90:
                        cur.executescript(f"UPDATE players SET gold = gold+100, mob4 = 2000, xp = xp+3,"
                                          f" hpxp = hpxp+1, dion = dion + 1 WHERE id = {user_id}")
                        await message.answer(fmt.text(
                            fmt.text('Поздравляю! Вы убили Аллигатора!\n Удача! Выпал Blue Gemstone! \nAdena +', fmt.hbold('100'),
                                     '\nXp +', fmt.hbold('3'))), parse_mode="HTML")
                    if drop < 90:
                        cur.executescript(f"UPDATE players SET gold = gold+100, mob4 = 2000,"
                                          f"xp = xp+3, hpxp = hpxp +1,aliq = aliq + 1 WHERE id = {user_id}")
                        await message.answer(fmt.text(
                            fmt.text(' Поздравляю! Вы убили Аллигатора!\nAdena +', fmt.hbold('100'), '\nXp +',
                                     fmt.hbold('3'),'\nЧешуя +', fmt.hbold('1'))), parse_mode="HTML")
            elif c < 90:
                if r > 0:
                    cur.executescript(f"UPDATE players SET mob4 = mob4 - atk - atkxp, hp = hp - (1100/(def + defxp)) WHERE id = {user_id}")
                    cur.execute(f"SELECT mob4,atk,hp,atkxp FROM players WHERE id = {user_id}")
                    rows = cur.fetchone()
                    await message.answer(fmt.text(fmt.text('\U0001F4A5 Вы отняли у Аллигатора :', fmt.hbold(rows['atk']),'+', fmt.hbold(rows['atkxp']) ,
                                                           '\nАллигатор атакует, ваше ХП стало:', fmt.hbold(rows['hp']),
                                               '\n\U0001F40AХП Аллигатора стало:', fmt.hbold(rows['mob4']))), parse_mode="HTML")
                elif r <= 0:
                    drop = random.randrange(100)
                    if drop > 90:
                        cur.executescript(f"UPDATE players SET gold = gold+100, mob4 = 2000, xp = xp+3,"f" hpxp = hpxp+1, dion = dion + 1 WHERE id = {user_id}")
                        await message.answer(fmt.text(
                            fmt.text(' Поздравляю! Вы убили Аллигатора!\nУдача! Выпал Blue Gemstone! \nAdena +',fmt.hbold('100'),'\nXp +', fmt.hbold('3'))), parse_mode="HTML")
                    if drop < 90:
                        cur.executescript(f"UPDATE players SET gold = gold+100, mob4 = 2000,"
                                          f"xp = xp+3, hpxp = hpxp +1, aliq = aliq+1 WHERE id = {user_id}")
                        await message.answer(fmt.text(
                            fmt.text(' Поздравляю! Вы убили Аллигатора!\nAdena +', fmt.hbold('100'), '\nXp +',
                                     fmt.hbold('3'),'\nЧешуя +', fmt.hbold('1'))), parse_mode="HTML")
        else:
            cur.executescript(f"UPDATE players SET mob4 = 2000, hp = 0 where id = {user_id}")
            await message.answer('\U0001F3F3Вас убили, хп монстра восстановилось\U0001F3F3')
@dp.message_handler(commands=['wrb'])
@dp.throttled(rate=1)
async def minirb(message:types.Message):
    con = sq.connect("game.db")
    con.row_factory = sq.Row
    cur = con.cursor()
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
            r = cur.execute(f"SELECT hp FROM players where id = {user_id}").fetchone()
            for i in r:
                if i > 0 :
                    c = int(random.randrange(100))
                    if c > 90:
                        cur.executescript(f"UPDATE rbboss SET rb1 = rb1 - (SELECT atk + atkxp + krit*4 FROM players WHERE id = {user_id})")
                        cur.executescript(f"UPDATE players SET hp = hp - (120000/(def + defxp)) WHERE id = {user_id}")
                        cur.execute(f"SELECT players.atk, players.krit, players.hp, players.atkxp, rbboss.rb1 FROM players, rbboss WHERE players.id = {user_id}")
                        rows = cur.fetchone()
                        await message.answer(fmt.text(
                           fmt.text('\U0001F4A5\U0001F4A5\U0001F4A5КРИТ!!! Вы отняли у Ant queen :', fmt.hbold(rows['atk']), '-', fmt.hbold(rows['krit']), '*', fmt.hbold('4'),'-', fmt.hbold(rows['atkxp']),
                                 '\n\U0001F577ХП Ant queen стало:', fmt.hbold(rows['rb1']),
                                 '\nAnt queen атакует, ваше ХП стало:', fmt.hbold(rows['hp']))),parse_mode="HTML")
                        c = cur.execute("SELECT rb1 FROM rbboss").fetchone()
                        for x in c:
                            if x <= 0:
                                cur.executescript(f"UPDATE players SET gold = gold+100000, tochkab = tochkab + 2 WHERE id = {user_id}")
                                cur.executescript(f"UPDATE rbboss SET rb1 = 2000000 ")
                                cur.executescript(f"UPDATE players SET xp = xp+6000 WHERE id = {user_id}")
                                cur.executescript(f"UPDATE players SET hpxp = hpxp +1 WHERE id = {user_id}")
                                cur.executescript(f"UPDATE players SET srec = 'Arcana Mace(S)' WHERE id = {user_id}")
                                await message.answer(fmt.text(
                                    fmt.text(' Поздравляю! Вы убили \U0001F577Ant queen!\nВыпало 2 Блесс точки!\nВыпал рецепт Arcana Mace(S)!\nAdena +', fmt.hbold('100000'),'\nXp +',fmt.hbold('6000'))),parse_mode="HTML")

                    elif c < 90:
                        cur.executescript(f"UPDATE rbboss SET rb1 = rb1 - (SELECT atk + atkxp FROM players WHERE id = {user_id})")
                        cur.executescript(f"UPDATE players SET hp = hp - (120000/(def + defxp)) WHERE id = {user_id}")
                        cur.execute(f"SELECT players.atk,players.hp, players.atkxp, rbboss.rb1 FROM players, rbboss WHERE players.id = {user_id}")
                        rows = cur.fetchone()
                        await message.answer(fmt.text(fmt.text('\U0001F4A5 Вы отняли у Ant queen:', fmt.hbold(rows['atk']),'+', fmt.hbold(rows['atkxp']) ,
                                                               '\n\U0001F577ХП Ant queen стало:', fmt.hbold(rows['rb1']),
                                                               '\nAnt queen атакует, ваше ХП стало:', fmt.hbold(rows['hp']))), parse_mode="HTML")
                        c =  cur.execute("SELECT rb1 FROM rbboss").fetchone()
                        for x in c:
                            if x <= 0:
                                cur.executescript(f"UPDATE players SET gold = gold+100000, tochkab = tochkab + 2 WHERE id = {user_id}")
                                cur.executescript(f"UPDATE rbboss SET rb1 = 2000000")
                                cur.executescript(f"UPDATE players SET xp = xp+6000 WHERE id = {user_id}")
                                cur.executescript(f"UPDATE players SET hpxp = hpxp +1 WHERE id = {user_id}")
                                cur.executescript(f"UPDATE players SET srec = 'Arcana Mace(S)' WHERE id = {user_id}")
                                await message.answer(fmt.text(
                                    fmt.text(' Поздравляю! Вы убили \U0001F577Ant queen!\nВыпало 2 Блесс точки!\nВыпал рецепт Arcana Mace(S)!\nAdena +', fmt.hbold('100000'),'\nXp +',fmt.hbold('6000'))), parse_mode="HTML")
                else:
                    cur.executescript(f"UPDATE players SET hp = 0 where id = {user_id}")
                    await message.answer('\U0001F3F3Вас убили\U0001F3F3')
@dp.message_handler(commands='help')
@dp.throttled(rate=1)
async def help (message: types.Message):
    await message.answer('/shop - магазин\n/res- список материалов\n/craft - список вещей которые можно скрафтить'
                         '\n/tochka - точить \n/loc - локации с мобами\n/rb - Raid Boss'
                         '\n/wrb - напасть на World RB\n/skill - прокачать скилы и выбрать профу\n/buff - бафы'
                         '\n/info - инфа о персонаже\n/top - top 10(по заточке оружия)'
                         '\nХил - лечение (стоит 10% от Макс.ХП (Можно уйти в минус \U0001FAE3) <b>Если -2000 Aden, то будет отниматся и опыт -2</b>',parse_mode="html")
@dp.message_handler(Text(equals='\U0001F912Хил\U0001F912'))
@dp.throttled(rate=1)
async def heal (message: types.Message):
    con = sq.connect("game.db")
    con.row_factory = sq.Row
    cur = con.cursor()
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        m = int(cur.execute(f'SELECT rbfight FROM players WHERE id = {user_id}').fetchone()[0])
        if m == 0:
            weapon = cur.execute(f"SELECT gold FROM players WHERE id = {user_id}").fetchone()
            for i in weapon:
                if i > -2000:
                    cur.executescript(f"UPDATE players SET gold = gold-(maxhp*0.1) WHERE id = {user_id}")
                    cur.executescript(f"UPDATE players SET hp = maxhp  WHERE id = {user_id}")
                    cur.execute(f"SELECT maxhp,gold FROM players where id = {user_id}")
                    rows = cur.fetchone()
                    await message.answer(fmt.text(fmt.text('\U0001F912 Хп восстановленно \U0001F912',
                                                           '\nМакс. ХП =', fmt.hbold(rows['maxhp']),'\nAdena стало ',fmt.hbold(rows['gold']))),parse_mode="html")
                elif i < -2000:
                    cur.executescript(f"UPDATE players SET gold = gold-(maxhp*0.1) WHERE id = {user_id}")
                    cur.executescript(f"UPDATE players SET hp = maxhp  WHERE id = {user_id}")
                    cur.executescript(f"UPDATE players SET xp = xp - 2  WHERE id = {user_id}")
                    cur.execute(f"SELECT maxhp,gold,xp FROM players where id = {user_id}")
                    rows = cur.fetchone()
                    await message.answer(fmt.text(fmt.text('Cлишком большой минус, теперь будет отниматься и опыт\n\U0001F912 Хп восстановленно \U0001F912',
                                                           '\nМакс. ХП =', fmt.hbold(rows['maxhp']),
                                                           '\nОпыта стало =', fmt.hbold(rows['xp']),
                                                           '\nAdena стало ',fmt.hbold(rows['gold']))), parse_mode="html")
        elif m == 1:
            await message.answer("Ты сражаешься с RB! Убей его или умри, чтобы я мог снова восстанавливать тебе ХП!")
@dp.message_handler(commands='info')
@dp.throttled(rate=1)
async def heal (message: types.Message):
    con = sq.connect("game.db")
    con.row_factory = sq.Row
    cur = con.cursor()
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        cur.execute(f"SELECT Weapon,atk,atkxp,tochkam,krit,profa,hpxp,maxmp,def,mp,tochkar,tochkab,hpbanka,mpbanka,def,defxp,zat,zat2,hp,maxhp,gold,xp,armor FROM players WHERE id = {user_id}")
        rows = cur.fetchone()
        await message.answer(fmt.text(fmt.text(fmt.hbold(rows['Weapon']), fmt.hbold(rows['zat']),
                                                '\n',fmt.hbold(rows['armor']), fmt.hbold(rows['zat2']),
                                               '\n\U0001F9B8',fmt.hbold(rows['profa']),'\U0001F9B8',
                                               '\n\U0001F386Крит дамаг =', fmt.hbold(rows['krit']),
                                               '\n\U0001F5E1Атака =', fmt.hbold(rows['atk']),
                                               '\n\U0001F6E1Защита =', fmt.hbold(rows['def']),
                                               '\n\U0001F493ХП =', fmt.hbold(rows['hp']),'/',fmt.hbold(rows['maxhp']),
                                               '\n\U0001F4A7МП =', fmt.hbold(rows['mp']),'/',fmt.hbold(rows['maxmp']),
                                               '\n\n\U0001F377ХП банки:', fmt.hbold(rows['hpbanka']),
                                               '\n\U0001F9CAМП банки:',fmt.hbold(rows['mpbanka']),
                                               '\n\n\U0001F939Опыт (XP) =', fmt.hbold(rows['xp']),
                                               '\n\U0001F6E1Защита (скил) +', fmt.hbold(rows['defxp']),
                                               '\n\U00002694Атака (скил) +', fmt.hbold(rows['atkxp']),
                                               '\n\n\U0001FA99Adena :', fmt.hbold(rows['gold']),
                                               '\n\U0001F4C3Блесс точек :', fmt.hbold(rows['tochkab']),
                                               '\n\U0001F3C6РБ убито :', fmt.hbold(rows['tochkar']),
                                               '\n\U0001F506Мобов убито :', fmt.hbold(rows['hpxp']),
                                               '\n\U0001F48DБижутерия:',fmt.hbold(rows['tochkam']),
                                               )), parse_mode="HTML")
@dp.message_handler(Text(equals='\U00002694Атака (скил)(+5)\U00002694'))
@dp.throttled(rate=1)
async def atkxp (message: types.Message):
    con = sq.connect("game.db")
    con.row_factory = sq.Row
    cur = con.cursor()
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        xp = cur.execute(f"SELECT xp FROM players WHERE id = {user_id}" ).fetchone()
        for i in xp:
            if i >=50:
                cur.executescript(f"UPDATE players SET atkxp = atkxp + 5 WHERE id = {user_id} ")
                cur.executescript(f"UPDATE players SET xp = xp - 50 WHERE id = {user_id}")
                await message.answer("Атака (скил) + <b>5</b>", parse_mode="html")
            else:
                await message.answer("Мало опыта, для прокачки надо <b>50</b>", parse_mode="html")
@dp.message_handler(Text(equals='\U0001F6E1Защита (скил)(+2)\U0001F6E1'))
@dp.throttled(rate=1)
async def defxp (message: types.Message):
    con = sq.connect("game.db")
    con.row_factory = sq.Row
    cur = con.cursor()
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        xp = cur.execute(f"SELECT xp FROM players WHERE id = {user_id}" ).fetchone()
        for i in xp:
            if i >=200:
                cur.executescript(f"UPDATE players SET defxp = defxp + 2 WHERE id = {user_id} ")
                cur.executescript(f"UPDATE players SET xp = xp - 200 WHERE id = {user_id}")
                await message.answer("Защита (скил) + <b>2</b>", parse_mode="html")
            else:
                await message.answer("Мало опыта, для прокачки надо <b>200</b>", parse_mode="html")
    else:
        await message.answer("Зарегистрируйся!")
@dp.message_handler(Text(equals='\U00002665Макс ХП(+20)\U00002665'))
@dp.throttled(rate=1)
async def maxhp (message: types.Message):
    con = sq.connect("game.db")
    con.row_factory = sq.Row
    cur = con.cursor()
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        xp = cur.execute(f"SELECT xp FROM players WHERE id = {user_id}" ).fetchone()
        for i in xp:
            if i >=20:
                cur.executescript(f"UPDATE players SET maxhp = maxhp + 20 WHERE id = {user_id} ")
                cur.executescript(f"UPDATE players SET xp = xp - 20 WHERE id = {user_id}")
                await message.answer("Макс. ХП + <b>20</b>", parse_mode="html")
            else:
                await message.answer("Мало опыта, для прокачки надо <b>20</b>", parse_mode="html")
    else:
        await message.answer("Зарегистрируйся!")

@dp.message_handler(Text(equals='\U0001F4A7Макс МП(+1)\U0001F4A7'))
@dp.throttled(rate=1)
async def maxhp (message: types.Message):
    con = sq.connect("game.db")
    con.row_factory = sq.Row
    cur = con.cursor()
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
            a = str(cur.execute(f'SELECT profa FROM players WHERE id = {user_id}').fetchone()[0])
            if a == "Treasure Hunter":
                xp = cur.execute(f"SELECT xp FROM players WHERE id = {user_id}" ).fetchone()
                for i in xp:
                    if i >=30:
                        cur.executescript(f"UPDATE players SET maxmp = maxmp + 1 WHERE id = {user_id} ")
                        cur.executescript(f"UPDATE players SET xp = xp - 50 WHERE id = {user_id}")
                        await message.answer("Макс. МП + <b>1</b>", parse_mode="html")
                    else:
                        await message.answer("Мало опыта, для прокачки надо <b>50</b>", parse_mode="html")
            elif a == "Gladiator":
                xp = cur.execute(f"SELECT xp FROM players WHERE id = {user_id}" ).fetchone()
                for i in xp:
                    if i >=30:
                        cur.executescript(f"UPDATE players SET maxmp = maxmp + 1 WHERE id = {user_id} ")
                        cur.executescript(f"UPDATE players SET xp = xp - 50 WHERE id = {user_id}")
                        await message.answer("Макс. МП + <b>1</b>", parse_mode="html")
                    else:
                        await message.answer("Мало опыта, для прокачки надо <b>50</b>", parse_mode="html")
            elif a == "Paladin":
                xp = cur.execute(f"SELECT xp FROM players WHERE id = {user_id}" ).fetchone()
                for i in xp:
                    if i >=30:
                        cur.executescript(f"UPDATE players SET maxmp = maxmp + 1 WHERE id = {user_id} ")
                        cur.executescript(f"UPDATE players SET xp = xp - 50 WHERE id = {user_id}")
                        await message.answer("Макс. МП + <b>1</b>", parse_mode="html")
                    else:
                        await message.answer("Мало опыта, для прокачки надо <b>50</b>", parse_mode="html")
            else:
                await message.answer("Качать можно только с профой!")
@dp.message_handler(commands='top')
@dp.throttled(rate=1)
async def top (message: types.Message):
    con = sq.connect("game.db")
    cur = con.cursor()
    cur.execute(f"SELECT nick,profa,weapon,zat,armor,zat2,tochkar,hpxp FROM players ORDER BY zat DESC LIMIT 5")
    result = cur.fetchall()
    for i, item in enumerate(result):
        reply_message = f"[{i + 1}] {item[0]} {item[1]} \n{item[2]} {item[3]} {item[4]} {item[5]} \nРб убил: {item[6]} Мобов убил: {item[7]} "
        await message.answer(reply_message)
@dp.message_handler(commands='skill')
@dp.throttled(rate=1)
async def skills (message: types.Message):
    con = sq.connect("game.db")
    con.row_factory = sq.Row
    cur = con.cursor()
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        cur.execute(f"SELECT xp FROM players WHERE id = {user_id}")
        rows = cur.fetchone()
        await message.answer(fmt.text(fmt.text('Здесь можно прокачать скилы и выбрать профу!\n<b>ПРОФА ВЫБИРАЕТСЯ СРАЗУ!!!'
                                               '\nПРОЧТИ ИНФОРМАЦИЮ ЗАРАНЕЕ</b>'
                                               '\nАтака (скил) + <b>5</b> - <b>50xp</b>'
                                               '\nЗащита (скил) + <b>2</b> - <b>200xp</b>'
                                               '\nМакс. ХП + <b>20</b> - <b>20xp</b>'
                                               '\nМакс. МП + <b>1</b> - <b>50xp</b>'
                                               '\nУ тебя XP =', fmt.hbold(rows['xp']))),reply_markup=skill,parse_mode='HTML')
@dp.message_handler(Text(equals='\U0001FAACКрит(+300)Treasure Hunter\U0001FAAC(1000)')) #дагер
@dp.throttled(rate=1)
async def buffkrit_dagger(message:types.Message):
    con = sq.connect("game.db")
    con.row_factory = sq.Row
    cur = con.cursor()
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        bufff = cur.execute(f"SELECT buff FROM players where id = {user_id}").fetchone()
        for i in bufff:
            if i < 3:
                profa = cur.execute(f"SELECT profa FROM players where id = {user_id}").fetchone()
                for i in profa:
                    if i == 'Paladin':
                        await message.answer("Только для Treasure Hunter")
                    elif i == 'Gladiator':
                        await message.answer("Только для Treasure Hunter")
                    elif i == '0':
                        await message.answer("Только для Treasure Hunter")
                    elif i != (("Gladiator") or ("Paladin")):
                        weapon = cur.execute(f"SELECT gold FROM players where id = {user_id}").fetchone()
                        for i in weapon:
                            if i >= 1000:
                                cur.executescript(f"UPDATE players SET krit = krit+300,gold = gold - 1000  WHERE id = {user_id} ")
                                cur.executescript(f"UPDATE players SET buff = buff+1  WHERE id = {user_id} ")
                                await message.answer('Бафф крит +300')
                                await asyncio.sleep(300)
                                cur.executescript(f"UPDATE players SET krit = krit-300  WHERE id = {user_id} ")
                                cur.executescript(f"UPDATE players SET buff = buff-1  WHERE id = {user_id} ")
                                await message.answer('Бафф закончился, крит -300')
                            else:
                                await message.answer('Недостаточно Adena, нужно 1000')
            else:
                await message.answer('У тебя максимальное колличество баффов(3)')
@dp.message_handler(Text(equals='\U0001FAACАтака(+250)Gladiator\U0001FAAC(1000)'))  # воин
@dp.throttled(rate=1)
async def buffatk_war(message: types.Message):
    con = sq.connect("game.db")
    con.row_factory = sq.Row
    cur = con.cursor()
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        bufff = cur.execute(f"SELECT buff FROM players where id = {user_id}").fetchone()
        for i in bufff:
            if i < 3:
                profa = cur.execute(f"SELECT profa FROM players where id = {user_id}").fetchone()
                for i in profa:
                    if i == 'Paladin':
                        await message.answer("Только для Gladiator")
                    elif i == 'Treasure Hunter':
                        await message.answer("Только для Gladiator")
                    elif i == '0':
                        await message.answer("Только для Gladiator")
                    elif i != (("Treasure Hunter") or ("Paladin")):
                        weapon = cur.execute(f"SELECT gold FROM players where id = {user_id}").fetchone()
                        for i in weapon:
                            if i >= 1000:
                                cur.executescript(f"UPDATE players SET atkxp = atkxp+250,gold = gold - 1000  WHERE id = {user_id} ")
                                cur.executescript(f"UPDATE players SET buff = buff+1  WHERE id = {user_id} ")
                                await message.answer('Бафф атака +250')
                                await asyncio.sleep(300)
                                cur.executescript(f"UPDATE players SET atkxp = atkxp-250  WHERE id = {user_id} ")
                                cur.executescript(f"UPDATE players SET buff = buff-1  WHERE id = {user_id} ")
                                await message.answer('Бафф закончился, атака -250')
                            else:
                                await message.answer('Недостаточно Adena, нужно 1000')
            else:
                await message.answer('У тебя максимальное колличество баффов(3)')
@dp.message_handler(Text(equals='\U0001FAACЗащита(+100)Paladin\U0001FAAC(1000)'))  # танк
@dp.throttled(rate=1)
async def buffdef_tank(message: types.Message):
    con = sq.connect("game.db")
    con.row_factory = sq.Row
    cur = con.cursor()
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        bufff = cur.execute(f"SELECT buff FROM players where id = {user_id}").fetchone()
        for i in bufff:
            if i < 3:
                profa = cur.execute(f"SELECT profa FROM players where id = {user_id}").fetchone()
                for i in profa:
                    if i == 'Gladiator':
                        await message.answer("Только для Paladin")
                    elif i == 'Treasure Hunter':
                        await message.answer("Только для Paladin")
                    elif i == '0':
                        await message.answer("Только для Paladin")
                    elif i != (("Treasure Hunter") or ("Gladiatorn")):
                        weapon = cur.execute(f"SELECT gold FROM players where id = {user_id}").fetchone()
                        for i in weapon:
                            if i >= 1000:
                                cur.executescript(f"UPDATE players SET defxp = defxp+100,gold = gold - 1000 WHERE id = {user_id} ")
                                cur.executescript(f"UPDATE players SET buff = buff+1  WHERE id = {user_id} ")
                                await message.answer('Бафф защита +300')
                                await asyncio.sleep(300)
                                cur.executescript(f"UPDATE players SET defxp = defxp-100  WHERE id = {user_id} ")
                                cur.executescript(f"UPDATE players SET buff = buff-1  WHERE id = {user_id} ")
                                await message.answer('Бафф закончился, защита -300')
                            else:
                                await message.answer('Недостаточно Adena, нужно 1000')
            else:
                await message.answer('У тебя максимальное колличество баффов(3)')
@dp.message_handler(Text(equals='\U0001FAACХп(+1000)(Все профы)\U0001FAAC(500)'))  # дагер, воин, танк
@dp.throttled(rate=1)
async def buffhp(message: types.Message):
    con = sq.connect("game.db")
    con.row_factory = sq.Row
    cur = con.cursor()
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        bufff = cur.execute(f"SELECT buff FROM players where id = {user_id}").fetchone()
        for i in bufff:
            if i < 3:
                weapon = cur.execute(f"SELECT gold FROM players where id = {user_id}").fetchone()
                for i in weapon:
                    if i >= 500:
                        cur.executescript(f"UPDATE players SET maxhp = maxhp+1000,gold = gold - 500  WHERE id = {user_id} ")
                        cur.executescript(f"UPDATE players SET buff = buff+1  WHERE id = {user_id} ")
                        await message.answer('Бафф Макс.ХП +1000')
                        await asyncio.sleep(300)
                        cur.executescript(f"UPDATE players SET maxhp = maxhp-1000  WHERE id = {user_id} ")
                        cur.executescript(f"UPDATE players SET buff = buff-1  WHERE id = {user_id} ")
                        await message.answer('Бафф закончился, Макс.ХП -1000')
                    else:
                        await message.answer('Недостаточно Adena, нужно 1000')
            else:
                await message.answer('У тебя максимальное колличество баффов(3)')
@dp.message_handler(Text(equals='\U0001FAACАтака(+100)(TH,Pal)\U0001FAAC(500)'))  # дагер, танк
@dp.throttled(rate=1)
async def buffatk_dagtank(message: types.Message):
    con = sq.connect("game.db")
    con.row_factory = sq.Row
    cur = con.cursor()
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        bufff = cur.execute(f"SELECT buff FROM players where id = {user_id}").fetchone()
        for i in bufff:
            if i < 3:
                profa = cur.execute(f"SELECT profa FROM players where id = {user_id}").fetchone()
                for i in profa:
                    if i == 'Gladiator':
                        await message.answer("Только для Treasure Hunter и Paladin")
                    elif i == '0':
                        await message.answer("Только для Treasure Hunter и Paladin")
                    elif i != "Gladiator":
                        weapon = cur.execute(f"SELECT gold FROM players where id = {user_id}").fetchone()
                        for i in weapon:
                            if i >= 500:
                                cur.executescript(f"UPDATE players SET atkxp = atkxp+100,gold = gold - 500  WHERE id = {user_id} ")
                                cur.executescript(f"UPDATE players SET buff = buff+1  WHERE id = {user_id} ")
                                await message.answer('Бафф атака +100')
                                await asyncio.sleep(300)
                                cur.executescript(f"UPDATE players SET atkxp = atkxp-100  WHERE id = {user_id} ")
                                cur.executescript(f"UPDATE players SET buff = buff-1  WHERE id = {user_id} ")
                                await message.answer('Бафф закончился, атака - 100')
                            else:
                                await message.answer('Недостаточно Adena, нужно 1000')
            else:
                await message.answer('У тебя максимальное колличество баффов(3)')
@dp.message_handler(Text(equals='\U0001FAACКрит(+100)Gladiator\U0001FAAC(500)'))  # воин
@dp.throttled(rate=1)
async def buff_war(message: types.Message):
    con = sq.connect("game.db")
    con.row_factory = sq.Row
    cur = con.cursor()
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        bufff = cur.execute(f"SELECT buff FROM players where id = {user_id}").fetchone()
        for i in bufff:
            if i < 3:
                profa = cur.execute(f"SELECT profa FROM players where id = {user_id}").fetchone()
                for i in profa:
                    if i == 'Paladin':
                        await message.answer("Только для Gladiator")
                    elif i == 'Treasure Hunter':
                        await message.answer("Только для Gladiator")
                    elif i == '0':
                        await message.answer("Только для Gladiator")
                    elif i != (("Treasure Hunter") or ("Paladin")):
                        weapon = cur.execute(f"SELECT gold FROM players where id = {user_id}").fetchone()
                        for i in weapon:
                            if i >= 500:
                                cur.executescript(f"UPDATE players SET krit = krit+100,gold = gold - 500  WHERE id = {user_id} ")
                                cur.executescript(f"UPDATE players SET buff = buff+1  WHERE id = {user_id} ")
                                await message.answer('Бафф крит +100')
                                await asyncio.sleep(300)
                                cur.executescript(f"UPDATE players SET krit = krit-100  WHERE id = {user_id} ")
                                cur.executescript(f"UPDATE players SET buff = buff-1  WHERE id = {user_id} ")
                                await message.answer('Бафф закончился, крит -100')
                            else:
                                await message.answer('Недостаточно Adena, нужно 1000')
            else:
                await message.answer('У тебя максимальное колличество баффов(3)')
@dp.message_handler(Text(equals='\U0001F5E1Treasure Hunter\U0001F5E1'))
@dp.throttled(rate=1)
async def th(message: types.Message):
    con = sq.connect("game.db")
    con.row_factory = sq.Row
    cur = con.cursor()
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        profa = cur.execute(f"SELECT profa FROM players where id = {user_id}").fetchone()
        for i in profa:
            if i == "Treasure Hunter":
                await message.answer("У тебя уже есть Профа!")
            elif i == "Gladiator":
                await message.answer("У тебя уже есть Профа!")
            elif i == "Paladin":
                await message.answer("У тебя уже есть Профа!")
            elif i != (("Treasure Hunter") or ("Gladiator") or ("Paladin")):
                weapon = cur.execute(f"SELECT hpxp FROM players where id = {user_id}").fetchone()
                for i in weapon:
                    if i >= 300:
                        cur.executescript(f"UPDATE players SET profa = 'Treasure Hunter'  WHERE id = {user_id} ")
                        cur.executescript(f"UPDATE players SET krit = krit+80, atkxp = atkxp + 30, maxhp = maxhp + 400, maxmp = 10 WHERE id = {user_id} ")
                        await message.answer('Поздравляю у тебя появилась профа!')
                    else:
                        await message.answer('Недостаточно убил Мобов, нужно 300!')
@dp.message_handler(Text(equals='\U00002694Gladiator\U00002694'))
@dp.throttled(rate=1)
async def glad(message: types.Message):
    con = sq.connect("game.db")
    con.row_factory = sq.Row
    cur = con.cursor()
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        profa = cur.execute(f"SELECT profa FROM players where id = {user_id}").fetchone()
        for i in profa:
            if i == "Treasure Hunter":
                await message.answer("У тебя уже есть Профа!")
            elif i == "Gladiator":
                await message.answer("У тебя уже есть Профа!")
            elif i == "Paladin":
                await message.answer("У тебя уже есть Профа!")
            elif i != (("Treasure Hunter") or ("Gladiator") or ("Paladin")):
                weapon = cur.execute(f"SELECT hpxp FROM players where id = {user_id}").fetchone()
                for i in weapon:
                    if i >= 300:
                        cur.executescript(f"UPDATE players SET profa = 'Gladiator'  WHERE id = {user_id} ")
                        cur.executescript(f"UPDATE players SET krit = krit+20, atkxp = atkxp + 100, maxhp = maxhp + 400, maxmp = 10 WHERE id = {user_id} ")
                        await message.answer('Поздравляю у тебя появилась профа!')
                    else:
                        await message.answer('Недостаточно убил Мобов, нужно 300!')
@dp.message_handler(Text(equals='\U0001F6E1Paladin\U0001F6E1'))
@dp.throttled(rate=1)
async def pal(message: types.Message):
    con = sq.connect("game.db")
    con.row_factory = sq.Row
    cur = con.cursor()
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        profa = cur.execute(f"SELECT profa FROM players where id = {user_id}").fetchone()
        for i in profa:
            if i == "Treasure Hunter":
                await message.answer("У тебя уже есть Профа!")
            elif i == "Gladiator":
                await message.answer("У тебя уже есть Профа!")
            elif i == "Paladin":
                await message.answer("У тебя уже есть Профа!")
            elif i != (("Treasure Hunter") or ("Gladiator") or ("Paladin")):
                weapon = cur.execute(f"SELECT hpxp FROM players where id = {user_id}").fetchone()
                for i in weapon:
                    if i >= 300:
                        cur.executescript(f"UPDATE players SET profa = 'Paladin'  WHERE id = {user_id} ")
                        cur.executescript(f"UPDATE players SET defxp= defxp + 20, atkxp = atkxp + 30, maxhp = maxhp + 1000, maxmp = 10 WHERE id = {user_id} ")
                        await message.answer('Поздравляю у тебя появилась профа!')
                    else:
                        await message.answer('Недостаточно убил Мобов, нужно 300!')
@dp.message_handler(Text(equals='\U0001F914Информация о профах\U0001F914'))
@dp.throttled(rate=1)
async def pal(message: types.Message):
    await message.answer("\U0001F5E1<b>Treasure Hunter</b>\U0001F5E1\nКрит + 80, Атака + 30, Макс.ХП + 400, МП + 10"
                         "\nСтановится достпупен скил:\n<b>Крит+</b>  (50% шанс + 4 крит за 500 Aden)"
                         "\n\n\U0001F6E1<b>Paladin</b>\U0001F6E1 \nЗащита + 20, Атака + 30, Макс.ХП + 1000, МП + 10"
                         "\nСтановится доступен скил:\n<b>Макс.ХП+</b>  (50% шанс + 100 Макс.ХП за 500 Aden)"
                         "\n\n\U00002694<b>Gladiator</b>\U00002694 \nКрит + 20, Атака + 100, Макс.ХП + 400, МП + 10"
                         "\nСтановится доступен скил:\n<b>Атака+</b> (50% шанс + 2 Атака (cкил) за 500 Aden)"
                         "\n\n<b>У ВСЕХ ПРОФ ПОЯВЛЯЮТСЯ ОСОБЫЕ БАФЫ команда /buff</b>"
                         "\n\n<b>У ВСЕХ ПРОФ ПОЯВЛЯЮТСЯ ОСОБЫЕ СКИЛЫ в битве с RB!</b>",parse_mode="html")
@dp.message_handler(Text(equals='\U0001F5E1Крит+\U0001F5E1')) #дагер
@dp.throttled(rate=1)
async def buffkrit_dagger(message:types.Message):
    con = sq.connect("game.db")
    con.row_factory = sq.Row
    cur = con.cursor()
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        profa = cur.execute(f"SELECT profa FROM players where id = {user_id}").fetchone()
        for i in profa:
            if i == 'Paladin':
                await message.answer("Только для Treasure Hunter")
            elif i == 'Gladiator':
                await message.answer("Только для Treasure Hunter")
            elif i == '0':
                await message.answer("Только для Treasure Hunter")
            elif i != (("Gladiator") or ("Paladin")):
                gokd = cur.execute(f"SELECT gold FROM players where id = {user_id}").fetchone()
                for i in gokd:
                    if i >= 500:
                        e = int(random.randrange(100))
                        if e > 55:
                            cur.executescript(f"UPDATE players SET krit = krit+4,gold = gold - 500  WHERE id = {user_id} ")
                            await message.answer('Крит +4')
                        else:
                            cur.executescript(f"UPDATE players SET gold = gold - 500  WHERE id = {user_id} ")
                            await message.answer('Неудача')
                    else:
                        await message.answer('Недостаточно Aden')
@dp.message_handler(Text(equals='\U0001F6E1Макс.ХП+\U0001F6E1')) #дагер
@dp.throttled(rate=1)
async def buffkrit_dagger(message:types.Message):
    con = sq.connect("game.db")
    con.row_factory = sq.Row
    cur = con.cursor()
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        profa = cur.execute(f"SELECT profa FROM players where id = {user_id}").fetchone()
        for i in profa:
            if i == 'Treasure Hunter':
                await message.answer("Только для Paladin")
            elif i == 'Gladiator':
                await message.answer("Только для Paladin")
            elif i == '0':
                await message.answer("Только для Paladin")
            elif i != (("Gladiator") or ("Treasure Hunter")):
                gokd = cur.execute(f"SELECT gold FROM players where id = {user_id}").fetchone()
                for i in gokd:
                    if i >= 500:
                        e = int(random.randrange(100))
                        if e > 55:
                            cur.executescript(f"UPDATE players SET maxhp = maxhp+100,gold = gold - 500  WHERE id = {user_id} ")
                            await message.answer('Макс.ХП +100')
                        else:
                            cur.executescript(f"UPDATE players SET gold = gold - 500  WHERE id = {user_id} ")
                            await message.answer('Неудача')
                    else:
                        await message.answer('Недостаточно Aden')
@dp.message_handler(Text(equals='\U00002694Атака+\U00002694')) #дагер
@dp.throttled(rate=1)
async def buffkrit_dagger(message:types.Message):
    con = sq.connect("game.db")
    con.row_factory = sq.Row
    cur = con.cursor()
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        profa = cur.execute(f"SELECT profa FROM players where id = {user_id}").fetchone()
        for i in profa:
            if i == 'Treasure Hunter':
                await message.answer("Только для Gladiator")
            elif i == 'Paladin':
                await message.answer("Только для Gladiator")
            elif i == '0':
                await message.answer("Только для Gladiator")
            elif i != (("Treasure Hunter") or ("Paladin")):
                gokd = cur.execute(f"SELECT gold FROM players where id = {user_id}").fetchone()
                for i in gokd:
                    if i >= 500:
                        e = int(random.randrange(100))
                        if e > 55:
                            cur.executescript(f"UPDATE players SET atkxp = atkxp+2,gold = gold - 500  WHERE id = {user_id} ")
                            await message.answer('Атака (скил) +2')
                        else:
                            cur.executescript(f"UPDATE players SET gold = gold - 500  WHERE id = {user_id} ")
                            await message.answer('Неудача')
                    else:
                        await message.answer('Недостаточно Aden')

@dp.message_handler(Text(equals='\U00002049Квесты\U00002049'))
@dp.throttled(rate=1)
async def pal22(message: types.Message):
    await message.answer("Здесь ты сможешь найти задания",reply_markup=quest)

@dp.message_handler(Text(equals='\U0001F198Сага Кладоискателя'))
@dp.throttled(rate=1)
async def pal33(message: types.Message):
    con = sq.connect("game.db")
    con.row_factory = sq.Row
    cur = con.cursor()
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        photo = open('quest1.jpg', 'rb')
        await bot.send_photo(message.chat.id, photo =photo,caption= 'Путник, я вижу тебе не чем занятся? Хочешь получить немного ресов? '
                             '\nПринеси мне <b>30</b> чешуи аллигаторов и <b>20</b> яиц дино\n\nТааак посмотрим сколько там у тебя их, подожди пару секунд', parse_mode="html")
        await asyncio.sleep(3)
        d = int(cur.execute(f"SELECT dinoq FROM players where id = {user_id}").fetchone()[0])
        a = int(cur.execute(f"SELECT aliq FROM players where id = {user_id}").fetchone()[0])
        if ((a >= 30) and (d >= 20)):
            cur.executescript(f"UPDATE players SET dinoq = dinoq - 20,aliq = aliq - 30, minirb = minirb + 15, dion = dion +5 WHERE id = {user_id}")
            await message.answer("Спасибо тебе! Вот держи \nIrone Ore = <b>15</b>\nBlue Gemstone = <b>5</b>",parse_mode="html")
        else:
            await message.answer("Маловато, нужно больше иди и сражайся, если хочешь награду!")

@dp.message_handler(Text(equals='\U0001F198Во имя отца'))
@dp.throttled(rate=1)
async def pal333(message: types.Message):
    con = sq.connect("game.db")
    con.row_factory = sq.Row
    cur = con.cursor()
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        photo = open('quest2.jpg','rb')
        await bot.send_photo(message.chat.id, photo =photo,caption= 'Воин ты что пришёл ко мне за заданием? У меня как раз есть для тебя.'
                             '\nПринеси мне <b>25</b> черепов носорогов и <b>25</b> хвостов буфало\n\nНу что ты там принёс? Дай гляну, подожди пару секунд', parse_mode="html")
        await asyncio.sleep(3)
        d = int(cur.execute(f"SELECT nosq FROM players where id = {user_id}").fetchone()[0])
        a = int(cur.execute(f"SELECT bufq FROM players where id = {user_id}").fetchone()[0])
        if ((a >= 25) and (d >= 25)):
            cur.executescript(f"UPDATE players SET nosq = nosq - 25,bufq = bufq - 25, Varnish = Varnish + 15, dion = dion +15 WHERE id = {user_id}")
            await message.answer("Спасибо тебе! Вот держи \nVarnish = <b>15</b>"
                                 "\nBlue Gemstone = <b>15</b>", parse_mode="html")
        else:
            await message.answer("Маловато, нужно больше иди и сражайся, если хочешь награду!")

@dp.message_handler(Text(equals='\U0001F198История Рыцаря Ада'))
@dp.throttled(rate=1)
async def pal444(message: types.Message):
    con = sq.connect("game.db")
    con.row_factory = sq.Row
    cur = con.cursor()
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        photo = open('quest3.jpg', 'rb')
        await bot.send_photo(message.chat.id, photo=photo,
                             caption='Ну что вот ты и пришёл ко мне, я долго тебя ждал думаю ты очень хочешь '
                             'принести мне <b>25</b> кусков плоти льва и <b>25</b> костей медведя, не так ли?\n\nНу как покажи, что ты там держишь', parse_mode="html")
        await asyncio.sleep(3)
        d = int(cur.execute(f"SELECT lionq FROM players where id = {user_id}").fetchone()[0])
        a = int(cur.execute(f"SELECT bearq FROM players where id = {user_id}").fetchone()[0])
        if ((a >= 25) and (d >= 25)):
            cur.executescript(f"UPDATE players SET bearq = bearq - 25,lionq = lionq - 25, minirb = minirb + 25, varnish = varnish + 10 WHERE id = {user_id}")
            await message.answer("Спасибо тебе! Вот держи \nIrone Ore = <b>25</b>\nVarnish = <b>10</b>",parse_mode="html")
        else:
            await message.answer("Маловато, нужно больше иди и сражайся, если хочешь награду!")

@dp.message_handler(commands='quest')
@dp.throttled(rate=1)
async def quest (message: types.Message):
    con.row_factory = sq.Row
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        cur.execute(f"SELECT dinoq,nosq,aliq,lionq,bufq,bearq FROM players WHERE id = {user_id}")
        rows = cur.fetchone()
        await message.answer(fmt.text(fmt.text('<b>Квестовые предметы:</b>\n\U0001FA72Чешуя аллигатора:', fmt.hbold(rows['aliq']),
                                               '\n\U0001FABAЯйца дракона:', fmt.hbold(rows['dinoq']),
                                               '\n\U0001F480Череп носорога', fmt.hbold(rows['nosq']),
                                               '\n\U0001F969Плоть льва', fmt.hbold(rows['lionq']),
                                               '\n\U0001FAA2Хвост буфало', fmt.hbold(rows['bufq']),
                                               '\n\U0001F9B4Кость медведя',fmt.hbold(rows['bearq']),
                                               )), parse_mode="HTML")



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        skip_updates=True,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )




