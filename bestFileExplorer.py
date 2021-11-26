from pick import pick
import files as fl

path = "/Users/aysilsimge/School/5. Dönem"
fl = fl.getAllFilesInGivenDirectory(path)

options = []

for option in fl:
	options.append(option["name"])


title = f'Files in location: {path}'
# options = ['Java', 'JavaScript', 'Python', 'PHP', 'C++', 'Erlang', 'Haskell']
option, index = pick(options, title)
print(option)
print(index)