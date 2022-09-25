import asyncio
import logging
import os
import random
import aiogram.utils.markdown as fmt
import psycopg2
from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove
from aiogram.utils.exceptions import Throttled
from aiogram.utils.executor import start_webhook

from keyboards import *
from lock import Catacombs,craft_s,rb3,Rb2,PVP,Rb
from lock import giran, Aden, Dion, Profi, godart,shop_don
from lock import rb4
from skilsss import *

Profi.register_profi(dp)
Dion.register_dion(dp)
giran.register_giran(dp)
Catacombs.register_catacombs(dp)
Rb.register_rb(dp)
Aden.register_aden(dp)
Rb.register_rb(dp)
godart.register_goddart(dp)

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


# with sq.connect("game.db") as con:
#     cur = con.cursor()
#     cur.execute("""CREATE TABLE IF NOT EXISTS players (
#     id integer ,nick TEXT, zat INTEGER ,Krit INTEGER ,def INTEGER ,atk INTEGER ,atkxp INTEGER ,
#     hp integer ,hpxp integer ,xp integer ,RB1 INTEGER ,RB2 INTEGER ,RB3 INTEGER ,
#     tochkab INTEGER, tochkam TEXT, tochkar INTEGER, minirb INTEGER , mob1 INTEGER ,
#     mob2 INTEGER , mob3 INTEGER, minirb2 INTEGER, Weapon TEXT, dion integer, giran TEXT, aden TEXT,
#     mob4 integer, mob5 integer, mob6 integer, minirb3 integer, mob7 integer, mob8 integer, mob9 integer,
#     mob10 integer, armor TEXT, gold integer, defxp integer, maxhp integer, zat2 integer,
#      profa text,sp integer,srec text, Varnish integer,rbfight integer,mp integer,
#      maxmp integer,hpbanka integer,mpbanka integer,mob11 integer,mob12 integer,dinoq integer,nosq integer,
#      aliq integer,bufq integer,lionq integer,bearq integer,mobr integer,mobra integer,jinq integer,
#      akuq integer,pvphp integer,pvpatk integer,pvpdef integer,pvpnick text,pvpkrit integer,pvpwin integer,pvplose integer,
#      pvppoint integer,pvpdmg integer,pvpcp integer,hpcp integer,pvpmp integer,mob13 integer,
#      mob14 integer,mob15 integer,mob16 integer,tree integer,save integer,zub integer,
#      dwarf integer,elf integer,hum integer,race text,rb4 integer,name text,
#      wolf1 integer,wolf2 integer,wolfrb integer,lshp integer, lsmp unteger,ls1 integer,ls2 integer,
#      ls3 integer,kill integer,krits integer,pvpkrits integer,sop integer)""")
#     cur.execute("""CREATE TABLE IF NOT EXISTS rbboss (rb1 integer, rb2 integer)""")
con = psycopg2.connect(DB_URI,sslmode = 'require')
cur = con.cursor()
@dp.message_handler(commands=['start'])
@dp.throttled(rate=1)
async def start1(message: types.Message):
    user_id = message.from_user.id
    nick = message.from_user.username
    df = "Demon Fang(D) +"
    bs = "Brigandine Set(D) +"
    rec = "0"
    rec2 = "0"
    atr = "\U0001F5E1"
    name = message.from_user.first_name
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is None:
        cur.execute(f'INSERT INTO players(id ,nick , zat ,Krit ,def  ,atk  ,atkxp ,hp  ,hpxp  ,'
                    f'xp  ,RB1  ,RB2  ,RB3  , tochkab , tochkam , tochkar , minirb  , mob1 ,mob2  , mob3 , minirb2 , Weapon , dion ,'
                    f' giran , aden ,mob4 , mob5, mob6 , minirb3 , mob7 , mob8 , mob9 ,mob10 , armor , gold , defxp ,'
                    f' maxhp , zat2 ,profa ,sp ,srec , Varnish ,rbfight ,mp ,maxmp ,hpbanka ,mpbanka ,mob11 ,mob12 ,dinoq ,'
                    f' nosq ,aliq ,bufq ,lionq ,bearq ,mobr ,mobra,jinq ,akuq ,pvphp ,pvpatk ,pvpdef ,'
                    f'pvpnick ,pvpkrit ,pvpwin ,pvplose ,pvppoint ,pvpdmg ,pvpcp ,hpcp ,pvpmp ,mob13 ,'
                    f'mob14 ,mob15 ,mob16 ,tree ,save ,zub ,dwarf ,elf ,hum ,race ,rb4 ,name ,'
                    f'wolf1 ,wolf2 ,wolfrb ,lshp , lsmp ,ls1 ,ls2 ,ls3 ,kill ,krits ,pvpkrits ,'
                    f'sop,pvpid,rank,mob17,mob18,mob19,mob20,lvl,lvlup,prem1,prem2,aa,rb5,mdef,ice,iceinfo,fireinfo,fire,pvpice,pvpmdef)  VALUES (%s,%s,0,1,1,5,0,200,0,0,10000,'
                          f'50000,150000,0,0,0,0,100,600,1200,200000,'
                          f'%s,0,0,0,2000,3600,5000,400000,6400,10000,11000,13000,'
                          f'%s,1000,0,200,0,%s,0,%s,0,0,10,10,0,0,16000,16000,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'
                    f'0,0,0,0,0,0,0,20000,24000,30000,36000,0,0,0,0,0,0,0,800000,%s,'
                    f'8000,12000,150000,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,20,1,0,0,1350000,1,0,%s,0,0,0,0)',(user_id,nick,df,bs,rec,rec2,name,atr))
        con.commit()
        await message.answer('Вы зарегистрированы, введи ещё раз /start для выбора расы')
    else:
        await message.answer('\U0001F385Dwarf - <i>+5% к шансу заточки</i>\n\U0001F9DDElf - <i>+Требуется меньше опыта при прокачке Атака(скил)</i>'
                             '\n\U0001F9D4Human - <i>Требуется меньше опыта при прокачке Макс.ХП</i>',parse_mode="HTML",reply_markup=race)
@dp.message_handler(Text(equals="\U0001F385Dwarf\U0001F385"))
@dp.throttled(rate=1)
async def dwraf(message: types.Message):
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        cur.execute(f'SELECT dwarf,elf,hum FROM players WHERE id = {user_id}')
        race = cur.fetchone()
        if race[0] == 5:
            await message.answer("Ты уже выбрал расу!")
        elif race[1] == 1:
            await message.answer("Ты уже выбрал расу!")
        elif race[2] == 1:
            await message.answer("Ты уже выбрал расу!")
        else:
            cur.execute(f"UPDATE players SET dwarf = 5,race = '\U0001F385Dwarf' WHERE id = {user_id} ")
            con.commit()
            await message.answer("Теперь ты Dwarf",reply_markup = ReplyKeyboardRemove())
@dp.message_handler(Text(equals="\U0001F9DDElf\U0001F9DD"))
@dp.throttled(rate=1)
async def elf(message: types.Message):
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        cur.execute(f'SELECT dwarf,elf,hum FROM players WHERE id = {user_id}')
        race = cur.fetchone()
        if race[0] == 5:
            await message.answer("Ты уже выбрал расу!")
        elif race[1] == 1:
            await message.answer("Ты уже выбрал расу!")
        elif race[2] == 1:
            await message.answer("Ты уже выбрал расу!")
        else:
            cur.execute(f"UPDATE players SET elf = 1,race = '\U0001F9DDElf' WHERE id = {user_id} ")
            con.commit()
            await message.answer("Теперь ты Elf",reply_markup = ReplyKeyboardRemove())
@dp.message_handler(Text(equals="\U0001F9D4Human\U0001F9D4"))
@dp.throttled(rate=1)
async def hum(message: types.Message):
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        cur.execute(f'SELECT dwarf,elf,hum FROM players WHERE id = {user_id}')
        race = cur.fetchone()
        if race[0] == 5:
            await message.answer("Ты уже выбрал расу!")
        elif race[1] == 1:
            await message.answer("Ты уже выбрал расу!")
        elif race[2] == 1:
            await message.answer("Ты уже выбрал расу!")
        else:
            cur.execute(f"UPDATE players SET hum = 1,race = '\U0001F9D4Human' WHERE id = {user_id} ")
            con.commit()
            await message.answer("Теперь ты Human",reply_markup = ReplyKeyboardRemove())
@dp.message_handler(commands=['sp'])
@dp.throttled(rate=1)
async def spp(message: types.Message):
    await message.answer(("\U0001F4D3Прокачать характеристики за Sp\U0001F4D3\n\n<b>!Только когда у тебя будет минимум 1250 черепов мобов!</b>"
                          "\nSp можно получить путём обмена на черепа мобов.\n<b>1 Sp = 250</b> черепов"),parse_mode="html", reply_markup = buff)
@dp.message_handler(Text(equals="\U0001F4D3Получить Sp\U0001F4D3"))
@dp.throttled(rate=1)
async def sp_get(message: types.Message):
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        cur.execute(f'SELECT hpxp FROM players WHERE id = {user_id}')
        hp = cur.fetchone()
        if hp[0] > 1250:
            cur.execute(f"UPDATE players SET sp = sp + 1, hpxp = hpxp - 250 WHERE id = {user_id} ")
            con.commit()
            await message.answer("Ты получил 1 Sp")
        else:
            await message.answer("Нужно минимум 1250 чтобы можно было обменять")

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
@dp.message_handler(Text(equals='\U0001F687Catacombs\U0001F687'))
@dp.throttled(rate=1)
async def catss(message: types.Message):
  await message.answer(("<i>\U0001F92FДобро пожаловать в катакомбы!"
                        " Здесь ты найдёшь опасных врагов с которых падает уникальный дроп,"
                        " вход платный <b>2000 Aden</b></i>"),parse_mode="html", reply_markup = cats)

@dp.message_handler(Text(equals='Heretics Catacomb'))
@dp.throttled(rate=1)
async def catssher(message: types.Message):
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        photo = open('wolf.jpg', 'rb')
        cur.execute(f'SELECT gold FROM players WHERE id = {user_id}')
        gold = cur.fetchone()
        if gold[0] >= 2000:
            cur.execute(f"UPDATE players SET gold = gold - 2000 where id = {user_id}")
            con.commit()
            await bot.send_photo(message.chat.id, photo=photo, caption="Ты атакуешь", reply_markup = hercat)
        else:
            await message.answer("Не хватает Aden")
@dp.message_handler(Text(equals='\U0001F54DTown of Giran\U0001F54D'))
@dp.throttled(rate=1)
async def giran2(message: types.Message):
  await message.answer(("Ты Атакуешь"), reply_markup = giran1)
@dp.message_handler(Text(equals='\U0001F3F0Town of Aden\U0001F3F0'))
@dp.throttled(rate=1)
async def adentown(message: types.Message):
  await message.answer(("Ты Атакуешь"), reply_markup = aden)

@dp.message_handler(Text(equals='\U0001F3EFTown of Goddart\U0001F3EF'))
@dp.throttled(rate=1)
async def goddarttown(message: types.Message):
  await message.answer(("Ты Атакуешь"), reply_markup = goddart)
@dp.message_handler(Text(equals="\U0001F30BRaid Boss's\U0001F30B"))
@dp.throttled(rate=1)
async def rb1(message: types.Message):
  await message.answer(("Здарова"),parse_mode="html", reply_markup = rb)
