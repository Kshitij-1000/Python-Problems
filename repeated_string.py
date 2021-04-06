# The Problem :-
# There is a string, 's', of lowercase English letters that is repeated infinitely many times. 
# Given an integer, 'n', find and print the number of letter a's in the first 'n' letters of the 
# infinite string.

# Example
# s = 'abcac'
# n = 10
# The substring we consider is abcacabcac, the first 10 characters of the infinite string. There #are 4 occurrences of a in the substring.

# Sample Input 1
# aba
# 10

# Sample Output 1
# 7

# Explanation 1
# The first n=10 letters of the infinite string are abaabaabaa. Because there are 7 a's, we #return 7.

# Sample Input 2
# a
# 1000000000000

# Sample Output 2
# 1000000000000

# Explanation 2
# Because all of the first n = 1000000000000 letters of the infinite string are a, we return 1000000000000.


import math
import os
import random
import re
import sys

def repeatedString(s, n):
    new_s = s[:n%len(s)]
    ct = 0
    for ele in s:
        ct+=ele=='a' and 1 or 0
    ct = ct*int(n/len(s))
    for ele in new_s:
        ct+=ele=='a' and 1 or 0
    return ct

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()
    n = int(input())
    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')
    fptr.close()
