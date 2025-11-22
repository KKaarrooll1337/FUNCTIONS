###
# Calculates the sum of the digits in a number
#
number = abs(int(input("Enter a number: ")))

def sum_digits(number):
    number_str = str(number)
    result = 0
    for i in range(len(number_str)):
        result += int(number_str[i])
    return result

result = sum_digits(number)
print(f'The sum of the digits in the number {number} is {result}')