@dp.message_handler(commands=['res'])
@dp.throttled(rate=1)
async def craftm(message: types.Message):
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        cur.execute(f"SELECT minirb,dion,giran,aden,srec,Varnish,ls1,ls2,ls3,sop FROM players WHERE id = {user_id}")
        res = cur.fetchone()
        await message.answer(fmt.text(fmt.text('\n<b>Ресурсы:</b>'
                                               '         \n\U0001F9F1Iron Ore:',fmt.hbold(res[0]),
                                               '         \n\U0001F9FFBlue Gemstone:',fmt.hbold(res[1]),
                                                        '\n\U0001F943Varnish:',fmt.hbold(res[5]),
                                               '\n\U0001F3D0SOP:', fmt.hbold(res[9]),
                                               '\n\U0001F4D5Красная краска:', fmt.hbold(res[6]),
                                               '\n\U0001F4D8Синяя краска:', fmt.hbold(res[7]),
                                               '\n\U0001F4D7Зелёная краска:', fmt.hbold(res[8]),
                                               '\n\n<b>Рецепты:</b>',
                                                         '\n(B)\U0001F4DC',(res[2]),
                                                         '\n(A)\U0001F4DC',(res[3]),
                                                         '\n(S)\U0001F4DC',(res[4])
                                               )),parse_mode= "html")
@dp.message_handler(Text(equals="\U0001F377ХП банка\U0001F377(RB)(300)"))
@dp.throttled(rate=1)
async def hpbanka(message: types.Message):
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        cur.execute(f'SELECT gold,rbfight,hpbanka FROM players WHERE id = {user_id}')
        gg = cur.fetchone()
        if gg[0] >=300:
            if gg[1] == 0:
                if gg[2] < 5:
                    cur.execute(f"UPDATE players SET hpbanka = hpbanka + 1, gold = gold - 300 WHERE id = {user_id} ")
                    con.commit()
                    await message.answer("Ты купил  ХП банку")
                elif gg[2] >= 5:
                    await message.answer("Максимум 5 банок!")
            else:
                await message.answer("Ты можешь купить банки ещё, но только после смерти RB или твоей!")
        else:
            await message.answer('Не хватает Aden')
@dp.message_handler(Text(equals="\U0001F9CAМП банка\U0001F9CA(RB)(400)"))
@dp.throttled(rate=1)
async def mpbanka(message: types.Message):
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        cur.execute(f'SELECT gold,rbfight,mpbanka FROM players WHERE id = {user_id}')
        gg = cur.fetchone()
        if gg[0] >=300:
            if gg[1] == 0:
                if gg[2] < 5:
                    cur.execute(f"UPDATE players SET mpbanka = mpbanka + 1, gold = gold - 400 WHERE id = {user_id} ")
                    con.commit()
                    await message.answer("Ты купил  МП банку")
                elif gg[2] >= 5:
                    await message.answer("Максимум 5 банок!")
            else:
                await message.answer("Ты можешь купить банки ещё, но только после смерти RB или твоей!")
        else:
            await message.answer('Не хватает Aden')
@dp.message_handler(Text(equals='\U0001F4B0Продажа материалов\U0001F4B0'))
@dp.throttled(rate=1)
async def sellshop(message: types.Message):
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        cur.execute(f"SELECT minirb,dion,Varnish,gold FROM players WHERE id = {user_id}")
        rows = cur.fetchone()
        await message.answer(fmt.text(fmt.text('У тебя:','\n\U0001F9F1Iron Ore:', fmt.hbold(rows[0]),
                                               '\n\U0001F9FFBlue Gemstone:', fmt.hbold(rows[1]),
                                               '\n\U0001F943Varnish:', fmt.hbold(rows[2]),
                                               '\n\U0001FA99Aden:', fmt.hbold(rows[3]))), parse_mode="HTML",reply_markup=sell)

@dp.message_handler(Text(equals='\U0001FA72Чешуя Аллигатора(100 штук -1к Aden)'))
@dp.throttled(rate=1)
async def sellali(message: types.Message):
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        cur.execute(f"SELECT aliq FROM players WHERE id = {user_id}")
        gold = cur.fetchone()
        if gold[0] >= 100:
            cur.execute(f"UPDATE players SET aliq = aliq - 100, gold = gold + 1000 WHERE id = {user_id} ")
            con.commit()
            await message.answer(fmt.text(fmt.text('Ты продал Чешую Аллигатора, Adena +', fmt.hbold('1000'))),
                                 parse_mode="HTML")
        elif gold[0] < 100:
            await message.answer("У тебя нет Чешуи Аллигатора")
@dp.message_handler(Text(equals='\U0001F9F1Iron Ore (100)'))
@dp.throttled(rate=1)
async def sellshop(message: types.Message):
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        cur.execute(f"SELECT minirb FROM players WHERE id = {user_id}")
        gold = cur.fetchone()
        if gold[0] >= 1:
            cur.execute(f"UPDATE players SET minirb = minirb - 1, gold = gold + 100 WHERE id = {user_id} ")
            con.commit()
            await message.answer(fmt.text(fmt.text('Ты продал Iron Ore, Adena +', fmt.hbold('100'))),
                                 parse_mode="HTML")
        else:
            await message.answer("У тебя нет Iron Ore")
@dp.message_handler(Text(equals='\U0001F9FFBlue Gemstone (200)'))
@dp.throttled(rate=1)
async def sellshop(message: types.Message):
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        cur.execute(f"SELECT dion FROM players WHERE id = {user_id}")
        gold = cur.fetchone()
        if gold[0] >= 1:
            cur.execute(f"UPDATE players SET dion = dion - 1, gold = gold + 200 WHERE id = {user_id} ")
            con.commit()
            await message.answer(fmt.text(fmt.text('Ты продал Blue Gemstone, Adena +', fmt.hbold('200'))),
                                 parse_mode="HTML")
        else:
            await message.answer("У тебя нет Blue Gemstone")
@dp.message_handler(Text(equals='\U0001F943Varnish (300)'))
@dp.throttled(rate=1)
async def sellshop(message: types.Message):
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        cur.execute(f"SELECT Varnish FROM players WHERE id = {user_id}")
        gold = cur.fetchone()
        if gold[0] >= 1:
            cur.execute(f"UPDATE players SET Varnish = Varnish - 1, gold = gold + 300 WHERE id = {user_id} ")
            con.commit()
            await message.answer(fmt.text(fmt.text('Ты продал Varnish, Adena +', fmt.hbold('300'))),
                                 parse_mode="HTML")
        else:
            await message.answer("У тебя нет Varnish")

@dp.message_handler(Text(equals='Продажа B рецепта(3000)'))
@dp.throttled(rate=1)
async def sellshop(message: types.Message):
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        cur.execute(f"SELECT giran FROM players WHERE id = {user_id}")
        rec = cur.fetchone()
        if rec[0] == "Earing of Black Ore(B)":
            cur.execute(f"UPDATE players SET giran = 0, gold = gold + 3000 WHERE id = {user_id} ")
            con.commit()
            await message.answer(fmt.text(fmt.text('Ты продал рецепт, Adena +', fmt.hbold('3000'))),
                                 parse_mode="HTML")
        elif rec[0] == "Blue Wolf Armor(B)":
            cur.execute(f"UPDATE players SET giran = 0, gold = gold + 3000 WHERE id = {user_id} ")
            con.commit()
            await message.answer(fmt.text(fmt.text('Ты продал рецепт, Adena +', fmt.hbold('3000'))),
                                 parse_mode="HTML")
        else:
            await message.answer("У тебя нет рецепта")
@dp.message_handler(Text(equals='Продажа A рецептов(10000)'))
@dp.throttled(rate=1)
async def sellshop(message: types.Message):
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        cur.execute(f"SELECT aden FROM players WHERE id = {user_id}")
        reca = cur.fetchone()
        if reca[0] == "Sword of Miracles(A)90%":
            cur.execute(f"UPDATE players SET aden = 0, gold = gold + 10000 WHERE id = {user_id} ")
            con.commit()
            await message.answer(fmt.text(fmt.text('Ты продал рецепт, Adena +', fmt.hbold('10000'))),
                                 parse_mode="HTML")
        elif reca[0] == "Dark Crystal Armor(A)90%":
            cur.execute(f"UPDATE players SET aden = 0, gold = gold + 10000 WHERE id = {user_id} ")
            con.commit()
            await message.answer(fmt.text(fmt.text('Ты продал рецепт, Adena +', fmt.hbold('10000'))),
                                 parse_mode="HTML")
        elif reca[0] == "Majestic Necklace(A)(90%)":
            cur.execute(f"UPDATE players SET aden = 0, gold = gold + 10000 WHERE id = {user_id} ")
            con.commit()
            await message.answer(fmt.text(fmt.text('Ты продал рецепт, Adena +', fmt.hbold('10000'))),
                                 parse_mode="HTML")
        else:
            await message.answer("У тебя нет рецепта")

@dp.message_handler(Text(equals='Продажа S рецептов(30000)'))
@dp.throttled(rate=1)
async def sellshop(message: types.Message):
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        cur.execute(f"SELECT srec FROM players WHERE id = {user_id}")
        gold = cur.fetchone()
        if gold[0] == "Imperial Crusader Set(S)(70%)":
            cur.execute(f"UPDATE players SET srec = 0, gold = gold + 30000 WHERE id = {user_id} ")
            con.commit()
            await message.answer(fmt.text(fmt.text('Ты продал рецепт, Adena +', fmt.hbold('30000'))),
                                 parse_mode="HTML")
        elif gold[0] == "Tateossian Necklace(S)(70%)":
            cur.execute(f"UPDATE players SET srec = 0, gold = gold + 30000 WHERE id = {user_id} ")
            con.commit()
            await message.answer(fmt.text(fmt.text('Ты продал рецепт, Adena +', fmt.hbold('30000'))),
                                 parse_mode="HTML")
        elif gold[0] == "Arcane Mace (S)(70%)":
            cur.execute(f"UPDATE players SET srec = 0, gold = gold + 30000 WHERE id = {user_id} ")
            con.commit()
            await message.answer(fmt.text(fmt.text('Ты продал рецепт, Adena +', fmt.hbold('30000'))),
                                 parse_mode="HTML")
        else:
            await message.answer("У тебя нет рецепта")
@dp.message_handler(Text(equals='\U0001F4DBВыход\U0001F4DB'))
@dp.throttled(rate=1)
async def exitshop(message: types.Message):
    await message.answer("Скоро увидимся!", reply_markup = ReplyKeyboardRemove())
@dp.message_handler(commands=['tochka'])
@dp.throttled(rate=1)
async def tochka_s(message: types.Message):
  await message.answer(("<b>Точить оружие - 15%(10% у Dwarf) шанс что сломается</b>"
                        "\nDemon fang(D) - 10 Adena за 1 точку"
                        "\nHomunkulus sword(C) - 50 Adena за 1 точку"
                        "\nSword of Valhalla(B) - 200 Adena за 1 точку"
                        "\nSword of Miracles(A) - 500 Adena за 1 точку"
                        "\nArcane Mace(S) - 2000 Adena за 1 точку\n\n<b>Точить доспехи - 30%(25% у Dwarf) шанс что сломается</b>"
                        "\nBrigandine Set(D) - 20 Adena за 1 точку"
                        "\nComposite Set(C) - 60 Adena за 1 точку"
                        "\nBlue Wolf Armor(B) - 300 Adena за 1 точку"
                        "\nDark Crystal Armor(A) - 600 Adena за 1 точку"
                        "\nImperial Crusader Set(S) - 3000 Adena за 1 точку\n\n<b>Точить Блесс точкой - 60% шанс что не заточится</b>"
                        "\nДобавить Ice - 20 Blue Gemstone, 1 синяя краска"
                        "\nДобавить Fire - 20 Blue Gemstone, 2 красные краски "
                        "\n<b>ВИД АТРИБУТА МОЖЕТ БЫТЬ ТОЛЬКО 1! ПРИ ЗАМЕНЕ СТАРЫЙ ОБНУЛЯЕТСЯ!</b>"), reply_markup = tochka,parse_mode="html")
