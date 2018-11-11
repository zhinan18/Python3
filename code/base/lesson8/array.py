letters = ['a', 'b', 'c', 'd', 'e']
print(letters)
letters.append(['3','4'])
print(letters)

friends = ['Tom','张三']
print(friends)
friends.append('Tom1')
print(friends)
friends.insert(1,"李四")
print(friends)
#print(friends[1])
friends1 = friends[0:2]
print(friends1)
friends.sort()
print(friends)
num1 = friends.index('Tom1')
print(num1)
