import Database
import pickle
import sys
import time


def management_model():
	print('\n\nManagement Model')

	while True:
		print('\n\n-----------------------------')
		print('1: Calculator Information')
		print('2: Account and Password')
		print('3: Command Line')
		print('4: Exit Management Model')
		print('5: Exit Calculator')

		choose = input('\nPlease choose pattern:')

		if choose is None:
			print('Please write right number!')
			continue

		if choose == '1':
			print('\n\n~~~~~~~~~~~~~~~~~~~~~~')
			print('Calculator Information')
			print('\nSimple and Pure')
			print('This is Calculator.')
			print('We stick to the simple and pure original heart.')
			print('Our goal is to create a convenient and fast computing experience.')
			input("\nPlease press 'Enter' to continue")

		if choose == '2':
			print('\n\n~~~~~~~~~~~~~~~~~~~~~~')
			print('Account and Password')
			try:
				with open('Data.cal', 'rb+') as open_file:
					data = pickle.load(open_file)
					open_file.close()
				pass
			except EOFError:
				Database.save_data()
				with open('Data.cal', 'rb+') as open_file:
					data = pickle.load(open_file)
					open_file.close()
			except FileNotFoundError:
				Database.create_data()
				Database.save_data()
				with open('Data.cal', 'rb+') as open_file:
					data = pickle.load(open_file)
					open_file.close()
			while True:
				data['Administrator'] = '8764438675876'
				print()
				print('\n', data)
				print("\nPS: 1. 'Administrator' can not be changed！")
				print('    2. All changes will be saved when you exit this item, if you forcibly exit the program halfway, '
				      'the changes will be invalid！')
				print('\n1: Delete')
				print('2: Add')
				print('3: Reset')
				print('4: Exit')
				choose_account = input('\nPlease choose:')
				if choose_account == '1':
					while True:
						delete_account = input('\nPlease write which account you want to delete:')
						try:
							data.pop(delete_account)
							print('Successfully delete!')
							break
						except KeyError:
							print("We can't find this account!\nPlease try again!")
							continue
					continue
				if choose_account == '2':
					add_account = input('\nPlease write which account you want to add:')
					add_account_password = input('Please write your password of this account:')
					data[add_account] = add_account_password
					print('Successfully add!')
					continue
				if choose_account == '3':
					while True:
						reset_account = input('\nPlease write which account you want to reset:')
						if reset_account in data:
							reset_account_password = input('Please write your new password of this account:')
							data[reset_account] = reset_account_password
							print('Successfully reset!')
							break
						else:
							print('\nPlease write right account!')
							continue
					continue
				if choose_account == '4':
					break
				else:
					print('\nPlease write right number!')

			with open('Data.cal', 'wb+') as save_file:
				pickle.dump(data, save_file)
				save_file.close()
			print('\nSuccessfully saved all of the setting!')

		if choose == '3':
			print("\nPS: You can input 'exit' to exit!")
			print("You can only enter an executable Python command or internal command!\n")
			while True:
				number = input('Calculator > ')
				try:
					if number == 'exit':
						break
					# here will be used to add API
					result = eval(number)
					print(result, '\n')
					continue
				except:
					print('Please input right command!\n')
					continue
			continue

		if choose == '4':
			return

		if choose == '5':
			print('\nCalculator will exit 2 seconds later!')
			time.sleep(2)
			sys.exit()

		else:
			print('\nPlease write right number!')
			continue
