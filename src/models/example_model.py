import sqlite3

class ExampleModel:
    def __init__(self, id=None, name=None, description=None):
        self.id = id
        self.name = name
        self.description = description

    def create(self, connection):
        cursor = connection.cursor()
        cursor.execute("INSERT INTO example_table (id, name, description) VALUES (?, ?, ?)", 
                       (self.id, self.name, self.description))
        connection.commit()

    @staticmethod
    def read(connection, id):
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM example_table WHERE id = ?", (id,))
        return cursor.fetchone()

    def update(self, connection):
        cursor = connection.cursor()
        cursor.execute("UPDATE example_table SET name = ?, description = ? WHERE id = ?", 
                       (self.name, self.description, self.id))
        connection.commit()

    @staticmethod
    def delete(connection, id):
        cursor = connection.cursor()
        cursor.execute("DELETE FROM example_table WHERE id = ?", (id,))
        connection.commit()
        
    def create_database(db_file):
        """Create an SQLite database and define the schema."""
        connection = sqlite3.connect(db_file)
        cursor = connection.cursor()

        # Define the schema for the example_table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS example_table (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            description TEXT
        )
        """)

        print(f"Database '{db_file}' and table 'example_table' created successfully.")
        connection.commit()
        connection.close()
        
if __name__ == "__main__":
    
    ExampleModel.create_database("src/database/database.db")
    # Example usage