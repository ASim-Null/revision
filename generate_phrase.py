"""
Create required phrase.
----------------------
​
You are given a string of available characters and a string representing a word or a phrase that you need to generate.
Write a function that checks if you cab generate required word/phrase using the characters provided.
If you can, then please return True, otherwise return False.
​
NOTES:
    You can only generate the phrase if the frequency of unique characters in the characters string is equal or greater
    than frequency in the document string.
​
FOR EXAMPLE:
​
    characters = "cbacba"
    phrase = "aabbccc"
​
    In this case you CANNOT create required phrase, because you are 1 character short!
​
IMPORTANT:
    The phrase you need to create can contain any characters including special characters, capital letter, numbers
    and spaces.
​
    You can always generate an empty string.
​
"""
​
​
def generate_phrase(characters, phrase):
    for char in phrase:
        phrase_frequency = count_char_frequency(char, phrase)
        char_frequency = count_char_frequency(char, characters)
        if phrase_frequency > char_frequency:
            return False
    return True
​
​
def count_char_frequency(char, target):
    f = 0
    for c in target:
        if c == char:
            f += 1
    return f
​
​
###################################################
​
# Test case 1 -- False
​
# characters = "odeC stFir slrG"
# phrase = "Code First Girls"
#
# print(generate_phrase(characters, phrase))
​
###################################################
​
# Test case 2 -- False
​
# characters = "A"
# phrase = "a"
#
# print(generate_phrase(characters, phrase))
​
###################################################
​
# Test case 3 -- True
​
# characters = "odeC stFir slrG"
# phrase = ""
#
# print(generate_phrase(characters, phrase))
​
###################################################
​
# Test case 4 -- True
​
# characters = "aheaollabbhb"
# phrase = "hello"
#
# print(generate_phrase(characters, phrase))
