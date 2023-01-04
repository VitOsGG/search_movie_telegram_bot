from aiogram import types, Dispatcher
from create_bot import bot, dp
from keyboards import kb_user
from aiogram.types import ReplyKeyboardRemove
from data_base import sqlit_db, sqlit_db_fct
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from aiogram.dispatcher.filters import Text





""""НАЧАЛО РАБОТЫ БОТА ПОСЕ ОТПРАВКИ СТАРТОВОЙ КОМАНДЫ ОТ ПОЛЬЗОВАТЕЛЯ"""

async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, "Привет!\nНаконец-то у тебя появилось время для фильма))\n"
                                                     "Как будем выбирать?", reply_markup=kb_user)
        await message.delete()
    except:
        await message.reply('Могу подобрать фильм на вечер! Напиши боту в ЛС: \nhttps://t.me/Movie_for_Mommy_bot')


""""БЛОК ПОДБОРА ФИЛЬМА ПО КРИТЕРИЮ ЭМОЦИЙ"""

emotion = InlineKeyboardMarkup(row_width=3).add(InlineKeyboardButton(text='😊 Радость', callback_data='movie_hpp'),\
                                                InlineKeyboardButton(text='🤬 Гнев', callback_data='movie_ang'), \
                                                InlineKeyboardButton(text='🤩 Восторг', callback_data='movie_del'), \
                                                InlineKeyboardButton(text='😲 Любопытство', callback_data='movie_cur'), \
                                                InlineKeyboardButton(text='😱 Страх', callback_data='movie_fea'), \
                                                InlineKeyboardButton(text='🙁 Грусть', callback_data='movie_sad'))

@dp.message_handler(Text(equals="🌝 Эмоция"))
async def movie_choice_by_mood(message: types.Message):
    await bot.send_message(message.from_user.id, 'Итак, подберем фильм по эмоциям!')
    await message.answer('Выбирай:', reply_markup=emotion)

@dp.callback_query_handler(Text(startswith='movie_hpp'))
async def movie_choice_by_mood_hpp(callback: types.CallbackQuery):
    await sqlit_db.sql_read_movie_hpp(callback)
    await callback.answer()

@dp.callback_query_handler(Text(startswith='movie_ang'))
async def movie_choice_by_mood_ang(callback: types.CallbackQuery):
    await sqlit_db.sql_read_movie_ang(callback)
    await callback.answer()

@dp.callback_query_handler(Text(startswith='movie_del'))
async def movie_choice_by_mood_del(callback: types.CallbackQuery):
    await sqlit_db.sql_read_movie_del(callback)
    await callback.answer()

@dp.callback_query_handler(Text(startswith='movie_cur'))
async def movie_choice_by_mood_cur(callback: types.CallbackQuery):
    await sqlit_db.sql_read_movie_cur(callback)
    await callback.answer()

@dp.callback_query_handler(Text(startswith='movie_fea'))
async def movie_choice_by_mood_fea(callback: types.CallbackQuery):
    await sqlit_db.sql_read_movie_fea(callback)
    await callback.answer()

@dp.callback_query_handler(Text(startswith='movie_sad'))
async def movie_choice_by_mood_sad(callback: types.CallbackQuery):
    await sqlit_db.sql_read_movie_sad(callback)
    await callback.answer()





""""БЛОК ПОДБОРА ФИЛЬМОВ ПО КРИТЕРИЮ ЖАНРА"""

genre = InlineKeyboardMarkup(row_width=3).add(InlineKeyboardButton(text='Аниме', callback_data='movie_ani'), \
                                                InlineKeyboardButton(text='Биография', callback_data='movie_bio'), \
                                                InlineKeyboardButton(text='Драма', callback_data='movie_dra'), \
                                                InlineKeyboardButton(text='Боевик', callback_data='movie_act'), \
                                                InlineKeyboardButton(text='Комедия', callback_data='movie_com'), \
                                                InlineKeyboardButton(text='Триллер', callback_data='movie_thr'), \
                                                InlineKeyboardButton(text='Криминал', callback_data='movie_cri'), \
                                                InlineKeyboardButton(text='Фэнтези', callback_data='movie_fan'), \
                                                InlineKeyboardButton(text='Анимация', callback_data='movie_car'), \
                                                InlineKeyboardButton(text='Фантастика', callback_data='movie_fic'), \
                                                InlineKeyboardButton(text='Мелодрама', callback_data='movie_mel'), \
                                                InlineKeyboardButton(text='Остальные', callback_data='movie_oth_gen'))

@dp.message_handler(Text(equals="🎬 Жанр"))
async def movie_choice_by_genre(message: types.Message):
    await bot.send_message(message.from_user.id,
                           'Комедия, триллер или поплачем над мелодрамой?')
    await message.answer('Выбирай:', reply_markup=genre)
