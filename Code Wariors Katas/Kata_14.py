
a = [[1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]]
c=[[1]]
d=[[1,2],[3,4]]
b= [[1,2],
    [3,4]]
# go from upper left to lowerright
def corner_to_corner(matrix:list,upper_to_lower:bool = True):
    result = []
    length = len(matrix)
    if (upper_to_lower == True):
        for i in range(length):
            result.append(matrix[0][i])
            i +=1
        for i in range(1,length):
            result.append(matrix[i][length-1])
            i+= 1
    if (upper_to_lower == False):
        for i in range(length-1,-1,-1):
            result.append(matrix[length-1][i])
            i -=1
        for i in range(length-2,-1,-1):
            result.append(matrix[i][0])
            i+= 1
    return result

def slice_matrix(main_matirx:list,slice_upper:bool =True) -> list:
    result = []
    length = len(main_matirx)
    if(slice_upper==True):
        # if length == 2: 
        #     return [[main_matirx[1][0]]]
        for i in range(1,length):
            result.append(main_matirx[i][0:length-1])
            
    if(slice_upper== False):
        # if length == 2: 
        #     return [[main_matirx[0][1]]]
        for i in range(0,length-1):
            result.append(main_matirx[i][1:length])
    return result

def snail(snail_map:list):
    length = len(snail_map)
    result = []
    cur_matrix = snail_map
    upper_to_lower = True
    if length==1:
        return snail_map
    for n in range(length-1):
        # if we are in the last iteration stop and return the last element
        if(upper_to_lower == True):
            # go from upperleft to lowerright and appen the results
            result.extend(corner_to_corner(cur_matrix))
            cur_matrix = slice_matrix(cur_matrix)
            upper_to_lower = False
        if(upper_to_lower == False):
        # go from upperleft to lowerright and appen the results
            result.extend(corner_to_corner(cur_matrix,False))
            cur_matrix = slice_matrix(cur_matrix,False)
            upper_to_lower = True
        # print(cur_matrix, '  -> n is{}'.format(n))
        # go from lowerright to upperleft
    # print(result)
    return result
        # generate a new matrix from the leftovers
print(snail(a))        
print(snail(c))        
print(snail(d))        
# print(slice_matrix(a))    
# print(slice_matrix(b,False))
# print(a[1][0:2])
# print(corner_to_corner(a,False))
# print(snail(a))