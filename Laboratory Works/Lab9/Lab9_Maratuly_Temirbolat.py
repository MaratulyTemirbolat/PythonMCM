class MyTime:
	second = 0
	minute = 0
	hour = 0
	def __init__(self,hour,minute,second):
		self.second = second
		self.minute = minute
		self.hour = hour
	def convertToSeconds(self):
		self.hour = int(self.second/3600)
		self.second = self.second%3600
		self.minute = int(self.second/60)
		self.second = self.second%60
		print("HH:{} MM:{} SS:{}".format(self.hour,self.minute,self.second))
	def convertToMinutes(self):
		self.minute = self.minute + (self.hour * 60)
		self.minute = self.minute + (int(self.second /60))
		print("MM:".format(self.minute))

class AnalogTime(MyTime):
 	def __init__(self,hour,minute,second):
 		super().__init__(hour,minute,second)
 	def showAnalogTime(self):
 		if self.hour>12:
 			self.hour = self.hour-12
 		print(self.hour + ":" +self.minute + ":" + self.second)
 	def showAmericanTime(self):
 		if self.hour > 12:
 			print(self.hour - 12 + ":" + self.minute + ":" + self.second + "p.m.")
 		else:
 			print(self.hour + ":" + self.minute + ":" + self.second + "a.m.")

def main():
	anTime = AnalogTime(10,12,1)
	anTime.convertToSeconds()
	anTime.convertToMinutes()
	anTime2 = AnalogTime(23,12,2)
	anTime2.showAnalogTime()
	anTime2.showAmericanTime()