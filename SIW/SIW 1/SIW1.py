#rfind
print('rfind')
text = 'I live in Karagandy . Karagandy is a city of coal.'
y = text.rfind('Temirbolat')
x = text.rfind('Karagandy',0,len(text)) # method finds the last occurrence of the specified value or returns -1
print(x,y) # The same as rindex

#rindex
print()
print('rindex')
text = 'I live in Karagandy . Karagandy is a city of coal.'
#y = text.rindex('Temirbolat') # method finds the last occurrence of the specified value or an exception 
x = text.rindex('Karagandy',0,len(text)) # the same as rfind
print(x) 

#rjust
print()
print('rjust') # right align the string, using a specified character (space is default) as the fill character
text = 'apples' 
print('Hello',text.rjust(14,'X'),'are located in Almaty')

#rpartition
print()
print('rpartition')
txt = "I could eat apples all the day, apples are my favorite fruit"
#last occurrence of the word "bananas", and return a tuple with three elements:
#1 - everything before the "match"
#2 - the "match"
#3 - everything after the "match"
x = txt.rpartition("apples")
print(x)

#rsplit
print()
print('rsplit') # splits a string into a list, starting from the right.
text = 'Hello world. My name is Temirbolat. I study at KBTU.'
print(text.rsplit('.',1)) # string.rsplit(separator, maxsplit) defalt maxsplit = -1

#rstrip
print()
print('rstrip')
txt = "banana,,,,,ssqqqww....." # removes any trailing characters space is the default trailing character to remove.
x = txt.rstrip(",.qsw")
print(x)

#splitlines
print()
print('splitlines')
txt = 'Hello Guys\n Everything is good'
print(txt.splitlines(True)) # return a list deviding it by the \n. True means that we include \n into list. Default is False

#startswith
print()
print('startswith') # returns True if the string starts with the specified value, otherwise False.
txt = 'Hey guys. Everything is good!'
print(txt.startswith('He',0,len(txt)),txt.startswith('Hey',1,len(txt))) 

#strip
print()
print('strip')
txt = '.,.,.,.,,Temirbolat.,qweqw.,.'
print(txt.strip(',.aweq')) # removes any characters space is the default trailing character to remove.

#swapcase
print()
print('swapcase')
txt = 'Hello! My name is TEMIRBOLAT' # All upper cases becomes lower as well as lower becomes upper
print(txt.swapcase())

#title
print()
print('title') # Converts the first letter of each word into Upper Case. 
txt = "hello b2b2b2,and 3g3g3g"
x = txt.title()  # If it meets the number or symbol, the next letter after it will become upper
print(x)

#translate
print()
print('translate') # returns a string where some specified characters are replaced with the character described in a dictionary, or in a mapping table.
mydict = {97:  98} # If you use a dictionary, you must use ascii codes instead of characters.
txt = "My name is Temirbolat"
print(txt.translate(mydict))

#upper
print()
print('upper') # Make all the characters from lower to UPPER CASE
text = 'Good afternoon guys! 228'
print(text.upper())

#zfill
print()
print('zfill') # adds zeros (0) at the beginning of the string, until it reaches the specified length.
a = "Temirbolat"
b = "GPA"
c = "!#212.2"

print(a.zfill(10))
print(b.zfill(10))
print(c.zfill(10))

