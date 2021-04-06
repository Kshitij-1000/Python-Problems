# Problem:-
# There is a new mobile game that starts with consecutively numbered clouds. 
# Some of the clouds are thunderheads and others are cumulus. 
# The player can jump on any cumulus cloud having a number that is equal to the number of the current cloud plus 1 or 2. 
# The player must avoid the thunderheads. 
# Determine the minimum number of jumps it will take to jump from the starting postion to the last cloud. 
# It is always possible to win the game.

# For each game, you will get an array of clouds numbered 0 if they are safe or 1 if they must be avoided.

# Example:-
# c = [0,1,0,0,0,1,0]

# Index the array from 0 to 6 . 
# The number on each cloud is its index in the list so the player must avoid the clouds at indices 1 and 5. 
# They could follow these two paths: 0 > 2 > 3 > 4 > 6  or 0 > 2 > 4 > 6. The first path takes 3 jumps while the second takes 4. 
# Return 3 (minimum number of jumps).

# Sample Input 1 :-
# 7
# 0 0 1 0 0 1 0

# Sample Output 1 :-
# 4

# Explanation 1 :-
# The player must avoid c[2] and c[5]. 
# Hence, the game can be won with a minimum of 4 jumps.

# Sample Input 2 :-
# 6
# 0 0 0 0 1 0

# Sample Output 2 :-
# 3

# Explanation 2 :-
# The only thundercloud to avoid is c[4]. The game can be won in 3 jumps.

#Code:-
import math
import os
import random
import re
import sys

def jumpingOnClouds(c, n):
    i = 0
    jumps = 0
    while i < n-2:
        i+=c[i+2]==0 and 2 or 1
        jumps+=1
    if i==n-2:
        jumps+=1
    return jumps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    c = list(map(int, input().rstrip().split()))
    result = jumpingOnClouds(c, n)

    fptr.write(str(result) + '\n')
    fptr.close()
