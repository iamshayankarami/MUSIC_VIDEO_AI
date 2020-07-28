import os
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

def remove_N(data):
	for d in data:
		if d == None:
			data.remove(d)
	return data

def main(fi):
	#test = ["hello its Me I was WonderING 'about", "dfansdvlakdkscdmskd", "dseiwenkxnsd"]
	return main_change(data)

if __name__ == '__main__':
	directiry = 'Desktop/6776_81739_bundle_archive'
	for filename in os.listdir(directiry):
		#print(main(os.path.join(directiry, filename)), '\n')
		t = open(os.path.join(directiry, filename)).read().split('\n')
		for data in t:
			if data == None:
				t.remove(data)
			print(main(data.lower()))