@dp.message_handler(Text(equals='Точить оружие'))
@dp.throttled(rate=1)
async def tochw(message:types.Message):
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        cur.execute(f"SELECT dwarf FROM players where id = {user_id}")
        dwarf = cur.fetchone()
        cur.execute(f"SELECT save FROM players where id = {user_id}")
        save = cur.fetchone()
        if save[0] == 0:
            cur.execute(f"SELECT gold FROM players WHERE id = {user_id}")
            gold = cur.fetchone()
            if gold[0] >= 10:
                cur.execute(f"SELECT Weapon FROM players WHERE id = {user_id}")
                weapon = cur.fetchone()
                if weapon[0] == "Demon Fang(D) +":
                    a = int(random.randrange(100))
                    if a > 85 + dwarf[0]:
                       cur.execute(f"UPDATE players SET zat = 1, atk = 5, Krit = krit - zat +1,gold = gold - 10 WHERE id = {user_id} ")
                       con.commit()
                       await message.answer(fmt.text(fmt.text('\U0000274c Сломал Demon fang(D) +', fmt.hbold('1'))), parse_mode="HTML")
                    elif a < 85 + dwarf[0]:
                       cur.execute(f"UPDATE players SET zat = zat + 1, atk = zat*5, Krit = krit + 1, gold = gold - 10 WHERE id = {user_id}")
                       con.commit()
                       cur.execute(f"SELECT zat,atk,Krit FROM players WHERE id = {user_id}")
                       rows = cur.fetchone()
                       await message.answer(fmt.text(fmt.text('\U00002728 Demon fang(D) + ', fmt.hbold(rows[0]),
                                                       'Крит:', fmt.hbold(rows[2]),
                                                       'Атака =', fmt.hbold(rows[1]))), parse_mode="HTML")
                elif weapon[0] == "Homunkulus sword(С) +":
                    a = int(random.randrange(100))
                    if a > 85 + dwarf[0]:
                       cur.execute(f"UPDATE players SET zat = 1, atk = 8, Krit = krit - zat + 1,gold = gold - 50 WHERE id = {user_id} ")
                       con.commit()
                       await message.answer(fmt.text(fmt.text('\U0000274c Сломал Homunkulus sword(С) +', fmt.hbold('1'))), parse_mode="HTML")
                    elif a < 85+ dwarf[0]:
                       cur.execute(f"UPDATE players SET zat = zat + 1, atk = zat*8, Krit = krit + 1, gold=gold -50 WHERE id = {user_id}")
                       con.commit()
                       cur.execute(f"SELECT zat,atk,Krit FROM players WHERE id = {user_id}")
                       rows = cur.fetchone()
                       await message.answer(fmt.text(fmt.text('\U00002728 Homunkulus sword(С) + ', fmt.hbold(rows[0]),
                                                       'Крит:', fmt.hbold(rows[2]),
                                                       'Атака =', fmt.hbold(rows[1]))), parse_mode="HTML")
                elif weapon[0] == "Sword of Valhalla(B) +":
                    a = int(random.randrange(100))
                    if a > 85 + dwarf[0]:
                       cur.execute(f"UPDATE players SET zat = 1, atk = 14, Krit = krit -zat + 1 ,gold = gold - 200 WHERE id = {user_id} ")
                       con.commit()
                       await message.answer(fmt.text(fmt.text('\U0000274c Сломал Sword of Valhalla(B) +', fmt.hbold('1'))), parse_mode="HTML")
                    elif a < 85 + dwarf[0]:
                       cur.execute(f"UPDATE players SET zat = zat + 1, atk = zat*14, Krit = krit +1, gold = gold -200  WHERE id = {user_id}")
                       con.commit()
                       cur.execute(f"SELECT zat,atk,Krit FROM players WHERE id = {user_id}")
                       rows = cur.fetchone()
                       await message.answer(fmt.text(fmt.text('\U00002728 Sword of Valhalla(B) + ', fmt.hbold(rows[0]),
                                                       'Крит:', fmt.hbold(rows[2]),
                                                      'Атака =', fmt.hbold(rows[1]))), parse_mode="HTML")
                elif weapon[0] == "Sword of Miracles(A) +":
                    a = int(random.randrange(100))
                    if a > 85+ dwarf[0]:
                       cur.execute(f"UPDATE players SET zat = 1, atk = 30, Krit = krit - zat + 1 ,gold = gold - 500 WHERE id = {user_id} ")
                       con.commit()
                       await message.answer(fmt.text(fmt.text('\U0000274c Сломал Sword of Miracles(A) +', fmt.hbold('1'))), parse_mode="HTML")
                    elif a < 85+ dwarf[0]:
                       cur.execute(f"UPDATE players SET zat = zat + 1, atk = zat*30, Krit = krit +1, gold = gold -500  WHERE id = {user_id}")
                       con.commit()
                       cur.execute(f"SELECT zat,atk,Krit FROM players WHERE id = {user_id}")
                       rows = cur.fetchone()
                       await message.answer(fmt.text(fmt.text('\U00002728 Sword of Miracles(A) + ', fmt.hbold(rows[0]),
                                                       'Крит:', fmt.hbold(rows[2]),
                                                      'Атака =', fmt.hbold(rows[1]))), parse_mode="HTML")
                elif weapon[0] == "Arcane Mace (S) +":
                    a = int(random.randrange(100))
                    if a >  85 + dwarf[0]:
                       cur.execute(f"UPDATE players SET zat = 1, atk = 60, Krit = krit - zat + 1 ,gold = gold - 2000 WHERE id = {user_id} ")
                       con.commit()
                       await message.answer(fmt.text(fmt.text('\U0000274c Сломал Arcane Mace (S) +', fmt.hbold('1'))), parse_mode="HTML")
                    elif a < 85 + dwarf[0]:
                       cur.execute(f"UPDATE players SET zat = zat + 1, atk = zat*60, Krit = krit +1, gold = gold - 2000  WHERE id = {user_id}")
                       con.commit()
                       cur.execute(f"SELECT zat,atk,Krit FROM players WHERE id = {user_id}")
                       rows = cur.fetchone()
                       await message.answer(fmt.text(fmt.text('\U00002728 Arcane Mace (S) + ', fmt.hbold(rows[0]),
                                                       'Крит:', fmt.hbold(rows[2]),
                                                      'Атака =', fmt.hbold(rows[1]))), parse_mode="HTML")
            else:
                await message.answer("Не хватает Adena (Надо 10-50-200-500-2000)")
        elif save[0] == 1:
            cur.execute(f"SELECT gold FROM players WHERE id = {user_id}")
            gold = cur.fetchone()
            if gold[0] >= 10:
                cur.execute(f"SELECT Weapon FROM players WHERE id = {user_id}")
                weapon = cur.fetchone()
                if weapon[0] == "Homunkulus sword(С) +":
                    a = int(random.randrange(100))
                    if a > 85+ dwarf[0]:
                        cur.execute(f"UPDATE players SET zat = 30, atk = 240, Krit = krit - zat + 30,gold = gold - 300 WHERE id = {user_id} ")
                        con.commit()
                        await message.answer(
                            fmt.text(fmt.text('\U0000274c Сломал Homunkulus sword(С) +', fmt.hbold('30'))),
                            parse_mode="HTML")
                    elif a < 85+ dwarf[0]:
                        cur.execute(f"UPDATE players SET zat = zat + 1, atk = zat*8, Krit = krit + 1, gold=gold -300 WHERE id = {user_id}")
                        con.commit()
                        cur.execute(f"SELECT zat,atk,Krit FROM players WHERE id = {user_id}")
                        rows = cur.fetchone()
                        await message.answer(
                            fmt.text(fmt.text('\U00002728 Homunkulus sword(С) + ', fmt.hbold(rows[0]),
                                              'Крит:', fmt.hbold(rows[2]),
                                              'Атака =', fmt.hbold(rows[1]))), parse_mode="HTML")
                elif weapon[0] == "Sword of Valhalla(B) +":
                    a = int(random.randrange(100))
                    if a > 85+ dwarf[0]:
                        cur.execute(f"UPDATE players SET zat = 30, atk = 420, Krit = krit -zat + 30 ,gold = gold - 800 WHERE id = {user_id} ")
                        con.commit()
                        await message.answer(
                            fmt.text(fmt.text('\U0000274c Сломал Sword of Valhalla(B) +', fmt.hbold('30'))),
                            parse_mode="HTML")
                    elif a < 85+ dwarf[0]:
                        cur.execute(f"UPDATE players SET zat = zat + 1, atk = zat*14, Krit = krit +1, gold = gold -800  WHERE id = {user_id}")
                        con.commit()
                        cur.execute(f"SELECT zat,atk,Krit FROM players WHERE id = {user_id}")
                        rows = cur.fetchone()
                        await message.answer(
                            fmt.text(fmt.text('\U00002728 Sword of Valhalla(B) + ', fmt.hbold(rows[0]),
                                              'Крит:', fmt.hbold(rows[2]),
                                              'Атака =', fmt.hbold(rows[1]))), parse_mode="HTML")
                elif weapon[0] == "Sword of Miracles(A) +":
                    a = int(random.randrange(100))
                    if a > 85+ dwarf[0]:
                        cur.execute(f"UPDATE players SET zat = 30, atk = 900 Krit = krit - zat + 30 ,gold = gold - 2000 WHERE id = {user_id} ")
                        con.commit()
                        await message.answer(
                            fmt.text(fmt.text('\U0000274c Сломал Sword of Miracles(A) +', fmt.hbold('30'))),
                            parse_mode="HTML")
                    elif a < 85+ dwarf[0]:
                        cur.execute(f"UPDATE players SET zat = zat + 1, atk = zat*30, Krit = krit +1, gold = gold -2000  WHERE id = {user_id}")
                        con.commit()
                        cur.execute(f"SELECT zat,atk,Krit FROM players WHERE id = {user_id}")
                        rows = cur.fetchone()
                        await message.answer(
                            fmt.text(fmt.text('\U00002728 Sword of Miracles(A) + ', fmt.hbold(rows[0]),
                                              'Крит:', fmt.hbold(rows[2]),
                                              'Атака =', fmt.hbold(rows[1]))), parse_mode="HTML")
                elif weapon[0] == "Arcane Mace (S) +":
                    a = int(random.randrange(100))
                    if a > 85+ dwarf[0]:
                        cur.execute(f"UPDATE players SET zat = 30, atk = 1800, Krit = krit - zat + 30 ,gold = gold - 4000 WHERE id = {user_id} ")
                        con.commit()
                        await message.answer(
                            fmt.text(fmt.text('\U0000274c Сломал Arcane Mace (S) +', fmt.hbold('30'))),
                            parse_mode="HTML")
                    elif a < 85+ dwarf[0]:
                        cur.execute(f"UPDATE players SET zat = zat + 1, atk = zat*60, Krit = krit +1, gold = gold - 4000  WHERE id = {user_id}")
                        con.commit()
                        cur.execute(f"SELECT zat,atk,Krit FROM players WHERE id = {user_id}")
                        rows = cur.fetchone()
                        await message.answer(
                            fmt.text(fmt.text('\U00002728 Arcane Mace (S) + ', fmt.hbold(rows[0]),
                                              'Крит:', fmt.hbold(rows[2]),
                                              'Атака =', fmt.hbold(rows[1]))), parse_mode="HTML")
            else:
                await message.answer("Не хватает Adena (Надо 10-50-200-500-2000)")
