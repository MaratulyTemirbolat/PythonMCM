
#Dictionary

#clear
print()
print('Clear')

universities = {
	'KBTU':"Almaty",
	'SDU': "Almaty",
	'KGU':"Karagandy"
}
universities.clear()
print(universities)

#copy
print()
print('Copy')
universities = {
	'KBTU':"Almaty",
	'SDU': "Almaty",
	'KGU':"Karagandy"
}
universities_copy = universities.copy()
print(universities_copy)

#fromkeys
print()
print('fromkeys')

almaty_keys = ('SDU','KBTU','KIMEP')

new_dictionary = dict.fromkeys(almaty_keys,'Almaty') #returns a dictionary with the specified keys and the specified value.
print(new_dictionary)

#get()
print()
print('get')

universities = {
	'KBTU':"Almaty",
	'SDU': "Almaty",
	'KGU':"Karagandy"
}

print(universities.get('KBTU')) # returns the value of the item with the specified key.

#items()
print()
print('items')

marks = {
	'Toyota':'Japan',
	'Lada':'Russia',
	'BMW':'Germany'
}

x = marks.items() # returns a view object. The view object contains the key-value pairs of the dictionary, as tuples in a list.
print(x)			# If there is any changes in origin Dictionary, then in marks they will be too
marks['Toyota'] = 'JPN'
print(x)

#keys()
print()
print('keys')

marks = {
	'Toyota':'Japan',
	'Lada':'Russia',
	'BMW':'Germany'
}

x = marks.keys()

print(x)
marks['Toyota'] = 'Turkish' #  method returns a view object. The view object contains the keys of the dictionary, as a list.
print(x) # THE CHANGES WILL NOT BE REFLECTED

#pop
print()
print('Pop')

marks = {
	'Toyota':'Japan',
	'Lada':'Russia',
	'BMW':'Germany'
}

x = marks.pop('Toyota','Japan') # value of the removed item is the return value

print(x)

#popitem()
print()
print('popitem')

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.popitem() # removes the item that was last inserted into the dictionary

print(car) # removed item is the return value, as a tuple.

#setdefault
print()
print('setdefault')

cities = {
	"Karagandy":"Kazakhstan",
	"Moscow":"Russia",
	"Toronto":"Canada"
}

x = cities.setdefault('Vancouver','Canada')
y = cities.setdefault('Toronto','USA')

print(cities)

#update()
print()
print('update')
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.update({'creator':'Thomas'}) # inserts the specified items to the dictionary.
print(car) # can be a dictionary, or an iterable object with key value pairs

#values
print()
print('values')

cities = {
	"Karagandy":"Kazakhstan",
	"Moscow":"Russia",
	"Toronto":"Canada"
}

countries = cities.values() # returns a view object. The view object contains the values of the dictionary, as a list.

print(countries) # THE CHANGES WILL BE REFLECTED