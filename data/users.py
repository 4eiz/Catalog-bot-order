import aiosqlite


async def new_user(user_id):
    db = await aiosqlite.connect('data/db/base.db')
    try:
        # Проверка наличия пользователя в базе данных
        select_query = '''SELECT 1 FROM users WHERE id = ?;'''
        data_tuple = (user_id,)
        cursor = await db.execute(select_query, data_tuple)
        user_exists = await cursor.fetchone()
        
        if user_exists:
            print('Пользователь уже существует в базе данных.')
        else:
            # Вставка нового пользователя в базу данных
            insert_query = '''INSERT INTO users (id)
                              VALUES (?);'''
            await db.execute(insert_query, data_tuple)
            await db.commit()
            print('Запись успешно добавлена.')

    except aiosqlite.Error as error:
        print("Ошибка при подключении к SQLite", error)
    finally:
        await db.close()


async def get_all_ids_from_db():
    async with aiosqlite.connect('data/db/base.db') as db:
        async with db.execute('SELECT id FROM users') as cursor:
            rows = await cursor.fetchall()
            return [row[0] for row in rows]
        

async def get_user_count():
    db = await aiosqlite.connect('data/db/base.db')
    try:
        # Запрос для подсчета количества пользователей
        count_query = '''SELECT COUNT(*) FROM users;'''
        cursor = await db.execute(count_query)
        user_count = await cursor.fetchone()
        
        if user_count:
            return user_count[0]
        else:
            return 0

    except aiosqlite.Error as error:
        print("Ошибка при подключении к SQLite", error)
        return 0
    finally:
        await db.close()
