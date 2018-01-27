'''
#Regular expressions to match from the start of the string
import re

line = "Cats are smarter than dogs"

matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)

if matchObj:
   print("matchObj.group() : ", matchObj.group())
   print("matchObj.group(1) : ", matchObj.group(1))
   print("matchObj.group(2) : ", matchObj.group(2))
   print('Start position for string to be matched', matchObj.start())
   print('End position for string to be matched', matchObj.end())
else:
   print("No match!!")
'''

'''
# Example 2 - Compare match with search
import re

line = "Cats are smarter than dogs";

matchObj = re.match( r'dogs', line, re.M|re.I)
if matchObj:
   print("match --> matchObj.group() : ", matchObj.group())
else:
   print("No match!!")

searchObj = re.search( r'dogs', line, re.M|re.I)
if searchObj:
   print("search --> searchObj.group() : ", searchObj.group())
else:
   print("Nothing found!!")
'''

'''
#Example 3 - Replace in strings
import re

phone = "2004-959-559 # This is Phone Number"

# Delete Python-style comments
num = re.sub(r'#.*$', "", phone)
print("Phone Num : ", num)

# Remove anything other than digits
num = re.sub(r'\D', "", phone)
print("Phone Num : ", num)
'''

'''
#Example 4 - Find All
import re

result = re.findall(r'AV', 'AV Analytics Vedio AV')
print(result)

result=re.split(r'i','Analytics Video')
print(result)

result=re.split(r'i','Analytics Video', maxsplit=1)
print(result)
'''

'''
#Example - Substitute
import re

result=re.sub(r'India','the World','AV is largest Analytics community of India')
print(result)
'''

'''
#Example - Compile method
import re
pattern=re.compile('AV')
result=pattern.findall('AV Analytics AV')
print(result)
result2=pattern.findall('AV is largest analytics community of India')
print(result2)
'''
'''
#Example - Print all charecters
import re
result=re.findall(r'.','AV is largest Analytics community of India')
print(result)
'''

'''
#Example - Find all charecters with out spaces
import re
result=re.findall(r'\w','AV is largest Analytics community of India')
print(result)
'''
'''
#Example - Extract word by World
import re

result=re.findall(r'\w*','AV is largest Analytics community of India')
print(result)
'''
'''
#Example - Extract word by word
import re

result=re.findall(r'\w+','AV is largest Analytics community of India')
print(result)
'''
'''
#Example - Extract each World
import re
result=re.findall(r'^\w+','AV is largest Analytics community of India')
print(result)
'''

'''
#Example - Get one word from largest
import re

result=re.findall(r'\w+$','AV is largest Analytics community of India')
print(result)
'''

'''
#Example - Return first two charecters
import re
result=re.findall(r'\w\w','AV is largest Analytics community of India')
print(result)
'''

#Example - Find the domain in an email list
import re
result=re.findall(r'@\w+','abc.test@gmail.com, xyz@test.in, test.first@techcovery.com, first.test@rest.biz')
print (result)
'''
import re

result=re.findall(r'@\w+.\w+','abc.test@gmail.com, xyz@test.in, test.first@analytics.com, first.test@rest.biz')
print(result)
'''
