from aiogram.dispatcher import Dispatcher
from aiogram import  types
from aiogram.dispatcher.filters import Text
import sqlite3 as sq
import random
from skilsss import dp
from keyboards import craft



@dp.message_handler(commands=['craft'])
@dp.throttled(rate=1)
async def craftb12(message: types.Message):
  await message.answer(("Список вещей которые можно скрафтить"
                        "\n\n<b>Earing of Black Ore(B)</b> - 200 Iron Ore, 100 Blue Gemstone, рецепт"
                        "\n<b>Blue Wolf Armor(B)</b> - 200 Iron Ore, 200 Blue Gemstone, 100 Varnish, рецепт"
                        "\n<b>Dark Crystal Armor(A)</b> - 300 Iron Ore, 300 Blue Gemstone, 200 Varnish, рецепт"
                        "\n<b>Sword of Miracles(A)</b> - 300 Iron Ore, 300 Blue Gemstone, 300 Varnish, рецепт"), reply_markup = craft, parse_mode='HTML')


@dp.message_handler(Text(equals='\U0001F4FFEaring of Black Ore(B)(+1000 ХП, +40 Крит)\U0001F4FF'))
@dp.throttled(rate=1)
async def craftBO(message: types.Message):
    con = sq.connect("game.db")
    con.row_factory = sq.Row
    cur = con.cursor()
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        weapon = cur.execute(f"SELECT tochkam FROM players WHERE id = {user_id}").fetchone()
        for i in weapon:
            if i == "Earing of Black Ore(B)":
                await message.answer("У тебя уже есть Earing of Black Ore(B)")
            elif i != "Earing of Black Ore(B)":
                slit = cur.execute(f"SELECT minirb FROM players WHERE id = {user_id}").fetchone()
                for i in slit:
                    if i >= 200:
                        weapon = cur.execute(f"SELECT giran FROM players WHERE id = {user_id}").fetchone()
                        for i in weapon:
                            if i == "Earing of Black Ore(B)":
                                crystal = cur.execute(f"SELECT dion FROM players WHERE id = {user_id}").fetchone()
                                for i in crystal:
                                    if i >= 100:
                                        cur.executescript(f"UPDATE players SET tochkam = 'Earing of Black Ore(B)' WHERE id = {user_id} ")
                                        cur.executescript(f"UPDATE players SET maxhp = maxhp + 1000,krit = krit + 40 WHERE id = {user_id} ")
                                        cur.executescript(f"UPDATE players SET dion = dion -100, minirb = minirb - 200, giran = 0 WHERE id = {user_id} ")
                                        await message.answer("Поздравляем вы скрафтили Earing of Black Ore(B)!!")
                                    else:
                                        await message.answer("Недостаточно Blue Gemstone.Требуется 100")
                            else:
                                await message.answer("Требуется рецепт!")
                    else:
                        await message.answer("Недостаточно Iron Ore.Требуется 200")

@dp.message_handler(Text(equals='\U0001F43ABlue Wolf Armor(B)\U0001F43A'))
@dp.throttled(rate=1)
async def craftBw(message: types.Message):
    con = sq.connect("game.db")
    con.row_factory = sq.Row
    cur = con.cursor()
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        weapon = cur.execute(f"SELECT armor FROM players WHERE id = {user_id}").fetchone()
        for i in weapon:
            if i == "Blue Wolf Armor(B) +":
                await message.answer("У тебя уже есть Blue Wolf Armor(B)")
            elif i != "Blue Wolf Armor(B) +":
                slit = cur.execute(f"SELECT minirb FROM players WHERE id = {user_id}").fetchone()
                for i in slit:
                    if i >= 200:
                        weapon = cur.execute(f"SELECT giran FROM players WHERE id = {user_id}").fetchone()
                        for i in weapon:
                            if i == "Blue Wolf Armor(B)":
                                crystal = cur.execute(f"SELECT dion FROM players WHERE id = {user_id}").fetchone()
                                for i in crystal:
                                    if i >= 200:
                                        varnish = cur.execute(f"SELECT Varnish FROM players WHERE id = {user_id}").fetchone()
                                        for i in varnish:
                                            if i >= 100:
                                                cur.executescript(f"UPDATE players SET armor = 'Blue Wolf Armor(B) +' WHERE id = {user_id} ")
                                                cur.executescript(f"UPDATE players SET zat2 = 1,def = 3 WHERE id = {user_id} ")
                                                cur.executescript(f"UPDATE players SET dion = dion -200, minirb = minirb - 200, Varnish = Varnish - 100, giran = 0 WHERE id = {user_id} ")
                                                await message.answer("Поздравляем вы скрафтили Blue Wolf Armor(B)!!")
                                            else:
                                                await message.answer("Недостаточно Varnish.Требуется 100")
                                    else:
                                        await message.answer("Недостаточно Blue Gemstone.Требуется 200")
                            else:
                                await message.answer("Требуется рецепт Blue Wolf Armor(B)!")
                    else:
                        await message.answer("Недостаточно Iron Ore.Требуется 200")

