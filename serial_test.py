import serial, time
from datetime import datetime

def main():
    serial_host('/dev/serial0', 9600)

def serial_host(path, baud):
    ser = serial.Serial(port=path, #Replace ttyS0 with ttyAM0 for Pi1,Pi2,Pi0
        baudrate = baud,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1)
    while True:
        serial_loop(ser)

def serial_loop(ser):
    output = str.encode('Poll Time: %s\n\r' % datetime.now())
    num = ser.write(output)
    print('%i bytes: %s' % (num, output))
    time.sleep(1)

if __name__ == "__main__":
    main()
    