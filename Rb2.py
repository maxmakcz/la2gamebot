from aiogram import types
from aiogram.dispatcher.filters import Text
import aiogram.utils.markdown as fmt
import sqlite3 as sq
from keyboards import rbfight2
import random
from skilsss import *
import asyncio


@dp.message_handler(Text(equals='\U0001F432Antharas\U0001F432'))
@dp.throttled(rate=1)
async def antaras(message:types.Message):
    photo = open('antharas2.jpg', 'rb')
    await bot.send_photo(message.chat.id,photo=photo,reply_markup=rbfight2)
    con = sq.connect("game.db")
    con.row_factory = sq.Row
    cur = con.cursor()
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        await asyncio.sleep(30)
        cur.executescript(f"UPDATE players SET hp = hp - 300 WHERE id = {user_id}")
        await message.answer("Ты пришёл убить меня?\n\U0001F432Antharas всё помнит и отнял у вас <b>300</b>ХП", parse_mode="html")
        await asyncio.sleep(30)
        cur.executescript(f"UPDATE players SET hp = hp - 300 WHERE id = {user_id}")
        await message.answer("Ты пришёл убить меня?\n\U0001F432Antharas всё помнит и отнял у вас <b>300</b>ХП", parse_mode="html")
        await asyncio.sleep(30)
        cur.executescript(f"UPDATE players SET hp = hp - 300 WHERE id = {user_id}")
        await message.answer("Ты пришёл убить меня?\n\U0001F432Antharas всё помнит и отнял у вас <b>300</b>ХП",
                             parse_mode="html")
@dp.message_handler(Text(equals='Атака!'))
@dp.throttled(rate=1)
async def atk1(message:types.Message):
    con = sq.connect("game.db")
    con.row_factory = sq.Row
    cur = con.cursor()
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        cur.executescript(f"UPDATE players SET rbfight = 1  WHERE id = {user_id}")
        df = int(cur.execute(f'SELECT minirb3 FROM players WHERE id = {user_id}').fetchone()[0])
        if df > 0:
            a = int(cur.execute(f'SELECT hp FROM players WHERE id = {user_id}').fetchone()[0])
            if a > 0:
                cur.executescript(f"UPDATE players SET minirb3 = minirb3 - atk - atkxp  WHERE id = {user_id}")
                cur.executescript(f"UPDATE players SET hp = hp - 35000/(def + defxp)-50  WHERE id = {user_id}")
                cur.execute(f"SELECT minirb3,atk,atkxp,hp FROM players WHERE id = {user_id}")
                rows = cur.fetchone()
                await message.answer(fmt.text(
                    fmt.text('\U0001F4A5 Вы отняли у Antharas :', fmt.hbold(rows['atk']),'+', fmt.hbold(rows['atkxp']),
                             '\n\U0001F432ХП Antharas стало:', fmt.hbold(rows['minirb3']),
                             '\nAntharas Атакует! Ваше хп стало:',fmt.hbold(rows['hp']))),
                    parse_mode="HTML")
            else:
                cur.executescript(f"UPDATE players SET minirb3 = 400000  WHERE id = {user_id}")
                cur.executescript(f"UPDATE players SET rbfight = 0  WHERE id = {user_id}")
                await message.answer('Вас убили')
        elif df < 0:
            d = int(random.randrange(100))
            if d > 70:
                cur.executescript(f"UPDATE players SET rbfight = 0  WHERE id = {user_id}")
                cur.executescript(f"UPDATE players SET gold = gold + 50000, xp = xp + 1000, tochkar = tochkar + 1  WHERE id = {user_id}")
                cur.executescript(f"UPDATE players SET rbfight = 0  WHERE id = {user_id}")
                cur.executescript(f"UPDATE players SET minirb3 = 400000  WHERE id = {user_id}")
                cur.executescript(f"UPDATE players SET aden = 'Sword of Miracles(A)90%'  WHERE id = {user_id}")
                await message.answer(fmt.text(fmt.text('Вы убили рб!!Вам выпал рецепт Sword of Miracles(A)90%!!',
                                                       '\nAdena +', fmt.hbold('50000'),
                                                       '\nXP +', fmt.hbold('1000'),)),parse_mode="HTML")
            if d < 70:
                cur.executescript(f"UPDATE players SET rbfight = 0  WHERE id = {user_id}")
                cur.executescript(f"UPDATE players SET gold = gold + 50000, xp = xp + 1000, tochkar = tochkar + 1  WHERE id = {user_id}")
                cur.executescript(f"UPDATE players SET rbfight = 0  WHERE id = {user_id}")
                cur.executescript(f"UPDATE players SET minirb3 = 400000  WHERE id = {user_id}")
                cur.executescript(f"UPDATE players SET minirb = minirb + 20 dion = dion +20, Varnish = Varnish + 20 WHERE id = {user_id}")
                await message.answer(fmt.text(fmt.text('Вы убили рб!!Вам выпало', fmt.hbold('20'),
                                                       'Varnish и', fmt.hbold('20'), 'Blue Gemstone', fmt.hbold('20'), 'Iron Ore!!'
                                                                                     '\nAdena +', fmt.hbold('50000'),
                                                       '\nXP +', fmt.hbold('1000'),)),parse_mode='HTML')

