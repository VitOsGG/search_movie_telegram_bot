import sqlite3 as sq
from create_bot import bot


def sql_start_int_bd():
    global base, cur
    base = sq.connect('inter_movie_fact.db')
    cur = base.cursor()
    if base:
        print('Data base_2 connected OK!')


async def sql_start_int_fact_bd(message):
    for fct in cur.execute('SELECT fact FROM inter_movie_fact_2 WHERE rowid > (ABS(RANDOM()) % (SELECT max(rowid)\
                        FROM movie_db_on_mood_tab)) \
                        LIMIT 1').fetchall():
        await bot.send_message(message.from_user.id, fct[0])
