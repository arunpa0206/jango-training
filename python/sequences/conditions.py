
a=1
'''
if(a==2):
    print('This will not print')
elif(a==1):
    print('Elif passes')
else:
    print('Else will not print')


while(a==1):
    print('Inside while loop')
    a+=1
else:
    print('Inside else of while')


for i in range(2):
    if(i==0):
        print(i)
    break
'''

for i in range(3,8):
    if(i==4):
        pass
    if(i==3):
        print(i)
    if (i==5):
        continue
    if(i==6):
        print(i)
    if(i==7):
        break
