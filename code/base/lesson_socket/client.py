import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
content = input()

s.sendto(bytes(content, encoding="utf-8"), ('192.168.60.41', 9999))
print(s.recv(1024).decode('utf-8'))


