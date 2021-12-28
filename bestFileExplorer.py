from pick import Picker
import curses
import files as fl


def get_label(option): 
	return option.get("label")

def cli(path):
	options = fl.getAllFilesInGivenDirectory(path)
	title = f'Files in location: {path}'
	picker = Picker(options, title, indicator="=>", options_map_func=get_label)
	option, index = picker.start()

	if fl.isDirectory(option.get("path")):
		cli(option.get("path"))

	print(option, index)


def main():
	path = "/Users/aysilsimge/School/5. Dönem"
	cli(path)


if __name__ == "__main__":
	main()
