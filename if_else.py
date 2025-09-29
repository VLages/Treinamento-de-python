import math
import os
import random
import re
import sys

num = int(input().strip())
if num %2 == 0:
    if 2<=num<=5:
        print('Not Weird')
    if 6<=num<=20:
        print('Weird')
    if num>20:
        print('Not Weird')
else:
    print ('Weird')
