import sqlite3

class DatabaseConnection:
    def __init__(self, db_file):
        self.db_file = db_file
        self.connection = None

    def connect(self):
        """Establish a connection to the SQLite database."""
        if self.connection is None:
            try:
                self.connection = sqlite3.connect(self.db_file)
                print("Connection to database established.")
            except sqlite3.Error as e:
                print(f"Error connecting to database: {e}")

    def close(self):
        """Close the connection to the SQLite database."""
        if self.connection:
            self.connection.close()
            self.connection = None
            print("Connection to database closed.")