@dp.message_handler(Text(equals='Точить доспехи'))
@dp.throttled(rate=1)
async def tocha(message:types.Message):
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        cur.execute(f"SELECT dwarf,prem2 FROM players where id = {user_id}")
        dwarf = cur.fetchone()
        cur.execute(f"SELECT gold FROM players WHERE id = {user_id}")
        gold = cur.fetchone()
        if gold[0] >= 20:
            cur.execute(f"SELECT armor FROM players WHERE id = {user_id}")
            weapon = cur.fetchone()
            if weapon[0] == "Brigandine Set(D) +":
                a = int(random.randrange(100))
                if a > 70 + dwarf[0] + dwarf[1] :
                   cur.execute(f"UPDATE players SET zat2 = 1, def = 1,gold = gold -20 WHERE id = {user_id} ")
                   con.commit()
                   await message.answer(fmt.text(fmt.text('\U0000274c Сломал Brigandine Set(D) +', fmt.hbold('1'))), parse_mode="HTML")
                elif a < 70+ dwarf[0] + dwarf[1]:
                   cur.execute(f"UPDATE players SET zat2 = zat2 + 1, def = def+1, gold = gold -20 WHERE id = {user_id}")
                   con.commit()
                   cur.execute(f"SELECT zat2,def FROM players WHERE id = {user_id}")
                   rows = cur.fetchone()
                   await message.answer(fmt.text(fmt.text('\U00002728 Brigandine Set(D) + ', fmt.hbold(rows[0]),
                                                   'Защита:', fmt.hbold(rows[1]),
                                                       )), parse_mode="HTML")
            elif weapon[0] == "Composite Set(C) +":
                a = int(random.randrange(100))
                if a > 70+ dwarf[0] + dwarf[1]:
                   cur.execute(f"UPDATE players SET zat2 = 1, def = 2,gold=gold-60 WHERE id = {user_id} ")
                   con.commit()
                   await message.answer(fmt.text(fmt.text('\U0000274c Сломал Composite Set(C) +', fmt.hbold('1'))), parse_mode="HTML")
                elif a < 70+ dwarf[0] + dwarf[1]:
                   cur.execute(f"UPDATE players SET zat2 = zat2 + 1, def = zat2*2,gold=gold-60 WHERE id = {user_id}")
                   con.commit()
                   cur.execute(f"SELECT zat2,def FROM players WHERE id = {user_id}")
                   rows = cur.fetchone()
                   await message.answer(fmt.text(fmt.text('\U00002728 Composite Set(C) + ', fmt.hbold(rows[0]),
                                                   'Защита:', fmt.hbold(rows[1]),
                                                   )), parse_mode="HTML")
            elif weapon[0] == "Blue Wolf Armor(B) +":
                a = int(random.randrange(100))
                if a > 70+ dwarf[0] + dwarf[1]:
                   cur.execute(f"UPDATE players SET zat2 = 1, def = 3,gold=gold-300 WHERE id = {user_id} ")
                   con.commit()
                   await message.answer(fmt.text(fmt.text('\U0000274c Сломал Blue Wolf Armor(B) +', fmt.hbold('1'))), parse_mode="HTML")
                elif a < 70+ dwarf[0] + dwarf[1]:
                   cur.execute(f"UPDATE players SET zat2 = zat2 + 1, def = zat2*3,gold=gold-300 WHERE id = {user_id}")
                   con.commit()
                   cur.execute(f"SELECT zat2,def FROM players WHERE id = {user_id}")
                   rows = cur.fetchone()
                   await message.answer(fmt.text(fmt.text('\U00002728 Blue Wolf Armor(B) +', fmt.hbold(rows[0]),
                                                   'Защита:', fmt.hbold(rows[1]),
                                                   )), parse_mode="HTML")
            elif weapon[0] == "Dark Crystal Armor(A) +":
                a = int(random.randrange(100))
                if a > 70+ dwarf[0] + dwarf[1]:
                   cur.execute(f"UPDATE players SET zat2 = 1, def = 4,gold=gold-600 WHERE id = {user_id} ")
                   con.commit()
                   await message.answer(fmt.text(fmt.text('\U0000274c Сломал Dark Crystal Armor(A) +', fmt.hbold('1'))), parse_mode="HTML")
                elif a < 70+ dwarf[0] + dwarf[1]:
                   cur.execute(f"UPDATE players SET zat2 = zat2 + 1, def = zat2*4,gold=gold-600 WHERE id = {user_id}")
                   con.commit()
                   cur.execute(f"SELECT zat2,def FROM players WHERE id = {user_id}")
                   rows = cur.fetchone()
                   await message.answer(fmt.text(fmt.text('\U00002728 Dark Crystal Armor(A) +', fmt.hbold(rows[0]),
                                                   'Защита:', fmt.hbold(rows[1]),
                                                   )), parse_mode="HTML")
            elif weapon[0] == "Imperial Crusader Set(S) +":
                a = int(random.randrange(100))
                if a > 70+ dwarf[0] + dwarf[1]:
                   cur.execute(f"UPDATE players SET zat2 = 1, def = 5,gold=gold-3000 WHERE id = {user_id} ")
                   con.commit()
                   await message.answer(fmt.text(fmt.text('\U0000274c Сломал Imperial Crusader Set(S) +', fmt.hbold('1'))), parse_mode="HTML")
                elif a < 70+ dwarf[0] + dwarf[1]:
                   cur.execute(f"UPDATE players SET zat2 = zat2 + 1, def = zat2*5,gold=gold-3000 WHERE id = {user_id}")
                   con.commit()
                   cur.execute(f"SELECT zat2,def FROM players WHERE id = {user_id}")
                   rows = cur.fetchone()
                   await message.answer(fmt.text(fmt.text('\U00002728 Imperial Crusader Set(S) +', fmt.hbold(rows[0]),
                                                   'Защита:', fmt.hbold(rows[1]),
                                                   )), parse_mode="HTML")
        else:
            await message.answer("Не хватает Adena (Надо 20-60-300-600-3000)")
@dp.message_handler(Text(equals='Точить Блесс точкой'))
@dp.throttled(rate=1)
async def tochb(message:types.Message):
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        cur.execute(f"SELECT Weapon FROM players WHERE id = {user_id}")
        weapon = cur.fetchone()
        if weapon[0] == "Homunkulus sword(С) +":
            cur.execute(f"SELECT tochkab FROM players WHERE id = {user_id}")
            tochb = cur.fetchone()
            if tochb[0] >= 1:
                d = int(random.randrange(100))
                if d < 40:
                    cur.execute(f"UPDATE players SET zat = zat + 1,atk = zat*8,Krit = krit + 1,tochkab = tochkab - 1 WHERE id = {user_id}")
                    con.commit()
                    cur.execute(f"SELECT zat,atk,Krit,tochkab FROM players WHERE id = {user_id}")
                    rows = cur.fetchone()
                    await message.answer(fmt.text(fmt.text('\U00002728 Homunkulus sword(C) + ', fmt.hbold(rows[0]),
                                                           'Крит:', fmt.hbold(rows[2]),
                                                           'Атака =', fmt.hbold(rows[1]),
                                                           'Блесс точек:',fmt.hbold(rows[3]),
                                                           )), parse_mode="HTML")
                elif d > 40:
                    cur.execute(f"UPDATE players SET tochkab = tochkab - 1 WHERE id = {user_id}")
                    con.commit()
                    await message.answer("Неудача")
            else:
                await message.answer("Недостаточно Блесс точек")
        elif weapon[0] == "Sword of Valhalla(B) +":
            cur.execute(f"SELECT tochkab FROM players WHERE id = {user_id}")
            tochb = cur.fetchone()
            if tochb[0] >= 1:
                d = int(random.randrange(100))
                if d < 40:
                    cur.execute(f"UPDATE players SET zat = zat + 1,atk = zat*14,Krit = krit + 1,tochkab = tochkab - 1 WHERE id = {user_id}")
                    con.commit()
                    cur.execute(f"SELECT zat,atk,krit,tochkab FROM players WHERE id = {user_id}")
                    rows = cur.fetchone()
                    await message.answer(fmt.text(fmt.text('\U00002728 Sword of Valhalla(B) + ', fmt.hbold(rows[0]),
                                                           'Крит:', fmt.hbold(rows[2]),
                                                           'Атака =', fmt.hbold(rows[1]),
                                                           'Блесс точек:',fmt.hbold(rows[3]))), parse_mode="HTML")
                elif d > 40:
                    cur.execute(f"UPDATE players SET tochkab = tochkab - 1 WHERE id = {user_id}")
                    con.commit()
                    await message.answer("Неудача")
            else:
                await message.answer("Недостаточно Блесс точек")
        elif weapon[0] == "Sword of Miracles(A) +":
            cur.execute(f"SELECT tochkab FROM players WHERE id = {user_id}")
            tochb = cur.fetchone()
            if tochb[0] >= 1:
                d = int(random.randrange(100))
                if d < 40:
                    cur.execute(f"UPDATE players SET zat = zat + 1,atk = zat*30,Krit = krit + 1,tochkab = tochkab - 1 WHERE id = {user_id}")
                    con.commit()
                    cur.execute(f"SELECT zat,atk,krit,tochkab FROM players WHERE id = {user_id}")
                    rows = cur.fetchone()
                    await message.answer(
                        fmt.text(fmt.text('\U00002728 Sword of Miracles(A) + ', fmt.hbold(rows[0]),
                                          'Крит:', fmt.hbold(rows[2]),
                                          'Атака =', fmt.hbold(rows[1]),
                                          'Блесс точек:', fmt.hbold(rows[3]))),
                        parse_mode="HTML")
                elif d > 40:
                    cur.execute(f"UPDATE players SET tochkab = tochkab - 1 WHERE id = {user_id}")
                    con.commit()
                    await message.answer("Неудача")
            else:
                await message.answer("Недостаточно Блесс точек")
        elif weapon[0] == "Arcane Mace (S) +":
            cur.execute(f"SELECT tochkab FROM players WHERE id = {user_id}")
            tochb = cur.fetchone()
            if tochb[0] >= 1:
                d = int(random.randrange(100))
                if d < 40:
                    cur.execute(f"UPDATE players SET zat = zat + 1,atk = zat*60,Krit = krit + 1,tochkab = tochkab - 1 WHERE id = {user_id}")
                    con.commit()
                    cur.execute(f"SELECT zat,atk,krit,tochkab FROM players WHERE id = {user_id}")
                    rows = cur.fetchone()
                    await message.answer(
                        fmt.text(fmt.text('\U00002728 Arcane Mace(S) + ', fmt.hbold(rows[0]),
                                          'Крит:', fmt.hbold(rows[2]),
                                          'Атака =', fmt.hbold(rows[1]),
                                          'Блесс точек:', fmt.hbold(rows[3]))),
                        parse_mode="HTML")
                elif d > 40:
                    cur.executet(f"UPDATE players SET tochkab = tochkab - 1 WHERE id = {user_id}")
                    con.commit()
                    await message.answer("Неудача")
            else:
                await message.answer("Недостаточно Блесс точек")
@dp.message_handler(Text(equals='\U0000269CКупить Блесс точку\U0000269C(50000)'))
@dp.throttled(rate=1)
async def buy_homa(message:types.Message):
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        cur.execute(f"SELECT gold FROM players WHERE id = {user_id}")
        weapon = cur.fetchone()
        if weapon[0] >= 50000:
            cur.execute(f"UPDATE players SET tochkab = tochkab + 1,gold = gold - 50000  WHERE id = {user_id} ")
            con.commit()
            await message.answer(fmt.text(fmt.text('Вы купили Блесс точку ')))
        else:
            await message.answer(fmt.text(fmt.text('Не хватает Adena. Блесс точка стоит 50000')))
