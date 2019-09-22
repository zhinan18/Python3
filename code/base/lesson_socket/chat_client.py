import socket, select, threading

host = socket.gethostname()
addr = (host, 5999)

"""
连接
"""


def conn():
    s = socket.socket()
    s.connect(addr)
    return s


"""
获取群成员
"""


def lis(s):
    my = [s]
    while True:
        r, w, e = select.select(my, [], [])
        if s in r:
            try:
                print
                s.recv(1024)
            except socket.error:
                print("通信出现异常")
                exit()


"""
输入聊天
"""


def talk(s):
    while True:
        try:
            info = bytes(input(), encoding="utf-8")
        except Exception as e:
            print('can\'t input')
            exit()
        try:
            s.send(info)
        except Exception as e:
            print(e)
            exit()


"""
主函数，创建聊天和获取群成员线程
"""


def main():
    ss = conn()
    t = threading.Thread(target=lis, args=(ss,))
    t.start()
    t1 = threading.Thread(target=talk, args=(ss,))
    t1.start()


main()