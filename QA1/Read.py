import sqlite3

def get_table_names(cursor):
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    return [table[0] for table in cursor.fetchall()]

def get_table_data(cursor, table_name):
    cursor.execute(f"SELECT * FROM {table_name}")
    return cursor.fetchall()

def main():
    # Connect to the SQLite database
    connection = sqlite3.connect('questions_answers.db')
    cursor = connection.cursor()

    # Get all table names
    table_names = get_table_names(cursor)
    print("Tables in the database:", table_names)

    # Fetch and display data from each table
    for table in table_names:
        print(f"\nData from {table}:")
        data = get_table_data(cursor, table)
        for row in data:
            print(row)

    # Close the connection
    connection.close()

if __name__ == "__main__":
    main()