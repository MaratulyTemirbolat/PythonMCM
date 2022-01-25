from math import *
def calculate_distance(x1,x2,y1,y2):
	d = sqrt((x2-x1)**2 + (y2 - y1)**2)
	return d
def main():
	x1 = float(input('Please,type the point  X1 = '))
	x2 = float(input('Please,type the point  X2 = '))
	y1 = float(input('Please,type the point  Y1 = '))
	y2 = float(input('Please,type the point  Y2 = '))
	d = calculate_distance(x1,x2,y1,y2)
	print ('The distance between points is ' + str(d))
main()