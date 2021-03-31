''' Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements 
with the same value next to each other and preserving the original order of elements.

For example:

unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3])       == [1,2,3] '''
def unique_in_order(iterable):
    result = []
    i = 0
    # iterable = list()
    for item in iterable:
        if i == 0:
            result.append(item)
        if i>0 and iterable[i] != iterable[i-1]:
            result.append(iterable[i]) 
        i += 1
    return result

list1 =[1,1,2,2,3,3,4,4,4,2,3,4,5,5,5,6,6]
list2 = 'aaaabbbbgghghhjj'
print(unique_in_order(list1))
print(unique_in_order(list2))
# for item in zip(l, l[1:]):
#     if i == j:
#         print(i)
#     if i != j:
#         print(j)
# print(zip(l,l[1:]))