from aiogram.dispatcher import Dispatcher
from aiogram import  types
from aiogram.dispatcher.filters import Text
import aiogram.utils.markdown as fmt
import sqlite3 as sq
import random
from skilsss import dp
import asyncio

@dp.throttled(rate=1)  #Джин
async def mob5(message:types.Message):
    con = sq.connect("game.db")
    con.row_factory = sq.Row
    cur = con.cursor()
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        h = cur.execute(f"SELECT hp FROM players where id = {user_id}").fetchone()
        for m in h:
            if m > 0:
                c = int(random.randrange(100))
                if c > 90:
                    cur.executescript(f"UPDATE players SET mob5 = mob5 - atk - krit*4 - atkxp,"
                                      f" hp = hp - (2000/(def + defxp)) WHERE id = {user_id}")
                    cur.execute(f"SELECT mob5,atk,krit,hp,atkxp FROM players WHERE id = {user_id}")
                    rows = cur.fetchone()
                    await message.answer(fmt.text(fmt.text('\U0001F4A5\U0001F4A5\U0001F4A5КРИТ!!! Вы отняли у Джина :', fmt.hbold(rows['atk']),
                                                           '-', fmt.hbold(rows['krit']), '*', fmt.hbold('4'),'-', fmt.hbold(rows['atkxp']),
                             '\nДжин атакует, ваше ХП стало:', fmt.hbold(rows['hp']),
                             '\n\U0001F9DEХП Джин стало:', fmt.hbold(rows['mob5']))), parse_mode="HTML")
                    r = cur.execute(f"SELECT mob5 FROM players WHERE id = {user_id}").fetchone()
                    for i in r:
                        if i <= 0:
                            drop = random.randrange(100)
                            if drop < 80:
                                cur.executescript(f"UPDATE players SET gold = gold+150, mob5 = 3600, xp = xp+4,"
                                                  f" hpxp = hpxp +1 WHERE id = {user_id}")
                                await message.answer(fmt.text(
                                    fmt.text(' Поздравляю! Вы убили Джина!\nAdena +', fmt.hbold('150'),'\nXp +',fmt.hbold('4'))),parse_mode="HTML")
                            if drop > 80:
                                cur.executescript(f"UPDATE players SET gold = gold+150, mob5 = 3600, xp = xp+4,"
                                                  f" hpxp = hpxp+1, minirb = minirb + 2 WHERE id = {user_id}")
                                await message.answer(fmt.text(
                                    fmt.text(' Поздравляю! Вы убили Джина!\n Удача! Выпало 2 Iron Ore! \nAdena +', fmt.hbold('150'),
                                             '\nXp +', fmt.hbold('4'))), parse_mode="HTML")
                elif c < 90:
                    cur.executescript(f"UPDATE players SET mob5 = mob5 - atk - atkxp, hp = hp - (2000/(def + defxp)) WHERE id = {user_id}")
                    cur.execute(f"SELECT mob5,atk,hp,atkxp FROM players WHERE id = {user_id}")
                    rows = cur.fetchone()
                    await message.answer(fmt.text(fmt.text('\U0001F4A5 Вы отняли у Джина :', fmt.hbold(rows['atk']),'+', fmt.hbold(rows['atkxp']) ,
                                                           '\nДжин атакует, ваше ХП стало:', fmt.hbold(rows['hp']),
                                               '\n\U0001F9DEХП Джин стало:', fmt.hbold(rows['mob5']))), parse_mode="HTML")
                    r = cur.execute(f"SELECT mob5 FROM players WHERE id = {user_id} ").fetchone()
                    for i in r:
                        if i <= 0:
                            drop = random.randrange(100)
                            if drop < 80:
                                cur.executescript(f"UPDATE players SET gold = gold+150, mob5 = 3600, xp = xp+4,"
                                    f" hpxp = hpxp +1 WHERE id = {user_id}")
                                await message.answer(fmt.text(fmt.text(' Поздравляю! Вы убили Джина!\nAdena +', fmt.hbold('150'),
                                             '\nXp +', fmt.hbold('4'))), parse_mode="HTML")
                            if drop > 80:
                                cur.executescript(f"UPDATE players SET gold = gold+150, mob5 = 3600, xp = xp+4,"
                                                  f""f" hpxp = hpxp+1, minirb = minirb + 2 WHERE id = {user_id}")
                                await message.answer(fmt.text(
                                    fmt.text(' Поздравляю! Вы убили Джин!\nУдача! Выпало 2 Iron Ore!\nAdena +',fmt.hbold('150'),'\nXp +', fmt.hbold('4'))), parse_mode="HTML")
            else:
                cur.executescript(f"UPDATE players SET mob5 = 3600, hp = 0 where id = {user_id}")
                await message.answer('\U0001F3F3Вас убили, хп монстра восстановилось\U0001F3F3')

