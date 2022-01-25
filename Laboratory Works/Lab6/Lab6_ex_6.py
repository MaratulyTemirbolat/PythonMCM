def calculate_remaining(remaining_money):
	cnt_fifty = int(remaining_money/50)
	remaining_money = remaining_money%50

	cnt_twenty =  int(remaining_money/20)
	remaining_money = remaining_money%20

	cnt_ten = int(remaining_money/10)
	remaining_money = remaining_money%10

	cnt_five = int(remaining_money/5)
	remaining_money = remaining_money%5

	cnt_two = int(remaining_money/2)
	remaining_money = remaining_money%2
	return (cnt_fifty,cnt_twenty,cnt_ten,cnt_five,cnt_two,remaining_money)
def main():
	money_cents = int(input('Please,type the input money to the machine in cents: '))
	item_price = int(input('Please,type the price of the item int cents: '))
	remaining_money = money_cents - item_price
	(cnt_fifty,cnt_twenty,cnt_ten,cnt_five,cnt_two,remaining_money) = calculate_remaining(remaining_money)
	print('Number of 50 cent coins : ' + str(cnt_fifty))
	print('Number of 20 cent coins : ' + str(cnt_twenty))
	print('Number of 10 cent coins : ' + str(cnt_ten))
	print('Number of 5 cent coins : ' + str(cnt_five))
	print('Number of 2 cent coins : ' + str(cnt_two))
	print('Number of 1 cent coins : ' + str(remaining_money))
main()