# simple calculator program
num1 = int(input("enter first number:"))
num2 = int(input("enter second number:"))
operator = input("type any operator:+,-,*,/")
oper = "+-*/"
if operator == '+':
    print("the sum is",num1 + num2)
elif operator == '-':
    print("difference is",num1 - num2)
elif operator == '*':
    print("product is",num1 * num2)
elif operator == '/':
    if num2 != 0:
         print("quatient is",num1 / num2)
    else:
        print("this is invalid")
else:
    print("invalid operator")        
   