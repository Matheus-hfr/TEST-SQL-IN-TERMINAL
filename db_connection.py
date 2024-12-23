import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """
    Creates a connection to the SQLite database.
    If the database file does not exist, it will be created.

    :param db_file: Path to the database file.
    :return: Connection object or None in case of an error.
    """
    connection = None
    try:
        connection = sqlite3.connect(db_file)
        print(f"Connection established to the database: {db_file}")
    except Error as e:
        print(f"Error connecting to the database: {e}")
    return connection

def execute_query(connection, query):
    """
    Executes a single SQL query (e.g., CREATE TABLE).

    :param connection: SQLite connection object.
    :param query: The SQL query to execute.
    """
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully.")
    except Error as e:
        print(f"Error executing query: {e}")

def insert_data(connection, query, data):
    """
    Inserts data into a table using a parameterized SQL query.

    :param connection: SQLite connection object.
    :param query: The SQL INSERT query.
    :param data: Tuple of data values to insert.
    """
    try:
        cursor = connection.cursor()
        cursor.execute(query, data)
        connection.commit()
        print("Data inserted successfully.")
    except Error as e:
        print(f"Error inserting data: {e}")

def fetch_data(connection, query):
    """
    Fetches data from the database using a SELECT query.

    :param connection: SQLite connection object.
    :param query: The SQL SELECT query.
    :return: List of rows retrieved by the query.
    """
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        print("Data retrieved successfully.")
        return rows
    except Error as e:
        print(f"Error retrieving data: {e}")
        return []

def update_data(connection, query, data):
    """
    Updates existing data in the table using a parameterized SQL query.

    :param connection: SQLite connection object.
    :param query: The SQL UPDATE query.
    :param data: Tuple of new values to update.
    """
    try:
        cursor = connection.cursor()
        cursor.execute(query, data)
        connection.commit()
        print("Data updated successfully.")
    except Error as e:
        print(f"Error updating data: {e}")

def delete_data(connection, query, data):
    """
    Deletes data from a table using a parameterized SQL query.

    :param connection: SQLite connection object.
    :param query: The SQL DELETE query.
    :param data: Tuple of values to use in the query.
    """
    try:
        cursor = connection.cursor()
        cursor.execute(query, data)
        connection.commit()
        print("Data deleted successfully.")
    except Error as e:
        print(f"Error deleting data: {e}")
