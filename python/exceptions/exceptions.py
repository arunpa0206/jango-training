'''
try:
    print(1/0)
except ZeroDivisionError:
    print("You can't divide by zero, you're silly.")

import sys

try:
    number = int(input("Enter a number between 1 - 10"))
except ValueError:
    print('Err.. numbers only')
    sys.exit()

print('you entered number', number)

try:
    raise KeyboardInterrupt
finally:
    print('Goodbye, world!')


import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])


import sys

for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()



try:
    raise Exception('spam','eggs')
except Exception as inst:
    print(type(inst))
    print(inst.args)
    print(inst)

    x, y = inst.args
    print('x =', x)
    print('y =', y)



try:
    raise NameError('HiThere')
except NameError:
        print('An exception flew by!')
        raise
'''

with open("myfile.txt") as f:
    for line in f:
        print(line, end="")
