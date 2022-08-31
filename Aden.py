from aiogram.dispatcher import Dispatcher
from aiogram import  types
from aiogram.dispatcher.filters import Text
import aiogram.utils.markdown as fmt
import sqlite3 as sq
import random
from skilsss import *
import asyncio

@dp.throttled(rate=1)  #Акула
async def mob9(message:types.Message):
    con = sq.connect("game.db")
    con.row_factory = sq.Row
    cur = con.cursor()
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        h = int(cur.execute(f"SELECT hp FROM players where id = {user_id}").fetchone()[0])
        if h > 0:
            c = int(random.randrange(100))
            if c > 90:
                cur.executescript(f"UPDATE players SET mob9 = mob9 - atk - krit*4 - atkxp,"
                                  f" hp = hp - 150 - (7000/(def + defxp)) WHERE id = {user_id}")
                cur.execute(f"SELECT mob9,atk,krit,hp,atkxp FROM players WHERE id = {user_id}")
                rows = cur.fetchone()
                await message.answer(fmt.text(fmt.text('\U0001F4A5\U0001F4A5\U0001F4A5КРИТ!!! Вы отняли у Акулы :', fmt.hbold(rows['atk']),
                                                       '-', fmt.hbold(rows['krit']), '*', fmt.hbold('4'),'-', fmt.hbold(rows['atkxp']),
                         '\nАкула в ответ КУСАЕТ вас, ваше ХП стало:', fmt.hbold(rows['hp']),
                         '\n\U0001F988ХП Акулы стало:', fmt.hbold(rows['mob9']),)), parse_mode="HTML")
                r = int(cur.execute(f"SELECT mob9 FROM players WHERE id = {user_id}").fetchone()[0])
                if r <= 0:
                    drop = random.randrange(100)
                    if drop < 50:
                        cur.executescript(f"UPDATE players SET gold = gold+500, mob9 = 11000, xp = xp+6,"
                                          f" hpxp = hpxp +1 WHERE id = {user_id}")
                        await message.answer(fmt.text(
                            fmt.text(' Поздравляю! Вы убили Акулу!\nAdena +', fmt.hbold('500'),'\nXp +',fmt.hbold('6'))),parse_mode="HTML")
                    if drop > 50:
                        cur.executescript(f"UPDATE players SET gold = gold+500, mob9 = 11000, xp = xp+6,"
                                          f" hpxp = hpxp+1, minirb = minirb + 2 WHERE id = {user_id}")
                        await message.answer(fmt.text(
                            fmt.text('Поздравляю! Вы убили Акулу!\nУдача! Выпало 2 Iron Ore! \nAdena +', fmt.hbold('500'),
                                     '\nXp +', fmt.hbold('6'))), parse_mode="HTML")
            elif c < 90:
                cur.executescript(f"UPDATE players SET mob9 = mob9 - atk - atkxp, hp = hp - (7000/(def + defxp)) WHERE id = {user_id}")
                cur.execute(f"SELECT mob9,atk,hp,atkxp FROM players WHERE id = {user_id}")
                rows = cur.fetchone()
                await message.answer(fmt.text(fmt.text('\U0001F4A5 Вы отняли у Акулы :', fmt.hbold(rows['atk']),'+', fmt.hbold(rows['atkxp']) ,
                                                       '\nАкула атакует, ваше ХП стало:', fmt.hbold(rows['hp']),
                                           '\n\U0001F988ХП Акулы стало:', fmt.hbold(rows['mob9']))), parse_mode="HTML")
                r = int(cur.execute(f"SELECT mob9 FROM players WHERE id = {user_id} ").fetchone()[0])
                if r <= 0:
                    drop = random.randrange(100)
                    if drop < 50:
                        cur.executescript(f"UPDATE players SET gold = gold+500, mob9 = 11000, xp = xp+6,"
                            f" hpxp = hpxp +1 WHERE id = {user_id}")
                        await message.answer(fmt.text(fmt.text(' Поздравляю! Вы убили Акулу!\nAdena +', fmt.hbold('500'),
                                     '\nXp +', fmt.hbold('6'))), parse_mode="HTML")
                    if drop > 50:
                        cur.executescript(f"UPDATE players SET gold = gold+500, mob9 = 11000, xp = xp+6,"
                                          f""f" hpxp = hpxp+1, minirb = minirb + 2 WHERE id = {user_id}")
                        await message.answer(fmt.text(
                            fmt.text('Поздравляю! Вы убили Акулу!\nУдача! Выпало 2 Iron Ore!\nAdena +',fmt.hbold('500'),'\nXp +', fmt.hbold('6'))), parse_mode="HTML")
        else:
            cur.executescript(f"UPDATE players SET mob9 = 11000, hp = 0 where id = {user_id}")
            await message.answer('\U0001F3F3Вас убили, хп монстра восстановилось\U0001F3F3')

