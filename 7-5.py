n = int(input("Enter a number: "))
x = int(input("Enter a number defining a start: "))
y = int(input("Enter a number defining an end: "))

import module_7_5
def main():
    print(f'The number is withing a range: {module_7_5.isWithinRange(n, x, y)}')

if __name__ == "__main__":
    main()