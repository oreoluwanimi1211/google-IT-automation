#!/usr/bin/env python3

# def validate_user(username, minlen):
#   if minlen < 1:
#     raise ValueError("minlen must be at least 1")

#   if len(username) < minlen:
#     return False
#   if not username.isalnum():
#     return False
#   return True

# def validate_user(username, minlen):
#   assert type(username) == str, "username must be a string"
#   if minlen < 1:
#     raise ValueError("minlen must be at least 1")

#   if len(username) < minlen:
#     return False
#   if not username.isalnum():
#     return False
#   return True

# def read_file(filename):
# 	try:
# 		with open(filename, 'r') as f:
# 			return f.read()
# 	except FileNotFoundError:
# 		return "File not found!"
# 	finally:
# 		print("Finished reading file.")
		
# def faulty_read_and_divide(filename):
# 	with open(filename, 'r') as file:
# 		data = file.readlines()
# 		num1 = int(data[0])
# 		num2 = int(data[1])
# 		return num1 / num2

import unittest
from emails import find_email

class EmailsTest(unittest.TestCase):
	def test_basic(self):
		testcase = [None, "Bree", "Campbell"]
		expected = "breee@abc.edu"
		self.assertEqual(find_email(testcase), expected)

	def test_one_name(self):
		testcase = [None, "John"]
		expected = "Missing parameters"
		self.assertEqual(find_email(testcase), expected)
	
	def test_two_name(self):
		testcase = [None, "Roy", "Cooper"]
		expected = "No email address found"
		self.assertEqual(find_email(testcase), expected)
if __name__ == '__main__':
	unittest.main()
