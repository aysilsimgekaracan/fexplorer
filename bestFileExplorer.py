from typing import Optional
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
    
def edit(picker):
    if picker.all_selected != []:
        option = picker.options[picker.all_selected[0]]
        # picker.title = option.get("path")
        detailCli(option)
    
# def helpCli(picker, path):
#     title = """
#             ***INSTRUCTIONS***
#     - Navigation is done with the arrow keys [←↑→↓]
#     - To Browse Folders: First Select a folder by pressing [SPACE] then [ENTER]\n"
#     - To Edit An File: Select a file with [SPACE] and press [E]
#     - To Return Home: Press [R]
#     """
#     print(title, path)

def cli(path):

    options = fl.getAllFilesInGivenDirectory(path)
    title = f'Files in location: {path}'
    picker = Picker(options, title, indicator="=>", options_map_func=get_label)
    picker.multiselect = True
    picker.register_custom_handler(ord('r'), returnHome)
    picker.register_custom_handler(ord('e'), edit)
 
    # picker.register_custom_handler(ord("b"), returnBack)
    
    tuples = picker.start()
    
    if tuples != []:
        option, index = tuples[0]
    
        if fl.isDirectory(option.get("path")):
            cli(option.get("path"))

        # print(option, index)
    else:
        cli(path)


def main():
#	path = fl.getCurrentDirectory() # Start with the directory that you are currently in
	path = "/Users/aysilsimge/School/5. Dönem"
	cli(path)


if __name__ == "__main__":
	os.system('clear')
	main()


# def returnBack(picker):
#     path = fl.getCurrentDirectory()
#     # print("Option in return back" + path)
#     path = fl.goBackDirectory(path)
#     cli(path)