@dp.message_handler(Text(equals='Крит.атака! (30% шанс)'))
@dp.throttled(rate=1)
async def krt2(message:types.Message):
    con = sq.connect("game.db")
    con.row_factory = sq.Row
    cur = con.cursor()
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        cur.executescript(f"UPDATE players SET rbfight = 1  WHERE id = {user_id}")
        df = int(cur.execute(f'SELECT minirb3 FROM players WHERE id = {user_id}').fetchone()[0])
        if df > 0:
            b = int(cur.execute(f'SELECT hp FROM players WHERE id = {user_id}').fetchone()[0])
            if b > 0:
                c = int(random.randrange(100))
                if c > 70:
                    a = int(cur.execute(f'SELECT atk + atkxp + krit*4 FROM players WHERE id = {user_id}').fetchone()[0])
                    cur.executescript(f"UPDATE players SET minirb3 = minirb3 - (atk + atkxp + krit*4)  WHERE id = {user_id}")
                    cur.executescript(f"UPDATE players SET hp = hp - 35000/(def + defxp)-50  WHERE id = {user_id}")
                    cur.execute(f"SELECT minirb3,hp FROM players WHERE id = {user_id}")
                    rows = cur.fetchone()
                    await message.answer(fmt.text(
                        fmt.text('\U0001F4A5\U0001F4A5\U0001F4A5 Вы отняли у Antharas :', fmt.hbold(a),
                                 '\n\U0001F432ХП Antharas стало:', fmt.hbold(rows['minirb3']),
                                 '\nAntharas Атакует! Ваше хп стало:',fmt.hbold(rows['hp']))),
                        parse_mode="HTML")
                if c < 70:
                    cur.executescript(f"UPDATE players SET hp = hp - 35000/(def + defxp)-50  WHERE id = {user_id}")
                    cur.execute(f"SELECT hp FROM players WHERE id = {user_id}")
                    rows = cur.fetchone()
                    await message.answer(fmt.text(fmt.text('Промах',
                                                           '\nAntharas! Ваше хп стало:',fmt.hbold(rows['hp']))),parse_mode="HTML")
            else:
                cur.executescript(f"UPDATE players SET minirb3 = 400000  WHERE id = {user_id}")
                cur.executescript(f"UPDATE players SET rbfight = 0  WHERE id = {user_id}")
                await message.answer("Вас убили")
        elif df < 0:
            d = int(random.randrange(100))
            if d > 70:
                cur.executescript(f"UPDATE players SET rbfight = 0  WHERE id = {user_id}")
                cur.executescript(f"UPDATE players SET gold = gold + 50000, xp = xp + 1000, tochkar = tochkar + 1  WHERE id = {user_id}")
                cur.executescript(f"UPDATE players SET rbfight = 0  WHERE id = {user_id}")
                cur.executescript(f"UPDATE players SET minirb3 = 400000  WHERE id = {user_id}")
                cur.executescript(f"UPDATE players SET aden = 'Sword of Miracles(A)90%'  WHERE id = {user_id}")
                await message.answer(fmt.text(fmt.text('Вы убили рб!!Вам выпал рецепт Sword of Miracles(A)90%!!',
                                                       '\nAdena +', fmt.hbold('50000'),
                                                       '\nXP +', fmt.hbold('1000'),)),parse_mode="HTML")
            if d < 70:
                cur.executescript(f"UPDATE players SET rbfight = 0  WHERE id = {user_id}")
                cur.executescript(f"UPDATE players SET gold = gold + 50000, xp = xp + 1000, tochkar = tochkar + 1  WHERE id = {user_id}")
                cur.executescript(f"UPDATE players SET rbfight = 0  WHERE id = {user_id}")
                cur.executescript(f"UPDATE players SET minirb3 = 400000  WHERE id = {user_id}")
                cur.executescript(f"UPDATE players SET minirb = minirb + 20 dion = dion +20, Varnish = Varnish + 20 WHERE id = {user_id}")
                await message.answer(fmt.text(fmt.text('Вы убили рб!!Вам выпало', fmt.hbold('20'),
                                                       'Varnish и', fmt.hbold('20'), 'Blue Gemstone', fmt.hbold('20'), 'Iron Ore!!'
                                                                                     '\nAdena +', fmt.hbold('50000'),
                                                       '\nXP +', fmt.hbold('1000'),)),parse_mode='HTML')