@dp.throttled(rate=1)  #Носорог
async def mob6(message:types.Message):
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
                cur.executescript(f"UPDATE players SET mob6 = mob6 - atk - krit*4 - atkxp,"
                                  f" hp = hp - (3000/(def + defxp)) WHERE id = {user_id}")
                cur.execute(f"SELECT mob6,atk,krit,hp,atkxp FROM players WHERE id = {user_id}")
                rows = cur.fetchone()
                await message.answer(fmt.text(fmt.text('\U0001F4A5\U0001F4A5\U0001F4A5КРИТ!!! Вы отняли у Носорога :', fmt.hbold(rows['atk']),
                                                       '-', fmt.hbold(rows['krit']), '*', fmt.hbold('4'),'-', fmt.hbold(rows['atkxp']),
                         '\nНосорог атакует, ваше ХП стало:', fmt.hbold(rows['hp']),
                         '\n\U0001F98FХП Носорога стало:', fmt.hbold(rows['mob6']))), parse_mode="HTML")
                r = cur.execute(f"SELECT mob6 FROM players WHERE id = {user_id}").fetchone()
                for i in r:
                    if i <= 0:
                        drop = random.randrange(100)
                        if drop < 80:
                            cur.executescript(f"UPDATE players SET gold = gold+220, mob6 = 5000, xp = xp+4,"
                                              f" hpxp = hpxp +1,nosq=nosq+1 WHERE id = {user_id}")
                            await message.answer(fmt.text(
                                fmt.text(' Поздравляю! Вы убили Носорога!\nAdena +', fmt.hbold('220'),'\nXp +',fmt.hbold('4'),
                                         '\nЧереп носорога +', fmt.hbold('1'))),parse_mode="HTML")
                        if drop > 80:
                            cur.executescript(f"UPDATE players SET gold = gold+220, mob6 = 5000, xp = xp+4,"
                                              f" hpxp = hpxp+1, dion = dion + 2 WHERE id = {user_id}")
                            await message.answer(fmt.text(
                                fmt.text(' Поздравляю! Вы убили Носорога!\n Удача! Выпало 2 Blue Gemstone! \nAdena +', fmt.hbold('220'),
                                         '\nXp +', fmt.hbold('4'))), parse_mode="HTML")
            elif c < 90:
                cur.executescript(f"UPDATE players SET mob6 = mob6 - atk - atkxp, hp = hp - (3000/(def + defxp)) WHERE id = {user_id}")
                cur.execute(f"SELECT mob6,atk,hp,atkxp FROM players WHERE id = {user_id}")
                rows = cur.fetchone()
                await message.answer(fmt.text(fmt.text('\U0001F4A5 Вы отняли у Носорога :', fmt.hbold(rows['atk']),'+', fmt.hbold(rows['atkxp']) ,
                                                       '\nНосорог атакует, ваше ХП стало:', fmt.hbold(rows['hp']),
                                           '\n\U0001F98FХП Носорога стало:', fmt.hbold(rows['mob6']))), parse_mode="HTML")
                r = cur.execute(f"SELECT mob6 FROM players WHERE id = {user_id} ").fetchone()
                for i in r:
                    if i <= 0:
                        drop = random.randrange(100)
                        if drop < 80:
                            cur.executescript(f"UPDATE players SET gold = gold+220, mob6 = 5000, xp = xp+4,"
                                f" hpxp = hpxp +1,nosq = nosq + 1 WHERE id = {user_id}")
                            await message.answer(fmt.text(fmt.text(' Поздравляю! Вы убили Носорога!\nAdena +', fmt.hbold('220'),
                                         '\nXp +', fmt.hbold('4'),'\nЧереп носорога +', fmt.hbold('1'))), parse_mode="HTML")
                        if drop > 80:
                            cur.executescript(f"UPDATE players SET gold = gold+220, mob6 = 5000, xp = xp+4,"
                                              f""f" hpxp = hpxp+1, dion = dion + 2 WHERE id = {user_id}")
                            await message.answer(fmt.text(
                                fmt.text(' Поздравляю! Вы убили Носорога!\nУдача! Выпало 2 Blue Gemstone!\nAdena +',fmt.hbold('220'),'\nXp +', fmt.hbold('4'))), parse_mode="HTML")
        else:
            cur.executescript(f"UPDATE players SET mob6 = 5000, hp = 0 where id = {user_id}")
            await message.answer('\U0001F3F3Вас убили, хп монстра восстановилось\U0001F3F3')
