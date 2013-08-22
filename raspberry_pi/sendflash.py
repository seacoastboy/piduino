# code from http://www.doctormonk.com/2012/04/raspberry-pi-and-arduino.html

import serial

# adapt the port to the appropriate one for your installation
ser = serial.Serial('/dev/ttyACM0', 9600)

# should cause the Arduino LED to flash 7 times
# TODO: read input from user to choose this number
ser.write('7')
