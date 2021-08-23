# SIMPLE RECURSIVE FUNCTION

"""
If it is a little bit tricky for students to understand,
then use debugger and walk this function step by step
"""


def print_pattern(num):
    if num < 1:
        return
    else:
        print(num, end=" ")
        print_pattern(num - 1)
        print(num, end=" ")
        return


# Driver Code
my_number = 5
print_pattern(my_number)


########################################

# FACTORIAL

"""
E.g. factorial of 6 (6!) is 1*2*3*4*5*6 = 720
"""


def get_factorial(x):
    if x == 1:
        return 1
    else:
        return x * get_factorial(x - 1)


num = 6
print("The factorial of", num, "is", get_factorial(num))


###########################################

# FIBONACCI
"""
Fibonacci series of 5 is : 0 1 1 2 3
"""


def fib(n):

    if n == 0:
        return 0

    if n == 1 or n == 2:
        return 1

    else:
        return fib(n - 1) + fib(n - 2)


#######################################################

"""
Return all possible combinations of strings of given length, 
which can be formed from a set of supplied characters.
Input: 
char_set = {'a', 'b'}, length = 3
Output:
aaa
aab
aba
abb
baa
bab
bba
bbb
NB: we cannot use itertools product or permutations functions.
"""


def get_str_combinations(char_set, l):
    """
    The function that prints all possible strings of length l.
    """
    n = len(char_set)
    get_str_combinations_rec(char_set, "", n, l)


def get_str_combinations_rec(char_set, prefix, n, l):
    """
    Main recursive method that prints all possible strings of length l.
    """
    if l == 0:
        print(prefix)
        return

    # One by one add all characters
    # from char_set and recursively
    # call for l equals to l-1
    for i in range(n):
        new_prefix = prefix + char_set[i]

        # l is decreased, because we have added a new character
        get_str_combinations_rec(char_set, new_prefix, n, l - 1)


print("Test No1")
set1 = ['a', 'b']
k = 3
get_str_combinations(set1, k)

print("\nTest No2")
set2 = ['a', 'b', 'c', 'd']
k = 1
get_str_combinations(set2, k)
