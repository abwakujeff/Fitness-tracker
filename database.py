import sqlite3

def initialize_db():
    conn = sqlite3.connect('fitness_tracker.db')
    cursor = conn.cursor()

    # Create Users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        )
    ''')

    # Create Workouts table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Workouts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            exercise TEXT,
            duration INTEGER,
            date TEXT,
            FOREIGN KEY (user_id) REFERENCES Users (id)
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    initialize_db()