@dp.message_handler(Text(equals='\U0001F496ХП Банка!\U0001F496'))
@dp.throttled(rate=1)
async def healhp1 (message: types.Message):
    con = sq.connect("game.db")
    con.row_factory = sq.Row
    cur = con.cursor()
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        df = int(cur.execute(f'SELECT hpbanka FROM players WHERE id = {user_id}').fetchone()[0])
        if df >= 1:
            cur.executescript(f"UPDATE players SET hpbanka = hpbanka - 1 WHERE id = {user_id}")
            cur.executescript(f"UPDATE players SET hp = maxhp  WHERE id = {user_id}")
            cur.execute(f"SELECT maxhp,hpbanka FROM players where id = {user_id}")
            rows = cur.fetchone()
            await message.answer(fmt.text(fmt.text('\U0001F912 Хп восстановленно \U0001F912',
                                                   '\nМакс. ХП =', fmt.hbold(rows['maxhp']),
                                                    '\nБанок осталось ',fmt.hbold(rows['hpbanka']))),parse_mode="html")
        elif df < 1:
            await message.answer("Закончились ХП банки")

@dp.message_handler(Text(equals='\U0001F4A7МП банка!\U0001F4A7'))
@dp.throttled(rate=1)
async def healmp1 (message: types.Message):
    con = sq.connect("game.db")
    con.row_factory = sq.Row
    cur = con.cursor()
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        df = int(cur.execute(f'SELECT mpbanka FROM players WHERE id = {user_id}').fetchone()[0])
        if df >= 1:
            cur.executescript(f"UPDATE players SET mpbanka = mpbanka - 1, mp = maxmp WHERE id = {user_id}")

            cur.execute(f"SELECT maxmp,mpbanka FROM players where id = {user_id}")
            rows = cur.fetchone()
            await message.answer(fmt.text(fmt.text('\U0001F4A7 Мп восстановленно \U0001F4A7',
                                                   '\nМакс. МП =', fmt.hbold(rows['maxmp']),
                                                   '\nБанок осталось ',fmt.hbold(rows['mpbanka']))),parse_mode="html")
        elif df < 1:
            await message.answer("Закончились МП банки")

