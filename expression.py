# import re
# log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
# regex = r"\[(\d+)\]"
# result = re.search(regex, log)
# print(result[1])

# import re
# result = re.search(r"aza", "plaza")
# print(result)

import re

text = "plaza"

result = re.search(r"aza", text)

print(result)

if result:
    print("Match found!")
else:
    print("No match found.")


result = re.search(r"aza", "bazaar")
print(result)

result = re.search(r"aza", "maze")
print(result)

print(re.search(r"^x", "xenon"))

print(re.search(r"p.ng", "penguin"))

print(re.search(r"p.ng", "clapping"))
print(re.search(r"p.ng", "sponge"))
print(re.search(r"p.ng", "Pangaea", re.IGNORECASE))

import re
def check_aei (text):
  result = re.search(r"a", text)
  return result != None

print(check_aei("academia")) # True
print(check_aei("aerial")) # False
print(check_aei("paramedic")) # True


print(re.search(r"[a-z]way", "The end of the highway"))
print(re.search(r"[a-z]way", "What a way to go"))
print(re.search("cloud[a-zA-Z0-9]", "cloudy"))
print(re.search("cloud[a-zA-Z0-9]", "cloud9"))
print(re.search(r"[Pp]ython", "Python"))

print(re.search(r"[^a-zA-Z]", "This is a sentence with spaces."))
print(re.search(r"[^a-zA-Z ]", "This is a sentence with spaces."))

print(re.search(r"cat|dog", "I like cats."))
print(re.search(r"cat|dog", "I love dogs!"))
print(re.search(r"cat|dog", "I like both dogs and cats."))

print(re.search(r"cat|dog", "I like cats."))
print(re.search(r"cat|dog", "I love dogs!"))
print(re.search(r"cat|dog", "I like both dogs and cats."))
print(re.findall(r"cat|dog", "I like both dogs and cats."))

import re
def check_punctuation (text):
  result = re.search(r" ? ", text)
  return result != None

print(check_punctuation("This is a sentence that ends with a period.")) # True
print(check_punctuation("This is a sentence fragment without a period")) # False
print(check_punctuation("Aren't regular expressions awesome?")) # True
print(check_punctuation("Wow! We're really picking up some steam now!")) # True
print(check_punctuation("End of the line")) # False

print(re.search(r"Py.*n", "Pygmalion"))
print(re.search(r"Py.*n", "Python Programming"))
print(re.search(r"Py[a-z]*n", "Python Programming"))
print(re.search(r"Py[a-z]*n", "Pyn"))

print(re.search(r"o+l+", "goldfish"))
print(re.search(r"o+l+", "woolly"))
print(re.search(r"o+l+", "boil"))
print(re.search(r"p?each", "To each their own"))
print(re.search(r"p?each", "I like peaches"))
# escape character is \. to give the same character
print(re.search(r".com", "welcome"))
print(re.search(r"\.com", "welcome"))
print(re.search(r"\.com", "mydomain.com"))
# matches all kind of charcter

print(re.search(r"\w*", "This is an example"))
print(re.search(r"\w*", "And_this_is_another"))

# \d for matching digit 


# \s for matching wide space character
print(re.search(r"A.*a", "Argentina"))
print(re.search(r"A.*a", "Azerbaijan"))
print(re.search(r"^A.*a$", "Australia")) # $ indicate you want to match the end of the character

pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$" # these pattern an also take 
print(re.search(pattern, "_this_is_a_valid_variable_name"))
print(re.search(pattern, "this isn't a valid variable"))
print(re.search(pattern, "my_variable1"))
print(re.search(pattern, "2my_variable1"))

# Regex examples
# r”\d{3}-\d{3}-\d{4}”  This line of code matches U.S. phone numbers in the format 111-222-3333.


# r”^-?\d*(\.\d+)?$”  This line of code matches any positive or negative number, with or without decimal places.


# r”^/(.+)/([^/]+)/$” This line of code is often used to extract specific parts of URLs or file paths, such as the 


import re
def check_web_address(text):
  pattern = r"^[\w\.-]+\.[a-zA-Z]{2,}$"
  result = re.search(pattern, text)
  return result != None

print(check_web_address("gmail.com")) # True
print(check_web_address("www@google")) # False
print(check_web_address("www.Coursera.org")) # True
print(check_web_address("web-address.com/homepage")) # False
print(check_web_address("My_Favorite-Blog.US")) # True


