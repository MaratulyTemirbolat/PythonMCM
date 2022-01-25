# Create a new class and named it MyListClass. In the class define following:
# a) data fields(attributes, properties) with int data type for a list.
# b) constructor that initialize this list;
# c) methods for getting a max/min value, same numbers of the list and its count(the return data must be int list);
# e) method for getting sum of the list

class MyListClass:
	def __init__(self, myList):
		self.myList = myList

	def getMaxValue(self):
		maxNumber = -9999999
		for number in self.myList:
			if number>maxNumber:
				maxNumber = number
		return maxNumber
	def getMinValue(self):
		minNumber = 999999
		for number in self.myList:
			if number<minNumber:
				minNumber = number
		return minNumber
	def sameNumbersList(self):
		myDict = dict()
		for number in self.myList:
			myDict[str(number)] = 0
		for number in self.myList:
			myDict[str(number)] +=1
		resList = []
		for key in myDict:
			for value in range(myDict[key]):
				if myDict[key]>1:
					resList.append(key);
		return resList;

	def getSumOfTheList(self):
		sumNumbers = 0
		for number in self.myList:
			sumNumbers = sumNumbers + number
		return sumNumbers

myL = []

number = int(input('Type, the number: '))

while number!=0:
	myL.append(number)
	number = int(input('Type,the number: '))
	
myNewList = MyListClass(myL)

print(myNewList.getMaxValue())
print(myNewList.getMinValue())
print(myNewList.getSumOfTheList())
print(myNewList.sameNumbersList())