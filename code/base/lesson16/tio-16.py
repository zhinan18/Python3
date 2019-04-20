
import pickle

name = input("Enter your name: ")
age = input("Enter your age: ")
color = input("Enter your favorite color: ")
food = input("Enter your favorite food: ")

my_list = [name, age, color, food]

pickle_file = open("my_pickle_file.pkl", 'wb')
pickle_file.seek()
pickle.dump(my_list, pickle_file)

pickle_file.close()
