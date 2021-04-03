n = int(input('enter n: '))
k = int(input('enter k: '))
# my_list = list(range(n))
def loop_list(i:int, input_list:list):
    length = len(input_list)
    if(i<length):
        return input_list[i]
    if(i>= length):
        return input_list[i % length]
    
# def loop(n:int, k:int):
#     if()
# print(loop_list(2, my_list))

def number_of_jumps(n:int, k:int):
    number_list = list(range(n))
    doIt = True
    j = 0
    count = 0
    while (doIt): 
        j += k
        count += 1
        if(loop_list(j, number_list) == 0):
            return count


print(number_of_jumps(n,k))