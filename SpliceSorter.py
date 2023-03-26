import shutil
import os
import shutil




def get_user_input():
    source_folder = input("Please enter the path to the source folder: ")
    destination_parent = input("Please enter the path to the destination parent folder: ")    
    directory_name = input("Please enter the name of the destination directory: ")
    
#     # Construct the source and destination paths
# #     source_path = os.path.join(source_folder, file_name)
#     destination_path = os.path.join(destination_parent, directory_name)
    
# #     return source_path, destination_path
    return source_folder, destination_parent, directory_name


def initialize(source_folder, destination_parent, directory_name):

#     source_folder = "/Users/jonahbostrom/Documents/Test_repo"
#     destination_parent= "/Users/jonahbostrom/Documents"
#     directory_name = "test_secondary_dir"
    destination_folder = os.path.join(destination_parent, directory_name)

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    
    copy_files(source_folder, destination_folder)

def copy_files(source_folder, destination_folder):
    """
    Calculate the sum of a list of numbers.

    Args:
    lst: A list of numbers.

    Returns:
    The sum of the numbers in the list.
    """
    
    for file_name in os.listdir(source_folder):
        source = os.path.join(source_folder, file_name)
        
        ###check if file_name is a directory
        
        ###If in 
        if os.path.isdir(source): ### reads the source to find if directory
            if not os.path.exists(destination): ##this checks if folder exists in destination
                os.makedirs(destination)
            copy_files(source, destination)
        else: # source is a file; this is the case where we finally copy over our files
            ###append file name here
            destination = os.path.join(destination_folder)

            shutil.copy(source, destination)
#             os.remove(source) ###this may be deleting files


    
if __name__ == '__main__':
    src_lfd, dst_prt, dir_name= get_user_input()
    initialize(src_lfd, dst_prt, dir_name)