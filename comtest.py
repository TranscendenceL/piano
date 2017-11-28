import serial
import time

print ('hello')

ser=serial.Serial(port='COM4')

time.sleep(2)

n=ser.write('1'.encode())
n=ser.write('2'.encode())
n=ser.write('3'.encode())
n=ser.write('4'.encode())
n=ser.write('5'.encode())
n=ser.write('6'.encode())
n=ser.write('7'.encode())
list_q=['']

print ('after write')
print (n)

def run():
    action = "aaa"
    while action != "q":
        print ('select which tone do you want to play ? 1,2 q and others for quit')
        action = input("> ")
        if action == "1":
            for q in list_q:
                print (q)
                ser.write('list1'.encode())
            ser.write('1'.encode())                                                       b
        elif action == "2":
            ser.write('2'.encode())
        elif action == "3":
            ser.write('3'.encode())
        elif action == "4":
            ser.write('4'.encode())
        elif action == "5":
            ser.write('5'.encode())
        elif action == "6":
            ser.write('6'.encode())
        elif action == "7":
            ser.write('7'.encode())
        else :
            return

run()
