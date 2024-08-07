def feedDog(hunger_level, biscuit_size):
    hunger_level.sort()
    biscuit_size.sort()

    fed_dogs = 0
    i = 0
    for size in biscuit_size:
        if i >= len(hunger_level):
            break
        if size >= hunger_level[i]:
            fed_dogs += 1
            i += 1

    return fed_dogs
