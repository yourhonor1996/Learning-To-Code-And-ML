number_of_chars = input('Enter the numbger of chars ( :D ): ')
str1 = input('enter the first string input: ')
str2 = input('enter the second string input: ')

def count_mistakes(str1:str, str2:str):
    count = 0
    for i, item in enumerate(str1):
        if(item != str2[i]):
            count += 1
    return count
        
print(count_mistakes(str1, str2))