"""
Two strings are anagram if they have the same frequency of letters
"""


def anagram_solutions(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    if len(s1) != len(s2):
        return False

    dictionary = {}

    for letter in s1:

        if letter in dictionary:
            dictionary[letter] += 1
        else:
            dictionary[letter] = 1
    for letter in s2:
        if letter in dictionary:
            dictionary[letter] -= 1
        else:
            dictionary[letter] = 1

    for k in dictionary:
        if dictionary[k] != 0:
            return False

    return True


anagram_solutions("test", "test")
