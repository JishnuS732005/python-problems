#  https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true

import math
import os
import random
import re
import sys



if _name_ == '_main_':
    n = int(input().strip())
    if n % 2 != 0:
        print("Weird")
    else:
        if 2<= n <= 5:
            print("Not Weird")
        elif 6 <= n <=20:
            print("Weird")
        else:
            print("Not Weird")