@dp.throttled(rate=1)  #Дино
async def mob7(message:types.Message):
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
                cur.executescript(f"UPDATE players SET mob7 = mob7 - atk - krit*4 - atkxp,"
                                  f" hp = hp - (4500/(def + defxp)) WHERE id = {user_id}")
                cur.execute(f"SELECT mob7,atk,krit,hp,atkxp FROM players WHERE id = {user_id}")
                rows = cur.fetchone()
                await message.answer(fmt.text(fmt.text('\U0001F4A5\U0001F4A5\U0001F4A5КРИТ!!! Вы отняли у Дино :', fmt.hbold(rows['atk']),
                                                       '-', fmt.hbold(rows['krit']), '*', fmt.hbold('4'),'-', fmt.hbold(rows['atkxp']),
                         '\nДино атакует, ваше ХП стало:', fmt.hbold(rows['hp']),
                         '\n\U0001F995ХП Дино стало:', fmt.hbold(rows['mob7']))), parse_mode="HTML")
                r = cur.execute(f"SELECT mob7 FROM players WHERE id = {user_id}").fetchone()
                for i in r:
                    if i <= 0:
                        drop = random.randrange(100)
                        if drop < 80:
                            cur.executescript(f"UPDATE players SET gold = gold+270, mob7 = 6400, xp = xp+5,"
                                              f" hpxp = hpxp +1,dinoq = dinoq +1 WHERE id = {user_id}")
                            await message.answer(fmt.text(
                                fmt.text(' Поздравляю! Вы убили Дино!\nAdena +', fmt.hbold('270'),'\nXp +',fmt.hbold('5'),'\nЯйца дино +', fmt.hbold('1'))),parse_mode="HTML")
                        if drop > 80:
                            cur.executescript(f"UPDATE players SET gold = gold+270, mob7 = 6400, xp = xp+5,"
                                              f" hpxp = hpxp+1, Varnish = Varnish + 1 WHERE id = {user_id}")
                            await message.answer(fmt.text(
                                fmt.text(' Поздравляю! Вы убили Дино!\nУдача! Выпал Varnish! \nAdena +', fmt.hbold('270'),
                                         '\nXp +', fmt.hbold('5'))), parse_mode="HTML")
            elif c < 90:
                cur.executescript(f"UPDATE players SET mob7 = mob7 - atk - atkxp, hp = hp - (4500/(def + defxp)) WHERE id = {user_id}")
                cur.execute(f"SELECT mob7,atk,hp,atkxp FROM players WHERE id = {user_id}")
                rows = cur.fetchone()
                await message.answer(fmt.text(fmt.text('\U0001F4A5 Вы отняли у Дино :', fmt.hbold(rows['atk']),'+', fmt.hbold(rows['atkxp']) ,
                                                       '\nДино атакует, ваше ХП стало:', fmt.hbold(rows['hp']),
                                           '\n\U0001F995ХП Дино стало:', fmt.hbold(rows['mob7']))), parse_mode="HTML")
                r = cur.execute(f"SELECT mob7 FROM players WHERE id = {user_id} ").fetchone()
                for i in r:
                    if i <= 0:
                        drop = random.randrange(100)
                        if drop < 80:
                            cur.executescript(f"UPDATE players SET gold = gold+270, mob7 = 6400, xp = xp+5,"
                                f" hpxp = hpxp +1,dinoq = dinoq +1 WHERE id = {user_id}")
                            await message.answer(fmt.text(fmt.text(' Поздравляю! Вы убили Дино!\nAdena +', fmt.hbold('270'),
                                         '\nXp +', fmt.hbold('5'),'\nЯйца дино +', fmt.hbold('1'))), parse_mode="HTML")
                        if drop > 80:
                            cur.executescript(f"UPDATE players SET gold = gold+270, mob7 = 6400, xp = xp+5,"
                                              f""f" hpxp = hpxp+1, Varnish = Varnish + 1 WHERE id = {user_id}")
                            await message.answer(fmt.text(
                                fmt.text(' Поздравляю! Вы убили Дино!\nУдача! Выпал Varnish!\nAdena +',fmt.hbold('270'),'\nXp +', fmt.hbold('5'))), parse_mode="HTML")
        else:
            cur.executescript(f"UPDATE players SET mob7 = 6400, hp = 0 where id = {user_id}")
            await message.answer('\U0001F3F3Вас убили, хп монстра восстановилось\U0001F3F3')