@dp.throttled(rate=1)  #Медведь
async def mob10(message:types.Message):
    con = sq.connect("game.db")
    con.row_factory = sq.Row
    cur = con.cursor()
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        h = int(cur.execute(f"SELECT hp FROM players where id = {user_id}").fetchone()[0])
        if h > 0:
            c = int(random.randrange(100))
            if c > 70:
                cur.executescript(f"UPDATE players SET mob10 = mob10 - atk - krit*4 - atkxp,"
                                  f" hp = hp - 350 + defxp WHERE id = {user_id}")
                cur.execute(f"SELECT mob10,atk,krit,hp,atkxp FROM players WHERE id = {user_id}")
                rows = cur.fetchone()
                await message.answer(fmt.text(fmt.text('\U0001F4A5\U0001F4A5\U0001F4A5КРИТ!!! Вы отняли у Медведя :', fmt.hbold(rows['atk']),
                                                       '-', fmt.hbold(rows['krit']), '*', fmt.hbold('4'),'-', fmt.hbold(rows['atkxp']),
                         '\nМедведь в ответ ЦАРАПАЕТ вас, ваше ХП стало:', fmt.hbold(rows['hp']),
                         '\n\U0001F43BХП Медведя стало:', fmt.hbold(rows['mob10']),)), parse_mode="HTML")
                r = int(cur.execute(f"SELECT mob10 FROM players WHERE id = {user_id}").fetchone()[0])
                if r <= 0:
                    drop = random.randrange(100)
                    if drop < 50:
                        cur.executescript(f"UPDATE players SET gold = gold+600, mob10 = 13000, xp = xp+6,"
                                          f" hpxp = hpxp +1,bearq=bearq+1 WHERE id = {user_id}")
                        await message.answer(fmt.text(
                            fmt.text(' Поздравляю! Вы убили Медведя!\nAdena +', fmt.hbold('600'),'\nXp +',fmt.hbold('6'),'\nКость медведя +', fmt.hbold('1'))),parse_mode="HTML")
                    if drop > 50:
                        cur.executescript(f"UPDATE players SET gold = gold+600, mob10 = 13000, xp = xp+6,"
                                          f" hpxp = hpxp+1, dion = dion + 2 WHERE id = {user_id}")
                        await message.answer(fmt.text(
                            fmt.text('Поздравляю! Вы убили Медведя!\nУдача! Выпало 2 Blue Gemstone! \nAdena +', fmt.hbold('600'),
                                     '\nXp +', fmt.hbold('6'))), parse_mode="HTML")
            elif c < 70:
                cur.executescript(f"UPDATE players SET mob10 = mob10 - atk - atkxp, hp = hp - 250 + defxp WHERE id = {user_id}")
                cur.execute(f"SELECT mob10,atk,hp,atkxp FROM players WHERE id = {user_id}")
                rows = cur.fetchone()
                await message.answer(fmt.text(fmt.text('\U0001F4A5 Вы отняли у Медведя :', fmt.hbold(rows['atk']),'+', fmt.hbold(rows['atkxp']) ,
                                                       '\nМедведь атакует, ваше ХП стало:', fmt.hbold(rows['hp']),
                                           '\n\U0001F43BХП Медведя стало:', fmt.hbold(rows['mob10']))), parse_mode="HTML")
                r = int(cur.execute(f"SELECT mob10 FROM players WHERE id = {user_id} ").fetchone()[0])
                if r <= 0:
                    drop = random.randrange(100)
                    if drop < 50:
                        cur.executescript(f"UPDATE players SET gold = gold+600, mob10 = 13000, xp = xp+6,"
                                          f" hpxp = hpxp +1,bearq=bearq+1 WHERE id = {user_id}")
                        await message.answer(fmt.text(
                            fmt.text(' Поздравляю! Вы убили Медведя!\nAdena +', fmt.hbold('600'),'\nXp +',fmt.hbold('6'),'\nКость медведя +', fmt.hbold('1'))),parse_mode="HTML")
                    if drop > 50:
                        cur.executescript(f"UPDATE players SET gold = gold+600, mob10 = 13000, xp = xp+6,"
                                          f" hpxp = hpxp+1, dion = dion + 2 WHERE id = {user_id}")
                        await message.answer(fmt.text(
                            fmt.text('Поздравляю! Вы убили Медведя!\nУдача! Выпало 2 Blue Gemstone! \nAdena +', fmt.hbold('600'),
                                     '\nXp +', fmt.hbold('6'))), parse_mode="HTML")
        else:
            cur.executescript(f"UPDATE players SET mob10 = 13000, hp = 0 where id = {user_id}")
            await message.answer('\U0001F3F3Вас убили, хп монстра восстановилось\U0001F3F3')
