import csv

f = open("csv_file.txt")
csv_f = csv.reader(f)

for row in  csv_f:
    Name, Role, Phone = row
    print("Name:{}, Pole:{}, Phone:{}".format(Name, Role, Phone))
f.close()

import csv
f = open("csv_file.txt")
csv_f = csv.reader(f)
for row in csv_f:
    Name, Phone, Role = row
    print("Name: {}, Phone: {}, Role: {}".format(Name, Phone, Role))
f.close()

hosts = [["workstation.local", "192.168.25.46"],["webserver.cloud", "10.2.5.6"]]
with open('hosts.csv', 'w') as hosts_csv: 
    # open a new csv file
    writer = csv.writer(hosts_csv) 
    # open  to write  file
    writer.writerows(hosts)  
    # specify to put the above variable inside a given row 

with open('software.csv', 'w') as software:
    reader = csv.DictReader(software)
    for row in reader:
      print(("{} has {} users").format(row["name"], row["users"]))

users = [ {"name": "Sol Mansi", "username": "solm", "department": "IT infrastructure"}, 
 {"name": "Lio Nelson", "username": "lion", "department": "User Experience Research"}, 
  {"name": "Charlie Grey", "username": "greyc", "department": "Development"}]
keys = ["name", "username", "department"]
with open('by_department.csv', 'w') as by_department:
    writer = csv.DictWriter(by_department, fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)


# The most common format for importing and exporting data for spreadsheets is a .csv format. A Comma Separated Values (.csv) file is a plain text file that uses—you guessed it—commas to separate each piece of data. You may already be familiar with .csv files if you have saved a spreadsheet in the .csv format. Here is a simple example of a .csv file displaying employee information:

# Name, Department, Salary

# Aisha Khan, Engineering, 80000

# Jules Lee, Marketing, 67000

# Queenie Corbit, Human Resources, 90000

# Notice that each row represents an employee’s information, and the values are separated by commas. 

# In this reading, you will examine different commands to use when working with .csv files in Python and be provided with additional links for more information.

# Module contents
# The .csv module is a built-in Python functionality used to read and work with .csv files. Let’s look at how the .csv module defines some of these functions:

# csv.reader This function returns a reader object that iterates over lines in the .csv file.

# csv.writer This function returns a writer object that’s responsible for converting the user’s data into delimited strings on the given file-like object.

# class csv.DictReader This function creates an object that functions as a regular reader but maps the information in each row to a dictionary whose keys are given by the optional fieldname parameters.

# Dialects and formatting parameters
# Dialects are rules that define how a .csv file is structured, and parameters are formed to control the behavior of the .csv reader and writer and live within dialects. The following  features are supported by dialects:

# Dialect.delimiter This attribute is a one-character string used to separate fields and defaults to a comma.

# Dialect.quotechar  This attribute is a one-character string used to quote fields containing special characters and defaults to ‘ ‘’ ‘.

# Dialect.strict  This attribute’s default is False, but when True, exception csv.Error will be raised if an error is detected.

# Reader objects
# A reader object contains the following public methods and attributes:

# csvreader._next_() This method returns the next row of the reader’s iterable object as a list or a dictionary, parsed properly to the current dialect. Typically, you would call this next(reader).

# csvreader.dialect This attribute is a read-only description of the dialect in use by the parser.

# Writer objects
# Writer objects provide you the capability to write data to a .csv file. Let’s look at a couple of public methods and attributes for writer objects:

# csvwriter.writerows(rows) This method writes all elements in rows to the writer’s file object and formats following the current dialect.

# csvwriter.dialect This attribute is a read-only description of the dialect being used by the writer.

# Key takeaways
# If you haven’t worked with .csv files yet, it’s only a matter of time. Become familiar with the .csv module’s reader and writer objects to work more efficiently with .csv files. The modules, features, and attributes in this reading are only some of the commands that can be used while working with .csv files. 







import os
import csv

# Create a file with data in it
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")


# Read the file contents and format the information about each row
def contents_of_file(filename):
  return_string = ""

  # Call the function to create the file 
  create_file(filename)

  # Open the file
  with open(filename, "r") as file:
    # Read the rows of the file into a dictionary
    reader = csv.DictReader(file)
    # Process each item of the dictionary
    for row in reader:
      return_string += "a {} {} is {}\n".format(row["color"], row["name"], row["type"])
  return return_string

