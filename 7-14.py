x = int(input("Enter 1st number: "))
y = int(input("Enter 2nd number: "))
op = input("Enter operator (+,-,*,%,**): ")

import module_7_14
def main():
        print(module_7_14.calc(x, y, op))

if __name__ == "__main__":
    main()