x = int(input("Enter starting number: "))
y = int(input("Enter ending number: "))


import module_7_10
def main():
        print(f'Range "{x}-{y}" has:',module_7_10.countNum(x, y))

if __name__ == "__main__":
    main()