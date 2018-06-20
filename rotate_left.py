# left Rotation
#Function Description

#rotLeft has the following parameter(s):

#An array of integers .
#An integer , the number of rotations.
#Input Format

#The first line contains two space-separated integers  and , the size of  and the number of left rotations you must perform. 
#The second line contains  space-separated integers .

def array_left_rotation(a, n, k):
    return a[k:] + a[:k]
  

n, k = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))
answer = array_left_rotation(a, n, k);
print ' '.join(map(str,answer))
