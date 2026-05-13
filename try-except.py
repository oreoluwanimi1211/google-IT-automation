from validations import validate_user
import unittest

# class TestValidateUser(unittest.TestCase):
#   def test_valid(self):
#     self.assertEqual(validate_user("validuser", 3), True)

#   def test_too_short(self):
#     self.assertEqual(validate_user("inv", 5), False)

#   def test_invalid_characters(self):
#     self.assertEqual(validate_user("invalid_user", 1), False)
    
#   def test_invalid_minlen(self):
#     self.assertRaises(ValueError, validate_user, "user", -1)


# # Run the tests
# unittest.main()

# def enhanced_read_and_divide(filename):
#   try:
#       with open(filename, mode='r') as file:
#           data = file.readline()

#       # Ensure there are at least two lines in the file
#       if len(data) < 2:
#          raise ValueError ("Not enough data in the file.")
#       num1 = int(data[0])
#       num2 = int(data[1])

#       # Check if second number is zero
#       if num2 == 0:
#         raise ZeroDivisionError("The denominator is zero.")
      
#       return num1 / num2
  
#   except FileNotFoundError:
#           return "Error: The file was not found"
  
#   except ValueError as ve:
#             return f"Value error: {ve}"
  
#   except ZeroDivisionError as zde:
#               return f"Division error: {zde}"
  

# my_list = [27, 5, 9, 6, 8]

# def RemoveValue(myVal):
#     my_list.remove(myVal)
#     return my_list
# print(RemoveValue(27))


# def RemoveValue(myVal):
#     if myVal not in my_list:
#       raise ValueError("the specified number is not in the list")
#     else:
#         my_list.remove(myVal)
#     return my_list

# print(RemoveValue(27))


# my_word_list = ['east', 'after', 'up', 'over', 'inside']
# my_lib = {}
# def OrganizeList(myList):
#     myList.sort()
#     return myList
# print(OrganizeList(my_word_list))

# my_new_list = [6, 3, 8, "12", 42]

# def OrganizeList(myList):
#     for item in myList:
#      assert type(item) == int, "my list must be a integer"
#     myList.sort()
#     return myList

# print(OrganizeList(my_new_list))

import random

participants = ['Jack','Jill','Larry','Tom']

def Guess(participants):
    my_participant_dict = {}
    for participant in participants:
        my_participant_dict[participant] = random.randint(1, 9)
    if my_participant_dict['Larry'] == 9:
        return True
    else:
        return False
    
print(Guess(participants))


# Revised Guess() function
def Guess(participants):
    my_participant_dict = {}
    for participant in participants:
        my_participant_dict[participant] = random.randint(1, 9)
    if my_participant_dict['Larry'] == 9:
        return True
    else:
        return False

participants = ['Cathy','Fred','Jack','Tom']
print(Guess(participants))
























