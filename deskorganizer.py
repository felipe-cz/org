import os
import shutil
from datetime import date


images = [".png", ".jpeg", ".jpg", ".bmp", ".gif", ".tif", ".tiff", ".jfif"]
documents = [".txt", ".docx", ".pdf", ".pptx", ".xls", "xlsx"]


def print_center(s):
    print(s.center(shutil.get_terminal_size().columns), end="")


def folder():

    folder_dir = "C:/Past/" + str(date.today())

    if not os.path.exists(folder_dir):
        os.mkdir(folder_dir)
        os.mkdir(folder_dir + "/Pictures")
        os.mkdir(folder_dir + "/Documents")
        os.mkdir(folder_dir + "/Miscellaneous")
    return folder_dir


def organize():

    path = "C:/Users/" + os.getlogin() + "/Desktop/"

    files = os.listdir(path)
    
    dir = folder()

    for file in files:
        
        file_name = os.path.splitext(file)

        if file_name[0] == "org" or file_name[0] == "else":
            continue
        elif file_name[1] in images:
            move(path, file, file_name, dir + "/Pictures")
        elif file_name[1] in documents:
            move(path, file, file_name, dir + "/Documents")
        else:
            move(path, file, file_name, dir + "/Miscellaneous")
        

def move(path, file, file_name, directory):
    i = 2
    while True:
        try:
            if i == 2:
                shutil.move(path + file, directory)
                write("move", file, directory, True)
            else:
                shutil.move(path + new, directory)
                write("move", new, directory,)
        except:
            if i == 2:
                old = file
                write("move", file, directory, True)
            else:
                write("move", new, directory)
                old = new
            new = file_name[0] + " (%i)" % i + file_name[1] 
            os.rename(path+old, path+new)
            write("rename", old, new)
            i += 1
        else:
            break


def write(action, old, new, first=False):

    dir = folder()
    try:
        log = open(dir + "/log.txt", "x")
    except FileExistsError:
        log = open(dir + "/log.txt", "a")

    if first:
        log.write("\n%sd\t%s   to   %s\n" % (action, old, new))
    else:
        log.write("    - ")
        log.write("%sd\t%s   to   %s\n" % (action, old, new))

    log.close()
    

os.system("cls")
organize()
os.system("cls")
