n, energy = [int(item) for item in input().split()]
# fruits = {2:3, 1:6, 7:1, 5:3}
fruits = {}
for i in range(n):
    fruits.update([[int(item) for item in input().split()]])

# for j in range(n):
# if len(fruits) == 0:
#     break
sortedList = sorted(fruits.keys())
for key in sortedList:
    value = fruits[key]
    # if(key >= value):
    #     fruits.pop(key)
        
    if(key < value and energy >= key):
        energy += (value - key)
        # fruits.pop(key)

print(energy)
