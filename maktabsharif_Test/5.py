n = int(input('input n: '))
input_list = []
for i in range(n):
    input_list.append(int(input(f'enter number {i+1}: ')))

def num_of_changes(numbers:list):
    count = 0
    for i, item in enumerate(numbers):
        if(i>0 and item!=numbers[i-1]):
            count +=1
    return count

print(num_of_changes(input_list))
