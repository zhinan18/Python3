user_dictionary = {}
while 1:
    command = input("'a' to add word,  'l' to lookup a word,  'q' to quit ")
    if command == "a":
        word = input("Type the word: ")
        definition = input("Type the definition: ")
        user_dictionary[word] = definition
        print("Word added!")
    elif command == "l":
        word = input("Type the word: ")
        if word in user_dictionary.keys():
            print(user_dictionary[word])
        else:
            print("That word isn't in the dictionary yet.")
    elif command == 'q':
        break
