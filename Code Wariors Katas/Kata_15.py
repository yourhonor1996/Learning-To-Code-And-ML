''' Divisors of 42 are : 1, 2, 3, 6, 7, 14, 21, 42. These divisors squared are: 1, 4, 9, 36, 49, 196, 441, 1764. The sum of the squared divisors is 2500 which is 50 * 50, a square!

Given two integers m, n (1 <= m <= n) we want to find all integers between m and n whose sum of squared divisors is itself a square. 42 is such a number.

The result will be an array of arrays or of tuples (in C an array of Pair) or a string, each subarray having two elements, first the number whose squared divisors is a square and then the sum of the squared divisors.

Examples:
list_squared(1, 250) --> [[1, 1], [42, 2500], [246, 84100]]
list_squared(42, 250) --> [[42, 2500], [246, 84100]]
The form of the examples may change according to the language, see Example Tests: for more details.

Note

In Fortran - as in any other language - the returned string is not permitted to contain any redundant trailing whitespace: you can use dynamically allocated character strings. '''
import math
def Divisors(n:int):
    result = []
    for i in range(1,n+1):
        if(n%i==0): 
            result.append(i)
    return result
            
def Sum_Square(l:list):
    result = int(0)
    for item in l:
        result += item**2
    return result

def IsSquared(n:int):
    if (int(math.sqrt(float(n)))**2 == n):
        return True
    return False
        

def list_squared(m, n):
    result = []
    for item in range(m,n+1):
        sumsqrd = Sum_Square(Divisors(item))
        if(IsSquared(sumsqrd)):
            result.append([item,sumsqrd])
    return result
    
print(list_squared(1,250))