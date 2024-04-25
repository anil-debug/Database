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
    pg_interaction.create_table()

    # Insert data
    pg_interaction.insert_data("Some data")

    # Close connection
    pg_interaction.close_connection()

if __name__ == "__main__":
    interact_with_postgres()
