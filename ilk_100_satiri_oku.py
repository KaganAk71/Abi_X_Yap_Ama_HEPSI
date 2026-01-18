import sqlite3

conn = sqlite3.connect("Abi_X_Yap_TUMHEPSI.db")
cur = conn.cursor()

cur.execute("SELECT id, text FROM sentences LIMIT 100")

for row in cur.fetchall():
    print(f"{row[0]}: {row[1]}")

conn.close()

