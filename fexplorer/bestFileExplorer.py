from pick import Picker
import fexplorer.files as fl
import os
from fexplorer.mode import MODE
from fexplorer.customscript import customScript

def get_label(option):
    return option.get("label")

"""
Change Permisson of a file
"""
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
            for permission in permissions:
                sum = 0
                for p in permission:
                    sum += p.get("val")
                
                if sum == 0:
                    newPermissionsTitle += "---"
                elif sum == 1:
                    newPermissionsTitle += "--x"
                elif sum == 2:
                    newPermissionsTitle += "-w-"
                elif sum == 3:
                    newPermissionsTitle += "-wx"
                elif sum == 4:
                    newPermissionsTitle += "r--"
                elif sum == 5:
                    newPermissionsTitle += "r-x"
                elif sum == 6:
                    newPermissionsTitle += "rw-"
                elif sum == 7:
                    newPermissionsTitle += "rwx"
                
            title += newPermissionsTitle
        
        options = [ {"label": "No Permission", "char": "-", "val": 0 }, {"label": "Execute", "char": "x", "val": 1 }, {"label": "Write", "char": "w", "val": 2 }, {"label": "Read", "char": "r", "val": 4 } ]
        
        permissionPicker = Picker(options, title, indicator="=>", options_map_func=get_label, min_selection_count=1)
        permissionPicker.multiselect = True
        tuples = permissionPicker.start()
        
        
        newPerms = [option for option, index in tuples]
        permissions.append(newPerms)
    parentDir = fl.getParentDirectory(option.get("path"))
    
    fl.changePermission(permissions, option.get("path"))
    print("Permissions have changed!...")
    os.system('sleep 2')
    
    cli(parentDir)
                
"""
Menu for getting file name input to rename it
"""      
def renameCli(option):
        path = option.get("path")
        extension = option.get("type")
    
        os.system('clear')
        print("Change name of the file: " + option.get("name"))
        newName = input("New File Name: ")
        
        parentDir = fl.getParentDirectory(path)
        newPath = parentDir + f"/{newName}"
        
        if extension != "folder": newPath += str(extension)
        
        fl.renameFile(path, newPath)
        
        print("File Name is changed!")
        os.system('sleep 2')
        cli(parentDir)

"""
Menu for getting a new path from user to copy a file
""" 
def copyCli(option):
    path = option.get("path")
    
    print("Copy " + option.get("name"))
    newPath = input("Destination: ")
    
    parentPath = fl.getParentDirectory(path)
    
    fl.cp(path, newPath) 
    cli(parentPath)

"""
Menu for getting a new path from user to move a file
""" 
def moveCli(option):
    path = option.get("path")
    
    print("Move" + option.get("name"))
    newPath = input("Destination: ")
    
    parentPath = fl.getParentDirectory(path)
    
    fl.mv(path, newPath)
    cli(parentPath)

"""
Editing menu
"""  
def detailCli(option):
    path = option.get("path")
    
    title = option.get("name") + "\n" + path + "\n" + option.get("fileDetails")
    
    options = ["Change Permissions", "Rename", "Copy", "Move", "Back"]
    
    detailPicker = Picker(options, title, indicator="*")
    selectedOption, index = detailPicker.start()
    
    if index == 0:
        permissionChangeCli(option)
    elif index == 1:
        renameCli(option)
    elif index == 2:
        copyCli(option)
    elif index == 3:
        moveCli(option)
    if index == len(options) - 1:
        cli(fl.getParentDirectory(path))

"""
Menu for printing the file content (if it is readable) and give options to edit and return back
"""   
def readFileCli(path):
    try:
        # check to see if file is readable
        with open(path) as file:
            options = ["Edit", "Back"]
            title = file.read()
            readFilePicker = Picker(options, title, indicator="*")
            selectedOption, index = readFilePicker.start()
            
            if index == 0:
                fl.editFile(path)
            else:
                cli(fl.getParentDirectory(path))

    except Exception as err:
        print("Not readable.")
        os.system("sleep 2")
        cli(fl.getParentDirectory(path))

"""
If user is pressed E while selected some file, bring detailCli() screen. Otherwise, exit
"""  
def edit(picker):
    if picker.all_selected != []:
        option = picker.options[picker.all_selected[0]]
        detailCli(option)
    
    return (-1, None)

"""
Main screen that lists all the files and folders
"""  
def cli(path):

    options = fl.getAllFilesInGivenDirectory(path)
    title = f'Files in location: {path}'
    picker = Picker(options, title, indicator="=>", options_map_func=get_label)
    picker.multiselect = True
    picker.register_custom_handler(ord('e'), edit)
    
    tuples = picker.start()
    
    if tuples != []:
        if tuples[0] != -1:
            
            option, index = tuples[0]
            
            if option.get("label") != "[Quit]":
                if fl.isDirectory(option.get("path")):
                    cli(option.get("path"))
                else:
                    if MODE.getMode() == "n":
                        readFileCli(option.get("path"))
                    else:
                        customScript()
    else:
        cli(path)