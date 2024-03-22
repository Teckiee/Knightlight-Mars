import serial
import threading
import glob

def read_serial(ser):
    while True:
        try:
            data = ser.readline().strip().decode('utf-8')
            if data:
                print(f"Received data from {ser.name}: {data}")
                #if ser.name == "/dev/ttyUSB1":
                ser.write("HiACK\n".encode('utf-8'))
                if data == "HELLO":
                    ser.write("ACK\n".encode('utf-8'))
        except Exception as e:
            print(f"Error reading from {ser.name}: {e}")
            # Define data here to handle the case where decoding fails
            data = ser.readline().strip()
            print(f"Received raw data from {ser.name}: {data}")



def start_serial():
    serall = []
    ttyUSB_devices = glob.glob('/dev/ttyUSB*')

    for device in ttyUSB_devices:
        ser = serial.Serial(device, 115200, timeout=1)
        serall.append(ser)
        print(f"Opened serial port: {ser.name}")
        ser.write("ONLINE\n".encode('utf-8'))

    threads = []
    for ser in serall:
        thread = threading.Thread(target=read_serial, args=(ser,))
        thread.daemon = True
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    start_serial()
