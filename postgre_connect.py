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

    def create_table(self):
        try:
            self.cur.execute("CREATE TABLE IF NOT EXISTS my_table (id SERIAL PRIMARY KEY, data TEXT);")
            self.conn.commit()
            print("Table 'my_table' created or already exists.")
        except psycopg2.Error as e:
            print(f"Error creating table: {e}")

    def insert_data(self, data):
        try:
            self.cur.execute("INSERT INTO my_table (data) VALUES (%s)", (data,))
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
    pg_interaction.create_table("my_table", ["id SERIAL PRIMARY KEY", "data TEXT"])

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

    # Close connection
    pg_interaction.close_connection()


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
