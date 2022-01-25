def calculateSum(number):
	myList = [number+1 for number in range(number)]
	return sum(myList)

number = int(input('Please,type the number of n: '))
total = calculateSum(number)	
print(total)