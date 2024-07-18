using System;
using System.Collections.Generic;
using Npgsql;

class PostgreSQLInteraction
{
    private string dbname;
    private string user;
    private string password;
    private string host;
    private int port;
    private NpgsqlConnection conn;
    private NpgsqlCommand cmd;

    public PostgreSQLInteraction(string dbname, string user, string password, string host = "localhost", int port = 5432)
    {
        this.dbname = dbname;
        this.user = user;
        this.password = password;
        this.host = host;
        this.port = port;
    }

    public void Connect()
    {
        try
        {
            string connString = $"Host={host};Port={port};Username={user};Password={password};Database={dbname}";
            conn = new NpgsqlConnection(connString);
            conn.Open();
            cmd = new NpgsqlCommand();
            cmd.Connection = conn;
            Console.WriteLine("Connected to PostgreSQL!");
        }
        catch (Exception e)
        {
            Console.WriteLine($"Error connecting to PostgreSQL: {e.Message}");
        }
    }

    public void CreateTableDb(string tableName, List<string> schema)
    {
        try
        {
            string schemaStr = string.Join(", ", schema);
            string query = $"CREATE TABLE IF NOT EXISTS {tableName} ({schemaStr});";
            cmd.CommandText = query;
            cmd.ExecuteNonQuery();
            Console.WriteLine($"Table '{tableName}' created or already exists.");
        }
        catch (Exception e)
        {
            Console.WriteLine($"Error creating table: {e.Message}");
        }
    }

    public void InsertData(string tableName, string data)
    {
        try
        {
            string query = $"INSERT INTO {tableName} (data) VALUES (@data)";
            cmd.CommandText = query;
            cmd.Parameters.AddWithValue("data", data);
            cmd.ExecuteNonQuery();
            Console.WriteLine("Data inserted successfully.");
        }
        catch (Exception e)
        {
            Console.WriteLine($"Error inserting data: {e.Message}");
        }
    }

    public void ExtractColumnValues(string columnName)
    {
        try
        {
            string query = $"SELECT {columnName} FROM my_table;";
            cmd.CommandText = query;
            using (var reader = cmd.ExecuteReader())
            {
                List<string> values = new List<string>();
                while (reader.Read())
                {
                    values.Add(reader.GetString(0));
                }
                Console.WriteLine($"All values in column '{columnName}': {string.Join(", ", values)}");
            }
        }
        catch (Exception e)
        {
            Console.WriteLine($"Error extracting column values: {e.Message}");
        }
    }

    public void SelectData(string tableName, List<string> columns = null)
    {
        try
        {
            string columnsStr = columns != null ? string.Join(", ", columns) : "*";
            string query = $"SELECT {columnsStr} FROM {tableName};";
            cmd.CommandText = query;
            using (var reader = cmd.ExecuteReader())
            {
                while (reader.Read())
                {
                    for (int i = 0; i < reader.FieldCount; i++)
                    {
                        Console.Write($"{reader.GetName(i)}: {reader.GetValue(i)}, ");
                    }
                    Console.WriteLine();
                }
            }
        }
        catch (Exception e)
        {
            Console.WriteLine($"Error selecting data: {e.Message}");
        }
    }

    public void UpdateData(string tableName, string updateColumn, string updateValue, string conditionColumn, string conditionValue)
    {
        try
        {
            string query = $"UPDATE {tableName} SET {updateColumn} = @updateValue WHERE {conditionColumn} = @conditionValue";
            cmd.CommandText = query;
            cmd.Parameters.AddWithValue("updateValue", updateValue);
            cmd.Parameters.AddWithValue("conditionValue", conditionValue);
            cmd.ExecuteNonQuery();
            Console.WriteLine("Data updated successfully.");
        }
        catch (Exception e)
        {
            Console.WriteLine($"Error updating data: {e.Message}");
        }
    }

    public void DeleteData(string tableName, string conditionColumn, string conditionValue)
    {
        try
        {
            string query = $"DELETE FROM {tableName} WHERE {conditionColumn} = @conditionValue";
            cmd.CommandText = query;
            cmd.Parameters.AddWithValue("conditionValue", conditionValue);
            cmd.ExecuteNonQuery();
            Console.WriteLine("Data deleted successfully.");
        }
        catch (Exception e)
        {
            Console.WriteLine($"Error deleting data: {e.Message}");
        }
    }

