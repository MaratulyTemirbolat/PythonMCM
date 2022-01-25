#Exercise 1
print('Exercise 1')
just_numbers = [2,1,5,4,3]
print(len(just_numbers)) # The length shows the number of elements in the list
						 # 5

print(sum(just_numbers)) # The sum of all elements(digits) of the list
print()					 # 15

#Exercise 2
print('Exercise 2')
print(sorted(just_numbers)) # The function 'sorted' sorts the list in increasing order and function 'print' has already showed the sorted list
							# [1, 2, 3, 4, 5]
							# Если элементы листа представляют собой слова, то сортировка будет происходить по алфавиту.

print(sorted(just_numbers,reverse = True)) # Do the same but here we sort in decreasing order
print()									   # [5, 4, 3, 2, 1]

#Exercise 3
print('Exercise 3')
words = ['один','два','три']			
print(sorted(words))						# ['два', 'один', 'три']
print() 

#Exercise 4
print('Exercise 4')
queries_string = "cмотреть сериалы онлайн,новости спорта,афиша кино,курс доллара,сериалы этим летом,курс по питону,сериалы про спорт"
print(queries_string.split(',')) # We obtain the list where all the elements are devided by ',' (comma)  and then just show as the list
print()							 # ['cмотреть сериалы онлайн', 'новости спорта', 'афиша кино', 'курс доллара', 'сериалы этим летом', 'курс по питону', 'сериалы про спорт']

#Exercise 5
print('Exercise 5')
file_string = "003_logs_2017-11-03;001_logs_2017-11-01;005_logs_2017-11-05;002_logs_2017-11-02;004_logs_2017-11-04" 
# A
print('Problem A')
file_string = file_string.split(';')
print(file_string)	# Answer: We can do it with the function "split"
print()				# ['003_logs_2017-11-03', '001_logs_2017-11-01', '005_logs_2017-11-05', '002_logs_2017-11-02', '004_logs_2017-11-04']
# B
print('Problem B')
file_list_sorted = sorted(file_string) # Answer: We can do it with file_list_sorted = sorted(file_list) 
print(file_list_sorted) 			   # ['001_logs_2017-11-01', '002_logs_2017-11-02', '003_logs_2017-11-03', '004_logs_2017-11-04', '005_logs_2017-11-05']
print()
# C
print('Problem C')
file_list_sorted.append('006_logs_2017-11-06')
print(file_list_sorted)   # Answer: ['001_logs_2017-11-01', '002_logs_2017-11-02', '003_logs_2017-11-03', '004_logs_2017-11-04', '005_logs_2017-11-05', '006_logs_2017-11-06']
print()					  

#Exercise 6
print('Exercise 6')
queriesList = [ 'смотреть сериалы онлайн', 'новости спорта', 'афиша кино', 'курс доллара', 'сериалы этим летом', 'курс по питону', 'сериалы про спорт' ] 
print(','.join(queriesList)) # The given function combines the provided list 'queriesList' into one string by the ','(comma)
							 # The result is смотреть сериалы онлайн,новости спорта,афиша кино,курс доллара,сериалы этим летом,курс по питону,сериалы про спорт
print()	

#Exercise 7
print('Exercise 7')
results = ['001_logs_2017-11-01', '002_logs_2017-11-02', '003_logs_2017-11-03', '004_logs_2017-11-04', '005_logs_2017-11-05', '006_logs_2017-11-06']
results = '||'.join(results)
print(results) # 001_logs_2017-11-01||002_logs_2017-11-02||003_logs_2017-11-03||004_logs_2017-11-04||005_logs_2017-11-05||006_logs_2017-11-06
print()

#Exercise 8
print('Exercise 8')
sequence = [ 'Google Adwords', 'Yandex Direct', 'Facebook', 'VK', 'Partner' ]
print(sequence[1])  # Yandex Direct
print()

#Exercise 9
print('Exercise 9')
print(sequence[0:3]) # ['Google Adwords', 'Yandex Direct', 'Facebook']
print()

#Exercise 10
print('Exercise 10')
print(sequence[:3]) # ['Google Adwords', 'Yandex Direct', 'Facebook']
print(sequence[0:3]) # ['Google Adwords', 'Yandex Direct', 'Facebook']
print()

#Exercise 11
print('Exercise 11')
sequence = [ 'Google Adwords', 'Yandex Direct', 'Facebook', 'VK', 'Partner' ] 
print(sequence[2:]) #['Facebook', 'VK', 'Partner']
print()

#Exercise 12
print('Exercise 12')
print(sequence[2:-1]) # ['Facebook', 'VK']
print(sequence[-3:4]) # ['Facebook', 'VK']

#Exercise 13
print('Exercise 13')
justNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
print(justNumbers[1::2]) # [2, 4, 6, 8, 10]

queriesList = [ 'смотреть сериалы онлайн', 'новости спорта', 'афиша кино', 'курс доллара', 'сериалы этим летом', 'курс по питону', 'сериалы про спорт' ]
queriesList += ['Hello World']
print(queriesList)