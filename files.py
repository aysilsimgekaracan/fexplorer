from os import listdir, getcwd
from os.path import isfile, join, splitext

def getAllFilesInGivenDirectory(path):
	# files = [f for f in listdir(path) if isfile(join(path, f))]
	dirs = listdir(path)

	files =[]
	for file in dirs:
		filePath = path + "/" + file
		name, extension = splitext(filePath)
		if extension == "": extension = "folder"
		files.append({"name": file, "path": filePath, "type": extension})


	return files

def listFiles(files):
	icon = ""
	for file in files:
		if file["type"] == "folder":
			icon = u"\U0001F4C1"
		elif file["type"] == ".png":
			icon = u"\U0001F5BC"
		else:
			icon = u"\u003F"

		print(icon + " " + file["name"])

def getCurrentDirectory():
	currentDirectory = getcwd()
	return currentDirectory

def main():
	#print(u"\U0001F4C1")
	#print(f"Your current directory: {getCurrentDirectory()}")
	path = "/Users/aysilsimge/School/5. Dönem"
	listFiles(getAllFilesInGivenDirectory(path))


if __name__ == "__main__":
    main()