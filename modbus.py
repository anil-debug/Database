from pymodbus.client.sync import ModbusTcpClient as ModbusClient
import json

# Define the Modbus device's IP address and port
MODBUS_IP = '192.168.1.100'
MODBUS_PORT = 502

# Define the data to be sent
data = {
    "temperature": 25,
    "humidity": 60,
    "status": "ok"
}

# Serialize the data to JSON
data_json = json.dumps(data)

try:
    # Connect to the Modbus TCP/IP device
    client = ModbusClient(MODBUS_IP, port=MODBUS_PORT)
    client.connect()

    # Convert the JSON data to bytes
    data_bytes = data_json.encode('utf-8')

    # Write the data to a holding register (assuming address 100)
    client.write_registers(100, [byte for byte in data_bytes])

    print("Data sent successfully.")

except Exception as e:
    print(f"Failed to send data: {e}")

finally:
    # Close the Modbus connection
    client.close()
