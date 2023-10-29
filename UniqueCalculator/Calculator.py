import time
import os
import sys
import pickle
import platform
import Function
import Database
import Management
import ZeroSolutionTool
import DataProcessing


# load
try:
	with open('Data.cal', 'rb+') as open_file:
		data = pickle.load(open_file)
		open_file.close()

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

except:
	print("\nThere are some problems!")
	print('Please try again!')
	time.sleep(5)

data['Administrator'] = 'zdthmxrynfnbr'


# enter main program
print('Calculator'.center(50, '='))


Username = input('\nUsername:')


# judge if "UserName" is none
while len(Username) == 0:
	Username = input('Username:')
	if len(Username) > 0:
		break
	else:
		continue

times = 5
while len(Username) > 0:

	Password = input('Password ( you have only ' + str(times) + ' times ):')

	# what times the user tried
	if int(times) == 1:
		print('\nYour password is wrong.\nCalculator will exit in 10 seconds!')
		time.sleep(10)
		sys.exit()
	else:
		pass

	# judge if "Password" is none
	if len(Password) == 0:
		continue

	if len(Password) > 0:
		if Username in data:
			if data[Username] == Password:
				break
			else:
				times = times - 1
				print('\nYour password is wrong!')
				continue
		else:
			print('\nSaving your information...\nPlease wait about 2 seconds...')
			data[Username] = Password
			# print(data)

			with open('Data.cal', 'wb+') as save_file:
				pickle.dump(data, save_file)
				save_file.close()
			time.sleep(2)
			print('Successfully saved!')
			break


if Username == 'Administrator':
	Administration = input('\nEntry the management model?[y/n]:')
	if Administration == 'y':
		Management.management_model()
	elif Administration == 'n':
		pass
	else:
		print('\nEntering user mode by default.')
else:
	pass


# welcome
print('\n\nHello,%s! Welcome to Calculator!' % Username)


# choose pattern
while True:
	print('\n\n-----------------------------')
	print('1: Version Information')
	print('2: Number (GUI by Microsoft Windows)')
	print('3: Number (Command Line)')
	print('4: Basic Functions of Middle School Mathematics')
	print('5: Zero Solution Tool')
	print('6: Experimental Data Processing')
	print('7: Exit')
	ChoosePattern = input('\nPlease choose pattern:')

	# version information
	if ChoosePattern == '1':
		print('\nVersion: 1.0.0')
		if platform.system() == 'Windows' or 'Linux':
			print('System :', platform.system())
		else:
			print('System : We cannot detect the current system.')
		input("\nPlease press 'Enter' to continue.")
		continue

	# entry windows calculator
	if ChoosePattern == '2':
		try:
			os.system('C:/WINDOWS/System32/calc.exe')
			continue
		except:
			print('\nMaybe there are some problems, please try again.')
			print('PS: Calculator only supports Microsoft Windows system now!')
			continue

	# entry calculation formula
	if ChoosePattern == '3':
		print("\nPS: You can input 'exit' to exit!\n")
		while True:
			number = input('Number > ')
			try:
				if number == 'exit':
					break
				result = eval(number)
				print(result, '\n')
				continue
			except:
				print('Please input right calculation formula!\n')
				continue
		continue

	# entry Function
	if ChoosePattern == '4':
		try:
			Function.main()
			continue
		except FileNotFoundError:
			print('\nMaybe there are some problems, please try again.')
			print('Error code: FileNotFoundError')
			continue

	# entry ZeroSolutionTool
	if ChoosePattern == '5':
		try:
			ZeroSolutionTool.zero_solution_tool()
			continue
		except FileNotFoundError:
			print('\nMaybe there are some problems, please try again.')
			print('Error code: FileNotFoundError')
			continue

	# entry DataProcessing
	if ChoosePattern == '6':
		try:
			DataProcessing.main()
			continue
		except FileNotFoundError:
			print('\nMaybe there are some problems, please try again.')
			print('Error code: FileNotFoundError')
			continue

	if ChoosePattern == '7':
		print('\nCalculator will exit 2 seconds later!')
		time.sleep(2)
		sys.exit()

	else:
		print('\nPlease input right number!')
		continue
