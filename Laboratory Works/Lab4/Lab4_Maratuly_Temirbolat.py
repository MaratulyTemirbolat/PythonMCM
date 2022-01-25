from math import *
#Exercise 1
print('Exercise 1')
x = 7 + 3 * 6/2-1
print('7 + 3 * 6/2-1 = ' + str(x))
x = (3 * 9 * (3 + (4*5/3)))
print('(3 * 9 * (3 + (4*5/3))) = ' + str(x))
x = 12.0 + 2/5 * 10.0
print('12.0 + 2/5 * 10.0 = ' + str(x))
x = 2/5 + 10.0*3 - 2.5
print('2/5 + 10.0*3 - 2.5 = '+ str(x))

#Exercise 2
print('Exercise 2')
fahrenheit_temperatures = float(input('Please, type the temperature in Fahrenheit: '))
celsius_temperature = (fahrenheit_temperatures - 32) * 5/9
print('Conversion from {} Fahrenheit to Celsius is {} '.format(fahrenheit_temperatures,celsius_temperature))

#Exercise 3
print('Exercise 3')
radius = float(input('Please, type the radius of the circle: '))
diameter = 2*radius
circumference = 3.14159*diameter
area = 3.14159*radius*radius
print('The diameter = {}, circumference = {}, area = {} '. format(diameter,circumference,area))

#Exercise 4
print('Exercise 4')
x1 = float(input('Please,type the point  X1 = '))
x2 = float(input('Please,type the point  X2 = '))
y1 = float(input('Please,type the point  Y1 = '))
y2 = float(input('Please,type the point  Y2 = '))

d = sqrt((x2-x1)**2 + (y2 - y1)**2)

print ('The distance between points is ' + str(d))

#Exercise 5
print('Exercise 5')
seconds_number = int(input('Please, type the number of seconds: '))
initial_number = seconds_number
hours = int(seconds_number/3600)
seconds_number = seconds_number%3600

minutes = int(seconds_number/60)
seconds_number = seconds_number%60

print("{} = H:{} M:{} S:{}".format(initial_number,hours,minutes,seconds_number))

#Exercise 6
print('Exercise 6')
money_cents = int(input('Please,type the input money to the machine in cents: '))
item_price = int(input('Please,type the price of the item int cents: '))
remaining_money = money_cents - item_price

cnt_fifty = int(remaining_money/50)
remaining_money = remaining_money%50

cnt_twenty =  int(remaining_money/20)
remaining_money = remaining_money%20

cnt_ten = int(remaining_money/10)
remaining_money = remaining_money%10

cnt_five = int(remaining_money/5)
remaining_money = remaining_money%5

cnt_two = int(remaining_money/2)
remaining_money = remaining_money%2

print('Number of 50 cent coins : ' + str(cnt_fifty))
print('Number of 20 cent coins : ' + str(cnt_twenty))
print('Number of 10 cent coins : ' + str(cnt_ten))
print('Number of 5 cent coins : ' + str(cnt_five))
print('Number of 2 cent coins : ' + str(cnt_two))
print('Number of 1 cent coins : ' + str(remaining_money))