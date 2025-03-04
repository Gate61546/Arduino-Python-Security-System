import serial
import time
# Configure the serial port
# MacOS looks somethinglike this: "/dev/ttyUSB0"
port = "COM4"  # Replace with your serial port
baud_rate = 9600
arduino = serial.Serial(port, baud_rate)
try:
    while True:
        # Send data
        message_to_send = "ON\n"
        arduino.write(message_to_send.encode('utf-8'))
        print(f"Sent: {message_to_send.strip()}") 
        # Receive data
        if arduino.in_waiting > 0:
            received_data = arduino.readline().decode('utf-8').strip()
            print(f"Received: {received_data}")
        time.sleep(1)  # Wait for 1 second
        message_to_send = "OFF\n"
        arduino.write(message_to_send.encode('utf-8'))
        print(f"Sent: {message_to_send.strip()}") 
        # Receive data
        if arduino.in_waiting > 0:
            received_data = arduino.readline().decode('utf-8').strip()
            print(f"Received: {received_data}")
        time.sleep(1)  # Wait for 1 second
except serial.SerialException as e:
    print(f"Error: {e}")
finally:
    arduino.close()
    print("Serial port closed")

    