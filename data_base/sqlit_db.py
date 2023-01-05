import sqlite3 as sq
from create_bot import bot


def sql_start():
    global base, cur
    base = sq.connect('movie_db_on_mood.db')
    cur = base.cursor()
    if base:
        print('Data base connected OK!')


"""БЛОК ЗАПРОСОВ ПОДБОРА ФИЛЬМА ПО КРИТЕРИЮ - ЭМОЦИЙ"""


async def sql_read_movie_hpp(message):
    for ret in cur.execute('SELECT img, name, rating, country, genre, description FROM movie_db_on_mood_tab \
                           WHERE mood == "Радость" ORDER BY RANDOM() LIMIT 1 ').fetchall():
        await bot.send_photo(message.from_user.id, ret[0],
                             f'{ret[1]}\n {ret[2]}\n {ret[3]}\n {ret[4]}\n {ret[-1]}')


async def sql_read_movie_ang(message):
    for ret in cur.execute('SELECT img, name, rating, country, genre, description FROM movie_db_on_mood_tab \
                           WHERE mood == "Гнев" ORDER BY RANDOM() LIMIT 1 ').fetchall():
        await bot.send_photo(message.from_user.id, ret[0],
                             f'{ret[1]}\n {ret[2]}\n {ret[3]}\n {ret[4]}\n {ret[-1]}')


async def sql_read_movie_del(message):
    for ret in cur.execute('SELECT img, name, rating, country, genre, description FROM movie_db_on_mood_tab \
                           WHERE mood == "Восторг" ORDER BY RANDOM() LIMIT 1 ').fetchall():
        await bot.send_photo(message.from_user.id, ret[0],
                             f'{ret[1]}\n {ret[2]}\n {ret[3]}\n {ret[4]}\n {ret[-1]}')


async def sql_read(message):
    for ret in cur.execute('SELECT img, name, rating, country, genre, description FROM movie_db_on_mood_tab \
                           WHERE mood == "Гнев" ORDER BY RANDOM() LIMIT 1 ').fetchall():
        await bot.send_photo(message.from_user.id, ret[0],
                             f'{ret[1]}\n {ret[2]}\n {ret[3]}\n {ret[4]}\n {ret[-1]}')


async def sql_read_movie_cur(message):
    for ret in cur.execute('SELECT img, name, rating, country, genre, description FROM movie_db_on_mood_tab \
                           WHERE mood == "Любопытство" ORDER BY RANDOM() LIMIT 1 ').fetchall():
        await bot.send_photo(message.from_user.id, ret[0],
                             f'{ret[1]}\n {ret[2]}\n {ret[3]}\n {ret[4]}\n {ret[-1]}')


async def sql_read_movie_fea(message):
    for ret in cur.execute('SELECT img, name, rating, country, genre, description FROM movie_db_on_mood_tab \
                           WHERE mood == "Страх" ORDER BY RANDOM() LIMIT 1 ').fetchall():
        await bot.send_photo(message.from_user.id, ret[0],
                             f'{ret[1]}\n {ret[2]}\n {ret[3]}\n {ret[4]}\n {ret[-1]}')


async def sql_read_movie_sad(message):
    for ret in cur.execute('SELECT img, name, rating, country, genre, description FROM movie_db_on_mood_tab \
                           WHERE mood == "Грусть" ORDER BY RANDOM() LIMIT 1 ').fetchall():
        await bot.send_photo(message.from_user.id, ret[0],
                             f'{ret[1]}\n {ret[2]}\n {ret[3]}\n {ret[4]}\n {ret[-1]}')


"""БЛОК ЗАПРОСОВ ПОДБОРА ФИЛЬМА ПО КРИТЕРИЮ ЖАНР"""


async def sql_read_movie_ani(message):
    for ret in cur.execute('SELECT img, name, rating, country, genre, description FROM movie_db_on_mood_tab \
                           WHERE genre == "аниме " ORDER BY RANDOM() LIMIT 1 ').fetchall():
        await bot.send_photo(message.from_user.id, ret[0],
                             f'{ret[1]}\n {ret[2]}\n {ret[3]}\n {ret[4]}\n {ret[-1]}')


async def sql_read_movie_bio(message):
    for ret in cur.execute('SELECT img, name, rating, country, genre, description FROM movie_db_on_mood_tab \
                           WHERE genre == "биография" ORDER BY RANDOM() LIMIT 1 ').fetchall():
        await bot.send_photo(message.from_user.id, ret[0],
                             f'{ret[1]}\n {ret[2]}\n {ret[3]}\n {ret[4]}\n {ret[-1]}')