@dp.message_handler(Text(equals='\U0001F5E1Купить Homunkulus sword(C)\U0001F5E1(5000)'))
@dp.throttled(rate=1)
async def buy_homa(message:types.Message):
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        cur.execute(f"SELECT gold FROM players WHERE id = {user_id}")
        weapon = cur.fetchone()
        if weapon[0] >= 5000:
            cur.execute(f"UPDATE players SET weapon = 'Homunkulus sword(С) +',gold = gold - 5000,atk = 8,zat = 0,krit = krit - zat + 1  WHERE id = {user_id} ")
            con.commit()
            await message.answer(fmt.text(fmt.text('Вы купили Homunkulus sword(С) ')))
        else:
            await message.answer(fmt.text(fmt.text('Не хватает Adena. Homunkulus sword(С) стоит 5000')))
    else:
        await message.answer("Зарегистрируйся!")
@dp.message_handler(Text(equals='\U0001F5E1Купить Sword of Valhalla(B)\U0001F5E1(30000)'))
@dp.throttled(rate=1)
async def buy_valhala(message:types.Message):
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        cur.execute(f"SELECT gold FROM players WHERE id = {user_id}")
        weapon=cur.fetchone()
        if weapon[0] >= 30000:
            cur.execute(f"UPDATE players SET weapon = 'Sword of Valhalla(B) +',gold = gold - 30000,atk = 14,zat = 0, krit = krit - zat + 1  WHERE id = {user_id} ")
            con.commit()
            await message.answer(fmt.text(fmt.text('Вы купили Sword of Valhalla  ')))
        else:
            await message.answer(fmt.text(fmt.text('Не хватает Adena. Sword of Valhalla(B) стоит 30000')))
    else:
        await message.answer("Зарегистрируйся!")
@dp.message_handler(Text(equals='\U0001F94BКупить Composite Set(С)\U0001F94B(6500)'))
@dp.throttled(rate=1)
async def buy_compset(message:types.Message):
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        cur.execute(f"SELECT gold FROM players where id = {user_id}")
        weapon=cur.fetchone()
        if weapon[0] >= 6500:
            cur.execute(f"UPDATE players SET armor = 'Composite Set(C) +',gold = gold - 6500,zat2 = 0,def = 1  WHERE id = {user_id} ")
            con.commit()
            await message.answer(fmt.text(fmt.text('Вы купили Composite Set ')))
        else:
            await message.answer(fmt.text(fmt.text('Не хватает Adena. Composite Set стоит 6500 ')))
    else:
        await message.answer("Зарегистрируйся!")

# @dp.message_handler(commands=['wrb'])
# @dp.throttled(rate=1)
# async def minirb(message:types.Message):
#     con = sq.connect("game.db")
#     con.row_factory = sq.Row
#     cur = con.cursor()
#     user_id = message.from_user.id
#     cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
#     data = cur.fetchone()
#     if data is not None:
#             r = cur.execute(f"SELECT hp FROM players where id = {user_id}").fetchone()
#             for i in r:
#                 if i > 0 :
#                     c = int(random.randrange(100))
#                     if c > 90:
#                         cur.executescript(f"UPDATE rbboss SET rb1 = rb1 - (SELECT atk + atkxp + krit*4 FROM players WHERE id = {user_id})")
#                         cur.executescript(f"UPDATE players SET hp = hp - (1200000/(def + defxp)) WHERE id = {user_id}")
#                         cur.execute(f"SELECT players.atk, players.krit, players.hp, players.atkxp, rbboss.rb1 FROM players, rbboss WHERE players.id = {user_id}")
#                         rows = cur.fetchone()
#                         await message.answer(fmt.text(
#                            fmt.text('\U0001F4A5\U0001F4A5\U0001F4A5КРИТ!!! Вы отняли у Ant queen :', fmt.hbold(rows['atk']), '-', fmt.hbold(rows['krit']), '*', fmt.hbold('4'),'-', fmt.hbold(rows['atkxp']),
#                                  '\n\U0001F577ХП Ant queen стало:', fmt.hbold(rows['rb1']),
#                                  '\nAnt queen атакует, ваше ХП стало:', fmt.hbold(rows['hp']))),parse_mode="HTML")
#                         c = cur.execute("SELECT rb1 FROM rbboss").fetchone()
#                         for x in c:
#                             if x <= 0:
#                                 cur.executescript(f"UPDATE players SET gold = gold+100000, tochkab = tochkab + 2 WHERE id = {user_id}")
#                                 cur.executescript(f"UPDATE rbboss SET rb1 = 2000000 ")
#                                 cur.executescript(f"UPDATE players SET xp = xp+6000 WHERE id = {user_id}")
#                                 cur.executescript(f"UPDATE players SET hpxp = hpxp +1 WHERE id = {user_id}")
#                                 cur.executescript(f"UPDATE players SET srec = 'Arcana Mace(S)' WHERE id = {user_id}")
#                                 await message.answer(fmt.text(
#                                     fmt.text(' Поздравляю! Вы убили \U0001F577Ant queen!\nВыпало 2 Блесс точки!\nВыпал рецепт Arcana Mace(S)!\nAdena +', fmt.hbold('100000'),'\nXp +',fmt.hbold('6000'))),parse_mode="HTML")
#
#                     elif c < 90:
#                         cur.executescript(f"UPDATE rbboss SET rb1 = rb1 - (SELECT atk + atkxp FROM players WHERE id = {user_id})")
#                         cur.executescript(f"UPDATE players SET hp = hp - (1200000/(def + defxp)) WHERE id = {user_id}")
#                         cur.execute(f"SELECT players.atk,players.hp, players.atkxp, rbboss.rb1 FROM players, rbboss WHERE players.id = {user_id}")
#                         rows = cur.fetchone()
#                         await message.answer(fmt.text(fmt.text('\U0001F4A5 Вы отняли у Ant queen:', fmt.hbold(rows['atk']),'+', fmt.hbold(rows['atkxp']) ,
#                                                                '\n\U0001F577ХП Ant queen стало:', fmt.hbold(rows['rb1']),
#                                                                '\nAnt queen атакует, ваше ХП стало:', fmt.hbold(rows['hp']))), parse_mode="HTML")
#                         c =  cur.execute("SELECT rb1 FROM rbboss").fetchone()
#                         for x in c:
#                             if x <= 0:
#                                 cur.executescript(f"UPDATE players SET gold = gold+100000, tochkab = tochkab + 2 WHERE id = {user_id}")
#                                 cur.executescript(f"UPDATE rbboss SET rb1 = 2000000")
#                                 cur.executescript(f"UPDATE players SET xp = xp+6000 WHERE id = {user_id}")
#                                 cur.executescript(f"UPDATE players SET hpxp = hpxp +1 WHERE id = {user_id}")
#                                 cur.executescript(f"UPDATE players SET srec = 'Arcana Mace(S)' WHERE id = {user_id}")
#                                 await message.answer(fmt.text(
#                                     fmt.text(' Поздравляю! Вы убили \U0001F577Ant queen!\nВыпало 2 Блесс точки!\nВыпал рецепт Arcana Mace(S)!\nAdena +', fmt.hbold('100000'),'\nXp +',fmt.hbold('6000'))), parse_mode="HTML")
#                 else:
#                     cur.executescript(f"UPDATE players SET hp = 0 where id = {user_id}")
#                     await message.answer('\U0001F3F3Вас убили\U0001F3F3')
@dp.message_handler(commands='help')
@dp.throttled(rate=1)
async def help (message: types.Message):
    help1 = '<a href="https://t.me/la2kipedia">Вся информация тут</a>'
    await message.answer(help1,parse_mode="html")

@dp.message_handler(Text(equals='\U0001F912Хил\U0001F912'))
@dp.throttled(rate=1)
async def heal (message: types.Message):
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        cur.execute(f'SELECT rbfight,mp,maxmp,maxhp FROM players WHERE id = {user_id}')
        heal1 = cur.fetchone()
        if heal1[0] == 0:
            if heal1[1] > 0:
                cur.execute(f"UPDATE players SET hp = maxhp, mp=mp-1-((maxhp-hp)/500) WHERE id = {user_id}")
                con.commit()
                cur.execute(f'SELECT mp,maxmp,maxhp FROM players WHERE id = {user_id}')
                heal12 = cur.fetchone()
                await message.answer(fmt.text(fmt.text('\U0001F912 Хп восстановленно \U0001F912',
                                                       '\n\U0001F496Макс. ХП =', fmt.hbold(heal12[2]),
                                                       '\n\U0001F4A7Мп = ',fmt.hbold(heal12[0]),'/',fmt.hbold(heal12[1]))),parse_mode="html")
            else:
                await message.answer('Недостаточно МП')
        elif heal1[0] == 1:
            await message.answer("Ты сражаешься с RB или на Олимпе! Убей его или умри, чтобы я мог снова восстанавливать тебе ХП!")

@dp.message_handler(Text(equals='\U0001F4A7Восстановить МП'))
@dp.throttled(rate=1)
async def healmp (message: types.Message):
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        try:
            await dp.throttle('\U0001F4A7Восстановить МП\U0001F4A7', rate=780)
        except Throttled:
            await message.reply(f'Мп можно восстанавливать раз в 15 минуту',parse_mode="HTML")
        else:
            cur.execute(f'SELECT rbfight FROM players WHERE id = {user_id}')
            rb = cur.fetchone()
            if rb[0] == 0:
                cur.execute(f"UPDATE players SET gold = gold - maxmp*15, mp=maxmp WHERE id = {user_id}")
                con.commit()
                cur.execute(f"SELECT mp,maxmp,gold FROM players where id = {user_id}")
                mp = cur.fetchone()
                await message.answer(fmt.text(fmt.text('\U0001F912 МП восстановленно \U0001F912',
                                                       '\n\U0001FA99Aden = ',fmt.hbold(mp[2]),
                                                       '\n\U0001F4A7Мп = ',fmt.hbold(mp[0]),'/',fmt.hbold(mp[1]))),parse_mode="html")
            elif rb[0] == 1:
                await message.answer("Ты сражаешься с RB или на Олимпе! Убей его или умри, чтобы я мог снова восстанавливать тебе ХП!")

