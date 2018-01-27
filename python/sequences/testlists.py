ids=[1,2,3,4,5]

print('ids:',ids)
print('No of ids:',len(ids))
print('Element 1 in ids', ids[1])
print('Elements 1 to 3 in ids', ids[1:3])
print('All elements except last element:', ids[:-1])


a,b=ids[1:3]
print('Unpacked list:',a,b)

new_ids=[6,7]
print('new ids:',new_ids)
print('No of new ids:',len(new_ids))

merged_ids=ids+new_ids
print('merged_ids:', merged_ids)

print('ids[3] in merged_ids', ids[3] in merged_ids)
print('new_ids[1] in merged_ids', new_ids[1] in merged_ids)


merged_ids*=10
print('merged_ids repeated 10 times:', merged_ids)

first_ten = [i for i in range(2,10,2)]
print('first ten list:',first_ten)

first_ten_squares = [i**2 for i in range(10)]
print('first ten squares:',first_ten_squares)


first_three_words= ['one','two','three']
print(first_three_words)


first_three=first_ten+first_three_words
print(first_three)

first_three.append('four')
print(first_three)

first_three.remove('four')
print(first_three)

first_three.insert(1,'zero')
print(first_three)

second_ten= [i for i in range(10,20,2)]
first_ten.extend(second_ten)
print('Second ten:',second_ten)

print('Extended first ten:', first_ten)

print('Second ten:',second_ten)
print('pop element:', second_ten.pop())
print('Second ten:',second_ten)

d=[3,4,5,6,0,1,2]
print('sorted list:', sorted(d))

'''



















a=[i for i in range(1,10,2)]
print(a)


'''
