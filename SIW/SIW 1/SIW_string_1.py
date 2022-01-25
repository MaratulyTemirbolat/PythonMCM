
# String


#Capitalize
print('Capitalize') 
text = 'my name is TEMIRBOLAT' 
new_text = text.capitalize() #returns a string where the first character is upper case. OTHER CHARACTERS ARE IN LOWER CASE
print(new_text) # My name is temirbolat

#Casefold
print()
print('casefold')
new_text = text.casefold() # returns a string where ALL the characters are LOWER CASE
print(new_text) # similar to the lower()

#Center
print()
print('center')
txt = "banana"
x = txt.center(20, "O") # center align the string, using a specified character (space is default) as the fill character.
print(x) # string.center(length, character) where length of the returned string  and character to fill the missing space on each side

#Count
print()
print('Count')
txt = 'I love anime episodes, anime plays a big role in our life'
x = txt.count('anime',0,len(txt)) #  method returns the number of times a specified value appears in the string.
print(x) # starts from 0 to end of the string

#Encode
print()
print('encode')
txt = "My name is Ståle"
x = txt.encode() # method encodes the string, using the specified encoding. If no encoding is specified, UTF-8 will be used.
print(x)

#endswith()
print()
print('endswith')
txt = 'My name is Temirbolat. I like watching Anime!'
x = txt.endswith('!') # Returns true if the string ends with the specified value
print(x) # string.endswith(value, start, end)

#extandtabs
print()
print('extandtabs')
txt = 'My\tname\tis\tTemirbolat'
x = txt.expandtabs(1) # method sets the tab size to the specified number of whitespaces.
print(x) # A number specifying the tabsize. Default tabsize is 8

#find # is almost the same as the index()
print()
print('find')
txt = 'My name is Temirbolat. I live in Karagandy'
x = txt.find('Karagandy',0,len(txt)) # method finds the first occurrence of the specified value.
print(x) # method returns -1 if the value is not found.

#format
print()
print('format')
print('I am {1}. I have {0} sisters'.format(2,20)) #Formats specified values in a string

#format_map
print()
print('format_map')
a = {'x':'John', 'y':'Wick'} # input stored in variable a. 
print("{x}'s last name is {y}".format_map(a)) # Returns key's values of the input dictionary.

#index
print()
print('index')
txt = 'My name is Temirbolat.'
x = txt.index('.',0,len(txt)) # finds the first occurrence of the specified value.
print(x) # raises an exception if the value is not found.

#isalnum
print()
print('isalnum')
txt = 'MyNameIsTemirbolat' # method returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9).
print(txt.isalnum())

#isalpha
print()
print('isalpha')
txt = 'IHave3Brothers'
print(txt.isalpha()) # returns True if all the characters are alphabet letters (a-z).

#isdecimal
print()
print('isdecimal')
txt = 'text'
numb = '034'
print(txt.isdecimal()) # returns True if all the characters are decimals (0-9)
print(numb.isdecimal())

#isdigit
print()
print('isdigit')
txt = 'low228'
numb = '228'
print(txt.isdigit()) # returns True if all the characters are digits, otherwise False.
print(numb.isdigit()) # Exponents, are also considered to be a digit.

#isidentifier
print()
print('isidentifier')
txt = 'Hello_world'
text = 'Hollat_229 '
print(txt.isidentifier()) #if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_).
print(text.isidentifier()) # cannot start with a number, or contain any spaces.

#islower
print() 
print('islower')
txt = 'holla_229' # returns True if all the characters are in lower case, otherwise False.
print(txt.islower())

#isnumeric
print()
print('isnumeric')
txt = '2323' #returns True if all the characters are numeric (0-9), otherwise False.
print(txt.isnumeric())

#isprintable
print()
print('isprintable')
txt = 'My name is \t Temirbolat' # none printable character can be carriage return and line feed.
text = ' Hello \n Guys'
print(txt.isprintable(),text.isprintable())

#isspace
print()
print('isSpace')
txt = "   " 
text = '    s   '
print(txt.isspace(),text.isspace()) # returns True if all the characters in a string are whitespaces

#isTitle
print()
print('istitle')
text = 'HELLO'
txt = ' !Hello229'
print(text.istitle(),txt.istitle()) #returns True if all words in a text start with a upper case letter, AND the rest of the word are lower case letters

#isupper
print()
print('isupper')
txt = 'HELLO '
text = 'HELLo WORLD'
print(txt.isupper(),text.isupper()) # returns True if all the characters are in upper case

#ljust
print()
print('ljust')
txt = 'hello'
print(txt.ljust(10,'X'), 'That\'s a methond') # Returen complete word where 10 is total length including txt and the rest is filled by X letters

#lower
print()
print('lower')
txt = 'Hello Friends'
print(txt.lower()) # converts everything into lower characters

#lstrip
print()
print('lstrip')
txt = ',.waHello      World'
print(txt.lstrip('.,aw')) # return a string. It deletes all the characters one by one starting from the left which are pointed at the function

#maketrans
print()
print('maketrans')
txt = "Hay Sam!"
x = "mSa"
y = "eJo"
mytable = txt.maketrans(x, y) # third parameter in the mapping table (Maketrans) describes characters that you want to remove from the string 
print(txt.translate(mytable)) # используется вместе с translate. Он хранит прям как буквы стоят друг под другом. Т.е вместо всех *a* будет 'o'

#partition
print()
print('partition')
txt = "I could eat bananas during the day"
# return a tuple with three elements:
# 1 - everything before the "match"
# 2 - the "match"
# 3 - everything after the "match"
x = txt.partition("bananas")
print(x)

#replace
print()
print('replace')
txt = 'The apples are so good, apples have lots of vitamins , apples are the best' # Default is all occurrences
print(txt.replace('apples','pineapples',2)) # Replace the two first occurrence of the word "apples"