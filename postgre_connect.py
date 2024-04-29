import psycopg2
from psycopg2 import OperationalError

class PostgreSQLInteraction:
    def __init__(self, dbname, user, password, host="localhost", port=5432):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.conn = None
        self.cur = None

    def connect(self):
        try:
            self.conn = psycopg2.connect(dbname=self.dbname, user=self.user, password=self.password, host=self.host, port=self.port)
            self.cur = self.conn.cursor()
            print("Connected to PostgreSQL!")
        except OperationalError as e:
            print(f"Error connecting to PostgreSQL: {e}")

    def create_table_db(self, table_name, schema):
        try:
            schema_str = ', '.join(schema)
            query = f"CREATE TABLE IF NOT EXISTS {table_name} ({schema_str});"
            self.cur.execute(query)
            self.conn.commit()
            print(f"Table '{table_name}' created or already exists.")
        except psycopg2.Error as e:
            print(f"Error creating table: {e}")


    def insert_data(self, table_name, data):
        try:
            self.cur.execute(f"INSERT INTO {table_name} (data) VALUES (%s)", (data,))
            self.conn.commit()
            print("Data inserted successfully.")
        except psycopg2.Error as e:
            print(f"Error inserting data: {e}")


    def extract_column_values(self, column_name):
        try:
            self.cur.execute(f"SELECT {column_name} FROM my_table;")
            rows = self.cur.fetchall()
            values = [row[0] for row in rows]
            print(f"All values in column '{column_name}': {values}")
            return values
        except psycopg2.Error as e:
            print(f"Error extracting column values: {e}")
    
    def select_data(self, table_name, columns=None):
        try:
            if columns:
                columns_str = ', '.join(columns)
                self.cur.execute(f"SELECT {columns_str} FROM {table_name};")
            else:
                self.cur.execute(f"SELECT * FROM {table_name};")
            rows = self.cur.fetchall()
            print("Selected data:")
            for row in rows:
                print(row)
            return rows
        except psycopg2.Error as e:
            print(f"Error selecting data: {e}")

    def update_data(self, table_name, update_column, update_value, condition_column, condition_value):
        try:
            self.cur.execute(f"UPDATE {table_name} SET {update_column} = %s WHERE {condition_column} = %s", (update_value, condition_value))
            self.conn.commit()
            print("Data updated successfully.")
        except psycopg2.Error as e:
            print(f"Error updating data: {e}")

    
    def delete_data(self, table_name, condition_column, condition_value):
        try:
            self.cur.execute(f"DELETE FROM {table_name} WHERE {condition_column} = %s", (condition_value,))
            self.conn.commit()
            print("Data deleted successfully.")
        except psycopg2.Error as e:
            print(f"Error deleting data: {e}")
    
    def list_tables(self):
        try:
            self.cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public';")
            tables = self.cur.fetchall()
            print("List of tables:")
            for table in tables:
                print(table[0])
            return tables
        except psycopg2.Error as e:
            print(f"Error listing tables: {e}")

    def describe_table(self, table_name):
        try:
            self.cur.execute(f"SELECT column_name, data_type FROM information_schema.columns WHERE table_name='{table_name}';")
            columns = self.cur.fetchall()
            print(f"Columns in table '{table_name}':")
            for column in columns:
                print(column[0], "-", column[1])
            return columns
        except psycopg2.Error as e:
            print(f"Error describing table: {e}")

    def count_rows(self, table_name):
        try:
            self.cur.execute(f"SELECT COUNT(*) FROM {table_name};")
            count = self.cur.fetchone()[0]
            print(f"Total number of rows in table '{table_name}': {count}")
            return count
        except psycopg2.Error as e:
            print(f"Error counting rows: {e}")

    def execute_query(self, query):
        try:
            self.cur.execute(query)
            self.conn.commit()
            print("Query executed successfully.")
        except psycopg2.Error as e:
            print(f"Error executing query: {e}")
    
    def drop_table(self, table_name):
        try:
            self.cur.execute(f"DROP TABLE IF EXISTS {table_name};")
            self.conn.commit()
            print(f"Table '{table_name}' dropped successfully.")
        except psycopg2.Error as e:
            print(f"Error dropping table: {e}")

    def truncate_table(self, table_name):
        try:
            self.cur.execute(f"TRUNCATE TABLE {table_name} RESTART IDENTITY CASCADE;")
            self.conn.commit()
            print(f"Table '{table_name}' truncated successfully.")
        except psycopg2.Error as e:
            print(f"Error truncating table: {e}")
    
    def backup_database(self, backup_file):
        try:
            with open(backup_file, 'w') as f:
                self.cur.copy_to(f, 'DATABASE')
            print("Database backed up successfully.")
        except psycopg2.Error as e:
            print(f"Error backing up database: {e}")

    def restore_database(self, backup_file):
        try:
            with open(backup_file, 'r') as f:
                self.cur.copy_from(f, 'DATABASE')
            print("Database restored successfully.")
        except psycopg2.Error as e:
            print(f"Error restoring database: {e}")

    def create_index(self, table_name, column_name):
        try:
            self.cur.execute(f"CREATE INDEX ON {table_name} ({column_name});")
            self.conn.commit()
            print(f"Index created successfully on {table_name}.{column_name}.")
        except psycopg2.Error as e:
            print(f"Error creating index: {e}")

    def drop_index(self, index_name):
        try:
            self.cur.execute(f"DROP INDEX IF EXISTS {index_name};")
            self.conn.commit()
            print(f"Index {index_name} dropped successfully.")
        except psycopg2.Error as e:
            print(f"Error dropping index: {e}")
    
    def inner_join(self, table1, table2, condition):
        try:
            query = f"SELECT * FROM {table1} INNER JOIN {table2} ON {condition};"
            self.cur.execute(query)
            rows = self.cur.fetchall()
            print("Inner join result:")
            for row in rows:
                print(row)
            return rows
        except psycopg2.Error as e:
            print(f"Error performing inner join: {e}")

    def left_outer_join(self, table1, table2, condition):
        try:
            query = f"SELECT * FROM {table1} LEFT OUTER JOIN {table2} ON {condition};"
            self.cur.execute(query)
            rows = self.cur.fetchall()
            print("Left outer join result:")
            for row in rows:
                print(row)
            return rows
        except psycopg2.Error as e:
            print(f"Error performing left outer join: {e}")

    def right_outer_join(self, table1, table2, condition):
        try:
            query = f"SELECT * FROM {table1} RIGHT OUTER JOIN {table2} ON {condition};"
            self.cur.execute(query)
            rows = self.cur.fetchall()
            print("Right outer join result:")
            for row in rows:
                print(row)
            return rows
        except psycopg2.Error as e:
            print(f"Error performing right outer join: {e}")

    def full_outer_join(self, table1, table2, condition):
        try:
            query = f"SELECT * FROM {table1} FULL OUTER JOIN {table2} ON {condition};"
            self.cur.execute(query)
            rows = self.cur.fetchall()
            print("Full outer join result:")
            for row in rows:
                print(row)
            return rows
        except psycopg2.Error as e:
            print(f"Error performing full outer join: {e}")

    def cross_join(self, table1, table2):
        try:
            query = f"SELECT * FROM {table1} CROSS JOIN {table2};"
            self.cur.execute(query)
            rows = self.cur.fetchall()
            print("Cross join result:")
            for row in rows:
                print(row)
            return rows
        except psycopg2.Error as e:
            print(f"Error performing cross join: {e}")

    def self_join(self, table, condition):
        try:
            query = f"SELECT * FROM {table} t1 INNER JOIN {table} t2 ON {condition};"
            self.cur.execute(query)
            rows = self.cur.fetchall()
            print("Self join result:")
            for row in rows:
                print(row)
            return rows
        except psycopg2.Error as e:
            print(f"Error performing self join: {e}")

    def calculate_sum(self, table_name, column_name):
        try:
            self.cur.execute(f"SELECT SUM({column_name}) FROM {table_name};")
            total_sum = self.cur.fetchone()[0]
            print(f"Total sum of values in column '{column_name}' of table '{table_name}': {total_sum}")
            return total_sum
        except psycopg2.Error as e:
            print(f"Error calculating sum: {e}")

    def group_by_column(self, table_name, group_column):
        try:
            self.cur.execute(f"SELECT {group_column}, COUNT(*) FROM {table_name} GROUP BY {group_column};")
            grouped_data = self.cur.fetchall()
            print(f"Grouped data by '{group_column}': {grouped_data}")
            return grouped_data
        except psycopg2.Error as e:
            print(f"Error grouping data: {e}")

    def filter_grouped_data(self, table_name, group_column, filter_condition):
        try:
            self.cur.execute(f"SELECT {group_column}, COUNT(*) FROM {table_name} GROUP BY {group_column} HAVING {filter_condition};")
            filtered_data = self.cur.fetchall()
            print(f"Filtered grouped data by '{filter_condition}': {filtered_data}")
            return filtered_data
        except psycopg2.Error as e:
            print(f"Error filtering grouped data: {e}")

    def begin_transaction(self):
        try:
            self.conn.autocommit = False
            print("Transaction started.")
        except psycopg2.Error as e:
            print(f"Error beginning transaction: {e}")

    def commit_transaction(self):
        try:
            self.conn.commit()
            self.conn.autocommit = True
            print("Transaction committed.")
        except psycopg2.Error as e:
            print(f"Error committing transaction: {e}")

    def rollback_transaction(self):
        try:
            self.conn.rollback()
            self.conn.autocommit = True
            print("Transaction rolled back.")
        except psycopg2.Error as e:
            print(f"Error rolling back transaction: {e}")


    def close_connection(self):
        try:
            if self.cur:
                self.cur.close()
            if self.conn:
                self.conn.close()
            print("Connection closed.")
        except psycopg2.Error as e:
            print(f"Error closing connection: {e}")

    

def interact_with_postgres():
    # Replace with your connection details
    dbname = "postgres"
    user = "postgres"
    password = "your_password"
    
    # Create an instance of PostgreSQLInteraction
    pg_interaction = PostgreSQLInteraction(dbname, user, password)

    # Connect to PostgreSQL
    pg_interaction.connect()

    # Create table
    pg_interaction.create_table_db("my_table", ["id SERIAL PRIMARY KEY", "data TEXT"])

    # Insert data
    pg_interaction.insert_data("my_table", ("Some data",))

    # List tables
    tables = pg_interaction.list_tables()

    # Describe table structure
    if tables:
        for table in tables:
            pg_interaction.describe_table(table[0])

    # Count rows in a table
    if tables:
        for table in tables:
            pg_interaction.count_rows(table[0])

    # Execute custom query
    query = "SELECT * FROM my_table;"
    pg_interaction.execute_query(query)

    # Select data
    pg_interaction.select_data("my_table")

    # Update data
    pg_interaction.update_data("my_table", "data", "New data", "id", 1)

    # Delete data
    pg_interaction.delete_data("my_table", "id", 1)

    # Close connection
    pg_interaction.close_connection()
if __name__ == "__main__":
    interact_with_postgres()
