text = input("Enter text to search from: ")
n = input("Enter a sign to look for: ")

import module_7_4
def main():
    print(f'"{n}" appears', module_7_4.count_sign(n, text), f'times in "{text}"')

if __name__ == "__main__":
    main()