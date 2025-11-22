a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

def triangle_area(a, b, c):
    import math
    p = (a + b + c) / 2
    tst = p*(p-a)*(p-b)*(p-c)
    s = math.sqrt(p*(p-a)*(p-b)*(p-c))
    return s

result = triangle_area(a, b, c)
print(f'The triangle area of a triangle with sides {a}, {b}, {c} is equal: {result}')