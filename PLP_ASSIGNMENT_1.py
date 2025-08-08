

'''while True:
    try:   
        num_1 = float(input('enter a number: ' ))
        break
    except ValueError:
        print('Error! please enter a number')

while True:
    try:
        num_2 = float(input('enter second number: '))
        break
    except ValueError:
        print(ValueError, 'please enter a number')
result= num_1 + num_2
print(result)'''


#requesting user operator
num1=float(input('enter a number: '))
num2= float(input('enter a second number: '))
operator=input('enter your operator, +, -, /, *, or %: ')

if operator == '+':
    result = num1 + num2
    print(f"The sum is: {result}")
elif operator == '-':
    result = num1 - num2
    print(f"The difference is: {result}")
elif operator == '*':
    result = num1 * num2
    print(f"The product is: {result}")
elif operator == '**':
    result = num1 ** num2
    print(f"The Power Product is: {result}")
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"The quotient is: {result}")
    else:
        print("Error! Division by zero.")
elif operator == '//':
    if num2 != 0:
        result = num1 // num2
        print(f"The Floor result is: {result}")
    else:
        print("Error! Division by zero.")

    
elif operator == '%':
    if num2 != 0:
        result = num1 % num2
        print(f"The remainder is: {result}")
    else:
        print("Error! Division by zero.")
else:
    print("Invalid operator. Please use +, -, *, /, or %.")