async def sql_read_movie_dra(message):
    for ret in cur.execute('SELECT img, name, rating, country, genre, description FROM movie_db_on_mood_tab \
                           WHERE genre == "драма" ORDER BY RANDOM() LIMIT 1 ').fetchall():
        await bot.send_photo(message.from_user.id, ret[0],
                             f'{ret[1]}\n {ret[2]}\n {ret[3]}\n {ret[4]}\n {ret[-1]}')


async def sql_read_movie_act(message):
    for ret in cur.execute('SELECT img, name, rating, country, genre, description FROM movie_db_on_mood_tab \
                           WHERE genre == "боевик" ORDER BY RANDOM() LIMIT 1 ').fetchall():
        await bot.send_photo(message.from_user.id, ret[0],
                             f'{ret[1]}\n {ret[2]}\n {ret[3]}\n {ret[4]}\n {ret[-1]}')


async def sql_read_movie_com(message):
    for ret in cur.execute('SELECT img, name, rating, country, genre, description FROM movie_db_on_mood_tab \
                           WHERE genre == "комедия" ORDER BY RANDOM() LIMIT 1 ').fetchall():
        await bot.send_photo(message.from_user.id, ret[0],
                             f'{ret[1]}\n {ret[2]}\n {ret[3]}\n {ret[4]}\n {ret[-1]}')


async def sql_read_movie_thr(message):
    for ret in cur.execute('SELECT img, name, rating, country, genre, description FROM movie_db_on_mood_tab \
                           WHERE genre == "триллер" ORDER BY RANDOM() LIMIT 1 ').fetchall():
        await bot.send_photo(message.from_user.id, ret[0],
                             f'{ret[1]}\n {ret[2]}\n {ret[3]}\n {ret[4]}\n {ret[-1]}')


async def sql_read_movie_cri(message):
    for ret in cur.execute('SELECT img, name, rating, country, genre, description FROM movie_db_on_mood_tab \
                           WHERE genre == "криминал" ORDER BY RANDOM() LIMIT 1 ').fetchall():
        await bot.send_photo(message.from_user.id, ret[0],
                             f'{ret[1]}\n {ret[2]}\n {ret[3]}\n {ret[4]}\n {ret[-1]}')


async def sql_read_movie_fan(message):
    for ret in cur.execute('SELECT img, name, rating, country, genre, description FROM movie_db_on_mood_tab \
                           WHERE genre == "фэнтези" ORDER BY RANDOM() LIMIT 1 ').fetchall():
        await bot.send_photo(message.from_user.id, ret[0],
                             f'{ret[1]}\n {ret[2]}\n {ret[3]}\n {ret[4]}\n {ret[-1]}')


async def sql_read_movie_car(message):
    for ret in cur.execute('SELECT img, name, rating, country, genre, description FROM movie_db_on_mood_tab \
                           WHERE genre == "анимация" ORDER BY RANDOM() LIMIT 1 ').fetchall():
        await bot.send_photo(message.from_user.id, ret[0],
                             f'{ret[1]}\n {ret[2]}\n {ret[3]}\n {ret[4]}\n {ret[-1]}')


async def sql_read_movie_fic(message):
    for ret in cur.execute('SELECT img, name, rating, country, genre, description FROM movie_db_on_mood_tab \
                           WHERE genre == "фантастика" ORDER BY RANDOM() LIMIT 1 ').fetchall():
        await bot.send_photo(message.from_user.id, ret[0],
                             f'{ret[1]}\n {ret[2]}\n {ret[3]}\n {ret[4]}\n {ret[-1]}')


async def sql_read_movie_mel(message):
    for ret in cur.execute('SELECT img, name, rating, country, genre, description FROM movie_db_on_mood_tab \
                           WHERE genre == "мелодрама" ORDER BY RANDOM() LIMIT 1 ').fetchall():
        await bot.send_photo(message.from_user.id, ret[0],
                             f'{ret[1]}\n {ret[2]}\n {ret[3]}\n {ret[4]}\n {ret[-1]}')


