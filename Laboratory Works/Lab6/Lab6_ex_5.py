def convert_seconds(seconds_number):
	initial_number = seconds_number
	hours = int(seconds_number/3600)
	seconds_number = seconds_number%3600

	minutes = int(seconds_number/60)
	seconds_number = seconds_number%60
	return (initial_number,hours,minutes,seconds_number)

def main():
	seconds_number = int(input('Please, type the number of seconds: '))
	(initial_number,hours,minutes,seconds_number) = convert_seconds(seconds_number)
	print("{} = H:{} M:{} S:{}".format(initial_number,hours,minutes,seconds_number))
main()