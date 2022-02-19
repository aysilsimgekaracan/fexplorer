# Simple File Explorer
## About The Project
[![PyPI version](https://badge.fury.io/py/fexplorer.svg)](https://badge.fury.io/py/fexplorer)

It is a simple cli file explorer project that I made for my school project.

![fexplorer](https://user-images.githubusercontent.com/43148881/154813226-6b8bf0c1-7770-4e81-b0db-affa238ba893.gif)

## Installation
```python
pip install fexplorer
```
## Usage
```python
fexplorer path mode(optional, default="n")
```
When mode is n (default),
- It reads the file contents (if the file is readible).
- You have options to open vi or you can go back.

When mode is e,
- The custom script you write will be run.
- Edit [customscript.py](https://github.com/aysilsimgekaracan/fexplorer/blob/main/fexplorer/customscript.py) file.

To start with your current directory, you can simply run:
```python
fexplorer .
```

If you want to run your script,
```python
fexplorer . --m e
```

## Instructions
- Navigation is done with the arrow keys [←↑→↓]
- If you see => as an indicator, you first need to select a file with SPACE and then ENTER.
- If you see * as an indicator, only press ENTER.
- To edit a file: First select the file with SPACE, then press E.
- To return your home directory: Press R

## Buit With
- [Python](https://www.python.org)
- [Pick](https://github.com/wong2/pick)
