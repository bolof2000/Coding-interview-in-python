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


def add(x, y):

    return x+y


def sub(x,y):
    return x-y


def mul(x, y):
    return x*y


def div(x,y):
    if y == 0:
        raise ValueError("can not divide by zero")
    return x/y


def uniq_string(s):
    return len(set(s)) == len(s)


# solution 2

def uniq_string2(s):
    if s == None:
        print("invalid")
    characters = set()
    for letter in s:
        if letter in characters:
            return False
        else:
            characters.add(letter)

    return True


def anagram(s1, s2):
    # edge check
    if len(s1) != len(s2):
        return False

    # remove white spaces and lower all letters

    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    dictionary = {}
    for letter in s1:
        if letter in dictionary:
            dictionary[letter] += 1
        else:
            dictionary[letter] = 1

            print(dictionary)
    for letter in s2:
        if letter in dictionary:
            dictionary[letter] -= 1
        else:
            dictionary[letter] = 1
            print(dictionary)

    for k in dictionary:
        if dictionary[k] != 0:
            return False

    return True


def sentense_rev(string):
    final_reversed_words = []
    length = len(string)
    i = 0
    spaces = [' ']

    while i < length:

        begin_words = i

        while i < length and s[i] not in spaces:
            i += 1

            final_reversed_words.append(s[begin_words:i])

        i += 1

    return " ".join(reversed(final_reversed_words))


def compression(string):
    r = ""
    length = len(string)

    count = 0

    for i in range(0, len(string)):
        if string[i] == string[i - 1]:
            count += 1
            print(count)

        else:
            r = r + string[i - 1] + str(count)
            print(r)

    r = r + string[i - 1] + str(count)
    print(r)

    return r


def comp(string):
    l = len(string)
    r = ""
    count = 1
    i = 1

    if len(string) == 1:
        return string + "1"
    if string == None:
        print("string required")

    while i < l:
        if string[i] == string[i - 1]:
            count += 1
            # print(count)
        else:

            r = r + string[i - i] + str(count)
            count = 1
            # print(r)

        i += 1

    r = r + string[i - 1] + str(count)
    # print(r)

    return r


def comp2(s):
    r = ""
    l = len(s)
    if l == 0:
        return ""

    if l == 1:
        return s + "1"

    count = 1
    i = 1
    while i < l:

        if s[i] == s[i - 1]:
            count += 1
        else:
            r = r + s[i - 1] + str(count)
            # r = r+str(count)+s[i-1]

            count = 1

        i += 1

    r = r + s[i - 1] + str(count)

    return r


def unique_char(s):
    if len(s) == 0:
        return

    if len(s) == 1:
        return True

    dic = {}

    for letter in s:
        if letter in dic:
            dic[letter] = 1
        else:
            dic[letter] += 1

        for k in dic:
            if dic[k] > 1:
                return False

    return True


def unique_character_solution(s):
    set_seen = ()
    for letter in s:
        if letter not in set_seen:
            set.add(letter)
    else:
        return False

    return True



# def most_frequent_number(num):
#      max_count = -1
#      max_num = None
#
#      dic = {}
#     if len(num) == 0:
#         return None
#     for i in num:
#         if i in dic:
#             dic[i] += 1
#         else:
#             dic[i] = 1
#         if dic[i] > max_count:
#             max_count = dic[i]
#             max_num = i
#
#     return max_num



# def common_element(arr1, arr2):
#       result = []
#     for i in range(0, len(arr1)):
#         for j in range(0, len(arr2)):
#             if arr1[i] == arr2[j]:
#                 result.append(arr1[i])
#
#     return result


def common2(arr1, arr2):
    dic = {}
    result = []
    for i in arr1:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    for j in arr2:
        if j in dic:
            result.append(j)

    return result


def common3(arr1, arr2):
    p1 = 0
    p2 = 0
    result = []

    while p1 < len(arr1) and p2 < len(arr2):
        if arr1[p1] == arr2[p2]:
            result.append(arr1[p1])
            p1 += 1
            p2 += 1
        elif arr1[p1] > arr2[p2]:
            p2 += 1

        else:
            p1 += 1
    return result


def non_repeating_char(char):
    counts = {}
    for i in char:
        if i in counts:
            counts[i] +=1
        else:
            counts[i] =1
    for i in char:
        if counts[i] ==1:
            return i
    return None


def reverse_array(nums):

    start_index = 0
    end_index = len(nums)-1

    while start_index < end_index:

        nums[start_index],nums[end_index] = nums[end_index],nums[start_index]

        start_index +=1
        end_index -=1

    return nums


def string_palindrome(s):

    string = ""
    for i in s:
        string = i+string

    if string == s:
        return True

    return False


def anagram_solution(str1,str2):

    if len(str1) != len(str2):
        return False

    str1 = sorted(str1)
    str2 = sorted(str2)

    for i in range(0,len(str1)):

        if str1[i] != str2[i]:
            return False

    return True










