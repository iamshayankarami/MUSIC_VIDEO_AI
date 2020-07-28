import os
def change_to_integer(ed):
	edjs = "abcdefghijklmnopqrstuvwxyz ,' ()"
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
	return [change_to_integer(data) for data in data]

def remove_N(DATA):
	for data in DATA:
		if len(data) == 0:
			DATA.remove(data)
	return DATA

def new_try(File):
	send = []
	for line in File:
		line = line.split(' ')
		send.append([main_change(data.lower()) for data in line])
	return send

def main(filename, Dir):
	FILE = open(os.path.join(Dir, filename)).read().split('\n')
	return new_try(FILE)

def transfer(data):
	for line in data:
		return [main_change(d) for d in line]

if __name__ == '__main__':
	directiry = 'Desktop/6776_81739_bundle_archive'
	for filename in os.listdir(directiry):
		data = main(filename, directiry)
		print(transfer(data))
