
import os
import os.path

print('Created path -',os.path.join(os.sep, 'home', 'user', 'work'))
print('split path -', os.path.split('/usr/bin/python'))
#print('Make Directory -', os.mkdir('temp'))

import os
pid = os.fork()
if pid == 0: # the child
     print("this is the child")
elif pid > 0:
     print("the child is pid %d" % pid)
else:
    print("An error occured")


import sys

print(sys.version)
print(sys.version_info)


#import sys

print("Going via stdout")
sys.stdout.write("Another way to do it!\n")

x = input("read value via stdin: ")
print(x)

print("type in value: ",  sys.stdin.readline()[:-1])



import math
x=10.8
print(math.ceil(x))
print(math.floor(x))
print(math.floor(x))
print(math.fabs(x))
