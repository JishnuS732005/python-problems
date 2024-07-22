#  https://www.hackerrank.com/challenges/capitalize/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys


def solve(s):
    words=s.split(' ')
    capitalized_words=[word.capitalize()for word in words]
    capitalized_string=' '.join(capitalized_words)
    return capitalized_string

if _name_ == '_main_':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
