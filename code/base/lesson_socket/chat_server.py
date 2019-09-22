import socket
import select

host = socket.gethostname()
port = 5999
addr = (host, port)
inputs = []
fd_name = {}

"""
遍历群成员
"""
def who_in_room(w):
    name_list = []
    for k in w:
        name_list.append(w[k])
    return name_list


"""
连接
"""
def conn():
    print("服务端开始运行")
    ss = socket.socket()
    ss.bind(addr)
    ss.listen(5)
    return ss


"""
添加新的群成员
"""
def new_coming(ss):
    client, add = ss.accept()
    print('欢迎 %s %s' % (client, add))
    wel = '''欢迎进入聊天室 . 请输入你的名字:'''
    try:
        client.send(bytes(wel, encoding="utf-8"))
        name = client.recv(1024)
        inputs.append(client)
        fd_name[client] = name
        nameList = "已在线聊天的群成员是 %s" % (who_in_room(fd_name))
        client.send(bytes(nameList, encoding="utf-8"))
    except Exception as e:
        print(e)

"""
遍历聊天信息
"""


def server_run():
    ss = conn()
    inputs.append(ss)
    while True:
        r, w, e = select.select(inputs, [], [])
        for temp in r:
            if temp is ss:
                new_coming(ss)
            else:
                disconnect = False
                try:
                    data = temp.recv(1024)
                    data = fd_name[temp] + " 说 : " + data
                except socket.error:
                    data = fd_name[temp] + "离开聊天室"
                    disconnect = True
                if disconnect:
                    inputs.remove(temp)
                    print(data)
                    for other in inputs:
                        if other != ss and other != temp:
                            try:
                                other.send(bytes(data, encoding="utf-8"))
                            except Exception as e:
                                print(e)
                    del fd_name[temp]
                else:
                    print(data)
                    for other in inputs:
                        if other != ss and other != temp:
                            try:
                                other.send(bytes(data, encoding="utf-8"))
                            except Exception as e:
                                print(e)


server_run()