@dp.throttled(rate=1)  #Цербер
async def mob11(message:types.Message):
    con = sq.connect("game.db")
    con.row_factory = sq.Row
    cur = con.cursor()
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        h = int(cur.execute(f"SELECT hp FROM players where id = {user_id}").fetchone()[0])
        if h > 0:
            c = int(random.randrange(100))
            if c > 90:
                cur.executescript(f"UPDATE players SET mob11 = mob11 - atk - krit*4 - atkxp,"
                                  f" hp = hp - 20 - (10000/(def + defxp)) WHERE id = {user_id}")
                cur.execute(f"SELECT mob11,atk,krit,hp,atkxp FROM players WHERE id = {user_id}")
                rows = cur.fetchone()
                await message.answer(fmt.text(fmt.text('\U0001F4A5\U0001F4A5\U0001F4A5КРИТ!!! Вы отняли у Цербера :', fmt.hbold(rows['atk']),
                                                       '-', fmt.hbold(rows['krit']), '*', fmt.hbold('4'),'-', fmt.hbold(rows['atkxp']),
                         '\nЦербер атакует вас, ваше ХП стало:', fmt.hbold(rows['hp']),
                         '\n\U0001F415ХП Цербера стало:', fmt.hbold(rows['mob11']),)), parse_mode="HTML")
                r = int(cur.execute(f"SELECT mob11 FROM players WHERE id = {user_id}").fetchone()[0])
                if r <= 0:
                    drop = random.randrange(100)
                    if drop < 70:
                        cur.executescript(f"UPDATE players SET hp = hp - 100 WHERE id = {user_id}")
                        cur.executescript(f"UPDATE players SET gold = gold+700, mob11 = 16000, xp = xp+7,"
                                          f" hpxp = hpxp +1 WHERE id = {user_id}")
                        await message.answer(fmt.text(
                            fmt.text(' Поздравляю! Вы убили Цербера!\nЦербер перед смертью успел вас ударить <b>ХП - 100</b>'
                                     '\nAdena +', fmt.hbold('700'),'\nXp +',fmt.hbold('7'))),parse_mode="HTML")
                    if drop > 70:
                        cur.executescript(f"UPDATE players SET hp = hp - 100 WHERE id = {user_id}")
                        cur.executescript(f"UPDATE players SET gold = gold+700, mob10 = 16000, xp = xp+7,"
                                          f" hpxp = hpxp+1, varnish = varnish + 2 WHERE id = {user_id}")
                        await message.answer(fmt.text(
                            fmt.text('Поздравляю! Вы убили Цербера!\nЦербер перед смертью успел вас ударить <b>ХП - 100</b>'
                                     '\nУдача! Выпало 2 Varnish! \nAdena +', fmt.hbold('700'),
                                     '\nXp +', fmt.hbold('7'))), parse_mode="HTML")
            elif c < 90:
                cur.executescript(f"UPDATE players SET mob11 = mob11 - atk - atkxp, hp = hp - 20 - (10000/(def + defxp)) WHERE id = {user_id}")
                cur.execute(f"SELECT mob11,atk,hp,atkxp FROM players WHERE id = {user_id}")
                rows = cur.fetchone()
                await message.answer(fmt.text(fmt.text('\U0001F4A5 Вы отняли у Цербера :', fmt.hbold(rows['atk']),'+', fmt.hbold(rows['atkxp']) ,
                                                       '\nЦербер атакует, ваше ХП стало:', fmt.hbold(rows['hp']),
                                           '\n\U0001F415ХП Цербера стало:', fmt.hbold(rows['mob11']))), parse_mode="HTML")
                r = int(cur.execute(f"SELECT mob11 FROM players WHERE id = {user_id} ").fetchone()[0])
                if r <= 0:
                    drop = random.randrange(100)
                    if drop < 70:
                        cur.executescript(f"UPDATE players SET hp = hp - 100 WHERE id = {user_id}")
                        cur.executescript(f"UPDATE players SET gold = gold+700, mob11 = 16000, xp = xp+7,"
                                          f" hpxp = hpxp +1 WHERE id = {user_id}")
                        await message.answer(fmt.text(
                            fmt.text(' Поздравляю! Вы убили Цербера!\nЦербер перед смертью успел вас ударить <b>ХП - 100</b>'
                                     '\nAdena +', fmt.hbold('700'),'\nXp +',fmt.hbold('7'))),parse_mode="HTML")
                    if drop > 70:
                        cur.executescript(f"UPDATE players SET hp = hp - 100 WHERE id = {user_id}")
                        cur.executescript(f"UPDATE players SET gold = gold+700, mob11 = 16000, xp = xp+7,"
                                          f" hpxp = hpxp+1, varnish = varnish + 2 WHERE id = {user_id}")
                        await message.answer(fmt.text(
                            fmt.text('Поздравляю! Вы убили Цербера!\nЦербер перед смертью успел вас ударить <b>ХП - 100</b>'
                                     '\nУдача! Выпало 2 Varnish! \nAdena +', fmt.hbold('700'),
                                     '\nXp +', fmt.hbold('7'))), parse_mode="HTML")

        else:
            cur.executescript(f"UPDATE players SET mob11 = 16000, hp = 0 where id = {user_id}")
            await message.answer('\U0001F3F3Вас убили, хп монстра восстановилось\U0001F3F3')

