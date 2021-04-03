import math
number = int(input('enter the number: ')) 

def least_number(number:int):
    number_str = str(math.factorial(number))
    if(len(number_str)==1):
        return number_str
    for i in range(len(number_str)-1, 0, -1):
        if(number_str[i]=='0'):
            pass
        else:
            return number_str[i]

print(least_number(number))