import time
import serial
import sys

# I crated a mock
# And made more changes


# configure the serial connections
ser = serial.Serial(
    #serial port data
    port='/dev/ttyUSB0',
    baudrate=19200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    xonxoff=0,
    rtscts=0
)

ser.isOpen()
ser.write('\x03\r\n')
time.sleep(1)
out=""
while ser.inWaiting() > 0:
        out += ser.read(1)

time.sleep(1)

print ' '
print 'Enter your commands below.\r\nInsert "exit" to leave the application.'
print ' '

input=1
while 1 :
    # get keyboard input
    input = raw_input(">> ")
        # Python 3 users
        # input = input(">> ")
    if input == 'exit':
        ser.close()
        exit()
    if input == 'C':
        ser.write('\x03\r\n')
	time.sleep(1)
	out=""
	while ser.inWaiting() > 0:
        	out += ser.read(1)
	time.sleep(1)
    if input == 'F1':
        ser.write('\x1bOP')
        time.sleep(1)
        out=""
        while ser.inWaiting() > 0:
                out += ser.read(1)
        time.sleep(1)
    if input == 'F3':
        ser.write('\x1bOR')
        time.sleep(1)
        out=""
        while ser.inWaiting() > 0:
                out += ser.read(1)
        time.sleep(1)
    if input == 'F4':
        ser.write('\x1bOS')
        time.sleep(1)
        out=""
        while ser.inWaiting() > 0:
                out += ser.read(1)
        time.sleep(1)

    else:
        # send the character to the device
        # (note that I happend a \r\n carriage return and line feed to the characters - this is requested by my device)
        ser.write(input + '\r\n')
        out = ''
        # let's wait one second before reading output (let's give device time to answer)
        time.sleep(1)
#        while ser.inWaiting() >0:
	timeout = time.time() + 60*2 # time out after two minutes if no '>' is received
        while ser.inWaiting() >-1:
		c = ser.read(1)
		out += c
		if c == '>': break
		sys.stdout.write(c)
		sys.stdout.flush()
		if time.time() > timeout: break

        if out != '':
		print ">>" + out

