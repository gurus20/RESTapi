from abc import ABC
import sqlite3

class AbstractDB(ABC):
    def __init__(self):
        self.connection = None

    def connect_to_db(self):
        pass

    def save_to_db(self):
        pass


class Database(AbstractDB):

    def connect_to_db(self, db=None):
        if db:
            self.connection = sqlite3.connect(db)
        else:
            self.connection = None

        return self.connection

    def create_table(self):
        print("creating table")
        cursor = self.connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS users (username TEXT, first_name TEXT, last_name TEXT, verified BOOL)')
        self.connection.commit()


    def save_to_db(self, data=None):
        
        if 'dict' not in str(type(data)):
            return "Provide Data as dict"

        if self.connection:
            self.create_table()
            cursor = self.connection.cursor()
            columns = tuple(data.keys())
            values = tuple(data.values())    
            cursor.execute(
                f'INSERT INTO users {columns} VALUES (?, ?, ?, ?)', values)

            self.connection.commit()

            