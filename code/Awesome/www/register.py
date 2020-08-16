f = open("users.txt", 'r+')
users = eval(f.read())  # f.read()读取的是字符串，用eval()将字符串转化为字典
# users = {}
for i in range(4):
    name = input('请输入姓名： ')
    passwd = input('请输入密码： ')
    c_passwd = input('请再次确认密码： ')
    if len(name.strip()) != 0 and name not in users and len(passwd.strip()) != 0 and passwd == c_passwd:
        users[name]= {'passwd':passwd, 'role':1} #往字典中插入新数据
        f.seek(0)
        f.truncate()  #清空文件内容
        f.writelines(str(users)) #将字典写入文件
        print('恭喜，注册成功')
        f.close()
        break
    elif len(name.strip()) == 0:
        print('用户名不能为空，请重新输入。还可输入%d次' %(3-i))
    elif name in users:
        print('用户名重复，请重新输入。还可输入%d次' %(3-i))
    elif len(passwd.strip()) == 0:
        print('密码不能为空，请重新输入。还可输入%d次' %(3-i))
    elif c_passwd != passwd:
        print('两次输入的密码不一致，请重新输入。还可输入%d次' %(3-i))