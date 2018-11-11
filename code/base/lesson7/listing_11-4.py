numBlocks = int(input('How many blocks of stars do you want? '))
for block in range(1, numBlocks + 1):
    for line in range(1, block * 2):                # Formulas for number of lines
        for star in range(1, (block + line) * 2):    #   and stars
            print('*', end="")
        print("")
    print("")

