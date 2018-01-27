'''
f=open('text.txt','r')
print(f.read())
f.close()
'''

with open('text.txt','r') as f:
    print(f.read())


with open('text.txt','w') as f:
    f.write('Writing from code')


with open('text.txt','r') as f:
    for line in f.readlines():
        print(line)

from shutil import copyfile

copyfile('text.txt', 'session1.txt')
