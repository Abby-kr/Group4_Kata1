#In an even word, each letter occurs an even number of times.
#Write a function solution that, given a string S consisting of N characters, returns the minimum number of letters that must be deleted to obtain an even word.
#Examples:
#1. Given S = "acbcbba", the function should return 1 (one letter b must be deleted).
#2. Given S = "axxaxa", your function should return 2 (one letter a and one letter x must be deleted).

def S(word):
    word.lower()
    uneven_letters = []

    for letter in word:
        if  word.count(letter) % 2 and letter not in uneven_letters:
            uneven_letters.append(letter)
    
    number_of_letters = len(uneven_letters)
    print(number_of_letters)

S('APPLE')