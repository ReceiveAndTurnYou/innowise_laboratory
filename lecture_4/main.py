import sqlite3

conn = sqlite3.connect('school.db')
cursor = conn.cursor()

conn.close()