@dp.throttled(rate=1)  #Буфало
async def mob8(message:types.Message):
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
            if c > 85:
                cur.executescript(f"UPDATE players SET mob8 = mob8 - atk - krit*4 - atkxp,"
                                  f" hp = hp - (6000/(def + defxp)) - 20 WHERE id = {user_id}")
                cur.execute(f"SELECT mob8,atk,krit,hp,atkxp FROM players WHERE id = {user_id}")
                rows = cur.fetchone()
                await message.answer(fmt.text(fmt.text('\U0001F4A5\U0001F4A5\U0001F4A5КРИТ!!! Вы отняли у Буфало :', fmt.hbold(rows['atk']),
                                                       '-', fmt.hbold(rows['krit']), '*', fmt.hbold('4'),'-', fmt.hbold(rows['atkxp']),
                         '\nБуфало атакует, ваше ХП стало:', fmt.hbold(rows['hp']),
                         '\n\U0001F403ХП Буфало стало:', fmt.hbold(rows['mob8']))), parse_mode="HTML")
                r = cur.execute(f"SELECT mob8 FROM players WHERE id = {user_id}").fetchone()
                for i in r:
                    if i <= 0:
                        drop = random.randrange(100)
                        if drop < 95:
                            cur.executescript(f"UPDATE players SET gold = gold+400, mob8 = 10000, xp = xp+5,"
                                              f" hpxp = hpxp +1,bufq=bufq+1 WHERE id = {user_id}")
                            await message.answer(fmt.text(
                                fmt.text(' Поздравляю! Вы убили Буфало!\nAdena +', fmt.hbold('400'),'\nXp +',fmt.hbold('5'),'\nХвост буфало +', fmt.hbold('1'))),parse_mode="HTML")
                        if drop > 95:
                            cur.executescript(f"UPDATE players SET gold = gold+400, mob8 = 10000, xp = xp+5,"
                                              f" hpxp = hpxp+1, giran = 'Blue Wolf Armor(B)' WHERE id = {user_id}")
                            await message.answer(fmt.text(
                                fmt.text(' Поздравляю! Вы убили Буфало!\n Удача! Выпал рецепт Blue Wolf Armor(B)! \nAdena +', fmt.hbold('400'),
                                         '\nXp +', fmt.hbold('5'))), parse_mode="HTML")
            elif c < 85:
                cur.executescript(f"UPDATE players SET mob8 = mob8 - atk - atkxp, hp = hp - (6000/(def + defxp))-20 WHERE id = {user_id}")
                cur.execute(f"SELECT mob8,atk,hp,atkxp FROM players WHERE id = {user_id}")
                rows = cur.fetchone()
                await message.answer(fmt.text(fmt.text('\U0001F4A5 Вы отняли у Буфало :', fmt.hbold(rows['atk']),'+', fmt.hbold(rows['atkxp']) ,
                                                       '\nБуфало атакует, ваше ХП стало:', fmt.hbold(rows['hp']),
                                           '\n\U0001F403ХП Буфало стало:', fmt.hbold(rows['mob8']))), parse_mode="HTML")
                r = cur.execute(f"SELECT mob8 FROM players WHERE id = {user_id} ").fetchone()
                for i in r:
                    if i <= 0:
                        drop = random.randrange(100)
                        if drop < 95:
                            cur.executescript(f"UPDATE players SET gold = gold+400, mob8 = 10000, xp = xp+5,"
                                f" hpxp = hpxp +1,bufq=bufq+1 WHERE id = {user_id}")
                            await message.answer(fmt.text(fmt.text(' Поздравляю! Вы убили Буфало!\nAdena +', fmt.hbold('400'),
                                         '\nXp +', fmt.hbold('5'),'\nХвост буфало +', fmt.hbold('1'))), parse_mode="HTML")
                        if drop > 95:
                            cur.executescript(f"UPDATE players SET gold = gold+400, mob8 = 10000, xp = xp+5,"
                                              f""f" hpxp = hpxp+1, giran = 'Blue Wolf Armor(B)' WHERE id = {user_id}")
                            await message.answer(fmt.text(
                                fmt.text(' Поздравляю! Вы убили Буфало!\nУдача! Выпал рецепт Blue Wolf Armor(B)!\nAdena +',fmt.hbold('400'),
                                         '\nXp +', fmt.hbold('5'))), parse_mode="HTML")
        else:
            cur.executescript(f"UPDATE players SET mob8 = 10000, hp = 0 where id = {user_id}")
            await message.answer('\U0001F3F3Вас убили, хп монстра восстановилось\U0001F3F3')

def register_giran(dp:Dispatcher):
  dp.register_message_handler(mob5, Text(equals='\U0001F9DEДжин\U0001F9DE'))
  dp.register_message_handler(mob6, Text(equals='\U0001F98FНосорог\U0001F98F'))
  dp.register_message_handler(mob7, Text(equals='\U0001F995Дино\U0001F995'))
  dp.register_message_handler(mob8, Text(equals='\U0001F403Буфало\U0001F403'))