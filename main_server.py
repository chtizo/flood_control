import time, socket, sys, serial, keyboard
import win32com.client as wincl
#speak = wincl.Dispatch("SAPI.SpVoice")

arduino = serial.Serial('COM3', 9600)

socket_server = socket.socket()

s_ip = '127.0.0.1'
s_port = 4455

print('This is server/host IP address: ',s_ip)


socket_server.bind((s_ip, s_port))
print( "Binding successful!")
print("This is your IP: ", s_ip)
name = "Server"
socket_server.listen(1)
conn, add = socket_server.accept()

print("connected")



while True:


    message = conn.recv(1024)
    
    MyText = message.decode()
##    if len(MyText) > 0:
##        print(MyText)
##        MyText = MyText.lower()
##        sentence=MyText.split()
##        numbers = []
##
##        if sentence.count('speed')>0:
##            
##            for word in sentence:
##                if(word.isdigit()):
##                    print("DC")
##                    print(int(word))
##                    data = "Y{}".format(int(word))
##                    arduino.write(data.encode())
##                    print(data)
##                    time.sleep(0.1)
##                    
##        if sentence.count('servo')>0:
##            for word in sentence:
##                if(word.isdigit()):
##                    print("Servo")
##                    print(int(word))
##                    data = "X{}".format(int(word))
##                    arduino.write(data.encode())
##                    print(data)
##                    time.sleep(0.1)
                
            
