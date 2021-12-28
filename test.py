from pick import pick

def secondFunc():
    output = input("any number: ")
    print(output)
    cli()

def cli():
    options = ['Java', 'JavaScript', 'Python', 'PHP', 'C++', 'Erlang', 'Haskell']
    title = 'Please choose your favorite programming language (press SPACE to mark, ENTER to continue): '
    selected = pick(options, title, multiselect=True, min_selection_count=1)
 
    print(selected)
    secondFunc()



def main():
#	path = fl.getCurrentDirectory() # Start with the directory that you are currently in
	path = "/Users/aysilsimge/School/5. Dönem"
	cli()


if __name__ == "__main__":
	main()