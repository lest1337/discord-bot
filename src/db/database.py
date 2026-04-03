import sqlite3

init_path = "src/db/db_init.sql"

def get_init_file():
    with open(init_path, 'r') as file:
        script = file.read()
        return script.split(';')

def get_connexion():
    conn = sqlite3.connect("src/db/elite-school-bot.db")
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    return conn

def init_db():
    with get_connexion() as conn:
        for query in get_init_file():
            conn.execute(query)