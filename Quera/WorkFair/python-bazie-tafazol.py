def game(number: int):
    number_str = str(number)
    numbers = [int(num) for num in number_str]
    maximum = max(numbers)
    minimum = min(numbers)
    return maximum - minimum
