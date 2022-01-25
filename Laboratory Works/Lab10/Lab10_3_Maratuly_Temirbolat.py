def generateFibonacci(number):
	myList = []
	myList.append(1)
	myList.append(1)
	[myList.append(myList[k-1] + myList[k-2]) for k in range(2,number) ]
	myList = [num for num in myList if num <= number]
	return myList
	

number = int(input('Please, type the number: '))
fibList = generateFibonacci(number)
print(fibList)