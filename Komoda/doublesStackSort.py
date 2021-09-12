stack1 = [1, 8, 7, 6, 5, 4, 3, 3, 9, 56]
stack2 = []

stack2.append(stack1.pop(0))
i = 0
while len(stack1) > 0:
    stack1_last = stack1.pop(0)
    if stack1_last >= stack2[i]:
        stack2.append(stack1_last)
    else:
        count = 0
        while stack1_last <= stack2[-1]:
            stack1.insert(0, stack2.pop())
            count += 1
        stack2.append(stack1_last)
        for j in range(count):
            stack2.append(stack1.pop(0))
    i += 1

print(stack2)
print(stack1)
