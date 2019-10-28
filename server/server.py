import socket

while True:
    allvars = '0\n0\n-10\n0\n0\n0\n0'

    write = open('/home/pi/python3d_game_dev/server/vars.info','w')
    write.write(allvars)
    write.close()

    s = socket.socket()
    host = socket.gethostname()
    port = 8080
    s.bind((host, port))
    s.listen(1)
    print("waiting...")
    conn, addr = s.accept()
    print(addr, "has connected")

    file = open('/home/pi/python3d_game_dev/server/vars.info', 'rb')
    file_data = file.read(1024)
    conn.send(file_data)
    print("file sent")
    s.close()
