import sqlite3
for row in sqlite3.connect('shop.db').execute('SELECT id, name, price FROM products'): print(row)
