# SpliceSorter

### DEPRECATED - use code as inspiration. I initially built this early in my programming career before ChatGPT. I aspire to rebuild this project utilizing the Splice APIs.
I keep this here as inspiration and as testament to my love of software and music technologies :) 

## Prerequisites

- Python 3
***Make sure you've downloaded Python3 and that you've navigated to the correct directory (cd to the folder of 

https://realpython.com/installing-python/

## Motivations

Many users of the music on-demand sample library Splice have reported difficulty accessing their samples, as the app by default stores them in nested directories. SpliceSorter bridges this gap by allowing users to quickly create new 'horizontal' directories with all their samples, enabling more efficient workflows.

## Usage

To use Download SpliceSorter.py and type "Python3 SpliceSorter" 

This script is designed to copy all files from a source folder to a destination folder. It can handle copying files as well as any subdirectories within the source folder. This script requires Python 3 to run.

## Instructions

1. Open a terminal or command prompt and navigate to the directory containing the script.
2. Run the script by entering the following command: `python file_copy.py`.
3. The script will prompt you to enter the path to the source folder, the path to the destination parent folder, and the name of the destination directory.
4. After entering the required information, the script will copy all files from the source folder to the destination folder.

## Notes

- If a folder with the same name as the destination directory already exists in the destination parent folder, the script will copy the files to that directory.
- If a file with the same name as a file being copied already exists in the destination directory, the script will overwrite the existing file.
- If a folder within the source folder contains subdirectories, the script will copy all files and subdirectories within that folder.
- This script may delete the source files after copying. To prevent this, comment out or delete the line `os.remove(source)` in the `copy_files()` function.

## Acknowledgements

This script was created with the `shutil` and `os` libraries in Python.

