#Sets

#Add
print('add')
marks = {'Toyota','Honda','Mazda','Lexus'}
marks.add('Subaru') # If the element already exists, the add() method does not add the element.
print(marks) 

#clear
print()
print('clear') 
furniture = {'sofa','chair','armchair','table'}
print(furniture)
furniture.clear() # removes all elements in a set.
print(furniture)

# copy
print()
print('copy') # method copies the set.
marks = {'Toyota','Honda','Mazda','Lexus'}
marks_copy = marks.copy()
print(marks_copy)

# difference
print()
print('difference')
marks_2 = {'Mercedes','BWM','Subaru','Mazda'} 
print(marks.difference(marks_2)) #  Return a set that contains the items that only exist in set MARKS, and not in set MARKS_2:

#difference_update
print()
print('difference_update')
marks.difference_update(marks_2) # method removes the items in MARKS that exist in both sets. 
print(marks)
print(marks_2)

#discard
print()
print('discard') # method is different from the remove() because remove can show error
subjects = {'Math','Math','Programming','Physics','PP2'}
print(subjects)
subjects.discard('Math') # method removes the specified item from the set.
print(subjects) 

#intersection
print()
print('intersection')
subjects2 = {'PP2','Art','PP1'}
print(subjects.intersection(subjects2)) # returns a set that contains the similarity between two or more sets.

#intersection_update
print()
print('intersection_update')
subjects.intersection_update(subjects2) # removes the items that is not present in both sets 
print(subjects)

#isdisjoint
print()
print('isdisjoint')
subjects = {'Math','Math','Programming','Physics','PP2'}
marks_2 = {'Mercedes','BWM','Subaru','Mazda','PP2'} 
print(subjects.isdisjoint(marks_2)) # returns True if NO ANY items in set MARKS_2 is present in SUBJECTS

#issubset
print()
print('issubset')
marks_2 = {'Mercedes','BWM','Subaru','Mazda','PP2'} 
print(marks_2.issubset(subjects)) # returns True if ALL the item of MARKS_2 are in SUBJECTS

#issuperset
print()
print('issuperset')
print(marks_2.issuperset(subjects)) # returns True if ALL the item of SUBJECTs are in MARKS_2

#pop
print()
print('pop')
marks_2 = {'Mercedes','BWM','Subaru','Mazda','PP2'} 
marks_2.pop() # removes a random item from the set.
print(marks_2) # method returns the removed item.

#remove
print()
print('remove')
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana") # removes the specified element from the set.
print(fruits) # method will raise an error if the specified item does not exist

#symmetric_difference
print()
print('symmetric_difference')
x = {"apple", "banana", "cherry"}  
y = {"google", "microsoft", "apple"}
print(x.symmetric_difference(y)) # Возвратит сет, где будут все элементы, кроме общих

#symmetric_difference_update
print()
print('symmetric_difference_update')
x.symmetric_difference_update(y) # Удалит Элементы в X, которые являются общими и добавит те, которые не общие
print(x)

#union
print()
print('union')
universities_kz = {'KBTU','SDU','KAZNU'}
universities_CND = {'UVIC','UT','UC'}
print(universities_kz.union(universities_CND)) #Return a set that contains all items from both sets, duplicates are excluded:

#update
print()
print('update')
universities_kz = {'KBTU','SDU','KAZNU'}
universities_CND = {'UVIC','UT','UC'}
universities_kz.update(universities_CND)
print(universities_kz) # updates the current set, by adding items from another set.