def convert_to_celsius(fahrenheit_temperatures):
	celsius_temperature = (fahrenheit_temperatures - 32) * 5/9
	return celsius_temperature
def main():
	fahrenheit_temperatures = float(input('Please, type the temperature in Fahrenheit: '))
	celsius_temperature = convert_to_celsius(fahrenheit_temperatures)
	print('Conversion from {} Fahrenheit to Celsius is {} '.format(fahrenheit_temperatures,celsius_temperature))
main()