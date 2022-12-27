# search_movie_telegram_bot
![Python](https://img.shields.io/badge/Python-3.11.0-yellow) ![aiogram](https://img.shields.io/badge/aiogram-blue) ![sqlite3](https://img.shields.io/badge/sqlite3-blue) 
___
Ссылки на вспомогательные проекты, которые были реализовы для создания данного проекта:
* [Парсер фильмов для базы данных](https://github.com/VitOsGG/parser_movie)
* [Создание базы данных (sqlite3)](https://github.com/VitOsGG/create_db_movie)

Данный проект - это **telegram-бот**, который является системой рекомендации фильмов по критериям запроса от пользователя.

Ссылка на бот: [Movie_for_Mommy](https://t.me/Movie_for_Mommy_bot)

Бот переодически улучшается и обновляется, поэтому может быть отключен в некоторый период времени. По всем вопросом обращаться в телеграмм или письмом на e-mail в описание профиля. 

![1](https://user-images.githubusercontent.com/114734775/209709643-f3eb16a8-8294-4eec-83cc-aa1bdf74c407.jpg) ![2](https://user-images.githubusercontent.com/114734775/209709699-1b102259-daa7-46cb-9831-125d47aa161e.jpg) ![3](https://user-images.githubusercontent.com/114734775/209714767-c8ef2a11-891f-43ed-ae82-958540478ce7.jpg)


___

**Структура проекта:**
* Папка venv

  Стандартная папка с виртуальный окружением для установки необходимых библиотек (список всех библиотек хранится в документе requirements.txt)
    
* Папка keyboards

  Пакет с кнопками для главного меню

* Папка handlers
  
  Пакет с командами на выполнения действий при нажатии на кнопки, а так же создание и подключение инлайн-кнопок
  
* Папка data_base

  Пакет с всеми запросами к базам данных

* Папка cenz
 
  Служебная папка для хранения файла с зацензурированными словами
  
* Файлы в корневой папке:

  * bot_movie.py - файл запуска бота
  
  * create_bot.py - файл инициализации бота
    
  * to_json.py - файл конвертирования файла из папки cenz в формат - .json
  
  * cenz.json - полученный файл для дальнейшего использования в функции цензурирования
   
  * movie_db_on_mood.db - база данных фильмов
  
  * inter_movie_fact.db - база данных интересных фактов
    
  * movie_db.db - база данных фильмов (тестовая) 

  * Heroku_Power - служебный файл для развертывания (deploy) бота с помощью сервиса Heroku
  
___

Ход разработки:
  * Идея
  
  За долго до того, как я начал погружаться в сферу IT моя мама часто задавала мне вопрос о том, что я могу ей посоветовать посмотреть из фильмов. Я очень люблю кино, как с точки зрения простого зретеля, так и люблю кино как искусство и смотрел много хороших и не хороших фильмов, но в нужный момент тяжело вспомнить, что хорошоего посоветовать, особенно когда человек уже многое видел и тогда я часто думал о том, что хорошо, если бы был бот, который мог бы посоветовать фильм. Я всречал подобные решения , но по том или иной причине они мне не нравились и вот когда я стал сам пистать код, я решил сделать этот проект. 
  
  * Планирование

  Перед началом проекта было принято решение о двух основные концепции бота:
    
  ** Бот будет простым. В нем не будет сложных комбинаций отбора фильмов с сочитанием, например, страны производства и жанра или других сочетний. По моему мнению это излишне, пользователь хочет быстро найти качественный фильм и приступить к просмотру получая от этого удовольствия, а не тратить время и терять настроение на долгий поиск.
    
  ** Каждая команда будет в виде кнопки. Это концепция является следствием первого пункта, потому что я хотел избавить пользователя от ввода информации с клавиатуры. Это позволяет экономить время на поиск фильма (ввод занимает больше времени и появляется возможность совершить опечатку).
  
  Так же была создана [схема](https://mm.tt/map/2524744615?t=VOBNX0T0pJ) разработки:
  
  ![План_разработки_проекта](https://user-images.githubusercontent.com/114734775/209698159-c42aecf2-67e8-4b6d-9b6e-75d81d27f86e.png)
  
  * Реализация
  
  Реализация является процессом написания различных блоков программы сильно взаимосязанных друг с другом. Вот некоторые типичные части кода:
  
  
  -Пакет handlers. Старт работы бота:
  
```python
 async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, "Привет!\nНаконец-то у тебя появилось время для фильма))\n
                                                     "Как будем выбирать?", reply_markup=kb_user)
        await message.delete()
    except:
        await message.reply('Могу подобрать фильм на вечер! Напиши боту в ЛС: \nhttps://t.me/Movie_for_Mommy_bot')
```

  -Пакет keyboards. Кнопки главного меню:
  
```python
b1 = KeyboardButton('/По_эмоциям')
b2 = KeyboardButton('/По_жанру')
b3 = KeyboardButton('/По_странам')
b4 = KeyboardButton('/Хочу_совет!')
b5 = KeyboardButton('/Интересный_факт^^')

kb_user = ReplyKeyboardMarkup(resize_keyboard=True)

kb_user.row(b1, b2).add(b3).add(b4).add(b5)
```
  
  -Пакет handlers. Inline-кнопки после ответа на команду ('/По_эмоциям'):
  
```python
emotion = InlineKeyboardMarkup(row_width=3).add(InlineKeyboardButton(text='Радость', callback_data='movie_hpp'),\
                                                InlineKeyboardButton(text='Гнев', callback_data='movie_ang'), \
                                                InlineKeyboardButton(text='Восторг', callback_data='movie_del'), \
                                                InlineKeyboardButton(text='Любопытство', callback_data='movie_cur'), \
                                                InlineKeyboardButton(text='Страх', callback_data='movie_fea'), \
                                                InlineKeyboardButton(text='Грусть', callback_data='movie_sad'))
```

 -Пакет handlers. Вывод Inline-кнопок после ответа на команду ('/По_эмоциям'):
 
```python
async def movie_choice_by_mood(message: types.Message):
    await bot.send_message(message.from_user.id, 'Итак, подберем фильм по эмоциям!')
    await message.answer('Выбирай:', reply_markup=emotion)
```
-Пакет handlers. Ответ на первую Inline-кнопку - ('Радость'):

```python
@dp.callback_query_handler(Text(startswith='movie_hpp'))
async def movie_choice_by_mood_hpp(callback: types.CallbackQuery):
    await sqlit_db.sql_read_movie_hpp(callback)
    await callback.answer()
```
-Пакет data_base. SQL-запрос в БД на получения фильма по критерию Inline-кнопки - ('Радость'):

```python
async def sql_read_movie_hpp(message):
    for ret in cur.execute('SELECT img, name, rating, country, genre, description FROM movie_db_on_mood_tab \
                           WHERE mood == "Радость" ORDER BY RANDOM() LIMIT 1 ').fetchall():
        await bot.send_photo(message.from_user.id, ret[0],
                             f'{ret[1]}\n {ret[2]}\n {ret[3]}\n {ret[4]}\n {ret[-1]}')
```
-Пакет handlers. Регистрация команда и передача их в бот:

```python
def register_handlers_user(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help', 'Start', 'Help'])

    dp.register_message_handler(movie_choice_by_mood, commands=['По_эмоциям'])
    dp.register_message_handler(movie_choice_by_mood_hpp, commands=['Радость'])
    dp.register_message_handler(movie_choice_by_mood_ang, commands=['Гнев'])
    dp.register_message_handler(movie_choice_by_mood_del, commands=['Восторг'])
    dp.register_message_handler(movie_choice_by_mood_cur, commands=['Любопытство'])
    dp.register_message_handler(movie_choice_by_mood_fea, commands=['Страх'])
    dp.register_message_handler(movie_choice_by_mood_sad, commands=['Грусть'])
```
По такому же принципу выполнены остальные ветви работы бота: 

По_эмоциям >> Радость, Восторг и тд.

По_жанру >> Комедия, Анимация и т.д.

По_странам >> Россия, США и т.д.

