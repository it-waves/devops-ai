import sqlite3
db = sqlite3.connect('shop.db')
db.execute('CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, name TEXT, price REAL)')
db.execute('DELETE FROM products')
db.executemany('INSERT INTO products VALUES (?,?,?)', [(1, 'Backpack', 39.0), (2, 'Water bottle', 12.5), (3, 'Notebook', 6.0)])
db.commit()