@dp.throttled(rate=1)  #Лев
async def mob12(message:types.Message):
    con = sq.connect("game.db")
    con.row_factory = sq.Row
    cur = con.cursor()
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        h = int(cur.execute(f"SELECT hp FROM players where id = {user_id}").fetchone()[0])
        if h > 0:
            c = int(random.randrange(100))
            if c > 90:
                cur.executescript(f"UPDATE players SET mob12 = mob12 - atk - krit*4 - atkxp,"
                                  f" hp = hp - 60 - (20000/(def + defxp)) WHERE id = {user_id}")
                cur.execute(f"SELECT mob12,atk,krit,hp,atkxp FROM players WHERE id = {user_id}")
                rows = cur.fetchone()
                await message.answer(fmt.text(fmt.text('\U0001F4A5\U0001F4A5\U0001F4A5КРИТ!!! Вы отняли у Льва :', fmt.hbold(rows['atk']),
                                                       '-', fmt.hbold(rows['krit']), '*', fmt.hbold('4'),'-', fmt.hbold(rows['atkxp']),
                         '\nЛев атакует вас, ваше ХП стало:', fmt.hbold(rows['hp']),
                         '\n\U0001F981ХП Льва стало:', fmt.hbold(rows['mob12']),)), parse_mode="HTML")
                r = int(cur.execute(f"SELECT mob12 FROM players WHERE id = {user_id}").fetchone()[0])
                if r <= 0:
                    drop = random.randrange(100)
                    if drop < 99:
                        cur.executescript(f"UPDATE players SET gold = gold+800, mob12 = 16000, xp = xp+8,"
                                          f" hpxp = hpxp +1,lionq=lionq+1 WHERE id = {user_id}")
                        await message.answer(fmt.text(
                            fmt.text(' Поздравляю! Вы убили Льва!\nAdena +', fmt.hbold('800'),'\nXp +',fmt.hbold('8'),
                                     '\nПлоть льва +', fmt.hbold('1'))),parse_mode="HTML")
                    if drop > 99:
                        cur.executescript(f"UPDATE players SET gold = gold+800, mob12 = 16000, xp = xp+8,"
                                          f" hpxp = hpxp+1, aden = 'Dark Crystal Armor(A)90%' WHERE id = {user_id}")
                        await message.answer(fmt.text(
                            fmt.text('Поздравляю! Вы убили Льва!\nУдача! Выпал рецепт Dark Crystal Armor(A)90%! \nAdena +', fmt.hbold('800'),
                                     '\nXp +', fmt.hbold('8'))), parse_mode="HTML")
            elif c < 90:
                cur.executescript(f"UPDATE players SET mob12 = mob12 - atk - atkxp, "
                                  f"hp = hp - 60 - (20000/(def + defxp)) WHERE id = {user_id}")
                cur.execute(f"SELECT mob12,atk,hp,atkxp FROM players WHERE id = {user_id}")
                rows = cur.fetchone()
                await message.answer(fmt.text(fmt.text('\U0001F4A5 Вы отняли у Льва :', fmt.hbold(rows['atk']),'+', fmt.hbold(rows['atkxp']) ,
                                                       '\nЛев атакует, ваше ХП стало:', fmt.hbold(rows['hp']),
                                           '\n\U0001F981ХП Льва стало:', fmt.hbold(rows['mob12']))), parse_mode="HTML")
                r = int(cur.execute(f"SELECT mob12 FROM players WHERE id = {user_id} ").fetchone()[0])
                if r <= 0:
                    drop = random.randrange(100)
                    if drop < 99:
                        cur.executescript(f"UPDATE players SET gold = gold+800, mob12 = 16000, xp = xp+8,"
                                          f" hpxp = hpxp +1,lionq=lionq+1 WHERE id = {user_id}")
                        await message.answer(fmt.text(
                            fmt.text(' Поздравляю! Вы убили Льва!\nAdena +', fmt.hbold('800'),'\nXp +',fmt.hbold('8'),
                                     '\nПлоть льва +', fmt.hbold('1'))),parse_mode="HTML")
                    if drop > 99:
                        cur.executescript(f"UPDATE players SET gold = gold+800, mob12 = 16000, xp = xp+8,"
                                          f" hpxp = hpxp+1, aden = 'Dark Crystal Armor(A)90%' WHERE id = {user_id}")
                        await message.answer(fmt.text(
                            fmt.text('Поздравляю! Вы убили Льва!\nУдача! Выпал рецепт Dark Crystal Armor(A)90%! \nAdena +', fmt.hbold('800'),
                                     '\nXp +', fmt.hbold('8'))), parse_mode="HTML")
        else:
            cur.executescript(f"UPDATE players SET mob12 = 16000, hp = 0 where id = {user_id}")
            await message.answer('\U0001F3F3Вас убили, хп монстра восстановилось\U0001F3F3')