@dp.message_handler(commands='info')
@dp.throttled(rate=1)
async def ifoo (message: types.Message):
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        cur.execute(f"SELECT Weapon,atk,atkxp,tochkam,krit,sp,profa,hpxp,maxmp,def,mp,"
                    f"tochkar,tochkab,hpbanka,mpbanka,defxp,zat,"
                    f"zat2,hp,maxhp,gold,xp,armor,pvpwin,pvplose,pvpcp,pvpdmg,"
                    f"pvppoint,race,lshp,lsmp,kill,krits,lvl,lvlup,rank,aa,dwarf,prem2,ice,fire,iceinfo,mdef FROM players WHERE id = {user_id}")
        rows = cur.fetchone()
        await message.answer(fmt.text(fmt.text('-------------------------------------------------------',
                                               '\n|',fmt.hbold(rows[33]),'|',fmt.hbold(rows[28]),'\U0001F9B8',fmt.hbold(rows[6]),
                                               '\n-------------------------------------------------------',
                                               '\n|\U0001F9E1CP |', fmt.hbold(rows[25]),
                                               '\n|\U0001F493ХП |', fmt.hbold(rows[18]),'/',fmt.hbold(rows[19]),
                                               '\n|\U0001F4A7МП |', fmt.hbold(rows[10]),'/',fmt.hbold(rows[8]),
                                               '\n-------------------------------------------------------',
                                               '\n|\U0001F939XP |', fmt.hbold(rows[21]),
                                               '\n|\U0001F4AFLvLUP |',fmt.hbold(rows[34]),
                                               '\n-------------------------------------------------------',
                                               '\n| Weapon |',fmt.hbold(rows[0]), fmt.hbold(rows[16]),
                                                '\n| Armor |',fmt.hbold(rows[22]), fmt.hbold(rows[17]),
                                               '\n|Бижутерия|',fmt.hbold(rows[3]),
                                               '\n|Атрибут|',fmt.hbold(rows[41]),fmt.hbold(rows[39]),'|',fmt.hbold(rows[40]),
                                               '\n-------------------------------------------------------',

                                               '\n\U0001F386Крит урон/шанс =', fmt.hbold(rows[4]),'/', fmt.hbold(((rows[32]+50)/10)),'%',
                                               '\n\U0001F5E1Атака =', fmt.hbold(rows[1]),'\n\U00002694Атака (скил) +', fmt.hbold(rows[2]),
                                               '\n\U0001F6E1Защита =', fmt.hbold(rows[9]),'\n\U0001F6E1Защита (скил) +', fmt.hbold(rows[15]),
                                               '\n\U0001F48CТату ХП +',fmt.hbold(rows[29]), '\U0001F499Тату МП +',fmt.hbold(rows[30]),
                                               '\n\n\U0001F377ХП банки:', fmt.hbold(rows[13]), '\U0001F9CAМП банки:',fmt.hbold(rows[14]),
                                                '\n\U0001F4D3Sp =', fmt.hbold(rows[5]),
                                               '\n\U0001F3F9Атака (PvP) +', fmt.hbold(rows[26]),
                                               '\n\U00002721М.деф =', fmt.hbold(rows[42]),'%',
                                               '\n\U00002618Шанс точки оружия:', fmt.hbold(rows[37]+85),'%',
                                               '\n\U00002618Шанс точки армора:',fmt.hbold(rows[38]+70+rows[37]),'%',
                                               '\n\n\U0001F451', fmt.hbold(rows[35]),
                                               '\n\U0001FA99Adena :', fmt.hbold(rows[20]),
                                               '\n\U0001FA99Ancient Adena :', fmt.hbold(rows[36]),
                                               '\n\U0001F4B3PvP point :', fmt.hbold(rows[27]),
                                               '\n\U0001F4C3Блесс точек :', fmt.hbold(rows[12]),
                                               '\n\U0001F3C6Убито мобов / RB :', fmt.hbold(rows[31]),'/', fmt.hbold(rows[11]),
                                               '\n\U00002620Черепа мобов :', fmt.hbold(rows[7]),
                                               '\n\U0001F396PvP : Win:',fmt.hbold(rows[23]),'/','Lose:',fmt.hbold(rows[24]),
                                               )), parse_mode="HTML")
@dp.message_handler(Text(equals='Атака (скил)\U00002694'))
@dp.throttled(rate=1)
async def atkxp (message: types.Message):
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        cur.execute(f"SELECT elf FROM players where id = {user_id}")
        elf = cur.fetchone()
        if elf[0] == 0:
            cur.execute(f"SELECT xp,lvl FROM players WHERE id = {user_id}" )
            xp = cur.fetchone()
            if xp[0] >= 18*xp[1]:
                cur.execute(f"UPDATE players SET atkxp = atkxp + 5+lvl,xp = xp - 18*lvl,lvlup=lvlup-2 WHERE id = {user_id} ")
                con.commit()
                cur.execute(f"SELECT xp FROM players WHERE id = {user_id}")
                xp1 = cur.fetchone()
                await message.answer(f"Атака (скил) + <b>{5+xp[1]}</b>, XP стало <b>{xp1[0]}</b> ", parse_mode="html")
                cur.execute(f"SELECT lvlup,sp,lvl FROM players WHERE id = {user_id}")
                lvlup = cur.fetchone()
                if lvlup[0] <= 0:
                    cur.execute(f"UPDATE players SET lvl = lvl + 1,lvlup = 20,sp = sp + 3 WHERE id = {user_id} ")
                    con.commit()
                    cur.execute(f"SELECT lvlup,sp,lvl FROM players WHERE id = {user_id}")
                    lvlu = cur.fetchone()
                    await message.answer(f"Вы повысили уровень! \nВаш LvL = <b>{lvlu[2]}</b>"
                                         f" \nSP стало: <b>{lvlu[1]}</b>\nДо следующего уровня: <b>{lvlu[0]}</b>", parse_mode="html")
            else:
                await message.answer(f"Мало опыта, для прокачки надо <b>{xp[1]*18}</b>", parse_mode="html")
        elif elf[0] == 1:
            cur.execute(f"SELECT xp,lvl FROM players WHERE id = {user_id}")
            xp = cur.fetchone()
            if xp[0] >= 15*xp[1]:
                cur.execute(
                    f"UPDATE players SET atkxp = atkxp + 5+lvl,xp = xp - 15*lvl,lvlup=lvlup-2 WHERE id = {user_id} ")
                con.commit()
                cur.execute(f"SELECT xp FROM players WHERE id = {user_id}")
                xp1 = cur.fetchone()
                await message.answer(f"Атака (скил) + <b>{5 + xp[1]}</b> ХР стало <b>{xp1[0]}</b>", parse_mode="html")
                cur.execute(f"SELECT lvlup,sp,lvl FROM players WHERE id = {user_id}")
                lvlup = cur.fetchone()
                if lvlup[0] <= 0:
                    cur.execute(f"UPDATE players SET lvl = lvl + 1,lvlup = 20,sp = sp + 3 WHERE id = {user_id} ")
                    con.commit()
                    cur.execute(f"SELECT lvlup,sp,lvl FROM players WHERE id = {user_id}")
                    lvlu = cur.fetchone()
                    await message.answer(f"Вы повысили уровень! \nВаш LvL = <b>{lvlu[2]}</b>"
                                         f" \nSP стало: <b>{lvlu[1]}</b>\nДо следующего уровня: <b>{lvlu[0]}</b>",
                                         parse_mode="html")
            else:
                await message.answer(f"Мало опыта, для прокачки надо <b>{xp[1] * 15}</b>", parse_mode="html")

@dp.message_handler(Text(equals='Защита (скил)(+1)\U0001F6E1'))
@dp.throttled(rate=1)
async def defxp (message: types.Message):
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        cur.execute(f"SELECT xp,lvl FROM players WHERE id = {user_id}")
        xp = cur.fetchone()
        if xp[0] >= 50*xp[1]:
            cur.execute(
                f"UPDATE players SET defxp = defxp + 1,xp = xp - 50*lvl,lvlup=lvlup-3 WHERE id = {user_id} ")
            con.commit()
            cur.execute(f"SELECT xp FROM players WHERE id = {user_id}")
            xp1 = cur.fetchone()
            await message.answer(f"Защита (скил) + <b>1</b> XP стало <b>{xp1[0]}</b>", parse_mode="html")
            cur.execute(f"SELECT lvlup,sp,lvl FROM players WHERE id = {user_id}")
            lvlup = cur.fetchone()
            if lvlup[0] <= 0:
                cur.execute(
                    f"UPDATE players SET lvl = lvl + 1,lvlup = 20,sp = sp + 3 WHERE id = {user_id} ")
                con.commit()
                cur.execute(f"SELECT lvlup,sp,lvl FROM players WHERE id = {user_id}")
                lvlu = cur.fetchone()
                await message.answer(f"Вы повысили уровень! \nВаш LvL = <b>{lvlu[2]}</b>"
                                     f" \nSP стало: <b>{lvlu[1]}</b>\nДо следующего уровня: <b>{lvlu[0]}</b>",
                                     parse_mode="html")
        else:
            await message.answer(f"Мало опыта, для прокачки надо <b>{xp[1] * 50}</b>", parse_mode="html")
@dp.message_handler(Text(equals='Крит шанс (+0,1%)(-1 Sp)\U0001F4A5'))
@dp.throttled(rate=1)
async def kritxpp (message: types.Message):
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        cur.execute(f"SELECT sp,profa,krits FROM players WHERE id = {user_id}")
        xp = cur.fetchone()
        if xp[0] >= 1 and xp[1]=='Gladiator' and xp[2] < 250:
            cur.execute(f"UPDATE players SET krits = krits + 1,sp = sp - 1 WHERE id = {user_id} ")
            con.commit()
            await message.answer("Крит шанс + <b>0,1 %</b>", parse_mode="html")
        elif xp[0] >= 1 and xp[1]=='Paladin' and xp[2] < 250:
            cur.execute(f"UPDATE players SET krits = krits + 1,sp = sp - 1 WHERE id = {user_id} ")
            con.commit()
            await message.answer("Крит шанс + <b>0,1 %</b>", parse_mode="html")
        elif xp[0] >= 1 and xp[1]=='Treasure Hunter' and xp[2] < 350:
            cur.execute(f"UPDATE players SET krits = krits + 1,sp = sp - 1 WHERE id = {user_id} ")
            con.commit()
            await message.answer("Крит шанс + <b>0,1 %</b>", parse_mode="html")
        else:
            await message.answer("Мало SP, для прокачки надо <b>1</b> (Нужна профа, либо достигнут максимум)", parse_mode="html")
@dp.message_handler(Text(equals='Макс ХП\U00002665'))
@dp.throttled(rate=1)
async def maxhp (message: types.Message):
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        cur.execute(f"SELECT hum FROM players where id = {user_id}")
        elf = cur.fetchone()
        if elf[0] == 0:
            cur.execute(f"SELECT xp,lvl FROM players WHERE id = {user_id}")
            xp = cur.fetchone()
            if xp[0] >= 9*xp[1]:
                cur.execute( f"UPDATE players SET maxhp = maxhp + 15 +lvl,xp = xp - 9*lvl,lvlup=lvlup-1 WHERE id = {user_id} ")
                con.commit()
                cur.execute(f"SELECT xp FROM players WHERE id = {user_id}")
                xp1 = cur.fetchone()
                await message.answer(f"Макс ХП + <b>{15 + xp[1]}</b>, XP стало <b>{xp1[0]}</b>", parse_mode="html")
                cur.execute(f"SELECT lvlup,lvl FROM players WHERE id = {user_id}")
                lvlup = cur.fetchone()
                if lvlup[0] <= 0:
                    cur.execute(f"UPDATE players SET lvl = lvl + 1,lvlup = 20,sp = sp + 3 WHERE id = {user_id} ")
                    con.commit()
                    cur.execute(f"SELECT lvlup,sp,lvl FROM players WHERE id = {user_id}")
                    lvlu = cur.fetchone()
                    await message.answer(f"Вы повысили уровень! \nВаш LvL = <b>{lvlu[2]}</b>"
                                         f" \nSP стало: <b>{lvlu[1]}</b>\nДо следующего уровня: <b>{lvlu[0]}</b>",
                                         parse_mode="html")
            else:
                await message.answer(f"Мало опыта, для прокачки надо <b>{xp[1] * 9}</b>", parse_mode="html")
        elif elf[0] == 1:
            cur.execute(f"SELECT xp,lvl FROM players WHERE id = {user_id}")
            xp = cur.fetchone()
            if xp[0] >= 7*xp[1]:
                cur.execute(
                    f"UPDATE players SET maxhp = maxhp + 15+lvl,xp = xp - 7*lvl,lvlup=lvlup-1 WHERE id = {user_id} ")
                con.commit()
                cur.execute(f"SELECT xp FROM players WHERE id = {user_id}")
                xp1 = cur.fetchone()
                await message.answer(f"Макс ХП + <b>{15 + xp[1]}</b>, XP стало <b>{xp1[0]}</b>", parse_mode="html")
                cur.execute(f"SELECT lvlup,sp,lvl FROM players WHERE id = {user_id}")
                lvlup = cur.fetchone()
                if lvlup[0] <= 0:
                    cur.execute(
                        f"UPDATE players SET lvl = lvl + 1,lvlup = 20,sp = sp + 3 WHERE id = {user_id} ")
                    con.commit()
                    cur.execute(f"SELECT lvlup,sp,lvl FROM players WHERE id = {user_id}")
                    lvlu = cur.fetchone()
                    await message.answer(f"Вы повысили уровень! \nВаш LvL = <b>{lvlu[2]}</b>"
                                         f" \nSP стало: <b>{lvlu[1]}</b>\nДо следующего уровня: <b>{lvlu[0]}</b>",
                                         parse_mode="html")
            else:
                await message.answer(f"Мало опыта, для прокачки надо <b>{xp[1] * 7}</b>", parse_mode="html")