@dp.message_handler(Text(equals='\U0001F386Critical Blow!\U0001F386\n(-2 МП)'))
@dp.throttled(rate=1)
async def skl4(message:types.Message):
    con = sq.connect("game.db")
    con.row_factory = sq.Row
    cur = con.cursor()
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        cur.executescript(f"UPDATE players SET rbfight = 1  WHERE id = {user_id}")
        df = int(cur.execute(f'SELECT minirb3 FROM players WHERE id = {user_id}').fetchone()[0])
        if df > 0:
            m = int(cur.execute(f'SELECT hp FROM players WHERE id = {user_id}').fetchone()[0])
            if m > 0:
                a = int(cur.execute(f'SELECT mp FROM players WHERE id = {user_id}').fetchone()[0])
                if a >= 2:
                    cur.executescript(f"UPDATE players SET minirb3 = minirb3 - krit*5,mp=mp-2  WHERE id = {user_id}")
                    cur.executescript(f"UPDATE players SET hp = hp - 35000/(def + defxp)-50  WHERE id = {user_id}")
                    cur.execute(f"SELECT minirb3, mp, krit,hp FROM players WHERE id = {user_id}")
                    rows = cur.fetchone()
                    await message.answer(fmt.text(
                        fmt.text('\U0001F386Вы используете Critical Blow!\U0001F386:', fmt.hbold(rows['krit']),'*',fmt.hbold('5'),
                                 '\n\U0001F4A7Ваше Мп стало:',fmt.hbold(rows['mp']),
                                 '\n\U0001F432ХП Antharas стало:', fmt.hbold(rows['minirb3']),
                                 '\nFlame Lord Shadar Атакует! Ваше хп стало:',fmt.hbold(rows['hp']))),
                        parse_mode="HTML")
                else:
                    await message.answer("Недостаточно МП")
            else:
                cur.executescript(f"UPDATE players SET minirb3 = 400000  WHERE id = {user_id}")
                cur.executescript(f"UPDATE players SET rbfight = 0  WHERE id = {user_id}")
                await message.answer("Вас убили")

        elif df < 0:
            d = int(random.randrange(100))
            if d > 70:
                cur.executescript(f"UPDATE players SET rbfight = 0  WHERE id = {user_id}")
                cur.executescript(f"UPDATE players SET gold = gold + 50000, xp = xp + 1000, tochkar = tochkar + 1  WHERE id = {user_id}")
                cur.executescript(f"UPDATE players SET rbfight = 0  WHERE id = {user_id}")
                cur.executescript(f"UPDATE players SET minirb3 = 400000  WHERE id = {user_id}")
                cur.executescript(f"UPDATE players SET aden = 'Sword of Miracles(A)90%'  WHERE id = {user_id}")
                await message.answer(fmt.text(fmt.text('Вы убили рб!!Вам выпал рецепт Sword of Miracles(A)90%!!',
                                                       '\nAdena +', fmt.hbold('50000'),
                                                       '\nXP +', fmt.hbold('1000'),)),parse_mode="HTML")
            if d < 70:
                cur.executescript(f"UPDATE players SET rbfight = 0  WHERE id = {user_id}")
                cur.executescript(f"UPDATE players SET gold = gold + 50000, xp = xp + 1000, tochkar = tochkar + 1  WHERE id = {user_id}")
                cur.executescript(f"UPDATE players SET rbfight = 0  WHERE id = {user_id}")
                cur.executescript(f"UPDATE players SET minirb3 = 400000  WHERE id = {user_id}")
                cur.executescript(f"UPDATE players SET minirb = minirb + 20 dion = dion +20, Varnish = Varnish + 20 WHERE id = {user_id}")
                await message.answer(fmt.text(fmt.text('Вы убили рб!!Вам выпало', fmt.hbold('20'),
                                                       'Varnish и', fmt.hbold('20'), 'Blue Gemstone', fmt.hbold('20'), 'Iron Ore!!'
                                                                                     '\nAdena +', fmt.hbold('50000'),
                                                       '\nXP +', fmt.hbold('1000'),)),parse_mode='HTML')