import re
def contains_acronym(text):
  pattern = r"\([A-Za-z0-9]{2,}\)" 
  result = re.search(pattern, text)
  return result != None

print(contains_acronym("Instant messaging (IM) is a set of communication technologies used for text-based communication")) # True
print(contains_acronym("American Standard Code for Information Interchange (ASCII) is a character encoding standard for electronic communication")) # True
print(contains_acronym("Please do NOT enter without permission!")) # False
print(contains_acronym("PostScript is a fourth-generation programming language (4GL)")) # True
print(contains_acronym("Have fun using a self-contained underwater breathing apparatus (Scuba)!")) # Tru


import re

def correct_function(text):
  result = re.search(r"\s\d{5}(-\d{4})?", text)  # Corrected regex pattern with space
  return result is not None

def check_zip_code(text):
  return correct_function(text)  # Call the correct_function

# Call the check_zip_code function with test cases
print(check_zip_code("The zip codes for New York are 10001 thru 11104."))  # True
print(check_zip_code("90210 is a TV show"))  # False (no space before 90210)
print(check_zip_code("Their address is: 123 Main Street, Anytown, AZ 85258-0001."))  # True
print(check_zip_code("The Parliament of Canada is at 111 Wellington St, Ottawa, ON K1A0A9."))  # False

import re
result = re.search(r"^(\w*), (\w*)$", "Lovelace, Ada")
print(result)
print(result.groups())
print(result[0])
print(result[1])
print(result[2])
"{} {}".format(result[2], result[1])


import re
def rearrange_name(name):
    result = re.search(r"^(\w*), (\w*)$", name)
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])
rearrange_name("Lovelace, Ada")


import re
def rearrange_name(name):
    result = re.search(r"^(\w*), (\w*)$", name)
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])
rearrange_name("Ritchie, Dennis")

import re
def rearrange_name(name):
    result = re.search(r"^([\w \.-]*), ([\w \.-]*)$", name)
    if result == None:
        return name
    return "{} {}".format(result[2], result[1])
rearrange_name("Hopper, Grace M.")

import re
def rearrange_name(name):
  result = re.search(r"^(\w*), (\w*)$", name)
  if result == None:
    return name
  return "{} {}".format(result[2], result[1])

name=rearrange_name("Kennedy, John F.")
print(name)

print(re.search(r"[a-zA-Z]{5}", "a ghost"))

print(re.search(r"[a-zA-Z]{5}", "a scary ghost appeared"))

print(re.findall(r"[a-zA-Z]{5}", "a scary ghost appeared"))


re.findall(r"\b[a-zA-Z]{5}\b", "A scary ghost appeared")


print(re.findall(r"\w{5,10}", "I really like strawberries"))

print(re.findall(r"\w{5,}", "I really like strawberries"))

print(re.search(r"s\w{,20}", "I really like strawberries"))

log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])

log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
result = re.search(regex, "A completely different string that also has numbers [34567]")
print(result[1])

log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
result = re.search(regex, "A completely different string that also has numbers [34567]")
result = re.search(regex, "99 elephants in a [cage]")
print(result[1])
#Note that this print command results in an error as shown in the video.


log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
result = re.search(regex, "A completely different string that also has numbers [34567]")
result = re.search(regex, "99 elephants in a [cage]")
def extract_pid(log_line):
    regex = r"\[(\d+)\]"
    result = re.search(regex, log_line)
    if result is None:
        return ""
    return result[1]
print(extract_pid(log))



log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
result = re.search(regex, "A completely different string that also has numbers [34567]")
result = re.search(regex, "99 elephants in a [cage]")
def extract_pid(log_line):
    regex = r"\[(\d+)\]"
    result = re.search(regex, log_line)
    if result is None:
        return ""
    return result[1]
print(extract_pid(log))
print(extract_pid("99 elephants in a [cage]"))

re.split(r"[.?!]", "One sentence. Another one? And the last one!")

re.split(r"([.?!])", "One sentence. Another one? And the last one!")

re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]", "Received an email for go_nuts95@my.example.com")

re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", "Lovelace, Ada")

re.split(r"the|a", "One sentence. Another one? And the last one!")



# dvanced regular expressions—commonly referred to as advanced regexes—are used by developers to execute complicated pattern
# matching against strings. In this reading, you will learn about some of the common examples of advanced regular expressions.

# Alterations
# An alteration matches any one of the alternatives separated by the pipe | symbol. Let’s look at an example:

