def difference(x, y, z):
    list = [0] * 3
    list[0] = x
    list[1] = y
    list[2] = z

    return max(list) - min(list)