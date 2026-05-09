# import os
# import datetime

# def file_date(filename):
# #   Create the file in the current directory
#     with open('newfile.txt', 'w') as f:
#         print(f)
#         timestamp = os.path.getmtime('newfile.txt')
#   # Convert the timestamp into a readable format, then into a string
#     datetime.datetime.fromtimestamp(timestamp)
#   # Return just the date portion 
#   # Hint: how many characters are in “yyyy-mm-dd”? 
#     return("{}".format(timestamp/3600))

# print(file_date("newfile.txt")) 
# # Should be today's date in the format of yyyy-mm-dd




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