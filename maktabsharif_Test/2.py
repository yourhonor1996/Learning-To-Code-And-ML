total_num = int(input('enter number of columns of quarters: '))
list_of_nums = []

for i in range(total_num):
    list_of_nums.append(int(input(f'enter number {i+1}: ')))
    
avrg = sum(list_of_nums)/len(list_of_nums)
total_moves_dbl = 0

for i, item in enumerate(list_of_nums):
    total_moves_dbl += abs(item - avrg)
    
print(total_moves_dbl/2)

    
    