

l = [3, 2, 5 ,4, 7, 1]
print(sorted(l))
print(sorted(l, reverse = True))


s=['zoom','boom']
print(sorted(s))


d = {1:'a', 3:'b', 2:'c'}
print(sorted(d))


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age=age
    def __repr__(self):
        return "<name: %s, age: %s>" % (self.name, self.age)

jack = Person('Jack', 19)
adam = Person('Adam', 43)
becky = Person('Becky', 11)

people = [jack, adam, becky]

def byName_key(person):
    return person.name

print(sorted(people, key = byName_key))


from operator import attrgetter

print(sorted(people, key = attrgetter('age')))
