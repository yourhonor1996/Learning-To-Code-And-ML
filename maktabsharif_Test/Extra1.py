import string

lower = string.ascii_lowercase

input_string = input()

def crypto(string:str):
    lowercase = string.lower()
    result = []
    Xi = 0
    Ai = 0
    y = 0
    for i, letter in enumerate(lowercase):
        Xi = lowercase.count(letter)
        Ai = lower.index(letter)
        y = (Xi*Ai + 1) % 26
        if(string[i].isupper()):
            result.append(lower[y].upper())
        else: 
            result.append(lower[y])
    return ''.join(result)

print(crypto(input_string))

        
    