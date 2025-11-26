###
# Allows to enter and print employee data. Due to personal
# data protection, you can determine whether information about
# the employee's salary will be printed
#
import keyboard_karol # your own defined module

# Reads employee's data from keyboard
first_name = keyboard_karol.input_string('Enter name: ')
last_name = keyboard_karol.input_string('Enter last name: ')
age = keyboard_karol.input_integer('Enter age: ')
salary = keyboard_karol.input_integer('Enter salary: ')
is_salary_hidden = keyboard_karol.input_boolean('Hide salary? (y/n) ')

# Prints employee's record
print('DATA RECORD')
print('===========')
print('Name:', first_name)
print('Last name: ', last_name)
print('Age: ', age)
if is_salary_hidden == False:
    print('Salary')