#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime as dt
# Complete the time_delta function below.
def time_delta(t1, t2):
    date_format = '%a %d %b %Y %H:%M:%S %z'
    for i in range(int(input())):
        print(int(abs((dt.strptime(input(),date_format)-
        dt.strptime(input(),date_format)).total_seconds())))
    return

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        # fptr.write(delta + '\n')

    # fptr.close()
