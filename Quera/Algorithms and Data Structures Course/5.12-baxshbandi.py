import copy
notneeded = input()
Set = [int(item) for item in input().split()]
n = len(Set)


result = []
for mask in range(1<<n):
    temp = []
    for i in range(n):
        if mask & (1<<i):
            temp.append(Set[i])
    result.append(temp)

sums = [sum(item) for item in result]
length = len(sums)
minimum = abs(sums[0]-sums[-1])
for j in range(length):
    for k in range(j+1, length):
        tempmin = abs(sums[k] - sums[j])
        if(tempmin < minimum):
            minimum = copy.deepcopy(tempmin)
# print(result)
# print(sums)
print(minimum)