#  r"location.*(London|Berlin|Madrid)" 

# This line of code will match the text string location is London, location is Berlin, or location is Madrid.

# Matching only at the beginning or end
# If you use the circumflex symbol (also known as a caret symbol) ^ as the first character of your regex, it will match only if
#  the pattern occurs at the start of the string. Alternatively, if you use the dollar sign symbol $ at the end of a regex, it will 
# match only if the pattern occurs at the end. Let’s look at an example:

# r”^My name is (\w+)” 

# This line of code will match My name is Asha but not Hello. My name is Asha.

# Character ranges
# Character ranges can be used to match a single character against a set of possibilities. Let’s look at a couple of examples:

# r”[A-Z] This will match a single uppercase letter.

# r”[0-9$-,.] This will match any of the digits zero through nine, or the dollar sign, hyphen, comma, or period.

# The two examples above are often combined with the repetition qualifiers. Let’s look at one more example:

# r”([0-9]{3}-[0-9]{3}-[0-9]{4})”

# This line of code will match a U.S. phone number such as 888-123-7612.

# Backreferences
# A backreference is used when using re.sub() to substitute the value of a capture group into the output. Let’s look at an example:

# >>> re.sub(r”([A-Z])\.\s+(\w+)”, r”Ms. \2”, “A. Weber and B. Bellmas have joined the team.”)

# This line of code will produce Ms. Weber and Ms. Bellmas have joined the team.

# Lookahead
# A lookahead matches a pattern only if it’s followed by another pattern. Let’s look at an example:

# If the regex was r”(Test\d)-(?=Passed)” and the string was “Test1-Passed, Test2-Passed, Test3-Failed, Test4-Passed, Test5-Failed” the output would be:

# Test1, Test2, Test4


import re
def convert_phone_number(phone):
  result = re.sub(r"(\d{3})-(\d{3})-(\d{4})", r"(\1) \2-\3", phone)
  return result

print(convert_phone_number("My number is 212-345-9999.")) # My number is (212) 345-9999.
print(convert_phone_number("Please call 888-555-1234")) # Please call (888) 555-1234
print(convert_phone_number("123-123-12345")) # 123-123-12345
print(convert_phone_number("Phone number of Buckingham Palace is +44 303 123 7300")) # Phone number of Buckingham Palace is +44 303 123 7300



import re
def transform_comments(line_of_code):
  result = re.sub(r"#+", "//", line_of_code)
  return result

print(transform_comments("### Start of program")) 
# Should be "// Start of program"
print(transform_comments("  number = 0   ## Initialize the variable")) 
# Should be "  number = 0   // Initialize the variable"
print(transform_comments("  number += 1   # Increment the variable")) 
# Should be "  number += 1   // Increment the variable"
print(transform_comments("  return(number)")) 
# Should be "  return(number)"


import re
def multi_vowel_words(text):
  pattern =r"\b\w*[aeiou]{2,}\w*\b"
  result = re.findall(pattern, text)
  return result

print(multi_vowel_words("Life is beautiful")) 
# ['beautiful']

print(multi_vowel_words("Obviously, the queen is courageous and gracious.")) 
# ['Obviously', 'queen', 'courageous', 'gracious']

print(multi_vowel_words("The rambunctious children had to sit quietly and await their delicious dinner.")) 
# ['rambunctious', 'quietly', 'delicious']

print(multi_vowel_words("The order of a data queue is First In First Out (FIFO)")) 
# ['queue']

print(multi_vowel_words("Hello world!")) 
# []


import re
def transform_record(record):
  new_record = re.sub(r"(\d{3}-\d{3}-\d{4}|\d{3}-\d{7})", r"+1-\1", record)
  return new_record

print(transform_record("Sabrina Green,802-867-5309,System Administrator")) 
# Sabrina Green,+1-802-867-5309,System Administrator

print(transform_record("Eli Jones,684-3481127,IT specialist")) 
# Eli Jones,+1-684-3481127,IT specialist

print(transform_record("Melody Daniels,846-687-7436,Programmer")) 
# Melody Daniels,+1-846-687-7436,Programmer

print(transform_record("Charlie Rivera,698-746-3357,Web Developer")) 
# Charlie Rivera,+1-698-746-3357,Web Developer


import re
def transform_record(record):
  new_record = re.sub(r",(\d{3}-\d{3,4}-?\d{0,4}|\d{3}-\d{7})", r",+1-\1", record)
  return new_record

