# def create_python_script(filename):
#   comments = "# Start of a new Python program"
#   with ___:
#     filesize = ___
#   return(filesize)

# print(create_python_script("program.py"))

import os

def create_python_script(filename):
  comments = "# Start of a new Python program"
  with open("program.py", 'w') as file:
    filesize = os.path.getsize("program.py")
  return(filesize)

print(create_python_script("program.py"))
