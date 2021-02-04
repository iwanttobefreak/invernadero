import serial
import time
from time import localtime, strftime

ser = serial.Serial('/dev/ttyACM0', 9600)

f = open("lecturas.txt","a")
x=ser.readline().split()
print x[0]
print x[1]
f.write(strftime("%d/%m/%Y %H:%M:%S ", localtime()))
f.write(x[0])
f.write(" ")
f.write(x[1])
f.write("\n")
f.close()
