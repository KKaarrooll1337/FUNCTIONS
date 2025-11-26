def sumRep(x):
    x_str = str(x)
    sum_rep = 0
    for char in x_str:
        if x_str.count(char) > 1:
            sum_rep += int(char)
    return sum_rep