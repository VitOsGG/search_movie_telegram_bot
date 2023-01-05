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
                        WHERE mood == "Радость" AND rowid > (ABS(RANDOM()) % (SELECT max(rowid)\
                        FROM movie_db_on_mood_tab)) \
                        LIMIT 1').fetchall():
        await bot.send_photo(message.from_user.id, ret[0],
                             f'{ret[1]}\n {ret[2]}\n {ret[3]}\n {ret[4]}\n {ret[-1]}')


"""SELECT max(rowid) FROM table - возвращает наибольший допустимый идентификатор строки для таблицы. 
SQLite может использовать индекс на rowid для эффективной работы.
ABS(RANDOM()) % ... - возвращает случайное число от 0 до max(rowid) - 1). 
Функция random SQLite генерирует число от -9223372036854775808 до +9223372036854775807. ABS гарантирует его 
положительное значение, а оператор модуля ставит его между max(rowid) - 1.
rowid > ... - вместо использования = используйте > в случае, если сгенерированное случайное число соответствует
 удаленной строке. Использование строго больше, чем гарантирует, что мы вернем строку с идентификатором от 1 (больше 0)
до max(rowid) (больше, чем max(rowid) - 1). 
SQLite также использует индекс первичного ключа для эффективного возврата этого результата.
Это также работает для запросов с предложениями WHERE. Примените предложение WHERE как к выходным данным, так и к подзапросу SELECT max(rowid)"""


async def sql_read_movie_ang(message):
    for ret in cur.execute('SELECT img, name, rating, country, genre, description FROM movie_db_on_mood_tab \
                        WHERE mood == "Гнев" AND rowid > (ABS(RANDOM()) % (SELECT max(rowid)\
                        FROM movie_db_on_mood_tab)) \
                        LIMIT 1').fetchall():
        await bot.send_photo(message.from_user.id, ret[0],
                             f'{ret[1]}\n {ret[2]}\n {ret[3]}\n {ret[4]}\n {ret[-1]}')


async def sql_read_movie_del(message):
    for ret in cur.execute('SELECT img, name, rating, country, genre, description FROM movie_db_on_mood_tab \
                        WHERE mood == "Восторг" AND rowid > (ABS(RANDOM()) % (SELECT max(rowid)\
                        FROM movie_db_on_mood_tab)) \
                        LIMIT 1').fetchall():
        await bot.send_photo(message.from_user.id, ret[0],
                             f'{ret[1]}\n {ret[2]}\n {ret[3]}\n {ret[4]}\n {ret[-1]}')


async def sql_read_movie_cur(message):
    for ret in cur.execute('SELECT img, name, rating, country, genre, description FROM movie_db_on_mood_tab \
                        WHERE mood == "Любопытство" AND rowid > (ABS(RANDOM()) % (SELECT max(rowid)\
                        FROM movie_db_on_mood_tab)) \
                        LIMIT 1').fetchall():
        await bot.send_photo(message.from_user.id, ret[0],
                             f'{ret[1]}\n {ret[2]}\n {ret[3]}\n {ret[4]}\n {ret[-1]}')


async def sql_read_movie_fea(message):
    for ret in cur.execute('SELECT img, name, rating, country, genre, description FROM movie_db_on_mood_tab \
                        WHERE mood == "Страх" AND rowid > (ABS(RANDOM()) % (SELECT max(rowid)\
                        FROM movie_db_on_mood_tab)) \
                        LIMIT 1').fetchall():
        await bot.send_photo(message.from_user.id, ret[0],
                             f'{ret[1]}\n {ret[2]}\n {ret[3]}\n {ret[4]}\n {ret[-1]}')


async def sql_read_movie_sad(message):
    for ret in cur.execute('SELECT img, name, rating, country, genre, description FROM movie_db_on_mood_tab \
                        WHERE mood == "Грусть" AND rowid > (ABS(RANDOM()) % (SELECT max(rowid)\
                        FROM movie_db_on_mood_tab)) \
                        LIMIT 1').fetchall():
        await bot.send_photo(message.from_user.id, ret[0],
                             f'{ret[1]}\n {ret[2]}\n {ret[3]}\n {ret[4]}\n {ret[-1]}')


"""БЛОК ЗАПРОСОВ ПОДБОРА ФИЛЬМА ПО КРИТЕРИЮ ЖАНР"""