async def sql_read_movie_oth(message):
    for ret in cur.execute('SELECT img, name, rating, country, genre, description FROM movie_db_on_mood_tab  WHERE '
                           'genre <> '
                           '"аниме " AND genre <> "биография" AND genre <> "драма" AND genre <> '
                           '"боевик" AND genre <> "комедия" AND genre <> "триллер" AND genre <> "криминал" AND genre '
                           '<> "фэнтези" AND genre <> "анимация" AND genre <> "фантастика" AND genre <> "мелодрама" '
                           'ORDER BY RANDOM() LIMIT 1 ').fetchall():
        await bot.send_photo(message.from_user.id, ret[0],
                             f'{ret[1]}\n {ret[2]}\n {ret[3]}\n {ret[4]}\n {ret[-1]}')


"""БЛОК ЗАПРОСОВ ПОДБОРА ФИЛЬМА ПО КРИТЕРИЮ - СТРАНА"""

sql_coun = "SELECT img, name, rating, country, genre, description FROM movie_db_on_mood_tab WHERE country " \
           "LIKE ? ORDER BY RANDOM() LIMIT 1 "


async def sql_read_movie_rus(message):
    for ret in cur.execute(sql_coun, ("%" + 'Россия' + "%",)).fetchall():
        await bot.send_photo(message.from_user.id, ret[0],
                             f'{ret[1]}\n {ret[2]}\n {ret[3]}\n {ret[4]}\n {ret[-1]}')


async def sql_read_movie_usa(message):
    for ret in cur.execute(sql_coun, ("%" + 'США' + "%",)).fetchall():
        await bot.send_photo(message.from_user.id, ret[0],
                             f'{ret[1]}\n {ret[2]}\n {ret[3]}\n {ret[4]}\n {ret[-1]}')


async def sql_read_movie_eng(message):
    for ret in cur.execute(sql_coun, ("%" + 'Великобритания' + "%",)).fetchall():
        await bot.send_photo(message.from_user.id, ret[0],
                             f'{ret[1]}\n {ret[2]}\n {ret[3]}\n {ret[4]}\n {ret[-1]}')


async def sql_read_movie_fre(message):
    for ret in cur.execute(sql_coun, ("%" + 'Франция' + "%",)).fetchall():
        await bot.send_photo(message.from_user.id, ret[0],
                             f'{ret[1]}\n {ret[2]}\n {ret[3]}\n {ret[4]}\n {ret[-1]}')


async def sql_read_movie_ger(message):
    for ret in cur.execute(sql_coun, ("%" + 'Германия' + "%",)).fetchall():
        await bot.send_photo(message.from_user.id, ret[0],
                             f'{ret[1]}\n {ret[2]}\n {ret[3]}\n {ret[4]}\n {ret[-1]}')


async def sql_read_movie_jap(message):
    for ret in cur.execute(sql_coun, ("%" + 'Япония' + "%",)).fetchall():
        await bot.send_photo(message.from_user.id, ret[0],
                             f'{ret[1]}\n {ret[2]}\n {ret[3]}\n {ret[4]}\n {ret[-1]}')


async def sql_read_movie_uss(message):
    for ret in cur.execute(sql_coun, ("%" + 'СССР' + "%",)).fetchall():
        await bot.send_photo(message.from_user.id, ret[0],
                             f'{ret[1]}\n {ret[2]}\n {ret[3]}\n {ret[4]}\n {ret[-1]}')



async def sql_read_movie_oth_cnt(message):
    for ret in cur.execute('SELECT img, name, rating, country, genre, description FROM movie_db_on_mood_tab  WHERE '
                           'country <> '
                           '"Россия" AND country <> "США" AND country <> "Великобритания" AND '
                           'country <> '
                           '"Франция" AND country <> "Германия"  AND country <> "Япония" AND country <> "СССР" '
                           'ORDER BY RANDOM() LIMIT 1 ').fetchall():
        await bot.send_photo(message.from_user.id, ret[0],
                             f'{ret[1]}\n {ret[2]}\n {ret[3]}\n {ret[4]}\n {ret[-1]}')


"""БЛОК ЗАПРОСОВ ПОДБОРА ФИЛЬМА ПО СОВЕТУ"""


async def sql_read_movie_rec(message):
    for ret in cur.execute('SELECT img, name, rating, country, genre, description FROM movie_db_on_mood_tab \
                           WHERE rating >= 8 ORDER BY RANDOM() LIMIT 1 ').fetchall():
        await bot.send_photo(message.from_user.id, ret[0],
                             f'{ret[1]}\n {ret[2]}\n {ret[3]}\n {ret[4]}\n {ret[-1]}')
