# My-first-Python-program---a-simple-calculator-

print('Welcome')
print('Enter a Number')
mynum1 = float(input('Enter your first number:')) 
mynum2 = float(input('Enter your second number:'))
operation = input('Choose an operation +,-,*,/ : ')
if operation == '+':
    print(mynum1 + mynum2)
elif operation == '-':
    print(mynum1 - mynum2)
elif operation == '*':
    print(mynum1 * mynum2)
elif operation == '/':
    if mynum2 == 0:
        print("Error: Cannot divide by zero.")
    else:
        print(mynum1 / mynum2)
