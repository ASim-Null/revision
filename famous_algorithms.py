"""
For our practice today we are going to look at few solutions to common Python algorithms
that are frequently asked problems in coding interview rounds.
The exercises covered in this practice (together with their solutions) are adjusted interpretations of problems
available on some coding practice websites.
Solutions we present here are just indicative ones -- there might be other ways to solve tasks, but this is a god start!
"""
####################################################################
# 1. Reverse Integer

# Given an integer, return the integer with reversed digits.
# Note: The integer could be either positive or negative.


def solution1(x):
    string = str(x)

    if string[0] == '-':
        return int('-' + string[:0:-1])
    else:
        return int(string[::-1])


print(solution1(-147))
print(solution1(852))


###################################################################
# 2. Average Words Length

# For a given sentence, return the average word length.
# Note: Remember to remove punctuation first.

sentence1 = "Hi class, we are practicing solving algorithms. It is fun, don't you think?.."
sentence2 = "We need to work very hard to learn more about algorithms!"


def solution2(sentence):
    for p in "!?',;.":
        sentence = sentence.replace(p, '')
    words = sentence.split()
    return round(sum(len(word) for word in words)/len(words),2)


print(solution2(sentence1))
print(solution2(sentence2))


###################################################################
#3. Add strings

# Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.

# Notes:
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.

num1 = '257'
num2 = '2754'


# Approach 1:
def solution3(num1, num2):
    eval(num1) + eval(num2)
    return str(eval(num1) + eval(num2))


print(solution3(num1, num2))


# Approach2
# Given a string of length one,
# the ord() function returns an integer representing the Unicode code point of the character
# when the argument is a unicode object, or the value of the byte when the argument is an 8-bit string.

def solution3_other(num1, num2):
    n1, n2 = 0, 0
    m1, m2 = 10 ** (len(num1) - 1), 10 ** (len(num2) - 1)

    for i in num1:
        n1 += (ord(i) - ord("0")) * m1
        m1 = m1 // 10

    for i in num2:
        n2 += (ord(i) - ord("0")) * m2
        m2 = m2 // 10

    return str(n1 + n2)


print(solution3(num1, num2))
print(solution3_other(num1, num2))


###################################################################
# 4. First unique character

# Given an input string, find the first non-repeating character

s = 'aabccbdcbe'


def solution4(s):
    unique = [ch for ch in s if s.count(ch) == 1] # ['d', 'e']
    return unique[0]


def solution4_other(s):
    return (ch for ch in s if s.count(ch) == 1).__next__()


print(solution4(s))
print(solution4_other(s))


###################################################################
# 5. Monotonic Array

# Given an array of integers, determine whether the array is monotonic or not.

"""
An array is monotonic if and only if it is monotone increasing, or monotone decreasing
"""

A = [100, 6, 5, 4, 4]
B = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
C = [1, 1, 2, 3, 7, 11, 22]


def solution5(nums):
    return (all(nums[i] <= nums[i + 1] for i in range(len(nums) - 1)) or
            all(nums[i] >= nums[i + 1] for i in range(len(nums) - 1)))


print(solution5(A))
print(solution5(B))
print(solution5(C))


###################################################################
# 6. Move zeros

# Given an array nums, write a function to move all zeroes to the end of it while maintaining the relative order of
# the non-zero elements.

array1 = [0, 1, 0, 3, 12]  # --> should be [1, 3, 12, 0, 0]
array2 = [1, 7, 0, 0, 8, 0, 10, 12, 0, 4]  # --> should be [1, 7, 8, 10, 12, 4, 0, 0, 0, 0]


def solution6(nums):
    for i in nums:
        if 0 in nums:
            nums.remove(0)
            nums.append(0)
    return nums


solution6(array1)
solution6(array2)


###################################################################
# 7. Fill in blanks

# Given an array containing None values fill in the None values with most recent
# non None value in the array

array1 = [1, None, 2, 3, None, None, 5, None]


def solution7(array):
    valid = 0
    res = []
    for i in array:
        if i is not None:
            res.append(i)
            valid = i
        else:
            res.append(valid)
    return res


print(solution7(array1))


##################################################################
# 8. Matched  / Mismatched words

# Given two sentences, return an array that has the words that appear in one sentence and not
# the other and an array with the words in common.

sentence1 = 'CFG Nano has engineering and data science streams'
sentence2 = 'As part of engineering we are learning about algorithms and data structures'


def solution8(sentence1, sentence2):
    set1 = set(sentence1.split())
    set2 = set(sentence2.split())

    return sorted(list(set1 ^ set2)), sorted(list(set1 & set2))  # ^ A.symmetric_difference(B), & A.intersection(B)


print(solution8(sentence1, sentence2))


##################################################################
# 9. Prime numbers array

# Given k numbers which are less than n, return the set of prime number among them
# Note: The task is to write a program to print all Prime numbers in an Interval.

"""
A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
"""

interval_num = 44


def solution9(interval):
    prime_nums = []
    for num in range(interval):
        if num > 1:  # all prime numbers are greater than 1
            for i in range(2, num):
                if (num % i) == 0:  # if a modulus == 0 is means that the number can be divided by a number preceding it
                    break
            else:
                prime_nums.append(num)
    return prime_nums


print(solution9(interval_num))
