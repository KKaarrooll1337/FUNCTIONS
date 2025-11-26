def power(x, n):
    # Warunek bazowy: dowolna liczba do potęgi 0 wynosi 1
    if n == 0:
        return 1
    # Rekurencja: x^n = x * x^(n-1)
    return x * x ** (n-1)