    public void ListTables()
    {
        try
        {
            string query = "SELECT table_name FROM information_schema.tables WHERE table_schema='public';";
            cmd.CommandText = query;
            using (var reader = cmd.ExecuteReader())
            {
                Console.WriteLine("List of tables:");
                while (reader.Read())
                {
                    Console.WriteLine(reader.GetString(0));
                }
            }
        }
        catch (Exception e)
        {
            Console.WriteLine($"Error listing tables: {e.Message}");
        }
    }

    public void DescribeTable(string tableName)
    {
        try
        {
            string query = $"SELECT column_name, data_type FROM information_schema.columns WHERE table_name='{tableName}';";
            cmd.CommandText = query;
            using (var reader = cmd.ExecuteReader())
            {
                Console.WriteLine($"Columns in table '{tableName}':");
                while (reader.Read())
                {
                    Console.WriteLine($"{reader.GetString(0)} - {reader.GetString(1)}");
                }
            }
        }
        catch (Exception e)
        {
            Console.WriteLine($"Error describing table: {e.Message}");
        }
    }

    public void CountRows(string tableName)
    {
        try
        {
            string query = $"SELECT COUNT(*) FROM {tableName};";
            cmd.CommandText = query;
            int count = Convert.ToInt32(cmd.ExecuteScalar());
            Console.WriteLine($"Total number of rows in table '{tableName}': {count}");
        }
        catch (Exception e)
        {
            Console.WriteLine($"Error counting rows: {e.Message}");
        }
    }

    public void ExecuteQuery(string query)
    {
        try
        {
            cmd.CommandText = query;
            cmd.ExecuteNonQuery();
            Console.WriteLine("Query executed successfully.");
        }
        catch (Exception e)
        {
            Console.WriteLine($"Error executing query: {e.Message}");
        }
    }

    public void DropTable(string tableName)
    {
        try
        {
            string query = $"DROP TABLE IF EXISTS {tableName};";
            cmd.CommandText = query;
            cmd.ExecuteNonQuery();
            Console.WriteLine($"Table '{tableName}' dropped successfully.");
        }
        catch (Exception e)
        {
            Console.WriteLine($"Error dropping table: {e.Message}");
        }
    }

    public void TruncateTable(string tableName)
    {
        try
        {
            string query = $"TRUNCATE TABLE {tableName} RESTART IDENTITY CASCADE;";
            cmd.CommandText = query;
            cmd.ExecuteNonQuery();
            Console.WriteLine($"Table '{tableName}' truncated successfully.");
        }
        catch (Exception e)
        {
            Console.WriteLine($"Error truncating table: {e.Message}");
        }
    }

    public void CloseConnection()
    {
        try
        {
            if (cmd != null)
            {
                cmd.Dispose();
            }
            if (conn != null)
            {
                conn.Close();
                conn.Dispose();
            }
            Console.WriteLine("Connection closed.");
        }
        catch (Exception e)
        {
            Console.WriteLine($"Error closing connection: {e.Message}");
        }
    }
}

class Program
{
    static void Main(string[] args)
    {
        // Replace with your connection details
        string dbname = "postgres";
        string user = "postgres";
        string password = "your_password";

        // Create an instance of PostgreSQLInteraction
        var pgInteraction = new PostgreSQLInteraction(dbname, user, password);

        // Connect to PostgreSQL
        pgInteraction.Connect();

        // Create table
        pgInteraction.CreateTableDb("my_table", new List<string> { "id SERIAL PRIMARY KEY", "data TEXT" });

        // Insert data
        pgInteraction.InsertData("my_table", "Some data");

        // List tables
        pgInteraction.ListTables();

        // Describe table structure
        pgInteraction.DescribeTable("my_table");

        // Count rows in a table
        pgInteraction.CountRows("my_table");

        // Execute custom query
        pgInteraction.ExecuteQuery("SELECT * FROM my_table;");

        // Select data
        pgInteraction.SelectData("my_table");

        // Update data
        pgInteraction.UpdateData("my_table", "data", "New data", "id", "1");

        // Delete data
        pgInteraction.DeleteData("my_table", "id", "1");

        // Close connection
        pgInteraction.CloseConnection();
    }
}
