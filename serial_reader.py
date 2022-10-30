# Receives a string from Arduino using readline()
# Requires PySerial

# (c) www.xanthium.in 2021
# Rahul.S

# config serial ports using:
# socat PTY,link=/tmp/ttyS0,raw,echo=0 PTY,link=/tmp/ttyS1,raw,echo=1
import serial
import time
 
pc_port = '/dev/tty0'

SerialObj = serial.Serial(pc_port,9600) # COMxx   format on Windows
                                        # /dev/ttyUSBx format on Linux
                                        #
                                        # Eg /dev/ttyUSB0
                                        # SerialObj = serial.Serial('/dev/ttyUSB0')

time.sleep(3)   # Only needed for Arduino,For AVR/PIC/MSP430 & other Micros not needed
                # opening the serial port from Python will reset the Arduino.
                # Both Arduino and Python code are sharing Com11 here.
                # 3 second delay allows the Arduino to settle down.


print("\nConected to ",pc_port, "\n")
SerialObj.timeout = 3 # set the Read Timeout

count = 0
while(1):
    ReceivedString = SerialObj.readline() #readline reads a string terminated by \n
    print (ReceivedString)
    #SerialObj.writelines("Hello")
    count=+1

#SerialObj.close()          # Close the port

# Only needed
# opening the
# Both Arduino
# 3 second