@dp.message_handler(Text(equals='\U0001F4A7Макс МП(+1)\U0001F4A7'))
@dp.throttled(rate=1)
async def maxhp (message: types.Message):
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        cur.execute(f"SELECT xp,lvl FROM players WHERE id = {user_id}")
        xp = cur.fetchone()
        if xp[0] >= 25*xp[1]:
            cur.execute(f"UPDATE players SET maxmp = maxmp + 1,xp = xp - 25*lvl,lvlup=lvlup-3 WHERE id = {user_id} ")
            con.commit()
            cur.execute(f"SELECT xp FROM players WHERE id = {user_id}")
            xp1 = cur.fetchone()
            await message.answer(f"Макс МП + <b>1</b>, XP стало <b>{xp1[0]}</b>", parse_mode="html")
            cur.execute(f"SELECT lvlup,sp,lvl FROM players WHERE id = {user_id}")
            lvlup = cur.fetchone()
            if lvlup[0] <= 0:
                cur.execute(
                    f"UPDATE players SET lvl = lvl + 1,lvlup = 20,sp = sp + 3 WHERE id = {user_id} ")
                con.commit()
                cur.execute(f"SELECT lvlup,sp,lvl FROM players WHERE id = {user_id}")
                lvlu = cur.fetchone()
                await message.answer(f"Вы повысили уровень! \nВаш LvL = <b>{lvlu[2]}</b>"
                                     f" \nSP стало: <b>{lvlu[1]}</b>\nДо следующего уровня: <b>{lvlu[0]}</b>",
                                     parse_mode="html")
        else:
            await message.answer(f"Мало опыта, для прокачки надо <b>{xp[1] * 25}</b>", parse_mode="html")

@dp.message_handler(commands='skill')
@dp.throttled(rate=1)
async def skills (message: types.Message):
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        cur.execute(f"SELECT xp,lvl,race FROM players WHERE id = {user_id}")
        rows = cur.fetchone()
        if rows[2] == '\U0001F9DDElf':
            await message.answer(fmt.text(fmt.text(f'Здесь можно прокачать скилы и выбрать профу!\n<b>ПРОФА ВЫБИРАЕТСЯ СРАЗУ!!!'
                                               f'\nПРОЧТИ ИНФОРМАЦИЮ ЗАРАНЕЕ</b>'
                                               f'\nАтака (скил)  + <b>{5+rows[1]}</b> требует <b>{15*rows[1]}</b> XP (2 lvlpoint)'
                                               f'\nЗащита (скил) + <b>1</b> требует <b>{50*rows[1]}</b> XP (3 lvlpoint)'
                                               f'\nМакс. ХП + <b>{15+rows[1]}</b> требует <b>{9*rows[1]}</b> XP (1 lvlpoint)'
                                               f'\nМакс. МП + <b>1</b> требует <b>{25*rows[1]}</b> XP (3 lvlpoint)'
                                               f'\nУ тебя XP =', fmt.hbold(rows[0]))),reply_markup=skill,parse_mode='HTML')
        elif rows[2] =='\U0001F9D4Human':
            await message.answer(fmt.text(fmt.text(f'Здесь можно прокачать скилы и выбрать профу!\n<b>ПРОФА ВЫБИРАЕТСЯ СРАЗУ!!!'
                                               f'\nПРОЧТИ ИНФОРМАЦИЮ ЗАРАНЕЕ</b>'
                                               f'\nАтака (скил)  + <b>{5+rows[1]}</b> требует <b>{18*rows[1]}</b> XP (2 lvlpoint)'
                                               f'\nЗащита (скил) + <b>1</b> требует <b>{50*rows[1]}</b> XP (3 lvlpoint)'
                                               f'\nМакс. ХП + <b>{15+rows[1]}</b> требует <b>{7*rows[1]}</b> XP (1 lvlpoint)'
                                               f'\nМакс. МП + <b>1</b> требует <b>{25*rows[1]}</b> XP (3 lvlpoint)' 
                                               f'\nУ тебя XP =', fmt.hbold(rows[0]))),reply_markup=skill,parse_mode='HTML')
        elif rows[2] == '\U0001F385Dwarf':
            await message.answer(fmt.text(fmt.text(f'Здесь можно прокачать скилы и выбрать профу!\n<b>ПРОФА ВЫБИРАЕТСЯ СРАЗУ!!!'
                                               f'\nПРОЧТИ ИНФОРМАЦИЮ ЗАРАНЕЕ</b>'
                                               f'\nАтака (скил)  + <b>{5+rows[1]}</b> требует <b>{18*rows[1]}</b> XP (2 lvlpoint)'
                                               f'\nЗащита (скил) + <b>1</b> требует <b>{50*rows[1]}</b> XP (3 lvlpoint)'
                                               f'\nМакс. ХП + <b>{15+rows[1]}</b> требует <b>{9*rows[1]}</b> XP (1 lvlpoint)'
                                               f'\nМакс. МП + <b>1</b> требует <b>{25*rows[1]}</b> XP (3 lvlpoint)'
                                               f'\nУ тебя XP =', fmt.hbold(rows[0]))),reply_markup=skill,parse_mode='HTML')
@dp.message_handler(Text(equals='Крит(+8)Treasure Hunter-(1 Sp)')) #дагер
@dp.throttled(rate=1)
async def buffkrit_dagger(message:types.Message):
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        cur.execute(f"SELECT profa FROM players where id = {user_id}")
        profa = cur.fetchone()
        if profa[0] == 'Paladin':
            await message.answer("Только для Treasure Hunter")
        elif profa[0] == 'Gladiator':
            await message.answer("Только для Treasure Hunter")
        elif profa[0] == '0':
            await message.answer("Только для Treasure Hunter")
        else:
            cur.execute(f"SELECT sp FROM players where id = {user_id}")
            sp=cur.fetchone()
            if sp[0] >= 1:
                cur.execute(f"UPDATE players SET krit = krit+8, sp = sp - 1  WHERE id = {user_id} ")
                con.commit()
                await message.answer('Крит +8')
            else:
                await message.answer('Недостаточно Sp')
@dp.message_handler(Text(equals='Атака(+4)Gladiator-(1 Sp)'))  # воин
@dp.throttled(rate=1)
async def buffatk_war(message: types.Message):
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        cur.execute(f"SELECT profa FROM players where id = {user_id}")
        profa = cur.fetchone()
        if profa[0] == 'Paladin':
            await message.answer("Только для Gladiator")
        elif profa[0] == 'Treasure Hunter':
            await message.answer("Только для Gladiator")
        elif profa[0] == '0':
            await message.answer("Только для Gladiator")
        else:
            cur.execute(f"SELECT sp FROM players where id = {user_id}")
            sp = cur.fetchone()
            if sp[0] >= 1:
                cur.execute(f"UPDATE players SET atkxp = atkxp+4,sp = sp - 1  WHERE id = {user_id} ")
                con.commit()
                await message.answer('Атака (скил) + 4')
            else:
                await message.answer('Недостаточно Sp')

@dp.message_handler(Text(equals='Защита(+1)Paladin-(1 Sp)'))  # танк
@dp.throttled(rate=1)
async def buffdef_tank(message: types.Message):
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        cur.execute(f"SELECT profa FROM players where id = {user_id}")
        profa = cur.fetchone()
        if profa[0] == 'Treasure Hunter':
            await message.answer("Только для Paladin")
        elif profa[0] == 'Gladiator':
            await message.answer("Только для Paladin")
        elif profa[0] == '0':
            await message.answer("Только для Paladin")
        else:
            cur.execute(f"SELECT sp FROM players where id = {user_id}")
            sp = cur.fetchone()
            if sp[0] >= 1:
                cur.execute(f"UPDATE players SET defxp = defxp + 1, sp = sp - 1  WHERE id = {user_id} ")
                con.commit()
                await message.answer('Защита (скил) + 1')
            else:
                await message.answer('Недостаточно Sp')
@dp.message_handler(Text(equals='Хп(+100)(Все профы)(750Adena)'))  # дагер, воин, танк
@dp.throttled(rate=1)
async def buffhp(message: types.Message):
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        cur.execute(f"SELECT gold FROM players where id = {user_id}")
        weapon = cur.fetchone()
        if weapon[0] >= 750:
            cur.execute(f"UPDATE players SET hp = hp+100,gold = gold - 750  WHERE id = {user_id} ")
            con.commit()
            await message.answer('Бафф ХП +100 (НЕ МАКСИМАЛЬНОЕ)')
        else:
            await message.answer('Недостаточно Adena, нужно 750')

@dp.message_handler(Text(equals='Макс ХП(+100)(TH,Pal)-(1 Sp)'))  # дагер, танк
@dp.throttled(rate=1)
async def buffatk_dagtank(message: types.Message):
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        cur.execute(f"SELECT profa FROM players where id = {user_id}")
        profa = cur.fetchone()
        if profa[0] == 'Gladiator':
            await message.answer("Только для Treasure Hunter и Paladin")
        elif profa[0] == '0':
            await message.answer("Только для Treasure Hunter и Paladin")
        else:
            cur.execute(f"SELECT sp FROM players where id = {user_id}")
            sp = cur.fetchone()
            if sp[0] >= 1:
                cur.execute(f"UPDATE players SET maxhp = maxhp+100,sp = sp - 1  WHERE id = {user_id} ")
                con.commit()
                await message.answer('Макс.ХП +100')
            else:
                await message.answer('Недостаточно Sp')
@dp.message_handler(Text(equals='Макс МП + 3 (Все)-(1 Sp)'))
@dp.throttled(rate=1)
async def buffmp(message: types.Message):
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        cur.execute(f"SELECT sp FROM players where id = {user_id}")
        sp = cur.fetchone()
        if sp[0] >= 1:
            cur.execute(f"UPDATE players SET maxmp = maxmp + 3,sp = sp - 1  WHERE id = {user_id} ")
            con.commit()
            await message.answer('Макс.МП +3')
        else:
            await message.answer('Недостаточно Sp')
@dp.message_handler(Text(equals='\U00002049Квесты\U00002049'))
@dp.throttled(rate=1)
async def pal22(message: types.Message):
    await message.answer("Здесь ты сможешь найти задания",reply_markup=quest)

