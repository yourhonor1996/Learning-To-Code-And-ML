def func(string:str, num:int):
    return [string[i] for i,letter in enumerate(string) if i%num==0]

print(func("0123456789",5))