@dp.callback_query_handler(Text(startswith='movie_ani'))
async def movie_choice_by_genre_ani(callback: types.CallbackQuery):
    await sqlit_db.sql_read_movie_ani(callback)
    await callback.answer()

@dp.callback_query_handler(Text(startswith='movie_bio'))
async def movie_choice_by_genre_bio(callback: types.CallbackQuery):
    await sqlit_db.sql_read_movie_bio(callback)
    await callback.answer()

@dp.callback_query_handler(Text(startswith='movie_dra'))
async def movie_choice_by_genre_dra(callback: types.CallbackQuery):
    await sqlit_db.sql_read_movie_dra(callback)
    await callback.answer()

@dp.callback_query_handler(Text(startswith='movie_act'))
async def movie_choice_by_genre_act(callback: types.CallbackQuery):
    await sqlit_db.sql_read_movie_act(callback)
    await callback.answer()

@dp.callback_query_handler(Text(startswith='movie_com'))
async def movie_choice_by_genre_com(callback: types.CallbackQuery):
    await sqlit_db.sql_read_movie_com(callback)
    await callback.answer()

@dp.callback_query_handler(Text(startswith='movie_thr'))
async def movie_choice_by_genre_thr(callback: types.CallbackQuery):
    await sqlit_db.sql_read_movie_thr(callback)
    await callback.answer()

@dp.callback_query_handler(Text(startswith='movie_cri'))
async def movie_choice_by_genre_cri(callback: types.CallbackQuery):
    await sqlit_db.sql_read_movie_cri(callback)
    await callback.answer()

@dp.callback_query_handler(Text(startswith='movie_fan'))
async def movie_choice_by_genre_fan(callback: types.CallbackQuery):
    await sqlit_db.sql_read_movie_fan(callback)
    await callback.answer()

@dp.callback_query_handler(Text(startswith='movie_car'))
async def movie_choice_by_genre_car(callback: types.CallbackQuery):
    await sqlit_db.sql_read_movie_car(callback)
    await callback.answer()

@dp.callback_query_handler(Text(startswith='movie_fic'))
async def movie_choice_by_genre_fic(callback: types.CallbackQuery):
    await sqlit_db.sql_read_movie_fic(callback)
    await callback.answer()

@dp.callback_query_handler(Text(startswith='movie_mel'))
async def movie_choice_by_genre_mel(callback: types.CallbackQuery):
    await sqlit_db.sql_read_movie_mel(callback)
    await callback.answer()

@dp.callback_query_handler(Text(startswith='movie_oth_gen'))
async def movie_choice_by_genre_oth_gen(callback: types.CallbackQuery):
    await sqlit_db.sql_read_movie_oth(callback)
    await callback.answer()


"""БЛОК ПОДБОРА ФИЛЬМОВ ПО КРИТЕРИЮ СТРАНЫ"""


country = InlineKeyboardMarkup(row_width=3).add(InlineKeyboardButton(text='🇷🇺 Россия', callback_data='movie_rus'), \
                                                InlineKeyboardButton(text='🇺🇸 США', callback_data='movie_usa'), \
                                                InlineKeyboardButton(text='🇰🇷 Корея', callback_data='movie_kor'), \
                                                InlineKeyboardButton(text='🇬🇧 Великобритания', callback_data='movie_eng'), \
                                                InlineKeyboardButton(text='🇫🇷 Франция', callback_data='movie_fre'), \
                                                InlineKeyboardButton(text='🇩🇪 Германия', callback_data='movie_ger'), \
                                                InlineKeyboardButton(text='🇯🇵 Япония', callback_data='movie_jap'), \
                                                InlineKeyboardButton(text='СССР', callback_data='movie_uss'), \
                                                InlineKeyboardButton(text='🇮🇹 Италия', callback_data='movie_itl'), \
                                                InlineKeyboardButton(text='🇦🇶 Остальные', callback_data='movie_oth_cnt'))


@dp.message_handler(Text(equals="🌎 Страна"))
async def movie_choice_by_country(message: types.Message):
    await bot.send_message(message.from_user.id,
                           'Старое доброе русское, шикарное американское или модное корейское кино?')
    await message.answer('Выбирай:', reply_markup=country)

@dp.callback_query_handler(Text(startswith='movie_rus'))
async def movie_choice_by_country_rus(callback: types.CallbackQuery):
    await sqlit_db.sql_read_movie_rus(callback)
    await callback.answer()

@dp.callback_query_handler(Text(startswith='movie_usa'))
async def movie_choice_by_country_usa(callback: types.CallbackQuery):
    await sqlit_db.sql_read_movie_usa(callback)
    await callback.answer()

@dp.callback_query_handler(Text(startswith='movie_kor'))
async def movie_choice_by_country_kor(callback: types.CallbackQuery):
    await sqlit_db.sql_read_movie_kor(callback)
    await callback.answer()

