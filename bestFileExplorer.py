from pick import Picker
import curses
import files as fl

def get_label(option):
	return option.get("label")

def returnHome(picker): # Return to home directory
    # path = fl.getHomeDirectory()
    path = "/Users/aysilsimge/School/5. Dönem"
    cli(path)

def cli(path):
	options = fl.getAllFilesInGivenDirectory(path)
	title = f'Files in location: {path}'
	picker = Picker(options, title, indicator="=>", options_map_func=get_label)
	picker.register_custom_handler(ord('h'), returnHome)
	# picker.register_custom_handler(ord("b"), returnBack)
 
	option, index = picker.start()
	
	if fl.isDirectory(option.get("path")):
		cli(option.get("path"))

	print(option, index)


def main():
#	path = fl.getCurrentDirectory() # Start with the directory that you are currently in
	path = "/Users/aysilsimge/School/5. Dönem"
	cli(path)


if __name__ == "__main__":
	main()


# def returnBack(picker):
#     path = fl.getCurrentDirectory()
#     # print("Option in return back" + path)
#     path = fl.goBackDirectory(path)
#     cli(path)
