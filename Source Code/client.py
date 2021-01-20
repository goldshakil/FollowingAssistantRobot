#This is the code for client
#You should run this code on a Linux Machine
#Please Configure the IP address and port number according to your RPI IP address

# for questions: contact Muhammad at omarshakil100@gmail.com
import socket

s = socket.socket()
host = "192.168.219.156"
port = 12338
s.connect((host, port))
output = 'Green HUE:64' # Change the color you need FAR to follow here
print(output," is sent")
s.sendall(output.encode('utf-8'))

s.close()
