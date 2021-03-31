def func1(num1,num2):
    if(num1*num2 > 1000):
        return num1+num2
    return num1*num2

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
print(func1(number1,number2))

    