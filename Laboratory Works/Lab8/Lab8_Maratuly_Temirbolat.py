class MyTime:
	hour = 0
	minute = 0
	second = 0
	def __init__(self,second):
		self.second = second

	def defineTime(self):
		self.hour = int(self.second/3600)
		self.second = self.second%3600
		self.minute = int(self.second/60)
		self.second = self.second%60
		print("HH:{} MM:{} SS:{}".format(self.hour,self.minute,self.second))


	def setSeconds(self,second):
		self.second = second

	def returnSeconds(self):
		return self.second
time1 = MyTime(3650)
time1.defineTime()