@dp.message_handler(Text(equals='\U0001F531Triple Slash!\U0001F531\n(-2 МП)'))
@dp.throttled(rate=1)
async def skl5(message:types.Message):
    con = sq.connect("game.db")
    con.row_factory = sq.Row
    cur = con.cursor()
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        cur.executescript(f"UPDATE players SET rbfight = 1  WHERE id = {user_id}")
        df = int(cur.execute(f'SELECT minirb3 FROM players WHERE id = {user_id}').fetchone()[0])
        if df > 0:
            m = int(cur.execute(f'SELECT hp FROM players WHERE id = {user_id}').fetchone()[0])
            if m > 0:
                a = int(cur.execute(f'SELECT mp FROM players WHERE id = {user_id}').fetchone()[0])
                if a >= 2:
                    cur.executescript(f"UPDATE players SET minirb3 = minirb3 - (atk + atkxp*3), mp=mp-2  WHERE id = {user_id}")
                    cur.executescript(f"UPDATE players SET hp = hp - 35000/(def + defxp)-50  WHERE id = {user_id}")
                    cur.execute(f"SELECT minirb2, mp, atk,atkxp,hp FROM players WHERE id = {user_id}")
                    rows = cur.fetchone()
                    await message.answer(fmt.text(
                        fmt.text('\U0001F531Вы используете Triple Slash\U0001F531:',fmt.hbold(rows['atk']),'+', fmt.hbold(rows['atkxp']),'*',fmt.hbold('3'),
                                 '\n\U0001F4A7Ваше Мп стало:',fmt.hbold(rows['mp']),
                                 '\n\U0001F432ХП Antharas стало:', fmt.hbold(rows['minirb3']),
                                 '\nAntharas Атакует! Ваше хп стало:', fmt.hbold(rows['hp']))), parse_mode="HTML")
                else:
                    await message.answer("Недостаточно МП")
            else:
                cur.executescript(f"UPDATE players SET minirb3 = 400000  WHERE id = {user_id}")
                cur.executescript(f"UPDATE players SET rbfight = 0  WHERE id = {user_id}")
                await message.answer('Вас убили,')
        elif df < 0:
            d = int(random.randrange(100))
            if d > 70:
                cur.executescript(f"UPDATE players SET rbfight = 0  WHERE id = {user_id}")
                cur.executescript(f"UPDATE players SET gold = gold + 50000, xp = xp + 1000, tochkar = tochkar + 1  WHERE id = {user_id}")
                cur.executescript(f"UPDATE players SET rbfight = 0  WHERE id = {user_id}")
                cur.executescript(f"UPDATE players SET minirb3 = 400000  WHERE id = {user_id}")
                cur.executescript(f"UPDATE players SET aden = 'Sword of Miracles(A)90%'  WHERE id = {user_id}")
                await message.answer(fmt.text(fmt.text('Вы убили рб!!Вам выпал рецепт Sword of Miracles(A)90%!!',
                                                       '\nAdena +', fmt.hbold('50000'),
                                                       '\nXP +', fmt.hbold('1000'),)),parse_mode="HTML")
            if d < 70:
                cur.executescript(f"UPDATE players SET rbfight = 0  WHERE id = {user_id}")
                cur.executescript(f"UPDATE players SET gold = gold + 50000, xp = xp + 1000, tochkar = tochkar + 1  WHERE id = {user_id}")
                cur.executescript(f"UPDATE players SET rbfight = 0  WHERE id = {user_id}")
                cur.executescript(f"UPDATE players SET minirb3 = 400000  WHERE id = {user_id}")
                cur.executescript(f"UPDATE players SET minirb = minirb + 20 dion = dion +20, Varnish = Varnish + 20 WHERE id = {user_id}")
                await message.answer(fmt.text(fmt.text('Вы убили рб!!Вам выпало', fmt.hbold('20'),
                                                       'Varnish и', fmt.hbold('20'), 'Blue Gemstone', fmt.hbold('20'), 'Iron Ore!!'
                                                                                     '\nAdena +', fmt.hbold('50000'),
                                                       '\nXP +', fmt.hbold('1000'),)),parse_mode='HTML')


