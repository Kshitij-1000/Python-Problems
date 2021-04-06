# Problem:-
# There is a large pile of socks that must be paired by color.
# Given an array of integers representing the color of each sock, 
# determine how many pairs of socks with matching colors there are.

# Example :
# n = 7
# ar = [1,2,1,2,1,3,2]

# There is one pair of color 1 and one of color 2.
# There are three odd socks left, one of each color 2. The number of pairs is 2.



# STDIN
# 9
# 10 20 20 10 10 30 50 10 20

# Sample Output
# 3


# Explaination
# 2 pairs of 10, 1 pair of 20, 1 single 50, 1 single 30, 1 single 20.
# Total 3 pairs of socks.
# code :-
import math
import os
import random
import re
import sys

def sockMerchant(n, ar):
    d = set(ar)
    del(n)
    dic = {}
    for ele in d:
        ctr = 0
        for e in ar:
            if ele == e:
                ctr+=1
        dic[ele]=ctr
    ctr = 0
    for key in dic:
        ctr = ctr + int(dic[key]/2)
    return ctr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)
    fptr.write(str(result) + '\n')
    fptr.close()