async def sql_read_movie_ani(message):
    for ret in cur.execute('SELECT img, name, rating, country, genre, description FROM movie_db_on_mood_tab \
                        WHERE genre == "аниме " AND rowid > (ABS(RANDOM()) % (SELECT max(rowid)\
                        FROM movie_db_on_mood_tab)) \
                        LIMIT 1').fetchall():
        await bot.send_photo(message.from_user.id, ret[0],
                             f'{ret[1]}\n {ret[2]}\n {ret[3]}\n {ret[4]}\n {ret[-1]}')


async def sql_read_movie_bio(message):
    for ret in cur.execute('SELECT img, name, rating, country, genre, description FROM movie_db_on_mood_tab \
                        WHERE genre == "биография" AND rowid > (ABS(RANDOM()) % (SELECT max(rowid)\
                        FROM movie_db_on_mood_tab)) \
                        LIMIT 1').fetchall():
        await bot.send_photo(message.from_user.id, ret[0],
                             f'{ret[1]}\n {ret[2]}\n {ret[3]}\n {ret[4]}\n {ret[-1]}')


async def sql_read_movie_dra(message):
    for ret in cur.execute('SELECT img, name, rating, country, genre, description FROM movie_db_on_mood_tab \
                        WHERE genre == "драма" AND rowid > (ABS(RANDOM()) % (SELECT max(rowid)\
                        FROM movie_db_on_mood_tab)) \
                        LIMIT 1').fetchall():
        await bot.send_photo(message.from_user.id, ret[0],
                             f'{ret[1]}\n {ret[2]}\n {ret[3]}\n {ret[4]}\n {ret[-1]}')


async def sql_read_movie_act(message):
    for ret in cur.execute('SELECT img, name, rating, country, genre, description FROM movie_db_on_mood_tab \
                        WHERE genre == "боевик" AND rowid > (ABS(RANDOM()) % (SELECT max(rowid)\
                        FROM movie_db_on_mood_tab)) \
                        LIMIT 1').fetchall():
        await bot.send_photo(message.from_user.id, ret[0],
                             f'{ret[1]}\n {ret[2]}\n {ret[3]}\n {ret[4]}\n {ret[-1]}')


async def sql_read_movie_com(message):
    for ret in cur.execute('SELECT img, name, rating, country, genre, description FROM movie_db_on_mood_tab \
                        WHERE genre == "комедия" AND rowid > (ABS(RANDOM()) % (SELECT max(rowid)\
                        FROM movie_db_on_mood_tab)) \
                        LIMIT 1').fetchall():
        await bot.send_photo(message.from_user.id, ret[0],
                             f'{ret[1]}\n {ret[2]}\n {ret[3]}\n {ret[4]}\n {ret[-1]}')


async def sql_read_movie_thr(message):
    for ret in cur.execute('SELECT img, name, rating, country, genre, description FROM movie_db_on_mood_tab \
                        WHERE genre == "триллер" AND rowid > (ABS(RANDOM()) % (SELECT max(rowid)\
                        FROM movie_db_on_mood_tab)) \
                        LIMIT 1').fetchall():
        await bot.send_photo(message.from_user.id, ret[0],
                             f'{ret[1]}\n {ret[2]}\n {ret[3]}\n {ret[4]}\n {ret[-1]}')


async def sql_read_movie_cri(message):
    for ret in cur.execute('SELECT img, name, rating, country, genre, description FROM movie_db_on_mood_tab \
                        WHERE genre == "криминал" AND rowid > (ABS(RANDOM()) % (SELECT max(rowid)\
                        FROM movie_db_on_mood_tab)) \
                        LIMIT 1').fetchall():
        await bot.send_photo(message.from_user.id, ret[0],
                             f'{ret[1]}\n {ret[2]}\n {ret[3]}\n {ret[4]}\n {ret[-1]}')


async def sql_read_movie_fan(message):
    for ret in cur.execute('SELECT img, name, rating, country, genre, description FROM movie_db_on_mood_tab \
                        WHERE genre == "фэнтези" AND rowid > (ABS(RANDOM()) % (SELECT max(rowid)\
                        FROM movie_db_on_mood_tab)) \
                        LIMIT 1').fetchall():
        await bot.send_photo(message.from_user.id, ret[0],
                             f'{ret[1]}\n {ret[2]}\n {ret[3]}\n {ret[4]}\n {ret[-1]}')


