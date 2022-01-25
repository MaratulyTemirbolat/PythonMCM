#LIST

#append
print('Append')  # add an element to the end of the list.
subjects = ['PP1','Calc1','Physics1']
subjects.append('Art')
print(subjects)

#clear
print()
print('clear') # removes all the elements from a list.
marks = [1,5,3]
print(marks)
marks.clear()
print(marks)

#copy
print()
print('copy') #returns a copy of the specified list.
x = subjects.copy()
print(x)

#count
print()
print('count') # returns the number of appearing the value in the list
marks = ['Honda','Toyota','BMW','Toyota']
print(marks.count('Toyota'))

#extend
print()
print('extend') #  adds the specified list elements (or any iterable) to the end of the current list
subjects.extend(marks)
print(subjects)

#index
print()
print('index') # returns the position at the first occurrence of the specified value.
numbers = [3,2,5,1,2,4]
print(numbers.index(2))

#insert
print()
print('insert') # inserts the specified value at the specified position.
numbers.insert(6,'letter')
print(numbers)

#pop
print()
print('pop') # removes the element at the specified position.
numbers.pop(len(numbers)-1) # default is -1 that means last element
print(numbers)

#remove
print()
print('remove') # removes the first occurence of the element in the list
bands = ['C','B1','B2','A2','B1']
bands.remove('B1')
print(bands)

#reverse
print()
print('reverse')
numbers = [1,2,3,4,5]
numbers.reverse()
print(numbers)

#sorts
print()
print('sorts') # sorts the list ascending by default.
marks.sort(reverse = True) #list.sort(reverse=True|False, key=myFunc)
print(marks)