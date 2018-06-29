# Author Vas Kuruganti

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    k = 0
    for i in note:
        if note.count(i) <= magazine.count(i):
           
            
            k += 1
    
    if k == len(note):
        print 'Yes'
    else:
        print 'No'