async def sql_read_movie_car(message):
    for ret in cur.execute('SELECT img, name, rating, country, genre, description FROM movie_db_on_mood_tab \
                        WHERE genre == "анимация" AND rowid > (ABS(RANDOM()) % (SELECT max(rowid)\
                        FROM movie_db_on_mood_tab)) \
                        LIMIT 1').fetchall():
        await bot.send_photo(message.from_user.id, ret[0],
                             f'{ret[1]}\n {ret[2]}\n {ret[3]}\n {ret[4]}\n {ret[-1]}')


async def sql_read_movie_fic(message):
    for ret in cur.execute('SELECT img, name, rating, country, genre, description FROM movie_db_on_mood_tab \
                        WHERE genre == "фантастика" AND rowid > (ABS(RANDOM()) % (SELECT max(rowid)\
                        FROM movie_db_on_mood_tab)) \
                        LIMIT 1').fetchall():
        await bot.send_photo(message.from_user.id, ret[0],
                             f'{ret[1]}\n {ret[2]}\n {ret[3]}\n {ret[4]}\n {ret[-1]}')


async def sql_read_movie_mel(message):
    for ret in cur.execute('SELECT img, name, rating, country, genre, description FROM movie_db_on_mood_tab \
                        WHERE genre == "мелодрама" AND rowid > (ABS(RANDOM()) % (SELECT max(rowid)\
                        FROM movie_db_on_mood_tab)) \
                        LIMIT 1').fetchall():
        await bot.send_photo(message.from_user.id, ret[0],
                             f'{ret[1]}\n {ret[2]}\n {ret[3]}\n {ret[4]}\n {ret[-1]}')


async def sql_read_movie_oth(message):
    for ret in cur.execute('SELECT img, name, rating, country, genre, description FROM movie_db_on_mood_tab  '
                           'WHERE '
                           'genre <> "аниме " AND genre <> "биография" AND genre <> "драма" AND '
                           'genre <> "боевик" AND genre <> "комедия" AND genre <> "триллер" AND '
                           'genre <> "криминал" AND genre <> "фэнтези" AND genre <> "анимация" AND '
                           'genre <> "фантастика" AND genre <> "мелодрама" AND '
                           'rowid > (ABS(RANDOM()) % (SELECT max(rowid) FROM movie_db_on_mood_tab)) LIMIT 1').fetchall():
        await bot.send_photo(message.from_user.id, ret[0],
                             f'{ret[1]}\n {ret[2]}\n {ret[3]}\n {ret[4]}\n {ret[-1]}')


"""БЛОК ЗАПРОСОВ ПОДБОРА ФИЛЬМА ПО КРИТЕРИЮ - СТРАНА"""

sql_coun = 'SELECT img, name, rating, country, genre, description FROM movie_db_on_mood_tab \
                        WHERE country LIKE ? AND rowid > (ABS(RANDOM()) % (SELECT max(rowid)\
                        FROM movie_db_on_mood_tab)) \
                        LIMIT 1'


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
    for ret in cur.execute('SELECT img, name, rating, country, genre, description FROM movie_db_on_mood_tab  '
                           'WHERE '
                           'country <> "Россия" AND country <> "США" AND country <> "Великобритания" AND '
                           'country <> "Франция" AND country <> "Германия"  AND country <> "Япония" AND '
                           'country <> "СССР" AND '
                           'rowid > (ABS(RANDOM()) % (SELECT max(rowid) FROM movie_db_on_mood_tab)) LIMIT 1').fetchall():
        await bot.send_photo(message.from_user.id, ret[0],
                             f'{ret[1]}\n {ret[2]}\n {ret[3]}\n {ret[4]}\n {ret[-1]}')


"""БЛОК ЗАПРОСОВ ПОДБОРА ФИЛЬМА ПО СОВЕТУ"""


async def sql_read_movie_rec(message):
    for ret in cur.execute('SELECT img, name, rating, country, genre, description FROM movie_db_on_mood_tab \
                        WHERE rating >= 7.5 AND rowid > (ABS(RANDOM()) % (SELECT max(rowid)\
                        FROM movie_db_on_mood_tab)) \
                        LIMIT 1').fetchall():
        await bot.send_photo(message.from_user.id, ret[0],
                             f'{ret[1]}\n {ret[2]}\n {ret[3]}\n {ret[4]}\n {ret[-1]}')
