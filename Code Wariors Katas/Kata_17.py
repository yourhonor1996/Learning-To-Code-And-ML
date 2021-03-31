''' Let's make it so Bob never misses another interesting number. We've hacked into his car's computer, and we have a box hooked up that reads mileage numbers. We've got a box glued to his dash that lights up yellow or green depending on whether it receives a 1 or a 2 (respectively).

It's up to you, intrepid warrior, to glue the parts together. Write the function that parses the mileage number input, and returns a 2 if the number is "interesting" (see below), a 1 if an interesting number occurs within the next two miles, or a 0 if the number is not interesting.

Note: In Haskell, we use No, Almost and Yes instead of 0, 1 and 2.

"Interesting" Numbers
Interesting numbers are 3-or-more digit numbers that meet one or more of the following criteria:

Any digit followed by all zeros: 100, 90000
Every digit is the same number: 1111
The digits are sequential, incementing†: 1234
The digits are sequential, decrementing‡: 4321
The digits are a palindrome: 1221 or 73837
The digits match one of the values in the awesome_phrases array
† For incrementing sequences, 0 should come after 9, and not before 1, as in 7890.
‡ For decrementing sequences, 0 should come after 1, and not before 9, as in 3210.

So, you should expect these inputs and outputs:

# "boring" numbers
is_interesting(3, [1337, 256])    # 0
is_interesting(3236, [1337, 256]) # 0

# progress as we near an "interesting" number
is_interesting(11207, []) # 0
is_interesting(11208, []) # 0
is_interesting(11209, []) # 1
is_interesting(11210, []) # 1
is_interesting(11211, []) # 2

# nearing a provided "awesome phrase"
is_interesting(1335, [1337, 256]) # 1
is_interesting(1336, [1337, 256]) # 1
is_interesting(1337, [1337, 256]) # 2
Error Checking
A number is only interesting if it is greater than 99!
Input will always be an integer greater than 0, and less than 1,000,000,000.
The awesomePhrases array will always be provided, and will always be an array, but may be empty. (Not everyone thinks numbers spell funny words...)
You should only ever output 0, 1, or 2.
'''

def is_allZeros(n:int):
    b = str(n)
    result = True
    for digit in b[1:]:
        if (digit!='0'):
            result = False
    return result
def is_same_number(n:int):
    b = str(n)
    result = True
    for i,digit in enumerate(b):
        if (b[i] != b[i-1]):
            result = False
    return result
def is_incrementing(n:int):
    b = str(n)
    result = False
    count = 0
    if(b[-1]=='0'):
        b = b[0:-1]
    if('01'not in b):
        for i in range(1,len(b)):
            if (int(b[i]) == int(b[i-1])+1):
                count += 1
    if (count == len(b)-1):
        result = True
    return result
def is_decrementing(n:int):
    b = str(n)
    result = False
    count = 0
    if(b[-1]=='0'):
        b = b[0:-1]
    for i in range(1,len(b)):
        if (int(b[i]) == int(b[i-1])-1):
            count += 1
    if (count == len(b)-1):
        result = True
    return result

def is_palindrome(n:int):
    b= str(n)
    length = len(b)
    result = True
    if(length%2 == 0):
        for i in range(0,length):
            if(b[i] != b[length-1-i]):
                result = False
    if(length%2 == 1):
        for i in range(0,length):
            if(i != (length-1)/2):
                if(b[i] != b[length-1-i]):
                    result = False
    return result
        

def is_interesting(n:int, awesome_phrases:list):
    if (n <98):
        return 0
    interesting = [is_allZeros(n),
                   is_same_number(n),
                   is_incrementing(n),
                   is_decrementing(n),
                   is_palindrome(n),
                   n in awesome_phrases]
    print(interesting)
    almost = [is_allZeros(n+1) or is_allZeros(n+2),
              is_same_number(n+1) or is_same_number(n+2),
              is_incrementing(n+1) or is_incrementing(n+2),
              is_decrementing(n+1) or is_decrementing(n+2),
              is_palindrome(n+1) or is_palindrome(n+2),
              n+1 in awesome_phrases or n+2 in awesome_phrases]
    print(almost)
    resDic = {'No':0,'Almost':1,'Yes':0}
    
    if (True in interesting): 
        return 2        
    if (True in almost): 
        return 1 
    return 0
b = 'abcdefg'
# print(is_allZeros(6000))
# print(is_same_number(3335))
# print(is_incrementing(7890))
# print(is_decrementing(9876543210))
# print(is_palindrome(123213))
# print(b[0:-1])
print(is_interesting(120, []))