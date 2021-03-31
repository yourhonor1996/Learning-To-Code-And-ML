''' Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !'''

def pig_it(text):
    # text = str()
    temp = text.split()
    resultList = []
    for item in temp:
        if item in ('!',"?"):
            resultList.append(item)
            continue
        resultList.append('{0}{1}ay'.format(item[1:],item[0]))
    return ' '.join(resultList)

print(pig_it('Hello world !'))    