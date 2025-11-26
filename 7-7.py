number = int(input("Enter number to check: "))

import module_7_7
def main():
    print(f'The number {number} is binary:', module_7_7.isBinary(str(number)))

if __name__ == "__main__":
    main()