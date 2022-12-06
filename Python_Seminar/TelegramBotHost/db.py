import sqlite3

__connection = None


def get_connection():
    global __connection
    if __connection is None:
        __connection = sqlite3.connect('ads.db')
    return __connection


def init_db(force: bool = False):
    conn = get_connection()
    c = conn.cursor()
    if force:
        c.execute('DROP TABLE IF EXISTS user_message')
        c.execute('''
            CREATE TABLE IF NOT EXISTS user_message (
                id          INTEGER PRIMARY KEY,
                user_id     INTEGER NOT NULL,
                text        TEXT NOT NULL
            )
        ''')
        # Сохранить изменения
        conn.commit()


# Добавляем сообщение
def add_message(user_id: int, text: str):
    conn = get_connection()
    c = conn.cursor()
    c.execute('INSERT INTO user_message (user_id, text) VALUES (?, ?)', (user_id, text))
    conn.commit()


def add_message_rabota(user_id: int, text: str):
    conn = get_connection()
    c = conn.cursor()
    c.execute('INSERT INTO user_message (user_id, text) VALUES (?, ?)', (user_id, text))
    conn.commit()


# подсчет количества сообщений от пользователя
def count_message(user_id: int):
    conn = get_connection()
    c = conn.cursor()
    c.execute('SELECT COUNT(*) user_message WHERE user_id = ?', (user_id,))
    (res,) = c.fetchall()
    return res


# Вывод последних 10 сообщений от позднего к самому последнему
def list_messages(user_id: int, limit: int = 10):
    conn = get_connection()
    c = conn.cursor()
    c.execute('SELECT id, text FROM user_message WHERE user_id = ? ORDER BY id DESC LIMIT ?', (user_id, limit))
    return c.fetchall()

# if __name__ == '__main__':
#     init_db()
#     add_message(user_id=123, text='keker')
#     r = count_message(user_id=123)
#     print(r)
