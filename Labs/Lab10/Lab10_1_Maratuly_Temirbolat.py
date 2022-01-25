def getPositiveOddNumbers(myList):
	newList = [number for number in myList if number%2 !=0 and number>0]
	return newList

def convertToPositiveNumbers(myList):
	newList = [number if number>0 else (-1)*number for number in myList]
	return newList

def getNumberOfPositiveOddNumbers(myList):
	newList = [number for number in myList if number%2!=0 and number>0]
	return len(newList)

def getAverageNumber(myList):
	newList = [number for number in myList]
	total = sum(newList)
	amount = len(newList)
	return int(total/amount)

def getPositiveAverageNumber(myList):
	newList = [number for number in myList if number>=0]
	total = sum(newList)
	amount = len(newList)
	return int(total/amount)

def getAverageNumberPositiveNegative(myList):
	newListPositive = [number for number in myList if number>=0]
	totalPositive = sum(newListPositive)
	amountPositive = len(newListPositive)
	newListNegative = [number for number in myList if number<0]
	totalNegative = sum(newListNegative)
	amountNegative = len(newListNegative)
	averageNegative = int(totalNegative/amountNegative)
	averagePositive = int(totalPositive/amountPositive)
	return averagePositive,averageNegative

def replaceNegToZero(myList):
	newList = [number if number >= 0 else 0 for number in myList ]
	return newList


myList = [4,-5,3,-2,0,10,-4,7,1]
list1 = getPositiveOddNumbers(myList)
list2 = convertToPositiveNumbers(myList)
numberOfPositiveOddNumbers = getNumberOfPositiveOddNumbers(myList)
averageNumber = getAverageNumber(myList)
positiveAverageNumber = getPositiveAverageNumber(myList)
averageNumberPosNeg = getAverageNumberPositiveNegative(myList)
list3 = replaceNegToZero(myList)

print('myList : ',myList)
print('list1 : ',list1)
print('list2 : ',list2)
print('numberOfPositiveOddNumbers : ',numberOfPositiveOddNumbers)
print('averageNumber : ',averageNumber)
print('positiveAverageNumber : ',positiveAverageNumber)
print('averageNumberPosNeg : ',averageNumberPosNeg)
print('list3 : ',list3)