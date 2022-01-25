def calculate_circle_part(radius):
	diameter = 2*radius
	circumference = 3.14159*diameter
	area = 3.14159*radius*radius
	return (diameter,circumference,area)
def main():
	radius = float(input('Please, type the radius of the circle: '))
	(diameter,circumference,area) = calculate_circle_part(radius)
	print('The diameter = {}, circumference = {}, area = {} '. format(diameter,circumference,area))
main()