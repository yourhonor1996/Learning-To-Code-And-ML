x1, y1 = input('Enter point 1 coordinates: ').split(' ')
x2, y2 = input('Enter point 1 coordinates: ').split(' ')
x3, y3 = input('Enter point 1 coordinates: ').split(' ')
x = [x1, x2, x3]
y = [y1, y2, y3]

def count_single(l:list):
    for item in l:
        if (l.count(item) == 1):
            return item
        
print(f'the last point is: ({count_single(x)},{count_single(y)})')