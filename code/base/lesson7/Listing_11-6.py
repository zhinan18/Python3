print("\t\tDog Bun Ketchup Mustard\tOnions")
count = 1
for dog in [0, 1]:                                 # dog loop
    for bun in [0, 1]:                             # bun loop
        for ketchup in [0, 1]:                     # ketchup loop
            for mustard in [0, 1]:                 # mustard loop
                for onion in [0, 1]:               # onion loop
                    print("#", count, "\t", end="")
                    print(dog, "\t", bun, "\t", ketchup, "\t", end="")
                    print("\t", mustard, "\t\t", onion)
                    count = count + 1
