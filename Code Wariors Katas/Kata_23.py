''' Let an array or a list

arr = [x(1), x(2), x(3), x(4), ..., x(i), x(i+1), ..., x(m), x(m+1)]

where all x(i) are positive integers. The length lg of this array will be a positive multiple of 4.

Let

P = (x(1) ** 2 + x(2) ** 2) * (x(3) ** 2 + x(4) ** 2) * ... * (x(m) ** 2 + x(m+1) ** 2),

x ** y means x raised to the power y.

Task
Given an array or list arr the task is to find:

two nonnegative integers A and B such as P = A ** 2 + B ** 2 (1).
The function solve(arr) should return an array or a list [A, B] where A and B verify (1).

Examples:
solve([2, 1, 3, 4]) returns [2, 11] :
(2*2 + 1*1) * (3*3 + 4*4) = 5 * 25 = 125 and 2 * 2 + 11 * 11 = 125

solve([2, 1, 3, 4, 2, 2, 1, 5, 2, 3, 4, 5]) returns [2344, 2892] :
(2*2 + 1*1) * (3*3 + 4*4) * (2*2 + 2*2) * (1*1 + 5*5) * (2*2 + 3*3) * (4*4 + 5*5) = 13858000
and 2344 * 2344 + 2892 * 2892 = 13858000
Notes
The decomposition into A ** 2 + B ** 2 is not unique: the testing function checks if (1) is verified.
Lengths of lists are less than 100 and elements of lists less than 30
Please ask before translating'''

import math
from typing import Iterable
def enumerate2(xs, start=0, step=1):
    length = len(xs)
    for x in xs:
        if start<length:
            yield (start, xs[start])
        start += step
        
def getProdSquare(inputList:list):
    result = 1
    myList = list(enumerate2(inputList,0,2))
    length = len(inputList)
    for i , item in myList:
        if i+1 < length:
            result = result*(item**2+inputList[i+1]**2)
    return result

def solve(arr:list):
    # find the multplication of the squared of the items in the list and name it c2
    c2 = getProdSquare(arr)
    y2 = 0
    doIt = True
    # solve for x and y and check if they are both integers 
    while doIt:
        a = math.sqrt(c2 - y2)
        if a.is_integer() and math.sqrt(y2).is_integer():
            doIt = False
            return [int(a),int(math.sqrt(y2))]
        y2 += 1

a = [2, 1, 3, 4]
b = list(enumerate2(a,0,2))
# print(b)
print(getProdSquare(a))
print(solve(a))
ob = object()
Iterable