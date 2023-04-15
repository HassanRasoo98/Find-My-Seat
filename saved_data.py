import os

def file_already_exists(filename):
    # check if a file named login info already exists
    # if not then ask user for credentials

    # folder path
    dir_path = os.path.abspath(os.path.curdir)

    # list to store files
    res = []

    # Iterate directory
    for path in os.listdir(dir_path):
        # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            res.append(path)

    if filename in res:
        return True
    
    return False