import sqlite3
import os

# Path to the shared database file
db_path = 'database.db'  # Store it in the current directory

# Create the database and table if it doesn't exist
def initialize_db():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create the locations table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS locations (
            driver_id TEXT PRIMARY KEY,
            location_link TEXT
        )
    ''')

    conn.commit()
    conn.close()
    print(f"Database initialized successfully at: {os.path.abspath(db_path)}")

# Initialize the database
initialize_db()
