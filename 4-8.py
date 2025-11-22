hours = int(input("Enter hours (1-23): "))
minutes = int(input("Minutes (0-59): "))
time_format = int(input("Enter time format (12/24): "))
result = ""

def calculate(hours, minutes, time_format):
    if time_format == 24:
        result = str(hours) + ':' + str(minutes)
    elif time_format == 12:
        hours -= 12
        result = str(hours) + ':' + str(minutes)
    else:
        result = print("Wrong time format")
    return result

result = calculate(hours, minutes, time_format)

print(f'For given parameters the result is: {result}')