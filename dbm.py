import sqlite3
# from text import list_img
#
connection = sqlite3.connect('pricebad.db')
curs = connection.cursor()
#
# str_create_db = '''
# CREATE TABLE IF NOT EXISTS PriceBads(
# id INTEGER PRIMARY KEY,
# name_bad TEXT NOT NULL,
# info TEXT,
# price FLOAT NOT NULL,
# name_file TEXT)
# '''
#
# curs.execute(str_create_db)
#
# for i in range(1, 5):
#     curs.execute('INSERT INTO PriceBads(name_bad, info, price, name_file) VALUES(?, ?, ?, ?)',
#                  (f'Product{i}', f'Описание{i}', i * 100, list_img[i - 1]))
#

s = curs.execute('SELECT * FROM PriceBads')
ss = s.fetchall()

connection.commit()
connection.close()

def dbOpen() -> list:
    connection = sqlite3.connect('pricebad.db')
    curs = connection.cursor()
    return [connection, curs]


def dbClose(connection: sqlite3.connect) -> None:
    connection.commit()
    connection.close()
