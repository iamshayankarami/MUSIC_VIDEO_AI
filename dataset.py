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

def main_change(data):
	data = data.lower()
	return [change_to_integer(data) for data in data]


def main():
	fi = open('data.txt', 'r').read().split('\n')
	#test = ["hello its Me I was WonderING 'about", "dfansdvlakdkscdmskd", "dseiwenkxnsd"]
	main_data = [data.replace('"', '') for data in test]	
	return [main_change(data) for data in main_data]

if __name__ == '__main__':
	print(main())
