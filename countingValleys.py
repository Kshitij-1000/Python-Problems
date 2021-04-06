#An avid hiker keeps meticulous records of their hikes. During the last hike that took exactly  steps, for every step it was noted if it was an uphill, U, or a downhill, D step. Hikes always start and end at sea level, and each step up or down represents a unit change in altitude. We define the following terms:

# 1. A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and ending with a step down to sea level.
# 2. A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending with a step up to sea level.
# 3. Given the sequence of up and down steps during a hike, find and print the number of valleys walked through.

# Example
# The hiker first enters a valley 2 units deep. Then they climb out and up onto a mountain 2 units high. Finally, the hiker returns to sea level and ends the hike.

# Sample Input
# 8
# UDDDUDUU

# Sample Output
# 1

import math
import os
import random
import re
import sys

def countingValleys(steps, path):
    path = [1 if ele=='U' else -1 for ele in path]
    ctr = 0
    v = 0
    for ele in path:
        v = v+ele
        if ele==1 and v==0:
            ctr+=1
    if v<0:
        ctr+=1
    return ctr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
