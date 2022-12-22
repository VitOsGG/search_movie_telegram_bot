from aiogram.utils import executor
from create_bot import dp
from data_base import sqlit_db, sqlit_db_fct


async def on_startup(_):
    print('Бот готов рекомендовать кино!')
    sqlit_db.sql_start()
    sqlit_db_fct.sql_start_int_bd()


from handlers import user, other

user.register_handlers_user(dp)
other.register_handlers_other(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
