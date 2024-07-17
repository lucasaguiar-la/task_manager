
import sqlite3

class DBManager:
    def __init__(self, db_name="database.db"):
        self.db_name = db_name
        self._initialize_db()

    def _initialize_db(self):
        self.execute_query("CREATE TABLE IF NOT EXISTS tasks(name TEXT, status TEXT)")

    def execute_query(self, query, params=[]):
        with sqlite3.connect(self.db_name) as con:
            cur = con.cursor()
            cur.execute(query, params)
            con.commit()
            return cur.fetchall()
