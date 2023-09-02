import serial
import threading
from vars import *

def startserial():
	try:
		# Configure the serial port settings (replace '/dev/ttyUSB0' with the correct device path)
		ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)

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
	#        else:
	#            print("Blank line received")

	except Exception as e:
		print("Error:", str(e))

	finally:
		ser.close()


