''' Trolls are attacking your comment section!

A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

Your task is to write a function that takes a string and return a new string with all vowels removed.

For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

Note: for this kata y isn't considered a vowel.'''

def disemvowel(string:str):
    vowels = ['a','e','i','o','u']
    all_vowels = vowels.copy()
    all_vowels.extend(i.capitalize() for i in vowels)
    l = []
    for char in string:
        if char not in all_vowels:
            l.append(char)
    new_string = ''.join(l)
    return new_string

print(disemvowel("This website is for losers LOL!"))    