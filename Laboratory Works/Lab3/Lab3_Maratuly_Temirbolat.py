print(list(range(10)))

print(range(0,10))

print(range(0,10,2))

number_list = list(range(19)) # In Python 3.x range is a iterator. So, you need to convert it to a list
print(number_list)

for i in range(101):
	print(i)


weekdays = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье'] 

for day in weekdays:
	print('Сегодня {}'.format(day)) 

direct_revenue = [83171,151604, 46315, 98753, 208648, 184682, 204061,134911,94791,109076,37254, 224991,36400,149320, 171336, 83854, 206799,180922, 235647, 217546, 200478, 239445, 144901, 26522,177971,148458,154937,196095,140202,189223] 
week_1_revenue = direct_revenue[:7]	#[83171, 151604, 46315, 98753, 208648, 184682, 204061]

myList = list(range(10))
result = 0
for element in myList:
	result+=element
print(result)

#Exercise 
total_revenue = 0
for day in week_1_revenue:
	total_revenue+= day
print(total_revenue)

#Exercise
step = 1
total_revenue = 0
for day in week_1_revenue:
	total_revenue+=day
	print('Значение element - {}, сумма на текущий момент - {}'.format(day, total_revenue))
	print('The step is {} the sum is {} '.format(step,total_revenue))
	step+=1

#Exercise
minValue = 4
maxValue = 18
#Step 1
list_num = list(range(minValue,maxValue+1))
print(list_num)

#Step 2
list_num = range(minValue,maxValue+1,2)
list_even = list_num[0::2]
print(list_even)
step_even = 1
for num in list_even:
	if step_even == len(list_even)-1:
		print('The penultimate number is {0} and its root is {1}'.format(num,num**0.5))
	else:
		print('The number {} the sqare root is {}'.format(num,num**0.5))
	step_even+=1

#Exercise
queriesList = "смотреть сериалы онлайн".split(' ')
print( queriesList )

#Exercise
cnt = 0
queriesText = 'смотреть сериалы онлайн;новости спорта;афиша кино;курс доллара;сериалы этим летом;курс по питону;сериалы про спорт'
queriesText = queriesText.split(';')
queriesText = ' '.join(queriesText)
print(queriesText)
for letter in queriesText:
	if(letter == ' '):
		cnt+=1
print('The number of words is '+ str(cnt+1))

#Exercise
vk_visitors = 1500
vk_orders = 14
facebook_visitors = 2200
facebook_orders = 17
if(facebook_orders/facebook_visitors < vk_orders/vk_visitors):
	print('Конверсия ВКонтакте выше')
else:
	print('Конверсия Facebook выше') 	# Конверсия ВКонтакте выше

#Exercise 
traffic_sources = ['прямой заход','яндекс','партнерка','вконтакте','инфопартнер'] 
for source in traffic_sources:
	if(source == 'нифопартнер' or source == 'прямой заход'):
		print('Это бесплатный переход')
	else:
		print('Это платный переход')
#
#Exercise
queries = "смотреть сериалы онлайн,новости спорта,афиша кино,курс доллара,сериалы этим летом,курс по питону,сериалы про спорт"
words = ['сериалы', 'курс']
queries = queries.split(',')
result = ''
for k in words:
	for j in queries:
		if k in j:
			result+=j+','
print(result)
result = result[0:len(result)-1] 
print(result)