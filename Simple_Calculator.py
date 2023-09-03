#Simple Calculator Project

#Obtain first numerical input
first_number = int(input('Enter first number: '))

#Obtain specific operator
first_operation = (input('Enter operator: '))

#Obtain second numerical input
second_number = int(input('Enter second number: '))

#Perfom the mathmatical determined in operator choice
if first_operation == '*':
  print('Answer: ', first_number * second_number)
elif first_operation == '+':
  print('Answer: ', first_number + second_number)
elif first_operation == '-':
  print('Answer: ', first_number - second_number)
elif first_operation == '/':
  print('Answer: ', first_number / second_number)
else:
  print('That is not a valid operation'
        )  #prints out string if invalid operation is used