print(transform_record("Sabrina Green,802-867-5309,System Administrator")) 
# Sabrina Green,+1-802-867-5309,System Administrator

print(transform_record("Eli Jones,684-3481127,IT specialist")) 
# Eli Jones,+1-684-3481127,IT specialist

print(transform_record("Melody Daniels,846-687-7436,Programmer")) 
# Melody Daniels,+1-846-687-7436,Programmer

print(transform_record("Charlie Rivera,698-746-3357,Web Developer")) 
# Charlie Rivera,+1-698-746-3357,Web Developer


import re
def multi_vowel_words(text):
  pattern = r"\b\w*[aeiou]{3,}\w*\b"
  result = re.findall(pattern, text)
  return result

print(multi_vowel_words("Life is beautiful")) 
# ['beautiful']

print(multi_vowel_words("Obviously, the queen is courageous and gracious.")) 
# ['Obviously', 'queen', 'courageous', 'gracious']

print(multi_vowel_words("The rambunctious children had to sit quietly and await their delicious dinner.")) 
# ['rambunctious', 'quietly', 'delicious']

print(multi_vowel_words("The order of a data queue is First In First Out (FIFO)")) 
# ['queue']

print(multi_vowel_words("Hello world!")) 
# []

import re
def transform_comments(line_of_code):
  result = re.sub(r"#+", "//", line_of_code)
  return result

print(transform_comments("### Start of program")) 
# Should be "// Start of program"
print(transform_comments("  number = 0   ## Initialize the variable")) 
# Should be "  number = 0   // Initialize the variable"
print(transform_comments("  number += 1   # Increment the variable")) 
# Should be "  number += 1   // Increment the variable"
print(transform_comments("  return(number)")) 
# Should be "  return(number)"

import re
def convert_phone_number(phone):
  result = re.sub(r"\b(\d{3})-(\d{3})-(\d{4})\b", r"(\1) \2-\3", phone)
  return result

print(convert_phone_number("My number is 212-345-9999.")) # My number is (212) 345-9999.
print(convert_phone_number("Please call 888-555-1234")) # Please call (888) 555-1234
print(convert_phone_number("123-123-12345")) # 123-123-12345
print(convert_phone_number("Phone number of Buckingham Palace is +44 303 123 7300")) # Phone number of Buckingham Palace is +44 303 123 7300


# Terms and definitions from course 2, module 3
# Alteration: RegEx that matches any one of the alternatives separated by the pipe symbol

# Backreference: This is applied when using re.sub( ) to substitute the value of a capture group into the output

# Character classes: These are written inside square brackets and let us list the characters we want to match inside of those brackets

# Character ranges: Ranges used to match a single character against a set of possibilities

# grep: An especially easy to use yet extremely powerful tool for applying RegExes

# Lookahead: RegEx that matches a pattern only if it’s followed by another pattern

# Regular expression: A search query for text that's expressed by string pattern, also known as RegEx or RegExp

# Wildcard: A character that can match more than one character


#!/usr/bin/env python3

# Quicklib 2 solution
import csv
import re


def contains_domain(address, domain):
  domain_pattern = r'[\w\.-]+@' + domain + '$'
  if re.match(domain_pattern, address):
    return True
  return False


def replace_domain(address, old_domain, new_domain):
  old_domain_pattern = r'' + old_domain + '$'
  address = re.sub(old_domain_pattern, new_domain, address)
  return address


def main():
  old_domain, new_domain = 'abc.edu', 'xyz.edu'

  csv_file_location = '/home/student/data/user_emails.csv'
  report_file = '/home/student/data/updated_user_emails.csv'

  user_email_list = []
  old_domain_email_list = []
  new_domain_email_list = []

  with open(csv_file_location, 'r') as f:
    user_data_list = list(csv.reader(f))
    user_email_list = [data[1].strip() for data in user_data_list[1:]]

  for email_address in user_email_list:
    if contains_domain(email_address, old_domain):
      old_domain_email_list.append(email_address)
      new_domain_email_list.append(
          replace_domain(email_address, old_domain, new_domain)
      )

  email_key = 'Email Address'
  email_index = user_data_list[0].index(email_key)

  for user in user_data_list[1:]:
    if user[email_index] in old_domain_email_list:
      index = old_domain_email_list.index(user[email_index])
      user[email_index] = new_domain_email_list[index]

  with open(report_file, 'w+') as output_file:
    writer = csv.writer(output_file)
    writer.writerows(user_data_list)


main()
