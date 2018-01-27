ids=(1,2,3)

print('ids as tuple:', ids)
print(ids[1])

print(ids[0:2])
print(ids*2)
print(ids)

new_ids=tuple([1,2,3])
print(new_ids)
print(type(new_ids))

letters = [('a', 'A'), ('b', 'B')]
for i, (lowercase, uppercase) in enumerate(letters):
    print ("Letter #%d is %s/%s" % (i, lowercase, uppercase))