@dp.message_handler(Text(equals='\U0001F198Сага Кладоискателя'))
@dp.throttled(rate=1)
async def pal33(message: types.Message):
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        photo = open('quest1.jpg', 'rb')
        await bot.send_photo(message.chat.id, photo =photo,caption= 'Путник, я вижу тебе не чем занятся? Хочешь получить немного ресов? '
                             '\nПринеси мне <b>20</b> \U0001FA72чешуи аллигаторов и <b>15</b> \U0001FABAяиц дино\n\nТааак посмотрим сколько там у тебя их, подожди пару секунд', parse_mode="html")
        await asyncio.sleep(1)
        cur.execute(f"SELECT aliq,dinoq FROM players where id = {user_id}")
        aliq = cur.fetchone()
        if ((aliq[0] >= 20) and (aliq[1]>= 15)):
            cur.execute(f"UPDATE players SET dinoq = dinoq - 15,aliq = aliq - 20, minirb = minirb + 15, dion = dion +5 WHERE id = {user_id}")
            con.commit()
            await message.answer("Спасибо тебе! Вот держи \nIrone Ore = <b>15</b>\nBlue Gemstone = <b>5</b>",parse_mode="html")
        else:
            await message.answer("Маловато, нужно больше иди и сражайся, если хочешь награду!")

@dp.message_handler(Text(equals='\U0001F198Во имя отца'))
@dp.throttled(rate=1)
async def pal333(message: types.Message):
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        photo = open('quest2.jpg','rb')
        await bot.send_photo(message.chat.id, photo =photo,caption= 'Воин ты что пришёл ко мне за заданием? У меня как раз есть для тебя.'
                             '\nПринеси мне <b>15</b> \U0001F480черепов носорогов и <b>15</b> \U0001FAA2хвостов буфало\n\nНу что ты там принёс? Дай гляну, подожди пару секунд', parse_mode="html")
        await asyncio.sleep(1)
        cur.execute(f"SELECT bufq,nosq FROM players where id = {user_id}")
        nos = cur.fetchone()
        if ((nos[0] >= 15) and (nos[1] >= 15)):
            cur.execute(f"UPDATE players SET nosq = nosq - 15,bufq = bufq - 15, Varnish = Varnish + 15, dion = dion +15 WHERE id = {user_id}")
            con.commit()
            await message.answer("Спасибо тебе! Вот держи \nVarnish = <b>15</b>"
                                 "\nBlue Gemstone = <b>15</b>", parse_mode="html")
        else:
            await message.answer("Маловато, нужно больше иди и сражайся, если хочешь награду!")

@dp.message_handler(Text(equals='\U0001F198История Рыцаря Ада'))
@dp.throttled(rate=1)
async def pal444(message: types.Message):
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        photo = open('quest3.jpg', 'rb')
        await bot.send_photo(message.chat.id, photo=photo,
                             caption='Ну что вот ты и пришёл ко мне, я долго тебя ждал думаю ты очень хочешь '
                             'принести мне <b>15</b> кусков \U0001F969плоти льва и <b>15</b> \U0001F9B4костей медведя, не так ли?\n\nНу как покажи, что ты там держишь', parse_mode="html")
        await asyncio.sleep(1)
        cur.execute(f"SELECT bearq,lionq FROM players where id = {user_id}")
        lion = cur.fetchone()
        if ((lion[0] >= 15) and (lion[1] >= 15)):
            cur.execute(f"UPDATE players SET bearq = bearq - 15,lionq = lionq - 15, minirb = minirb + 25, varnish = varnish + 10 WHERE id = {user_id}")
            con.commit()
            await message.answer("Спасибо тебе! Вот держи \nIrone Ore = <b>25</b>\nVarnish = <b>10</b>",parse_mode="html")
        else:
            await message.answer("Маловато, нужно больше иди и сражайся, если хочешь награду!")
@dp.message_handler(Text(equals='\U0001F198Поиски праха'))
@dp.throttled(rate=1)
async def pal4444(message: types.Message):
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        photo = open('quest4.jpg', 'rb')
        await bot.send_photo(message.chat.id, photo=photo,
                             caption='Привет воин! Спасибо тебе за всё, то, что ты для нас делаешь, мы тебе благодарны, но не мог ли ты '
                             'принести мне \U0001F4AEПрах Джина в колличестве <b>15</b> штук  и <b>15</b>\U0001FAD3Жабр Акул? Пожалуйста=)\n\nНу как дай гляну, что там у тебя.', parse_mode="html")
        await asyncio.sleep(1)
        cur.execute(f"SELECT akuq,jinq FROM players where id = {user_id}")
        aku = cur.fetchone()
        if ((aku[0] >= 15) and (aku[1] >= 15)):
            cur.execute(f"UPDATE players SET jinq = jinq - 15,akuq = akuq - 15, minirb = minirb + 20, dion = dion + 10 WHERE id = {user_id}")
            con.commit()
            await message.answer("Спасибо тебе! Вот держи \nIrone Ore = <b>20</b>\nBlue Gemstone = <b>10</b>",parse_mode="html")
        else:
            await message.answer("Маловато, нужно больше иди и сражайся, если хочешь награду!")

@dp.message_handler(Text(equals='\U0001F198Тайны семян'))
@dp.throttled(rate=1)
async def pal44442(message: types.Message):
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        photo = open('quest5.jpg', 'rb')
        await bot.send_photo(message.chat.id, photo=photo,
                             caption='Ой, не буду многословен, короче я меняю \U0001F331<b>30 семян</b> на ресурсы', parse_mode="html")
        await asyncio.sleep(1)
        cur.execute(f"SELECT tree FROM players where id = {user_id}")
        tree = cur.fetchone()
        if tree[0] >= 30:
            cur.execute(f"UPDATE players SET tree = tree - 30,minirb = minirb + 4, dion = dion + 4, varnish = varnish+4,sop = sop + 2 WHERE id = {user_id}")
            con.commit()
            await message.answer("Спасибо тебе! Вот держи \nIrone Ore = <b>4</b>\nBlue Gemstone = <b>4</b>\nVarnish = <b>4</b>\nSOP = <b>2</b>",parse_mode="html")
        else:
            await message.answer("Маловато, нужно больше иди и сражайся, если хочешь награду!")

@dp.message_handler(Text(equals='\U0001FAC5Noobless\U0001FAC5'))
@dp.throttled(rate=1)
async def nobless1(message: types.Message):
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        photo = open('noob.jpg', 'rb')
        await bot.send_photo(message.chat.id, photo=photo, caption='Привет, хочешь получить звание нублеса? Тогда принеси мне'
                                     '<i>\n30 всех квестовых предметов(кроме Чешуи),100000 Aden, Зуб Антараса.'
                                     ' А и у тебя должно быть минмум 100 побед в PvP</i>', parse_mode="html")
        await asyncio.sleep(1)
        cur.execute(f"SELECT nosq,bufq,lionq,bearq,dinoq,jinq,akuq,tree,gold,pvpwin,zub FROM players where id = {user_id}")
        nooble = cur.fetchone()
        if ((nooble[0] >= 30) and (nooble[1] >= 30) and (nooble[2] >= 30) and (nooble[3] >= 30) and (nooble[4 ] >= 30) and (nooble[5] >= 30) and (nooble[6] >= 30) and (nooble[7] >= 30) and (nooble[8] >= 100000) and (nooble[9] >= 100) and (nooble[10] >= 1)):
            cur.execute(f"UPDATE players SET save = 1, atkxp = atkxp + 500, pvpdmg = pvpdmg + 1000, maxmp=maxmp+20, aden = 'Sword of Miracles(A)70%' WHERE id = {user_id}")
            con.commit()
            cur.execute(f"UPDATE players SET nosq = nosq - 30, bufq = bufq -30, lionq = lionq -30,"
                              f" bearq=bearq-30,dinoq=dinoq-30,jinq=jinq-30,akuq=akuq-30,"
                              f"aliq=aliq-30,tree=tree-30,gold=gold-100000,zub = zub - 1 WHERE id = {user_id}")
            con.commit()
            await message.answer('Поздравляю теперь вы успешно прошли задание на Noobless,'
                                  ' теперь вам доступна Save заточка, атака + 500, атакак(пвп) + 1000,'
                                  ' Макс.Мп + 20 и также дарю вам рецепт Sword of Miracles(A)70%!', parse_mode="HTML")
        else:
            await message.answer("Маловато, нужно больше иди и сражайся, если хочешь награду!")

@dp.message_handler(commands='quest')
@dp.throttled(rate=1)
async def heal (message: types.Message):
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        cur.execute(f"SELECT dinoq,nosq,aliq,lionq,bufq,bearq,jinq,akuq,tree,zub FROM players WHERE id = {user_id}")
        rows = cur.fetchone()
        await message.answer(fmt.text(fmt.text('<b>Квестовые предметы:</b>\n\U0001FA72Чешуя аллигатора:', fmt.hbold(rows[2]),
                                               '\n\U0001FABAЯйца дракона:', fmt.hbold(rows[0]),
                                               '\n\U0001F4AEПрах Джина:', fmt.hbold(rows[6]),
                                               '\n\U0001FAD3Жабры Акулы:', fmt.hbold(rows[7]),
                                               '\n\U0001F480Череп носорога:', fmt.hbold(rows[1]),
                                               '\n\U0001F969Плоть льва:', fmt.hbold(rows[3]),
                                               '\n\U0001FAA2Хвост буфало:', fmt.hbold(rows[4]),
                                               '\n\U0001F9B4Кость медведя:',fmt.hbold(rows[5]),
                                               '\n\U0001F331Семена:',fmt.hbold(rows[8]),
                                               '\n\U0001F9B7Зуб Антараса:',fmt.hbold(rows[9]),
                                               )), parse_mode="HTML")

@dp.message_handler(Text(equals='Добавить Ice'))
@dp.throttled(rate=1)
async def ice (message: types.Message):
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        cur.execute(f'SELECT dion,ls2,ice FROM players WHERE id = {user_id}')
        ice = cur.fetchone()
        blue = ice[2]
        if ice[0] >= 20 and ice[1]>=(blue/10) :
            cur.execute(f"UPDATE players SET ice = ice + 20,dion = dion - 20, ls2 = ls2 - {blue/10}, iceinfo = '\U0001F9CA',fire = 0 WHERE id = {user_id}")
            con.commit()
            cur.execute(f'SELECT ice FROM players WHERE id = {user_id}')
            heal12 = cur.fetchone()
            await message.answer(fmt.text(fmt.text('\U0001F9CAАтрибут Ice успешно добавлен, его урон стал:',fmt.hbold(heal12[0]))),parse_mode="html")
        else:
            await message.answer(f"Требуется 20 Blue Gemstone и <b>{blue/10}</b> синей краски ",parse_mode="html")
@dp.message_handler(Text(equals='Добавить Fire'))
@dp.throttled(rate=1)
async def fire (message: types.Message):
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        cur.execute(f'SELECT dion,ls1,fire FROM players WHERE id = {user_id}')
        ice = cur.fetchone()
        blue = ice[2]
        if ice[0] >= 20 and ice[1]>=(blue/10):
            cur.execute(f"UPDATE players SET fire = fire + 20,dion = dion - 20, ls1 = ls1 - {blue/10}, iceinfo = '\U0001F525',ice = 0 WHERE id = {user_id}")
            con.commit()
            cur.execute(f'SELECT fire FROM players WHERE id = {user_id}')
            heal12 = cur.fetchone()
            await message.answer(fmt.text(fmt.text('\U0001F525Атрибут Fire успешно добавлен, его урон стал:',fmt.hbold(heal12[0]))),parse_mode="html")
        else:
            await message.answer(f"Требуется 20 Blue Gemstone и <b>{blue/10}</b> красной краски ",parse_mode="html")

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