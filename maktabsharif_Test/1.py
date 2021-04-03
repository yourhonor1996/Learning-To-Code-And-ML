var1 = int(input('first number: '))
var2 = int(input('second number: '))
var3 = int(input('third number: '))
number_list = [var1, var2, var3]
number_list.sort()
if(number_list[-1] ** 2 == number_list[0] ** 2 + number_list[1] ** 2):
    print('Yes')
else: 
    print('No')