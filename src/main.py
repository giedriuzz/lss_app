import sqlite3
from database.db_connection import DatabaseConnection
from models.example_model import ExampleModel

def main():
    # Initialize database connection
    db = DatabaseConnection('database.db')
    connection = db.connect()

    # Example of using the ExampleModel
    example_model = ExampleModel(connection)

    # Perform operations (e.g., create, read, update, delete)
    # example_model.create(...)
    # example_model.read(...)
    # example_model.update(...)
    # example_model.delete(...)

    # Close the database connection
    db.close()

if __name__ == '__main__':
    main()