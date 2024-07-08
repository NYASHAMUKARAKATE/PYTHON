num1 = input("enter your fist number!  :")
num2 = input("enter your second number!  :")

num1 = int(num1)
num2 = int(num2)

print('''PLEASE USE :
      
      * FOR MULTIPLICATION
      - FOR SUBTRACTION
      / FOR DIVISION
      + FOR ADDITION
      
      ''')

operation = input("enter the operation you want to use  :")

if operation == "+" :
    result = num1 + num2
    print(result)
    
elif operation == "-" :
    result = num1 - num2
    print(result)
    
elif operation == "/" :
    result = num1 / num2
    print(result)
    
elif operation == "*" :
    result = num1 * num2 
    print(result)
    
else :
    print("enter the correct operation symbol")