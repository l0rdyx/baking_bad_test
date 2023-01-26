import sqlite3


class DBAccess:
    def __init__(self):
        self.connection = sqlite3.connect("/Users/gleb.krasnopolin/baking-bad/prisma/dev.db")
        self.cursor = self.connection.cursor()

    def select_all(self):
        self.cursor.execute("SELECT * FROM Recipe")
        results = self.cursor.fetchall()
        return [result[1] for result in results]




