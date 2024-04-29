import json
from pymodbus.client.sync import ModbusSerialClient as ModbusRTUClient
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadBuilder
from pymodbus.payload import BinaryPayloadDecoder

class ModbusRTUClient:
    def __init__(self, port, baudrate=9600, timeout=1):
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.client = ModbusRTUClient(port=port, baudrate=baudrate, timeout=timeout)

    def connect(self):
        self.client.connect()

    def send_data(self, data, register_address):
        try:
            # Serialize the data to JSON
            data_json = json.dumps(data)
            # Convert the JSON data to bytes
            data_bytes = data_json.encode('utf-8')
            # Build payload
            builder = BinaryPayloadBuilder(byteorder=Endian.Big, wordorder=Endian.Little)
            builder.add_string(data_json)
            payload = builder.to_registers()
            # Write the data to a holding register
            self.client.write_registers(register_address, payload)
            print("Data sent successfully.")
        except Exception as e:
            print(f"Failed to send data: {e}")

    def read_registers(self, register_address, count):
        try:
            # Read data from holding registers
            response = self.client.read_holding_registers(register_address, count)
            if response.isError():
                print("Error reading registers: %s" % response.getExceptionCode())
                return None
            else:
                decoder = BinaryPayloadDecoder.fromRegisters(response.registers, byteorder=Endian.Big, wordorder=Endian.Little)
                data_json = decoder.decode_string()
                return json.loads(data_json)
        except Exception as e:
            print(f"Failed to read data: {e}")

    def close(self):
        self.client.close()

# Example usage for Modbus RTU
if __name__ == "__main__":
    # Define the Modbus device's serial port
    MODBUS_PORT = '/dev/ttyUSB0'
    # Define the data to be sent
    data = {
        "temperature": 25,
        "humidity": 60,
        "status": "ok"
    }
    # Create a Modbus RTU client
    rtu_client = ModbusRTUClient(MODBUS_PORT)
    try:
        # Connect to the Modbus RTU device
        rtu_client.connect()
        # Send data to Modbus RTU device
        rtu_client.send_data(data, register_address=100)
        # Read data from Modbus RTU device
        read_data = rtu_client.read_registers(register_address=100, count=2)
        print("Data read from Modbus RTU device:", read_data)
    finally:
        # Close the Modbus RTU connection
        rtu_client.close()
