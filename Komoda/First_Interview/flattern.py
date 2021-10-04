arr = [1, [2, 3], [1, [1, 3, [5, 6, 9]]]]


def flatten(array):
    results = []
    for item in array:
        if type(item) is int:
            results.append(item)
        elif type(item) is list:
            temp = flatten(item)
            for item2 in temp:
                results.append(item2)
    return results


print(flatten(arr))