@dp.message_handler(Text(equals='\U0001F525HP Blow!\U0001F525\n(-2 МП)'))
@dp.throttled(rate=1)
async def skl6(message:types.Message):
    con = sq.connect("game.db")
    con.row_factory = sq.Row
    cur = con.cursor()
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        cur.executescript(f"UPDATE players SET rbfight = 1  WHERE id = {user_id}")
        df = int(cur.execute(f'SELECT minirb3 FROM players WHERE id = {user_id}').fetchone()[0])
        if df > 0:
            m = int(cur.execute(f'SELECT hp FROM players WHERE id = {user_id}').fetchone()[0])
            if m > 0:
                a = int(cur.execute(f'SELECT mp FROM players WHERE id = {user_id}').fetchone()[0])
                if a >= 2:
                    cur.executescript(f"UPDATE players SET minirb3 = minirb3 - maxhp*0.4, mp=mp-2  WHERE id = {user_id}")
                    cur.executescript(f"UPDATE players SET hp = hp - 35000/(def + defxp)-50  WHERE id = {user_id}")
                    b = int(cur.execute(f'SELECT maxhp*0.4 FROM players WHERE id = {user_id}').fetchone()[0])
                    cur.execute(f"SELECT minirb3, mp,hp FROM players WHERE id = {user_id}")
                    rows = cur.fetchone()
                    await message.answer(fmt.text(
                        fmt.text('\U0001F525Вы используете HP Blow\U0001F525:',fmt.hbold(b),
                                 '\n\U0001F4A7Ваше Мп стало:',fmt.hbold(rows['mp']),
                                 '\n\U0001F432ХП Antharas стало:', fmt.hbold(rows['minirb3']),
                                 '\nAntharas Атакует! Ваше хп стало:', fmt.hbold(rows['hp']))),
                        parse_mode="HTML")
                else:
                    await message.answer("Недостаточно МП")
            else:
                cur.executescript(f"UPDATE players SET minirb3 = 400000  WHERE id = {user_id}")
                cur.executescript(f"UPDATE players SET rbfight = 0  WHERE id = {user_id}")
                await message.answer('Вас убили')
        elif df < 0:
            d = int(random.randrange(100))
            if d > 70:
                cur.executescript(f"UPDATE players SET rbfight = 0  WHERE id = {user_id}")
                cur.executescript(f"UPDATE players SET gold = gold + 50000, xp = xp + 1000, tochkar = tochkar + 1  WHERE id = {user_id}")
                cur.executescript(f"UPDATE players SET rbfight = 0  WHERE id = {user_id}")
                cur.executescript(f"UPDATE players SET minirb3 = 400000  WHERE id = {user_id}")
                cur.executescript(f"UPDATE players SET aden = 'Sword of Miracles(A)90%'  WHERE id = {user_id}")
                await message.answer(fmt.text(fmt.text('Вы убили рб!!Вам выпал рецепт Sword of Miracles(A)90%!!',
                                                       '\nAdena +', fmt.hbold('50000'),
                                                       '\nXP +', fmt.hbold('1000'),)),parse_mode="HTML")
            if d < 70:
                cur.executescript(f"UPDATE players SET rbfight = 0  WHERE id = {user_id}")
                cur.executescript(f"UPDATE players SET gold = gold + 50000, xp = xp + 1000, tochkar = tochkar + 1  WHERE id = {user_id}")
                cur.executescript(f"UPDATE players SET rbfight = 0  WHERE id = {user_id}")
                cur.executescript(f"UPDATE players SET minirb3 = 400000  WHERE id = {user_id}")
                cur.executescript(f"UPDATE players SET minirb = minirb + 20 dion = dion +20, Varnish = Varnish + 20 WHERE id = {user_id}")
                await message.answer(fmt.text(fmt.text('Вы убили рб!!Вам выпало', fmt.hbold('20'),
                                                       'Varnish и', fmt.hbold('20'), 'Blue Gemstone', fmt.hbold('20'), 'Iron Ore!!'
                                                                                     '\nAdena +', fmt.hbold('50000'),
                                                       '\nXP +', fmt.hbold('1000'),)),parse_mode='HTML')


def register_rb2(dp: Dispatcher):
        dp.register_message_handler(antaras, Text(equals='\U0001F432Antharas\U0001F432'))
        dp.register_message_handler(atk1, Text(equals='Атака!'))
        dp.register_message_handler(krt2, Text(equals='Крит.атака! (30% шанс)'))
        dp.register_message_handler(skl4, Text(equals='\U0001F386Critical Blow!\U0001F386(-2 МП)'))
        dp.register_message_handler(skl5, Text(equals='\U0001F531Triple Slash!\U0001F531\n(-2 МП)'))
        dp.register_message_handler(skl6, Text(equals='\U0001F525HP Blow!\U0001F525\n(-2 МП)'))

