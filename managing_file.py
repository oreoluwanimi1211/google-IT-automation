import os
# import datetime
# # print(os.remove('newfile.txt'))

# with open("newfile.py", 'w') as file:  #create a new file
    
#         print(file)

# print(os.remove('newfile.txt'))
# r_name = os.rename("newfile.txt", "new_file.txt")
# # print(r_name)
# print(os.path.exists("new_file.txt"))
# print(os.cwd("new_file.txt"))
# # print(os.path.exists("new_file.txt"))
# print(os.path.getsize("new_file.txt"))
# timestamp = os.path.getmtime("new_file.txt") # get time in  seconds

# print(datetime.datetime.fromtimestamp(timestamp)) # convert time to readable and understandable one
# print(os.path.abspath("new_file.txt"))

# print(os.getcwd())
with open('names.txt', 'w') as file:
    # print(file)
    file.write('Matteo Rossi')
#This code snippet returns the current working directory.

# os.mkdir("new_dir") # apply once
#The os.mkdir("new_dir") function creates a new directory called new_dir

# dir = "new_dir"
# os.chdir(dir) change the 

# os.chdir("new_dir") then you can change directory after making directory
# os.getcwd()
#This code snippet changes the current working directory to new_dir. 
#The second line prints the current working directory.


# os.mkdir("new_dir")
# os.rmdir("newer_dir")
#This code snippet creates a new directory called newer_dir. 
#The second line deletes the newer_dir directory.

# dir = "website"
# dir = "new_dir"
# for name in os.listdir(dir):
#         fullname = os.path.join(dir, name)
#     if os.path.isdir(fullname):
#             os.getcwd()
#         print("{} is a directory".format(fullname))
#     else:
# print("{} is a file".format(fullname))

# dest_dir = os.path.join(os.getcwd(), "test1")
# if not os.path.exists(dest_dir):
#         os.mkdir(dest_dir)

# src_file = os.path.join(os.getcwd(), "sample_data", "README.md")
# dest_file = os.path.join(os.getcwd(), "test1", "README.md")

# os.rename(src_file, dest_file)

# import os

# def new_directory(directory, filename):
#   # Before creating a new directory, check to see if it already exists
#   if os.path.isdir(directory) == False:
#     os.mkdir(directory)

#   # Create the new file inside of the new directory
#   file_path = os.path.join(directory, filename)
#   with open ('script.py', "a") as file:
#     pass

#   # Return the list of files in the new directory
#   return os.listdir(directory)

# import os
# def create_python_script(filename):
#   comments = "# Start of a new Python program"
#   with open(filename, 'w') as file:
#     file.write(comments)

#   filesize = os.path.getsize(filename)
#   return(filesize)

# print(create_python_script("program.py"))



# import os
# import datetime

# def file_date(filename):
#   # Create the file in the current directory
#   with open(filename, "w") as file:

#     timestamp = os.path.getmtime(filename)
#   # Convert the timestamp into a readable format, then into a string
#   date = datetime.datetime.fromtimestamp(timestamp)
#   # Return just the date portion 
#   # Hint: how many characters are in “yyyy-mm-dd”? 
#   return str(date)[:10]

# print(file_date("newfile.txt")) 
# # Should be today's date in the format of yyyy-mm-dd

# import os
# def parent_directory():
#   # Create a relative path to the parent 
#   # of the current working directory 
#   relative_parent = os.path.join(os.getcwd(), "..")

#   # Return the absolute path of the parent directory
#   return os.path.abspath(relative_parent)

# print(parent_directory())