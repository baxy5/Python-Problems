testNum = 332

def sc_perm_comb(x):

    y = str(x)
    result = 0

    # check if it is only one character
    if(len(y) == 1):
        return x

    # check if all the characters are the same
    if(y[0] == y[1] and y[1] == y[2]):
        duplicate = int(y[0]) + int(2*y[0]) + int(3*y[0])
        return duplicate

    for i in y:
        result += int(i)
        for a in y:
            



    return result

print(sc_perm_comb(testNum))
