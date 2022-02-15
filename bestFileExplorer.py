from typing import Optional
from pick import Picker
import curses
import files as fl
import os

def get_label(option):
    # print()
    return option.get("label")

# def changePermissionScreen(option):
#     path = option.get("path")
#     os.system('clear')
#     print(option.get("name") + "\n" + path)
#     print("Old Permissions: " + option.get("fileDetails"))

def permissionChangeCli(option):
    title = "Current Permissions: " + option.get("fileDetails") + "\n"
    
    permissions = []
    
    for i in range(3):
        perm_title = ""
        
        if i == 0:
            perm_title = "user"
        elif i == 1:
            perm_title = "group"
        else:
            perm_title = "other's"
        title = f"Change {perm_title} permissions of the file: " + option.get("name") + "\n"
        
        if permissions != []:
            newPermissionsTitle = ""
            for perms in permissions:
                t = ""
                for p in perms:
                    t += p.get("char")
                
                t += "-"
                newPermissionsTitle += t
                
        title += newPermissionsTitle
        
        options = [ {"label": "No Permission", "char": "-", "val": 0 }, {"label": "Execute", "char": "x", "val": 1 }, {"label": "Write", "char": "w", "val": 2 }, {"label": "Read", "char": "r", "val": 4 } ]
        
        permissionPicker = Picker(options, title, indicator="*", options_map_func=get_label, min_selection_count=1)
        permissionPicker.multiselect = True
        tuples = permissionPicker.start()
        
        newPerms = [option for option, index in tuples]
        
        permissions.append(newPerms)
                
        
def renameCli(option):
        path = option.get("path")
    
        os.system('clear')
        print("Change name of the file: " + option.get("name"))
        newName = input("New File Name: ")
        
        parentDir = fl.getParentDirectory(path)
        newPath = parentDir + f"/{newName}"
        
        fl.renameFile(path, newPath)
        
        print("File Name is changed!")
        os.system('sleep 2')
        cli(parentDir)
        

def detailCli(option):
    path = option.get("path")
    
    title = option.get("name") + "\n" + path + "\n" + option.get("fileDetails")
    
    options = ["Change Permissions", "Rename", "Back"]
    
    # if fl.isDirectory(path):
    #     options.append("Go to directory")
        
    detailPicker = Picker(options, title, indicator="*")
    selectedOption, index = detailPicker.start()
    
    if index == 0:
        permissionChangeCli(option)
    elif index == 1:
        renameCli(option)
    if index == 2:
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
    
    return (-1, None)
    
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
        if tuples[0] != -1:
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
