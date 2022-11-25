import sqlite3


# try:
#     conn = sqlite3.connect('datebase\date_base_bot.db')
#     cursor = conn.cursor()
#
#     # Создаем пользователя с user_id
#     cursor.execute("INSERT OR IGNORE INTO 'users' ('user_id') VALUES (?)", (1000),))
#     # Считываем всех пользователей
#     users = cursor.execute("SELEC * FROM 'users'")
#     print(users.fetchall())
#     # Подтверждаем изменения
#     conn.commit()
#
#
# except sqlite3.Error as error:
#     print("Errpr", error)
#
# finally:
#     if (conn):
#         conn.close()
class BotDB:

    def __init__(self, db_file):
        """Инициализация соединения с БД"""
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def user_exists(self, user_id):
        """Проверка наличия пользователя в БД"""
        result = self.cursor.execute("SELECT `id` FROM `users` WHERE `user_id` = ?", (user_id,))
        return bool(len(result.fetchall()))

    def get_user_id(self, user_id):
        """Получаем id пользователя в базе по его user_id в Телеграмме"""
        result = self.cursor.execute("SELECT `id` FROM `users` WHERE `user_id` = ?", (user_id,))
        return result.fetchone()[0]

    def add_user(self, user_id):
        """Добавляем пользователя в БД"""
        self.cursor.execute("INSERT INTO `users` (`user_id`) VALUES (?)", (user_id,))
        return self.conn.commit()

    def add_record(self, user_id, operation, value):
        """Создаем запись о расходе/доходе"""
        self.cursor.execute("INSERT INTO `records` (`user_id`, `operation`, `value`) VALUES (?, ?, ?)",
                            (self.get_user_id(user_id),
                             operation == '+',
                             value))
        return self.conn.commit()

    def get_records(self, user_id, within="*"):
        """Получаем историю операций за определенный период"""
        if (within == 'day'):
            # за последний день
            result = self.cursor.execute(
                "SELECT * FROM `records` WHERE `user_id` = ? AND `date` BETWEEN datetime('now', 'start of day') "
                "AND datetime('now', 'localtime') ORDER BY `date`",
                self.get_user_id(user_id))

        elif (within == 'month'):
            # за последний месяц
            result = self.cursor.execute(
                "SELECT * FROM `records` WHERE `user_id` = ? AND `date` BETWEEN datetime('now', '-6 days') "
                "AND datetime('now', 'localtime') ORDER BY `date`",
                self.get_user_id(user_id))
        elif (within == 'year'):
            # за последний год
            result = self.cursor.execute(
                "SELECT * FROM `records` WHERE `user_id` = ? AND `date` BETWEEN datetime('now', 'start of month') "
                "AND datetime('now', 'localtime') ORDER BY `date`",
                self.get_user_id(user_id))
        else:
            # За всё время
            result = self.cursor.execute(
                "SELECT * FROM `records` WHERE `user_id` = ? ORDER BY `date`",
                self.get_user_id(user_id))

        return result.fetchall()

    def close(self):
        """Закрытие соединения с БД"""
        self.conn.close()
