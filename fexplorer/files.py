from os import listdir, getcwd, popen, rename, system
from os.path import splitext, isdir, expanduser
from pathlib import Path

"""
Check if a given file path is a file or a directory
"""
def isDirectory(path): 
	if isdir(path):
		return True
	else:
		return False

"""
Format the path (fill the blank spaces with "\ " etc.)
"""
def formatPath(path):
    path = path.replace(" ", "\ ")
    path = path.replace("(", "\(")
    path = path.replace(")", "\)")
    
    return path

"""
Lists all the details for a given file
"""
def getFileDetails(filePath):
    filePath = formatPath(filePath)
    
    allDetails = popen("ls -ld " + filePath + " | awk '{print $1, $2, $3, $4, $5, $6, $7, $8}'").read() # exclude file name
    return allDetails.rstrip("\n")

"""
Renames a file
"""
def renameFile(oldFilePath, newFilePath):
    rename(oldFilePath, newFilePath)

"""
Finds all files and folders in a given path
Returns list of all files with a dict of name, label, file detail, path and extension properties
"""
def getAllFilesInGivenDirectory(path):
	files =[]
 
	if len(dirs) != 0: # If the folder is not empty
		max_lenght = max([len(d) for d in dirs]) + 10 # calculating some lenght for printing file details in the same order, otherwise it will look too complicated
		
		for file in dirs:
			if file[0] != ".": # Exclude hidden folders
				filePath = path + "/" + file
				name, extension = splitext(filePath)
				fileDetails = getFileDetails(filePath)
				if extension == "" and isDirectory(filePath) : extension = "folder"
				spaceLenght = max_lenght - len(file)
				icon = u"\U0001F4C1" if isDirectory(filePath) else "  " # If it is a directory use a uniqcode char.
				files.append({"name": file, "label": icon + " " + file + ' '*spaceLenght + fileDetails, "path": filePath, "type": extension, "fileDetails": fileDetails})

	# Add Parent Directory
	parentPath = getParentDirectory(path)
	files.append({"name": "Parent Directory", "label": "[Back]", "path": parentPath, "type": "folder"})

	# Add An Option to Quit
	files.append({"label": "[Quit]", "type": "quit"})
	return files
	

"""
Returns the one back directory of a given path (..)
"""
def getParentDirectory(givenPath): 
    p = Path(givenPath)
    return str(p.parent)

"""
Returns the current directory
"""
def getCurrentDirectory():
    currentDirectory = getcwd()
    return currentDirectory

"""
Returns user's home address
"""
def getHomeDirectory():
    return expanduser('~')

"""
Change permission of a file using chmod command
"""
def changePermission(permisson_list, path):
	path = formatPath(path)
    
	permissions = ""
	for perms in permisson_list: # user, group, etc
		sum = 0
		for p in perms: # read, write, execute, no permission
			sum += p.get("val")
		permissions += str(sum)
	system(f"chmod {permissions} {path}")
 
"""
Copy a file to another destination using cp command
"""
def cp(sourcePath, destinationPath):
	destinationPath = formatPath(destinationPath)
	sourcePath = formatPath(sourcePath)

	if not isDirectory(destinationPath):
		print("The new path is not valid")
	else:
		system(f"cp -r {sourcePath} {destinationPath}")
		print("Successful")
	
	system('sleep 2')

"""
Move a file to another destination using mv command
"""
def mv(sourcePath, destinationPath):
	destinationPath = formatPath(destinationPath)
	sourcePath = formatPath(sourcePath)

	if not isDirectory(destinationPath):
		print("The new path is not valid")
	else:
		system(f"mv -r {sourcePath} {destinationPath}")
		print("Successful")
	system('sleep 2')

"""
When in readFileCli, if the Edit option is selected, cd into the file's directory and run vi command 
"""
def editFile(path):
	path = formatPath(path)
 
	parentPath = getParentDirectory(path)
 
	system(f"cd {parentPath}")
	system(f"vi {path}")
