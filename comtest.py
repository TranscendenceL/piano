import serial
import time
import serial.tools.list_ports

print ('hello')
ports = list(serial.tools.list_ports.comports())
print (ports)
for p in ports:
    print (p[1])
    if "Arduino" in p[1]:
	    ser=serial.Serial(port=p[0])
    else :
	    print ("No Arduino Device was found connected to the computer")
#ser=serial.Serial(port='COM4')
song1 = ['1','1','5','5','6','6','5','5','4','4','3','3','2','2','1','1']
song2 = ['1','2','3','1','1','2','3','1','3','4','5','3','4','5']

f = open('mysongs.csv', 'r')
data = f.read()
rows = data.split('\n')
print(rows[0:5])
row=rows[0]
#song1 = row.split(',')

time.sleep(2)

n=ser.write('1'.encode())
n=ser.write('2'.encode())
n=ser.write('3'.encode())
n=ser.write('4'.encode())
n=ser.write('5'.encode())
n=ser.write('6'.encode())
n=ser.write('7'.encode())


print ('after write')
print (n)

def run():
    action = "aaa"
    while action != "q":
        print ('select which tone do you want to play ? 1,2 q and others for quit')
        action = input("> ")
        if action == "1":
            print("song name is:I don't know it is in the head of song")
            for notes in song1:
                ser.write(notes.encode())
                print ("send:"+notes)
                time.sleep(1)
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
