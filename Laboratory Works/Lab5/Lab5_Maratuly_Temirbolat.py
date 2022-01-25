#Exercise 1
print('Exercise 1')
with open('C:/Users/temir/OneDrive/Рабочий стол/KBTU/Programming on Python/Labs/Lab5/user_ids.txt','r') as f:
		for line in f:
			print(line.strip())

#Exercise 2
user_ids = []
with open('C:/Users/temir/OneDrive/Рабочий стол/KBTU/Programming on Python/Labs/Lab5/user_ids.txt','r') as f:
		for line in f:
			user_id = line.strip()
			user_ids.append(user_id)

print(user_ids[:5])
print(user_ids[4])

#Exercise 3
print(len(user_ids))
unique_user_ids = set(user_ids)
print('The unique ID number in the file {} '.format(len(unique_user_ids)))

#Exercise 4
with open('C:/Users/temir/OneDrive/Рабочий стол/KBTU/Programming on Python/Labs/Lab5/user_ids_header.txt','r') as f:
	for line in f:
		print(line.strip())   # The first row is user_id

#Exercise 5
print()
print('Exercise 5')
started = True
with open('C:/Users/temir/OneDrive/Рабочий стол/KBTU/Programming on Python/Labs/Lab5/user_ids_header.txt','r') as f:
	for line in f:
		if started == True:
			started = False
		else:
			print(line.strip())
#Exercise 6
print()
print('Exercise 6')
with open('data_3_columns.txt','r') as f:
	for line in f:
		line = line.strip().split('\t')
		print(line)
#Exercise 7
print()
print('Exercise 7')
with open('data_3_columns.txt','r') as f:
	for line in f:
		line = line.strip().split('\t')
		medium = line[0]
		source = line[1]
		amount_paid = float(line[2].replace(',','.'))
		print(source,medium,amount_paid)

#Exercise 8
print()
print('Exercise 8')
total_sum = 0
with open('data_3_columns.txt','r') as f:
	for line in f:
		line = line.strip().split('\t')
		amount_paid = float(line[2].replace(',','.'))
		total_sum+=amount_paid
		print('Текущая сумма расходов: {:.2f}'.format(total_sum))
print('The sum for the last time is {:.2f}'.format(total_sum))

#Exercise 9
print()
print('Exercise 9')
total_sum = 0
with open('data_3_columns.txt','r') as f:
	for line in f:
		line = line.strip().split('\t')
		medium = line[0]
		source = line[1]
		amount_paid = float(line[2].replace(',','.'))
		if source == 'yandex' and medium =='seo':
			total_sum+=amount_paid
			print(medium + ' ' + source +' ' +'Текущая сумма расходов: {:.2f}'.format(total_sum))