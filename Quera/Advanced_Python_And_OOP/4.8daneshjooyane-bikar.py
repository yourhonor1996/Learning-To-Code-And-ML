import re
def solve(input:str):
    inputs = input.split()
    nums = []
    nums.append(inputs[0]) 
    nums.append(inputs[2]) 
    nums.append(inputs[4]) 
    reals = [0,0,0]
    index = 0
    for i, item in enumerate(nums):
        if '#' in item:
            index = i
            nums[i] = item.replace('#', '\d')
            if i == 2:
                reals[2] = int(nums[0]) + int(nums[1])       
            elif i == 1:
                reals[1] = int(nums[2]) - int(nums[0])
            elif i == 0:
                reals[0] = int(nums[2]) - int(nums[1])
            break
    match = re.search(nums[index],str(reals[index])).group()
    if (match != None):
        return match

print(solve('10# + 50 = 10052'))
# print(re.search())
        
    
    

