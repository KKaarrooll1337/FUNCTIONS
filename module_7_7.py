def isBinary(n):

    for char in n:
        if char != '0' and char != '1':
            return False 
    return True