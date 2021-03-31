''' What is an anagram? Well, two words are anagrams of each other if they both contain the same letters. For example:

'abba' & 'baab' == true

'abba' & 'bbaa' == true

'abba' & 'abbba' == false

'abba' & 'abca' == false
Write a function that will find all the anagrams of a word from a list. You will be given two inputs a word and an array with words. 
You should return an array of all the anagrams or an empty array if there are none. For example:

anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']

anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']

anagrams('laser', ['lazing', 'lazy',  'lacer']) => [] '''

# def isAnagram(word1, word2):
#     word1 , word2 = str()
#     set1 = set(word1)
#     return set(word1) == set(word2) and len(word1) == len(word2)
def anagrams(word, words):
    result = []
    for w in words:
        if set(w) == set(word) and len(w) == len(word):
            result.append(w)
    return result

print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))