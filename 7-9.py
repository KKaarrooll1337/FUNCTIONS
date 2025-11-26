number = int(input("Enter number: "))
boolean = bool(input("Odd (n) or Even (y)?: ") == "y")

import module_7_9
def main():
    if boolean:
        print(f'The sum of even numbers of a number "{number}" is:', module_7_9.num_sum(number, boolean))
    else:
        print(f'The sum of odd numbers of a number "{number}" is:',module_7_9.num_sum(number, boolean))

if __name__ == "__main__":
    main()