#Call the function
print(contents_of_file("flowers.csv"))

import os
import csv

# Create a file with data in it
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")

# Read the file contents and format the information about each row
def contents_of_file(filename):
  return_string = ""

  # Call the function to create the file 
  create_file(filename)

  # Open the file
  with open(filename, 'r') as file:
    # Read the rows of the file
    rows =  csv.DictReader(file)
    # Process each row
    for row in rows:
      # name, color, type  = row
      # Format the return string for data rows only

      return_string += "a {} {} is {}\n".format(row["color"], row["name"],row["type"])
  return return_string

#Call the function
print(contents_of_file("flowers.csv"))

import csv

# Dictionary to store department counts
department_count = {}

# Read the CSV file
with open("employees.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        department = row["Department"]

        # Count employees per department
        if department in department_count:
            department_count[department] += 1
        else:
            department_count[department] = 1

# Generate report file
with open("report.txt", "w") as report:
    for department, count in department_count.items():
        report.write(f"{department}: {count}\n")

print("Report generated successfully!")
# Tracking number: c730025880764255



#!/usr/bin/env python3

import csv


# Read employees from CSV file
def read_employees(csv_file_location):

    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)

    employee_file = csv.DictReader(
        open(csv_file_location),
        dialect='empDialect'
    )

    employee_list = []

    for data in employee_file:
        employee_list.append(dict(data))

    return employee_list


# Process employee data
def process_data(employee_list):

    department_list = []

    for employee_data in employee_list:
        department_list.append(employee_data['Department'])

    department_data = {}

    for department_name in set(department_list):
        department_data[department_name] = department_list.count(department_name)

    return department_data


# Write report to text file
def write_report(dictionary, report_file):

    with open(report_file, "w+") as f:

        for k in sorted(dictionary):
            f.write(str(k) + ':' + str(dictionary[k]) + '\n')

        f.close()


# Main program
employee_list = read_employees('/home/student/data/employees.csv')

dictionary = process_data(employee_list)

write_report(dictionary, '/home/student/data/report.txt')



# For this lab, imagine you are an IT Specialist at a medium
# -sized company. The Human Resources Department at your company wants you
#  to find out how many people are in each department. You need to write a Python 
# script that reads a CSV file containing a list of the employees in the organization,
#  counts how many people are in each department, and then generates a report using this
#  information. The output of this script will be a plain text file.
# You will have 90 minutes to complete this lab
# Need help? If you encounter a problem starting or completing this lab, review the


#!/usr/bin/env python3
import csv

#Convert employee data to dictionary
def read_employees(csv_file_location):
    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
    employee_file = csv.DictReader(open(csv_file_location), dialect = 'empDialect')
    employee_list = []
    for data in employee_file:
        employee_list.append(data)
    return employee_list

#Process employee data
def process_data(employee_list):
    department_list = []
    for employee_data in employee_list:
        department_list.append(employee_data['Department'])
    department_data = {}
    for department_name in set(department_list):
        department_data[department_name] = department_list.count(department_name)
    return department_data

#Generate a report
def write_report(dictionary, report_file):
    with open(report_file, "w+") as f:
        for k in sorted(dictionary):
            f.write(str(k)+':'+str(dictionary[k])+'\n')
        f.close()

        

# Terms and definitions from course 2, module 2
# Absolute path: A full path to the resource in the file system

# Comma separated values (CSV): A very common data format used to
# store data as segment of text separated by commas

# Dialects: Rules that define how a CSV file is structured

# File systems: Methods and structures used to organize and control how 
# data is stored and accessed

# Mode: The format controlling what you can do with a recently opened file

# Qwiklabs: An online learning environment or virtual machine to simulate 
# real-world scenarios

# Reader objects:  Object that represents an element or entity within a scene 
# that needs to be rendered to the screen

# Relative path: A portion of a path to show where the resource is
# located in relation to the current working directory

# Virtual machine (VM): A computer simulated through software

# Writer objects: The capability to write data to a CSV file