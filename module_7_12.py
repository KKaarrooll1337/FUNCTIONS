def asteriks(x):
    if x == 1:
        result = "*"
    else:
        result = "*" + (x - 1) * "/*"

    return result