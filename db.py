from abc import ABC
import sqlite3


class AbstractDB(ABC):
    def __init__(self):
        self.connection = None

    """ Database Operations """

    def connect_to_db(self):
        pass

    def close_db(self):
        pass

    """ Table Operations """

    def create_table(self):
        pass

    def table_exist(self):
        pass

    def get_table_structure(self):
        pass

    """ Table Queries """

    def insert_to_table(self):
        pass

    def delete_to_table(self):
        pass


class Database(AbstractDB):

    def __init__(self, db_name=None):
        if not db_name:
            raise ValueError("Database Name is missing")
        else:
            self.connection = sqlite3.connect(f'{db_name}.db')

    """ Database Operations """

    def connect_to_db(self, db=None):
        if db:
            self.connection = sqlite3.connect(db)
            return self.connection
        else:
            self.connection = None
            raise ValueError("Database Name is missing")

    def close_db(self):
        if self.connection:
            self.connection.close()

    """ Table Operations """

    def create_table(self, table_name=None, table_struct=None):
        if not table_name:
            raise ValueError("Table Name cannot be null")

        if not table_struct:
            raise ValueError("Table Structure is missing")

        if self.connection:
            cursor = self.connection.cursor()
            query = f"""CREATE TABLE IF NOT EXISTS {table_name} ({table_struct})"""
            cursor.execute(query)
            self.connection.commit()
        else:
            raise ValueError("Database Connection not available")

    def get_table_structure(self, table_name=None):
        if not table_name:
            raise ValueError("Table Name cannot be null")

        cursor = self.connection.cursor()
        cursor.execute(
            "SELECT sql FROM sqlite_master WHERE type='table' AND name=?", (table_name,))

        result = cursor.fetchone()
        if result is not None:
            table_structure = result[0]
            print(table_structure)
        else:
            print(f"Table {table_name} does not exist")
        cursor.close()

    def insert_to_table(self, table_name=None, data=None):
        if not table_name:
            raise ValueError("Table Name cannot be null")

        if 'dict' not in str(type(data)) or not data or data=={}:
            raise ValueError("Provide Data as dict")

        if self.connection:
            cursor = self.connection.cursor()
            columns = tuple(data.keys())
            values = tuple(data.values())

            cursor.execute(
                f'INSERT INTO users {columns} VALUES (?, ?, ?, ?)', values)
            self.connection.commit()
            cursor.close()


database = Database("user")
table_struct = "username TEXT, first_name TEXT, last_name TEXT, verified BOOL"
database.create_table("users", table_struct)

database.insert_to_table("users",{'username': 'gurus20'})
