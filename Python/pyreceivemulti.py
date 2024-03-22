import serial
import threading
import glob

def startserial():
	
	serall = []
	# Configure the serial port settings (replace '/dev/ttyUSB0' with the correct device path)
	ttyUSB_devices = glob.glob('/dev/ttyUSB*')
	
	for device in ttyUSB_devices:
		ser = serial.Serial(device, timeout=1)
		serall.append(ser)
		print(f"Opened serial port: {ser.name}")
		ser.write("ONLINE\n".encode('utf-8'))

	while True:
		try:
			for ser in serall:
				data1 = ser.readline().strip().decode('utf-8')

				if data1:
					print(f"Received data from {ser.name}: {data1}")

					if data1 == "HELLO":
						ser.write("ACK\n".encode('utf-8'))
				#else:
					#print("Unexpected handshake request:", data1)
	#        else:
	#            print("Blank line received")

		except Exception as e:
			print("Error:", str(e))
		except UnicodeDecodeError:
				print("Received raw bytes:", data)

		finally:
			ser.close()

startserial()
