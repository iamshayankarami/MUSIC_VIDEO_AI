def change_to_integer(ed):
	edjs = "abcdefghijklmnopqrstuvwxyz ,'"
	all_data = []
	for i, edj in enumerate(edjs):
		send = i, edj
		all_data.append(send)
	if type(ed) == str:
		for data in all_data:
			if ed == data[1]:
				return data[0]
	else:
		for data in all_data:
			if ed == data[0]:
				return data[1]

#data = input()
def main_change(data):
	data = data.lower()
	send = []
	for data in data:
		send.append(change_to_integer(data))
	return send


def main():
	send_data = []
	fi = open('data.txt', 'r').read().split('\n')
	main_data = []
	for data in fi:
		main_data.append(data.replace('"', ''))
	
	for data in main_data:
		send_data.append(main_change(data))
	return send_data

if __name__ == '__main__':
	print(main())
