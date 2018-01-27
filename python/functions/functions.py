def add(i,j):
    return i+j

sum=add(1,2)
print('Sum of two numbers:',sum)

sum=add(1.5,2.5)
print('Sum of two decimals:',sum)

sum= add('CON','CAT')
print('Concatinate two words', sum)


#Pass by reference or value
def square(y):
    y=y**2

def squareList(y):
    y[0] = y[0]**2

x=5
square(x)
print(x)

x = [5]
squareList(x)
print(x[0])


#Global and local variables

def greetmelocally():
    greetings= 'namaste'
    print('Greet from greetmelocally:',greetings)

def greetmeglobally():
    print('Greet from greetmeglobally:',greetings)


greetings = 'Hi or hello'
greetmelocally()
greetmeglobally()



#Interesting bug
def f():
	#print(s)
	s = "Me too."
	print(s)


s = "I hate spam."
f()
#print(s)


#Default values
def record_score(name, score=0):
    print('%s scored %s' %(name, score))

record_score('arun')
record_score('jill',4)


#Defualt sequences
def add_items(new_items, base_items=[]):
    for item in new_items:
        base_items.append(item)
    return base_items

print(add_items((1, 2, 3)))


#Variable argument functions
def variable_function(*args, **kwargs):
    print('args:', args)
    print('kwargs:', kwargs)

variable_function('sample','test','123')
variable_function(type='Complex', fruit='apple')


def mixed_function(a, b, c=None, *args, **kwargs):
    print('(a, b, c):', (a, b, c))
    print('args:', args)
    print('kwargs:', kwargs)

mixed_function(1, 2, 3, 4, 5, d=10, e=20)


f= lambda x,y:x+y
print(f(1,2))


Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = map(lambda x: (float(9)/5)*x + 32, Celsius)
for item in Fahrenheit:
    print(item)


fib = [0,1,1,2,3,5,8,13,21,34,55]
result = filter(lambda x: x % 2, fib)
for item in result:
    print(item)



str='name'

print(dir(str))
