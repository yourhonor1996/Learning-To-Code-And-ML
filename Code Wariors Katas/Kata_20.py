def CountString(inputString:str, countString:str):
    return inputString.count(countString)
def first_non_repeating_letter(string:str):
    newString = string.lower()
    for ind, letter in enumerate(newString):
        if(newString.count(letter)==1):
            return string[ind]
    return ''
    

print (first_non_repeating_letter('sTreSS'))


