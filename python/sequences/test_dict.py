employees={1:'Arun',2:'Akshay'}

print(employees)
print(employees[1])


temp={'ooty':'19F','Bangalore':'23F'}
print(temp['ooty'])


print(temp.keys())
print(temp.values())
print(temp.items())


for k,v in temp.items():
    print(k,v)


print(temp.get('ooty'))
temp['Mysore']='22F'

print(temp)
print(len(temp))
