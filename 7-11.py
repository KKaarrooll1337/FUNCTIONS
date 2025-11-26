x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))


import module_7_11
def main():
        if module_7_11.isNegWithin(x, y, z):
            print(f'There is a negative value')
        else:
            print(f'No negative value')

if __name__ == "__main__":
    main()