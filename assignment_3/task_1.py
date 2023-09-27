import os

folder_path = r"D:\SEM_III\Programming_3\assignments\assignment_3"
file_name = "my_info.txt"
files_path = os.path.join(folder_path,file_name)

# function to automate
try:
    with open (files_path,"r") as file:
        for line in file:
            print(line, end="")
except FileNotFoundError:
    print(f"The file '{files_path}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")