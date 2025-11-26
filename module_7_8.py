def ammount(n):
    number_5 = n // 5
    number_2 = (n % 5) // 2
    number_1 = (n % 5) % 2 // 1
    return number_1 + number_2 + number_5