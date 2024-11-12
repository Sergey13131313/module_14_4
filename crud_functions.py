import sqlite3
from text import list_img


connection = sqlite3.connect('users_db.db')
curs = connection.cursor()


def initiate_db():
    str_create_db = '''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT,
    description TEXT,
    price INT NOT NULL,
    name_file TEXT)
    '''
    curs.execute(str_create_db)
    connection.commit()

initiate_db()
for i in range(1, 5):
    curs.execute('INSERT INTO Products(title, description, price, name_file) VALUES(?, ?, ?, ?)',
                  (f'Product{i}', f'Описание{i}', i * 100, list_img[i - 1]))


def get_all_products():
    curs.execute('SELECT * FROM Products')
    return curs.execute('SELECT * FROM Products').fetchall()


connection.commit()
connection.close()


