
def move_zeros(array:list):
    count = 0
    listofZeros = []
    for i, item in enumerate(array):
        if (item is False):
            # print('false')
            print(f'index: {i} | value: {item}')
            continue
        if(item == 0):
            print(f'index: {i} | value: {item}')
            count +=1
            listofZeros.append(i)
    for i in listofZeros:
        array.pop(i)
        array.append(0)
        
    print(count)
    print(listofZeros)
    # for i in range(count):
        # other.append(0)
    # return other
    print(array)

def move_zeros2(array:list):
    result = []
    count = 0
    for index ,i in enumerate(array):
        if((i is not 0) and (i is not 0.0)):
            result.append(i)
            count += 1
        
    for j in range(len(array)- count):
        result.append(0)
    return result


a= [0, 0, 0, 0, 'y', 'c', False,0,False,False,True,0.0,236,0.0] #'a', -4, 0, '0', 'string', -10, 0,False, 0, 0, 0,False, 3, 2, -10, 0, 3]
#    [0, 0, 'y', 'c', False, True, 'a', -4, '0', 'string', -10, 0, 0, 3, 2, -10, 3, 0, 0, 0, 0, 0, 0]
# print(move_zeros(a))
# move_zeros(a)
print(move_zeros2(a))