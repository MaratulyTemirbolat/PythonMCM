class NotCorrectSignException(Exception):
	def __init__(self):
		super().__init__()
	""" Raised when the the sign is not available"""

try:
	numberOne = int(input('Please,type the first number: '))
	numberTwo = int(input('Please,type the second number: '))
	sign = input('Please, type the operation: ')
	#myList = int([numberOne,numberTwo]) # My checking
	if (sign == '+'):
		print(numberOne + numberTwo)
	elif(sign == '-'):
		print(numberOne - numberTwo)
	elif(sign == '*'):
		print(numberOne - numberTwo)
	elif(sign == '/'):
		print(numberOne/numberTwo)
	elif(sign == '%'):
		print(numberOne%numberTwo)
	else:
		raise NotCorrectSignException()
except TypeError:
	print('Sorry, but the operand doesn\'t have correct type ')
except ValueError:
	print('Sorry, but the value is illegal')
except ZeroDivisionError:
	print('DIVISION BY ZERO IS IMPOSSIBLE')
except NotCorrectSignException:
	print('Wrong sighn is enterred!')
except:
	print('Unexpected Problem appeared!')
else:
	print('No Problems! The work finished successfully!')
finally:
	print('Good Buy !')