n = int(input("Enter a number between 1 and 12: "))
import module_7_3

def main():
    print(f'The name of month {n} is', module_7_3.month(n))

if __name__ == "__main__":
    main()