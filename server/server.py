import sys
import socket

s = socket.socket()
host = socket.gethostname()
port = 8080
s.bind((host, port))
s.listen(1)
print("waiting...")
conn, addr = s.accept()
print(addr, "has connected")

allvars = '0\n0\n-10\n0\n0\n0\n0'

write = open(sys.path[0]+"/vars.info", 'w')
write.write(allvars)
write.close()

file = open(sys.path[0]+"/vars.info", 'rb')
file_data = file.read(1024)
conn.send(file_data)
print("file sent")

while True:
    quitnow = str(input("quit y/n:"))
    if quitnow == "y":
        s.close()
        print("server shutdown complete")
        restart = str(input("restart y/n:"))
        if restart == "y":
            s.listen(1)
            print("waiting...")
            conn, addr = s.accept()
            print(addr, "has connected")

            allvars = '0\n0\n-10\n0\n0\n0\n0'

            write = open(sys.path[0]+"/vars.info", 'w')
            write.write(allvars)
            write.close()

            file = open(sys.path[0]+"/vars.info", 'rb')
            file_data = file.read(1024)
            conn.send(file_data)
            print("file sent")
        else:
            print("no restart server full shutdown")
            s.conn((host,port))
    if quitnow == "n":
        print("providing to", addr)
