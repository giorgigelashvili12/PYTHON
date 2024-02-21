import os
import shutil

path = 'text.txt'
try:
    os.remove(path) # delete a file
    # os.rmdir(path)# delete an empty directory
    # shutil.rmtree(path) # delete a directory containing files
    # to delete an empty folder
except FileNotFoundError:
    print("There's no file like zat")
except PermissionError:
    print("Yous ain't got permission")
except OSError:
    print("Nuh uh, you can't buddy, get over it")
else:
    print("Bro doesn't know that he was deleted🤑🤑")