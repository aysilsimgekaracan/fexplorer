from pick import Picker
import curses
import files as fl
import os

def get_label(option):
    print()
    return option.get("label")

def detailCli(option):
    path = option.get("path")
    
    title = option.get("name") + "\n" + path + "\n" + option.get("fileDetails")
    
    options = ["Change Permissions", "Rename", "Back"]
    
    if fl.isDirectory(path):
        options.append("Go to directory")
        
    detailPicker = Picker(options, title, indicator="*")
    option, index = detailPicker.start()
    
    if index == 3:
        cli(path)

def returnHome(picker): # Return to home directory
    # path = fl.getHomeDirectory()
    path = "/Users/aysilsimge/School/5. Dönem"
    cli(path)
    
def quit(picker):
    return -1

def edit(picker):

    option = picker.options[picker.all_selected[0]]
    # picker.title = option.get("path")
    detailCli(option)

def cli(path):

    options = fl.getAllFilesInGivenDirectory(path)
    title = f'Files in location: {path}'
    picker = Picker(options, title, indicator="=>", options_map_func=get_label)
    picker.multiselect = True
    picker.register_custom_handler(ord('h'), returnHome)
    picker.register_custom_handler(ord('q'), quit)
    picker.register_custom_handler(ord('e'), edit)
 
    # picker.register_custom_handler(ord("b"), returnBack)
    
    tuples = picker.start()
    print(tuples)
    option, index = tuples[0]
   
    if fl.isDirectory(option.get("path")):
        cli(option.get("path"))

	# print(option, index)


def main():
#	path = fl.getCurrentDirectory() # Start with the directory that you are currently in
	path = "/Users/aysilsimge/School/5. Dönem"
	cli(path)


if __name__ == "__main__":
	os.system('cls||clear')
	main()


# def returnBack(picker):
#     path = fl.getCurrentDirectory()
#     # print("Option in return back" + path)
#     path = fl.goBackDirectory(path)
#     cli(path)