@dp.throttled(rate=1)  #Призрак призыв
async def mob13(message:types.Message):
    con = sq.connect("game.db")
    con.row_factory = sq.Row
    cur = con.cursor()
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        a = int(cur.execute(f"SELECT nosq FROM players where id = {user_id}").fetchone()[0])
        b = int(cur.execute(f"SELECT bufq FROM players where id = {user_id}").fetchone()[0])
        c = int(cur.execute(f"SELECT lionq FROM players where id = {user_id}").fetchone()[0])
        d = int(cur.execute(f"SELECT bearq FROM players where id = {user_id}").fetchone()[0])
        e = int(cur.execute(f"SELECT aliq FROM players where id = {user_id}").fetchone()[0])
        if ((a >= 10) and (b >= 10) and (c >= 10) and (d >= 10) and (e >= 10)):
            hp = random.randint(8000, 500000)
            ataka = random.randint(10000, 70000)
            cur.executescript(f"UPDATE players SET mobr = {hp},mobra = {ataka} WHERE id = {user_id}")
            cur.executescript(f"UPDATE players SET nosq = nosq - 10, bufq = bufq -10, lionq = lionq -10, bearq=bearq-10,aliq=aliq-10,dinoq=dinoq-10 WHERE id = {user_id}")
            cur.execute(f"SELECT mobr,mobra FROM players where id = {user_id}")
            rows = cur.fetchone()
            await message.answer(fmt.text(fmt.text('Вы призвали призрака!\U0001F47B',
                                                                                         '\nЕго ХП:', fmt.hbold(rows['mobr']),
                                                   '\nЕго атака:', fmt.hbold(rows['mobra']))),parse_mode="HTML")
        else:
            await message.answer('Для призыва призрака нужно по 10 частей всех квестовых мобов!'
                                 '\n\nПризрак имеет случайное колличество хп и атакту, а так же дроп!'
                                 '\nНаходится в разделе с Raid Boss')

