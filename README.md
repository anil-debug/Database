# PostgreSQL Interaction Script

## Overview
This script provides a convenient way to interact with a PostgreSQL database using Python and the `psycopg2` library. It allows you to perform operations such as connecting to the database, creating tables, inserting data, and closing the connection.

## Prerequisites
Before using this script, ensure that you have the following:

- Python installed on your system.
- PostgreSQL installed and running.
- The `psycopg2` library installed. You can install it using pip:
  ```
  pip install psycopg2
  ```

## Usage
1. **Connection Details**:
   - Replace the `dbname`, `user`, and `password` variables in the `interact_with_postgres` function with your PostgreSQL database name, username, and password, respectively.

2. **Run the Script**:
   - Execute the script by running it with Python:
     ```
     python script_name.py
     ```
   - Ensure that the script file (`postgre_connect.py.py`) contains the provided code.

3. **Expected Output**:
   - Upon execution, the script will attempt to connect to the PostgreSQL database using the provided connection details.
   - It will create a table named `my_table` if it does not already exist.
   - It will insert sample data into the `my_table`.
   - Finally, it will close the database connection.

## Customization
You can customize the script according to your specific requirements:
- Modify the `create_table` method to create tables with different schemas.
- Adapt the `insert_data` method to insert data according to your data model.
- Extend the functionality by adding additional methods as needed.

## Notes
- This script assumes that PostgreSQL is running on the local machine (`localhost`) with the default port (`5432`). Modify the `PostgreSQLInteraction` class constructor if your PostgreSQL instance is located elsewhere or using a different port.


# Modbus Data Sender

## Overview

This Python script demonstrates how to send data to a Modbus TCP/IP device using the `pymodbus` library. It connects to a Modbus device, serializes data to JSON format, and writes the data to a holding register on the device.

## Prerequisites

- Python 3.x installed on your system
- `pymodbus` library installed. You can install it using pip:

```bash
pip install pymodbus
