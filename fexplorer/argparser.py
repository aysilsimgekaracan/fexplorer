import bestFileExplorer as fe
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="A filepath (. for the current directory)")
    args = parser.parse_args()
    print(args)
    
main()