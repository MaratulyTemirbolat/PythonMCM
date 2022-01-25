import re
f = open('C:/Users/temir/OneDrive/Рабочий стол/KBTU/Programming on Python/Labs/Lab7/NewFile.txt','a')

number = input("Please, type the number: ")
numbReg = "^[0-9]*$"
numberChecking = re.search(numbReg,number)
if str(numberChecking) != 'None':
	f.write('Number: ' + number )
else:
	f.write('Number: None')
f.write('\n')

firstLastName = input("Please,type the First Name and Last Name: ")
fullNameReg = "^[A-Z][a-z]+ [A-Z][a-z]+"
fullNameChecking = re.search(fullNameReg,firstLastName)
if str(fullNameChecking) != 'None':
	f.write('First name Last name: ' + firstLastName)
else:
	f.write('First name Last name: None')
f.write('\n')

dateOfBirth = input("Please, type the date of birth in a format dd/mm/yyyy : ")
dateReg = "^(([0][1-9])|([1-2][0-9])|([3][0-1]))/(([0][1-9])|([1][0-2]))/(([1][0-9][0-9][0-9])|([2][0][0-2][0-1]))$"
dateChecking = re.search(dateReg,dateOfBirth)
if str(dateChecking) != 'None':
	f.write('Date of birth: ' + dateOfBirth)
else:
	f.write('Date of birth: None')
f.write('\n')

email = input('Please, type the email: ')
emailReg = "^[a-z][a-zA-Z0-9]+@[a-z]+[.][a-z]+$"
emailChecking = re.search(emailReg,email)
if str(emailChecking) != 'None':
	f.write('Email: '+email)
else:
	f.write('Email: None')
f.write('\n')

mobileNumber = input('Please, type the mobile number: ')
mobileNumberReg = "^[+]7[(]7(([0][0-9])|(47)|(7[15678]))[)][0-9][0-9][0-9][-][0-9][0-9][-][0-9][0-9]$"
mobNumberChecking = re.search(mobileNumberReg,mobileNumber)
if str(mobNumberChecking) != 'None':
	f.write('Mobile number: ' + mobileNumber)
else:
	f.write('Mobile number: None')
f.write('\n')

iban = input('Please, type the IBAN: ')
ibanReg = "^KZ[0-9]{20}$"
ibanChecking = re.search(ibanReg,iban)
if str(ibanChecking) != 'None':
	f.write('IBAN: '+ iban)
else:
	f.write('IBAN: None')
f.write('\n')

f.close()