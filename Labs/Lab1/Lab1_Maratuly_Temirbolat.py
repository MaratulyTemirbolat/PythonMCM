# Exercise 1
print('Exercise 1')
a = 1
print('(a+1)**5 = ' , (a+1)**5) # (a+1)**5 =  32
print()

# Exercise 2
print('Exercise 2')
users_astana= 4900
revenue_astana = 63000
users_almapb = 3500
revenue_almapb = 48000
arru_astana = revenue_astana/users_astana
arru_almaty = revenue_almapb/users_almapb
print('Average revenue for Astana = ',round(arru_astana,2), 'Average revenue for Almaty = ', round(arru_almaty,2))  # Average revenue for Astana =  12.86 Average revenue for Almaty =  13.71
print()

# Exercise 3
print('Exercise 3')
project_name = 'Python для анализа данных'
print('Название курса ' + project_name)  # Название курса Python для анализа данных
print()

# Exercise 4
print('Exercise 4')
print('Значение ARPU пользователей Астаны равно ' + str(arru_astana)) # Значение ARPU пользователей Астаны равно 12.857142857142858

# Exercise 5
print('Exercise 5')
print('Астана: пользователей {}, выручка {} тенге, ARPU {}'.format(users_astana,revenue_astana,arru_astana)) # Астана: пользователей 4900, выручка 63000 тенге, ARPU 12.857142857142858
print()

# Exercise 6
print('Exercise 6')
print('Алматы: пользователей {}, выручка {} тенге, ARPU {:.4f}'.format(users_almapb,revenue_almapb,arru_almaty)) # Алматы: пользователей 3500, выручка 48000 тенге, ARPU 13.7143
print()

#Exercise 7
print('Exercise 7')
aa = 1
b = 2
print(a==b) # False
print()

#Exercise 8
print('Exercise 8')
float(arru_almaty)/float(arru_astana)
print(arru_almaty - arru_astana)
print(arru_almaty>arru_astana)  # 0.8571428571428559
								# True