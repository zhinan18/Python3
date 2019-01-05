names = [] # 初始化列表
#print("Enter 5 names (press the Enter key after each name)")
for i in range(0, 5):  #输入5个名字
    names.append(input("add name"))
print("The name are " + names.__str__())

replace = int(input("Which one ?(1,5):"))
newName = input("New name:")
names[replace - 1] = newName
print("The name are " + names.__str__())


