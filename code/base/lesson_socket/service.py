#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定端口:
s.bind(('192.168.60.41', 9999))

print('Bind UDP on 9999...')

while True:
    # 接收数据:
    data, addr = s.recvfrom(1024)
    print('Received from %s:%s.' % addr)
    print(data)
    reply = 'Hello, %s!' % data.decode('utf-8')
    s.sendto(reply.encode('utf-8'), addr)
    print(reply)

