import serial
import threading

def serial_handler(ser):
    try:
        while True:
            handshake_request = ser.readline().strip().decode('utf-8')

            if handshake_request:
                print("Received handshake request:", handshake_request)

                if handshake_request == "HELLO":
                    print("Valid handshake request: HELLO")
                    # Send a response back to the VB.NET application
                    ser.write("ACK\n".encode('utf-8'))
                else:
                    print("Unexpected handshake request:", handshake_request)

    except Exception as e:
        print("Error:", str(e))

def start_serial():
    ser = None
    try:
        # Configure the serial port settings (replace '/dev/ttyUSB0' with the correct device path)
        ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=10)

        # Start a separate thread to handle serial communication
        serial_thread = threading.Thread(target=serial_handler, args=(ser,), daemon=True)
        serial_thread.start()

        # Main thread can do other tasks or wait for user input
        while True:
            pass  # Or do other tasks

    finally:
        if ser is not None and ser.is_open:
            ser.close()

# Call the start_serial function to begin serial communication
start_serial()