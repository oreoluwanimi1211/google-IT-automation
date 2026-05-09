# guests = open("guests.txt", 'w')
# initial_guests = ["Bob", "Andrea", "Manuel", "Polly", "Khalid"]

# for i in initial_guests:
#     guests.write(i + "\n")
# guests.close()


# new_guests = ["Sam", "Danielle", "Jacob"]
# with open("guests.txt", 'a') as guests:
#     for i in new_guests:
#         guests.write(i + "\n")

# guests.close()

# with open("guests.txt") as guests:
#     for line in guests:
#         print(line.strip())


# check_out = ["Andrea", "Manuel", "Khalid"]
# temp_list = []

# with open("guests.txt", "r") as guests:
#     for g in guests:
#         temp_list.append(g)

# with open("guests.txt", 'a') as guests:
#     for name in temp_list:
#         if name not in check_out:
#             guests.write(name + "\n")

# with open("guests.txt") as guests:
#     for line in guests:
#         print(line.strip())



# guests_to_check = ['Bob', 'Andrea']
# checked_in = []

# with open("guests.txt","r") as guests:
#     for g in guests:
#         checked_in.append(g.strip())
#     for check in guests_to_check:
#         if check in checked_in:
#             print("{} is checked in".format(check))
#         else:
#             print("{} is not checked in".format(check))
# import os
# print(os.remove("novel.txt"))

# os.rename("first_draft.txt", "finished_masterpiece.txt")
# os.path.exists("userlist.txt")

# os.path.getmtime("spider.txt")
#This code will provide a unix timestamp for the file


#This code will provide the file size
# import os
# import datetime
# timestamp = os.path.getmtime("spider.txt")
# datetime.datetime.fromtimestamp(timestamp)
# print(os.path.getsize("spider.txt"))
# print(timestamp)
#This code will provide the date and time for the file in an 
#easy-to-understand format
# import os
# print(os.path.abspath("spider.txt"))

# import os
# file= "file.dat"
# if os.path.isfile(file):
#     print(os.path.isfile(file))
#     print(os.path.getsize(file))
# else:
# 	print(os.path.isfile(file))
#     print("File not found")

# import os
# print(os.getcwd())
# This code snippet returns the current working directory.

# os.mkdir("new_dir")
#The os.mkdir("new_dir") function creates a new directory called new_dir

# os.chdir("new_dir")
# os.getcwd()
#This code snippet changes the current working directory to new_dir. 
#The second line prints the current working directory.

# os.mkdir("newer_dir")
# os.rmdir("newer_dir")
# This code snippet creates a new directory called newer_dir. 
# The second line deletes the newer_dir directory.

# import os
# os.listdir("website")
#This code snippet returns a list of all the files and 
#sub-directories in the website directory.

#  dir = "website"
#  for name in os.listdir(dir):
#      fullname = os.path.join(dir, name)
#      if os.path.isdir(fullname):
#           print("{} is a directory".format(fullname))
#      else:
#           print("{} is a file".format(fullname))

# Create a directory and move a file from one directory to another
# using low-level OS functions.

# import os

# # Check to see if a directory named "test1" exists under the current
# # directory. If not, create it:
# dest_dir = os.path.join(os.getcwd(), "test1")
# if not os.path.exists(dest_dir):
#  os.mkdir(dest_dir)


# # Construct source and destination paths:
# src_file = os.path.join(os.getcwd(), "sample_data", "README.md")
# dest_file = os.path.join(os.getcwd(), "test1", "README.md")


# # Move the file from its original location to the destination:
# os.rename(src_file, dest_file)

# Create a directory and move a file from one directory to another
# using Pathlib.

# from pathlib import Path

# # Check to see if the "test1" subdirectory exists. If not, create it:
# dest_dir = Path("./test1/")
# if not dest_dir.exists():
#   dest_dir.mkdir()

# # Construct source and destination paths:
# src_file = Path("./sample_data/README.md")
# dest_file = dest_dir / "README.md"

# # Move the file from its original location to the destination:
# src_file.rename(dest_file)


# import os
# dest_dir = os.path.join(os.getcwd(), "test1")
# if not os.path.exists(dest_dir):
#     print(os.mkdir(dest_dir))
# src_file = os.path.join(os.getcwd(), "sample_data", "README.md")
# dest_file = os.path.join(os.getcwd(), "test1", "README.md")
# print(os.rename(src_file, dest_dir))









