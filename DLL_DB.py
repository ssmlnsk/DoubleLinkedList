from sqlite3 import connect

from DLL import DoubleLL


class Database(DoubleLL):
    def __init__(self, name):
        super().__init__()
        self.DLL = DoubleLL()
        self.connection = connect(f"{name}")
        self.create_table()

    def create_table(self):
        cursor = self.connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS val (id INTEGER PRIMARY KEY AUTOINCREMENT, value INTEGER)')
        self.connection.commit()
        cursor.close()

    def load_last(self):
        cursor = self.connection.cursor()
        cursor.execute('SELECT value FROM val WHERE id = (SELECT MAX(id) FROM val)')
        value = cursor.fetchone()
        cursor.close()
        return value

    def add_values(self, val):
        cursor = self.connection.cursor()
        cursor.execute(f"""INSERT INTO val (value) VALUES ('{val}')""")
        self.connection.commit()
        cursor.close()

    def delete_all(self):
        cursor = self.connection.cursor()
        cursor.execute("""DELETE FROM val""")
        cursor.execute("DELETE FROM sqlite_sequence WHERE name = 'val'")
        cursor.execute("UPDATE sqlite_sequence SET seq = 0 WHERE name = 'val'")
        self.connection.commit()
        cursor.close()

