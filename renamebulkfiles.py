#This python program will rename all files on a given destination based on the criteria provided by the user
#Step 1: Import OS library to utilize os functions
#Step 2: Ask the user for the path of the files to be renamed
#Step 3: Verify if the path exists
#Step 4: Ask for the naming convention 
#Step 5: Rename all the files and display a success message

import os


def renamefiles(path, name, type):
    #check if path exists
    check = os.path.exists(path)
    i=0
    success = False
    if check:
        for filename in os.listdir(path):
            dest_filename = name + str(i) + type
            source_filename = path + filename
            dest_filename = path + dest_filename
            os.rename(source_filename, dest_filename)
            i+=1
            success = True
    else:
        print("The path provided is invalid! Try again!")
        
    if success:
        print("Operation Completed sucessfully!")
        

path = input("Please enter a valid path: ")
name = input("What is you file naming convention? ")
type = input("what is the file type? ")
renamefiles(path, name, type)