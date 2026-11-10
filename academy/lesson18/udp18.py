import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM); s.bind(('127.0.0.1', 9999))
while True:
    d, a = s.recvfrom(1024)
    open('/home/student/udp.log', 'a').write('got: ' + d.decode().strip() + '\n')
