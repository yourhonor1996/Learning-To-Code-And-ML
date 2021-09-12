def find_divisions(n: int):
    results = []
    for num in range(1, n + 1):
        if n % num == 0:
            results.append(num)
    return results


def is_nice_number(n: int):
    divisions = find_divisions(n)
    if sum(divisions) % 3 == 0:
        return True
    else:
        return False


print(find_divisions(12))
