hours = int(input("Enter hours (1-23): "))
minutes = int(input("Minutes (0-59): "))
time_format = int(input("Enter time format (12/24): "))
minutes_str = ""
result = ""

def calculate(hours, minutes, time_format):
    if minutes < 10:
        minutes_str = "0" + str(minutes)
        print(minutes_str)
    else:
        minutes_str = str(minutes)

    if time_format == 24:
        result = str(hours) + ':' + minutes_str
    elif time_format == 12:
        if hours == 12:
            result = str(hours) + ':' + minutes_str + ' PM'
        elif hours > 12:
            hours -= 12
            result = str(hours) + ':' + minutes_str + ' PM'
        else:
            result = str(hours) + ':' + minutes_str + ' AM'
    else:
        result = print("Wrong time format")
    return result

result = calculate(hours, minutes, time_format)

print(f'For given parameters the result is: {result}')