@dp.message_handler(Text(equals='\U0001F30CSword of Miracles(A)90%\U0001F30C'))
@dp.throttled(rate=1)
async def craftsom(message: types.Message):
    con = sq.connect("game.db")
    con.row_factory = sq.Row
    cur = con.cursor()
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        weapon = cur.execute(f"SELECT weapon FROM players WHERE id = {user_id}").fetchone()
        for i in weapon:
            if i == "Sword of Miracles(A) +":
                await message.answer("У тебя уже есть Sword of Miracles(A)")
            elif i != "Sword of Miracles(A) +":
                slit = cur.execute(f"SELECT minirb FROM players WHERE id = {user_id}").fetchone()
                for i in slit:
                    if i >= 200:
                        weapon = cur.execute(f"SELECT aden FROM players WHERE id = {user_id}").fetchone()
                        for i in weapon:
                            if i == "Sword of Miracles(A)90%":
                                crystal = cur.execute(f"SELECT dion FROM players WHERE id = {user_id}").fetchone()
                                for i in crystal:
                                    if i >= 200:
                                        varnish = cur.execute(f"SELECT Varnish FROM players WHERE id = {user_id}").fetchone()
                                        for i in varnish:
                                            if i >= 100:
                                                c = int(random.randrange(100))
                                                if c < 90:
                                                    cur.executescript(f"UPDATE players SET weapon = 'Sword of Miracles(A) +' WHERE id = {user_id} ")
                                                    cur.executescript(f"UPDATE players SET krit = krit - zat WHERE id = {user_id} ")
                                                    cur.executescript(f"UPDATE players SET zat = 1,atk = 30 WHERE id = {user_id} ")
                                                    cur.executescript(f"UPDATE players SET dion = dion -100, minirb = minirb - 200, Varnish = Varnish - 100, aden = 0 WHERE id = {user_id} ")
                                                    await message.answer("Поздравляем вы скрафтили Sword of Miracles(A)!!")
                                                elif c > 90:
                                                    cur.executescript(f"UPDATE players SET dion = dion -100, minirb = minirb - 200, Varnish = Varnish - 100, aden = 0 WHERE id = {user_id} ")
                                                    await message.answer("Неудача \U0001F92F")
                                            else:
                                                await message.answer("Недостаточно Varnish.Требуется 300")
                                    else:
                                        await message.answer("Недостаточно Blue Gemstone.Требуется 300")
                            else:
                                await message.answer("Требуется рецепт Sword of Miracles(A)90%!")
                    else:
                        await message.answer("Недостаточно Iron Ore.Требуется 300")

@dp.message_handler(Text(equals='\U0001F52EDark Crystal Armor(A)90%\U0001F52E'))
@dp.throttled(rate=1)
async def craftDK(message: types.Message):
    con = sq.connect("game.db")
    con.row_factory = sq.Row
    cur = con.cursor()
    user_id = message.from_user.id
    cur.execute(f"SELECT id FROM players WHERE id = {user_id} ")
    data = cur.fetchone()
    if data is not None:
        weapon = cur.execute(f"SELECT armor FROM players WHERE id = {user_id}").fetchone()
        for i in weapon:
            if i == "Dark Crystal Armor(A) +":
                await message.answer("У тебя уже есть Dark Crystal Armor(A)")
            elif i != "Dark Crystal Armor(A) +":
                slit = cur.execute(f"SELECT minirb FROM players WHERE id = {user_id}").fetchone()
                for i in slit:
                    if i >= 300:
                        weapon = cur.execute(f"SELECT aden FROM players WHERE id = {user_id}").fetchone()
                        for i in weapon:
                            if i == "Dark Crystal Armor(A)(90%)":
                                crystal = cur.execute(f"SELECT dion FROM players WHERE id = {user_id}").fetchone()
                                for i in crystal:
                                    if i >= 300:
                                        varnish = cur.execute(f"SELECT Varnish FROM players WHERE id = {user_id}").fetchone()
                                        for i in varnish:
                                            if i >= 200:
                                                c = int(random.randrange(100))
                                                if c < 90:
                                                    cur.executescript(f"UPDATE players SET armor = 'Dark Crystal Armor(A) +' WHERE id = {user_id} ")
                                                    cur.executescript(f"UPDATE players SET zat2 = 1,def = 4 WHERE id = {user_id} ")
                                                    cur.executescript(f"UPDATE players SET dion = dion -300, minirb = minirb - 300, Varnish = Varnish - 200, aden = 0 WHERE id = {user_id} ")
                                                    await message.answer("Поздравляем вы скрафтили Dark Crystal Armor(A)!!")
                                                elif c > 90:
                                                    cur.executescript(f"UPDATE players SET dion = dion -300, minirb = minirb - 300, Varnish = Varnish - 200, aden = 0 WHERE id = {user_id} ")
                                                    await message.answer("Неудача \U0001F92F")
                                            else:
                                                await message.answer("Недостаточно Varnish.Требуется 200")
                                    else:
                                        await message.answer("Недостаточно Blue Gemstone.Требуется 300")
                            else:
                                await message.answer("Требуется рецепт Dark Crystal Armor(A)(90%)!")
                    else:
                        await message.answer("Недостаточно Iron Ore.Требуется 300")

def register_craft(dp:Dispatcher):
  dp.register_message_handler(craftb12, commands=['craftb'])
  dp.register_message_handler(craftBO, Text(equals='\U0001F4FFEaring of Black Ore(B)(+1000 ХП, +40 Крит)\U0001F4FF'))