@dp.callback_query_handler(Text(startswith='movie_eng'))
async def movie_choice_by_country_eng(callback: types.CallbackQuery):
    await sqlit_db.sql_read_movie_eng(callback)
    await callback.answer()

@dp.callback_query_handler(Text(startswith='movie_fre'))
async def movie_choice_by_country_fre(callback: types.CallbackQuery):
    await sqlit_db.sql_read_movie_fre(callback)
    await callback.answer()

@dp.callback_query_handler(Text(startswith='movie_ger'))
async def movie_choice_by_country_ger(callback: types.CallbackQuery):
    await sqlit_db.sql_read_movie_ger(callback)
    await callback.answer()

@dp.callback_query_handler(Text(startswith='movie_jap'))
async def movie_choice_by_country_jap(callback: types.CallbackQuery):
    await sqlit_db.sql_read_movie_jap(callback)
    await callback.answer()

@dp.callback_query_handler(Text(startswith='movie_uss'))
async def movie_choice_by_country_uss(callback: types.CallbackQuery):
    await sqlit_db.sql_read_movie_uss(callback)
    await callback.answer()

@dp.callback_query_handler(Text(startswith='movie_itl'))
async def movie_choice_by_country_itl(callback: types.CallbackQuery):
    await sqlit_db.sql_read_movie_itl(callback)
    await callback.answer()

@dp.callback_query_handler(Text(startswith='movie_oth_cnt'))
async def movie_choice_by_country_oth_cnt(callback: types.CallbackQuery):
    await sqlit_db.sql_read_movie_oth_cnt(callback)
    await callback.answer()


@dp.message_handler(Text(equals="🎞 Хочу совет!"))
async def movie_choice_by_rec(message: types.Message):
    await sqlit_db.sql_read_movie_rec(message)

@dp.message_handler(Text(equals="🗿 Интересный факт^^"))
async def interesting_fact(message: types.Message):
    await sqlit_db_fct.sql_start_int_fact_bd(message)


def register_handlers_user(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help', 'Start', 'Help'])

    # dp.register_message_handler(movie_choice_by_mood, commands=['По_эмоциям'])
    # dp.register_message_handler(movie_choice_by_mood_hpp, commands=['Радость'])
    # dp.register_message_handler(movie_choice_by_mood_ang, commands=['Гнев'])
    # dp.register_message_handler(movie_choice_by_mood_del, commands=['Восторг'])
    # dp.register_message_handler(movie_choice_by_mood_cur, commands=['Любопытство'])
    # dp.register_message_handler(movie_choice_by_mood_fea, commands=['Страх'])
    # dp.register_message_handler(movie_choice_by_mood_sad, commands=['Грусть'])

    # dp.register_message_handler(movie_choice_by_genre, commands=['По_жанру'])
    # dp.register_message_handler(movie_choice_by_genre_ani, commands=['Аниме'])
    # dp.register_message_handler(movie_choice_by_genre_bio, commands=['Биография'])
    # dp.register_message_handler(movie_choice_by_genre_dra, commands=['Драма'])
    # dp.register_message_handler(movie_choice_by_genre_act, commands=['Боевик'])
    # dp.register_message_handler(movie_choice_by_genre_com, commands=['Комедия'])
    # dp.register_message_handler(movie_choice_by_genre_thr, commands=['Триллер'])
    # dp.register_message_handler(movie_choice_by_genre_cri, commands=['Криминал'])
    # dp.register_message_handler(movie_choice_by_genre_fan, commands=['Фэнтези'])
    # dp.register_message_handler(movie_choice_by_genre_car, commands=['Анимация'])
    # dp.register_message_handler(movie_choice_by_genre_fic, commands=['Фантастика'])
    # dp.register_message_handler(movie_choice_by_genre_mel, commands=['Мелодрама'])
    # dp.register_message_handler(movie_choice_by_genre_oth_gen, commands=['Остальные'])

    # dp.register_message_handler(movie_choice_by_country, commands=['По_странам'])
    # dp.register_message_handler(movie_choice_by_country_rus, commands=['Россия'])
    # dp.register_message_handler(movie_choice_by_country_usa, commands=['США'])
    # dp.register_message_handler(movie_choice_by_country_kor, commands=['Корея'])
    # dp.register_message_handler(movie_choice_by_country_eng, commands=['Великобритания'])
    # dp.register_message_handler(movie_choice_by_country_fre, commands=['Франция'])
    # dp.register_message_handler(movie_choice_by_country_ger, commands=['Германия'])
    # dp.register_message_handler(movie_choice_by_country_jap, commands=['Япония'])
    # dp.register_message_handler(movie_choice_by_country_uss, commands=['СССР'])
    # dp.register_message_handler(movie_choice_by_country_oth_cnt, commands=['Остальные'])

    # dp.register_message_handler(movie_choice_by_rec, commands=['Хочу_совет!'])

    # dp.register_message_handler(interesting_fact, commands=['Интересный_факт^^'])