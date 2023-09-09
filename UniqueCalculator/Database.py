import pickle


def save_data():
	data = {'Administrator': '321654987'}
	with open('Data.cal', 'rb+') as save_file:
		pickle.dump(data, save_file)
		save_file.close()


# only for Management Model
def open_data():
	with open('Data.cal', 'rb+') as open_file:
		data = pickle.load(open_file)
		open_file.close()
		print(data)


def create_data():
	with open('Data.cal', 'a') as create_file:
		create_file.close()
