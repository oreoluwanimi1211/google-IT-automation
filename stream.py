# name = input("Please enter your name: ")
# print("Hello, " + name)


# def to_seconds(hours, minutes, seconds):
#     return hours*3600+minutes*60+seconds

# print("Welcome to this time converter")

# cont = "y"
# while(cont.lower() == "y"):
#     hours = int(input("Enter the number of hours: "))
#     minutes = int(input("Enter the number of minutes: "))
#     seconds = int(input("Enter the number of seconds: "))

#     print("That's {} seconds".format(to_seconds(hours, minutes, seconds)))
#     print()
#     cont = input("Do you want to do another conversion? [y to continue] ")

# print("Goodbye!")

# ./seconds.py 
# Welcome to this time converter
# Enter the number of hours: 1
# Enter the number of minutes: 2
# Enter the number of seconds: 3

# Do you want to do another conversion? [y to continue] y
# Enter the number of hours: 3
# Enter the number of minutes: 2
# Enter the number of seconds: 1

# Do you want to do another conversion? [y to continue] n


# data = input("This will come from STDIN: ")
# print("Now we write it to STDOUT: " + data)
# print("Now we generate an error to STDERR: " + data + 1)

# ./streams.py 
# This will come from STDIN: Python Rocks!
# Now we write it to STDOUT: Python Rocks!

# cat greeting.txt 
# Well hello there, STDOUT

# cat greeting.txt 
# Well hello there, STDOUT


# echo $PATH
# /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
# cat variables.py
# #!/usr/bin/env python3
# import os
# print("HOME: " + os.environ.get("HOME", ""))
# print("SHELL: " + os.environ.get("SHELL", ""))
# print("FRUIT: " + os.environ.get("FRUIT", ""))
# ./variables.py 
# export FRUIT=Pineapple
# ./variables.py 

# cat parameters.py 
# #!/usr/bin/env python3
# import sys
# print(sys.argv)

# ./parameters.py
# ['./parameters.py'] 

# ./parameters.py one two three
# ['./parameters.py', 'one', 'two', 'three']


# wc variables.py
# 7 19 174 variables.py 	
# echo $?
# 0

# wc notpresent.sh
# wc: notpresent.sh: No such file or directory
# echo $?
# 1

#!/usr/bin/env python3

# import os
# import sys

# filename = sys.argv[1]

# if not os.path.exists(filename):
#     with open(filename, "w") as f:
#         f.write("New file created\n")
# else:
#     print("Error, the file {} already exists!".format(filename))
#     sys.exit(1)

# ./create_file.py example
# echo $?
# 0

# cat example 
# New file created
# ./create_file.py example
# Error, the file example already exists!
# echo $?
# 1

# my_number = raw_input('Please Enter a Number: \n')
# print(my_number)

#  GNU nano 7.2                 raw.py
# my_number = input('Please Enter a Number: \n')
# print(my_number)
# type(my_number)
# eval(my_number)
# eval(my_number)

# import subprocess
# print(subprocess.run(["date"]))
# print(subprocess.run(["sleep", "2"]))
# result = subprocess.run(["ls", "this_file_does_not_exist"])
# print(result.returncode)


# import subprocess

# result = subprocess.run(["host", "8.8.8.8"], capture_output=True) to capture a logged in user

# result = subprocess.run(["host", "8.8.8.8"], capture_output=True)
# print(result.returncode)

# result = subprocess.run(["host", "8.8.8.8"], capture_output=True)
# print(result.stdout)

# result = subprocess.run(["host", "8.8.8.8"], capture_output=True)
# print(result.stdout.decode().split())

# import subprocess
# result = subprocess.run(["rm", "does_not_exist"], capture_output=True)


# import subprocess
# result = subprocess.run(["rm", "does_not_exist"], capture_output=True)
# print(result.returncode)

# import subprocess
# result = subprocess.run(["rm", "does_not_exist"], capture_output=True)
# print(result.returncode)
# print(result.stdout)
# print(result.stderr)


# import os
# import subprocess
# my_env = os.environ.copy()
# my_env["PATH"] = os.pathsep.join(["/opt/myapp/", my_env["PATH"]])