@dp.throttled(rate=1)  #Призрак бой
async def mob14(message:types.Message):
    con = sq.connect("game.db")
    con.row_factory = sq.Row
    cur = con.cursor()
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        h = int(cur.execute(f"SELECT hp FROM players where id = {user_id}").fetchone()[0])
        atak = int(cur.execute(f"SELECT mobra FROM players where id = {user_id}").fetchone()[0])
        if ((atak >=4000) and (h >= 0)):
            c = int(random.randrange(100))
            if c > 90:
                cur.executescript(f"UPDATE players SET mobr = mobr - atk - krit*4 - atkxp,"
                                  f" hp = hp - ({atak}/(def +defxp)) WHERE id = {user_id}")
                cur.execute(f"SELECT mobr,atk,krit,hp,atkxp FROM players WHERE id = {user_id}")
                rows = cur.fetchone()
                await message.answer(fmt.text(fmt.text('\U0001F4A5\U0001F4A5\U0001F4A5КРИТ!!! Вы отняли у Призрака :', fmt.hbold(rows['atk']),
                                                       '-', fmt.hbold(rows['krit']), '*', fmt.hbold('4'),'-', fmt.hbold(rows['atkxp']),
                         '\nПризрак атакует вас, ваше ХП стало:', fmt.hbold(rows['hp']),
                         '\n\U0001F47BХП Призрака стало:', fmt.hbold(rows['mobr']),)), parse_mode="HTML")
                r = int(cur.execute(f"SELECT mobr FROM players WHERE id = {user_id}").fetchone()[0])
                if r <= 0:
                    gold = random.randint(500,6000)
                    xp = random.randrange(100)
                    cur.executescript(f"UPDATE players SET gold = gold+{gold}, mobra = 0, xp = xp+{xp},"
                                      f" tochkar=tochkar+1, tochkab = tochkab +1 WHERE id = {user_id}")
                    await message.answer(fmt.text(
                        fmt.text('Поздравляю! Вы убили Призрака!\nВыпала Блесс точка \nAdena +', fmt.hbold(f'{gold}'),
                                 '\nXp +', fmt.hbold(f'{xp}'))), parse_mode="HTML")
            elif c < 90:
                cur.executescript(f"UPDATE players SET mobr = mobr - atk - atkxp, "
                                  f"hp = hp - ({atak}/(def + defxp)) WHERE id = {user_id}")
                cur.execute(f"SELECT mobr,atk,hp,atkxp FROM players WHERE id = {user_id}")
                rows = cur.fetchone()
                await message.answer(fmt.text(fmt.text('\U0001F4A5 Вы отняли у Призрака :', fmt.hbold(rows['atk']),'+', fmt.hbold(rows['atkxp']) ,
                                                       '\nПризрак атакует, ваше ХП стало:', fmt.hbold(rows['hp']),
                                           '\n\U0001F47BХП ПРизрака стало:', fmt.hbold(rows['mobr']))), parse_mode="HTML")
                r = int(cur.execute(f"SELECT mobr FROM players WHERE id = {user_id} ").fetchone()[0])
                if r <= 0:
                    gold = random.randrange(10000)
                    xp = random.randrange(100)
                    cur.executescript(f"UPDATE players SET gold = gold+{gold}, mobra = 0, xp = xp+{xp},"
                                      f" tochkar=tochkar+1, tochkab = tochkab +1,mobr = 0 WHERE id = {user_id}")
                    await message.answer(fmt.text(
                        fmt.text('Поздравляю! Вы убили Призрака!\nВыпала Блесс точка \nAdena +', fmt.hbold(f'{gold}'),
                                 '\nXp +', fmt.hbold(f'{xp}'))), parse_mode="HTML")

        else:
            cur.executescript(f"UPDATE players SET mobra = 0, hp = 0 where id = {user_id}")
            await message.answer('\U0001F3F3Вас убили или вы не призвали призрака\U0001F3F3')




def register_aden(dp:Dispatcher):
  dp.register_message_handler(mob9, Text(equals='\U0001F988Акула\U0001F988'))
  dp.register_message_handler(mob10, Text(equals='\U0001F43BМедведь\U0001F43B'))
  dp.register_message_handler(mob11, Text(equals='\U0001F415Цербер\U0001F415'))
  dp.register_message_handler(mob12, Text(equals='\U0001F981Лев\U0001F981'))
  dp.register_message_handler(mob13, Text(equals='\U0001F47BПризвать призрака\U0001F47B'))
  dp.register_message_handler(mob14, Text(equals='\U0001F47BБой с призраком\U0001F47B'))

