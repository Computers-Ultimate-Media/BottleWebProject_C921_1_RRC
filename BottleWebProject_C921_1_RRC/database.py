import mysql.connector  # pip install mysql-connector-python
from mysql.connector import errorcode

HOST = "localhost"
USER = "root"
PASSWORD = "root"

# строка подключения к базе
db = mysql.connector.connect(
    host=HOST,
    user=USER,
    password=PASSWORD,
    use_pure=True)


# создание БД и таблиц
def create_database():
    cursor = db.cursor()
    db_name = 'bottle_db'

    def create_db(cursor):
        try:
            cursor.execute("create database {}".format(db_name))
            print("Database created.")
        except mysql.connector.Error as err:
            print("Database creation failed:", err)
            exit(1)

    try:
        db.database = db_name
        print('Database {} already exist.'.format(db_name))
    except mysql.connector.Error as err:
        # если ДБ не существует, создать
        if errorcode.ER_BAD_DB_ERROR == err.errno:
            create_db(cursor)
            db.database = db_name

    # скрипт создания таблицы с результатами
    tables = {
        "CREATE TABLE `bottle_db`.`result` ("
        "`id` INT NOT NULL,  "
        "`timestamp` DATETIME NOT NULL DEFAULT NOW(),"
        "`alg_type` INT NOT NULL,"
        "`input` TEXT NOT NULL,"
        "`output` TEXT NOT NULL,"
        "PRIMARY KEY (`id`));"
    }

    for table in tables:
        try:
            cursor.execute(table)
        except mysql.connector.Error as err:
            if errorcode.ER_TABLE_EXISTS_ERROR == err.errno:
                print('Table already exists.')


# select данных из таблицы
def __select__(sql_: str, f_all: bool):
    my_cursor = db.cursor()
    my_cursor.execute(sql_)
    if f_all:
        my_result = my_cursor.fetchall()
    else:
        my_result = my_cursor.fetchone()
    return my_result


# select первой строки из таблицы
def select_one(sql_: str):
    return __select__(sql_, False)


# select нескольких строк из таблицы
def select_all(sql_: str):
    return __select__(sql_, True)


# insert записи в таблицы
def insert(sql_: str, val_: any):
    my_cursor = db.cursor()
    try:
        my_cursor.execute(sql_, val_)
        db.commit()
    except mysql.connector.Error:
        pass
