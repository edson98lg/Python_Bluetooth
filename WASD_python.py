import serial
import keyboard as k
import time

try: 
    ser = serial.Serial("com5", 9600)	#SELECT THE PORT WHERE THE MODULE BLUETOOTH HAS BEEN CONNECTED

    while True:
        time.sleep(0.02)

        if k.is_pressed("w"):  #FORWARD
            ser.write(b'w')

        if k.is_pressed("d"):  #RIGHT
            ser.write(b'd')

        if k.is_pressed("s"):  #BACKWARD
            ser.write(b's')
            
        if k.is_pressed("a"):  #LEFT
            ser.write(b'a')

        if k.is_pressed("SPACE"):  #STOP
            ser.write(b'p')


except TimeoutError:
    print("error")
finally:                                                                           
    print("error")
