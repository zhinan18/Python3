f = open("users.txt", 'r', encoding='utf8')
users = eval(f.read())
for count in range(3):
    name = input('请输入用户名： ')
    password = input('请输入密码： ')
    if name in users and password == users[name]['passwd']:
        print('登录成功！')
        break
    else:
        print('用户名或密码错误,还有%d次机会'%(2-count))
f.close()