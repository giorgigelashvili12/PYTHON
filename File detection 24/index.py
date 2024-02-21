import os
# it is included in python library
path = 'C:\\Users\\ADMIN\\Desktop\\Courses\\Python Course'
# double \\ is the escape sequence so use it
if os.path.exists(path): # our path is passed in as an argument
    print("Location doesn't exist")
    if os.path.isfile(path): # if file exists
        print("That is a file")
    elif os.path.isdir(path): # if the file is a directory
        print("That is a directory")
else:
    print("Location doesn't exist")