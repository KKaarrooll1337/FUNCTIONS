def checkCode(x):
    i = 0
    sum_i = 0

    lista = [0] * len(str(x))
    for char in str(x):
        lista[i] = int(char)
        i += 1

    i = 0
    for i in range(len(str(x))-1):
        sum_i += lista[i]
    
    if sum_i % 7 == lista[3]:
        return True
    else:
        return False