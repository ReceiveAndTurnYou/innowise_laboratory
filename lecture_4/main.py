import os
import sqlite3

def execute_sql_file_simple(db_path, sql_file_path):

    if not os.path.exists(sql_file_path):
        print(f"File does not exist: {sql_file_path}")
        return False

    try:
        with open(sql_file_path) as sql_file:
            sql_scripts = sql_file.read()

        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.executescript(sql_scripts)

        conn.commit()

        print(f"SQL script: {sql_file_path} successfully executed")
        return True

    except sqlite3.Error as e:
        print(f"Error from sqlite: {e}")
        return False
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if conn:
            conn.close()


execute_sql_file_simple('school.db', 'queries.sql')