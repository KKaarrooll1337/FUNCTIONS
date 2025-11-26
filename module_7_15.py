def detector(x):
    count = 0
    for char in x:
        if char == "+":
            count += 1
            if count == 3:
                return True
        if char == "-":
            if count > 0:
                count -= 1
    return False