# result = subprocess.run(["myapp"], env=my_env)
#!/bin/env/python3

# import sys

# logfile = sys.argv[1]
# with open(logfile) as f:
#   for line in f:
#     print(line.strip())



#!/bin/env/python3

# import sys

# logfile = sys.argv[1]
# with open(logfile) as f:
#   for line in f:
#     if "CRON" not in line:
#       continue
#     print(line.strip())



import re
pattern = r"USER \((\w+)\)$"
line = "Jul 6 14:03:01 computer.name CRON[29440]: USER (naughty_user)"
result = re.search(pattern, line)
print(result[1])



#!/bin/env/python3

# import re
# import sys

# logfile = sys.argv[1]
# with open(logfile) as f:
#   for line in f:
#     if "CRON" not in line:
#       continue
#     pattern = r"USER \((.+)\)$"
#     result = re.search(pattern, line)
#     print(result[1])


# chmod +x check_cron.py 
# ./check_cron.py syslog 


import re
def show_time_of_pid(line):
  pattern = r"USER \((\w+)\)$"
  result = re.search(pattern, line)
  return line

print(show_time_of_pid("Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)")) # Jul 6 14:01:23 pid:29440

print(show_time_of_pid("Jul 6 14:02:08 computer.name jam_tag=psim[29187]: (UUID:006)")) # Jul 6 14:02:08 pid:29187

print(show_time_of_pid("Jul 6 14:02:09 computer.name jam_tag=psim[29187]: (UUID:007)")) # Jul 6 14:02:09 pid:29187

print(show_time_of_pid("Jul 6 14:03:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:03:01 pid:29440

print(show_time_of_pid("Jul 6 14:03:40 computer.name cacheclient[29807]: start syncing from \"0xDEADBEEF\"")) # Jul 6 14:03:40 pid:29807

print(show_time_of_pid("Jul 6 14:04:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:04:01 pid:29440

print(show_time_of_pid("Jul 6 14:05:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:05:01 pid:29440


usernames = {}
name = "good_user"
usernames[name] = usernames.get(name, 0) + 1
print(usernames)
usernames[name] = usernames.get(name, 0) + 1
print(usernames)


#!/bin/env/python3

import re
import sys

logfile = sys.argv[1]
usernames = {}
with open(logfile) as f:
  for line in f:
    if "CRON" not in line:
      continue
    pattern = r"USER \((\w+)\)$"
    result = re.search(pattern, line)

    if result is None:
      continue
    name = result[1]
    usernames[name] = usernames.get(name, 0) + 1

print(usernames)


# When searching log files using regex, which statement uses a capture group to search for the alphanumeric 
# word "IP" followed by one or more digits wrapped in parentheses at the end of a line?
r"IP \((\d+)\)$"

#!/usr/bin/env python3
# import sys
# import os
# import re


# def error_search(log_file):
#         error = input("What is the error?")
#         returned_errors = []
#         with open(log_file, mode='r',encoding='UTF-8') as file:
#                 for log in file.readlines():
#                         error_patterns = ["error"]
#                 for i in range(len(error.split(' '))):
# client_loop: send disconnect: I/O errorappend(r"{}".format(error.split(' ')[i].lower()))
#                 if all(re.search(error_pattern, log.lower()) for error_pattern in error_patterns$
#                         returned_errors.append(log)
#         file.close()
#         return returned_errors


# def file_output(returned_errors):
#         with open(os.path.expanduser('~') + '/data/errors_found.log', 'w') as file:
#                 for error in returned_errors:
#                         file.write(error)
#                 file.close()
# if __name__ == "__main__":
#         log_file = sys.argv[1]
#         returned_errors = error_search(log_file)
#         file_output(returned_errors)
#         sys.exit(0)

# sudp chmod +x find_error.py
# ./find_error.py ~/data/fishy.log
# CRON ERROR Failed to start
# cat ~/data/errors_found.log
# July 31 04:11:32 mycomputername CRON[51253]: ERROR: Failed to start CRON job due to script syntax error. Inform the CRON job owner!