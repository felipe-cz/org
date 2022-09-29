from sys import argv
import os
import shutil
from datetime import date

# adicione sua propria categoria criando uma lista e colocando-a dentro de categories.
# o primeiro indice da lista sera o nome de sua pasta.
apps = ["/Apps", ".exe"]
images = ["/Images", ".png", ".jpeg", ".jpg", ".bmp", ".gif", ".tif", ".tiff", ".jfif"]
documents = ["/Documents", ".txt", ".docx", ".pdf", ".pptx", ".xls", "xlsx"]
categories = [images, documents, apps]

def folder():

    folder_dir = "C:/Past/" + str(date.today())

    if not os.path.exists(folder_dir):
        os.mkdir(folder_dir)   
        for category in categories:
            os.mkdir(folder_dir + category[0])
        os.mkdir(folder_dir + "/Miscellaneous")
    return folder_dir


def organize():

    name = argv[0].encode()
    name = name.split(b"\\")[-1]
    name = name.decode('utf-8')
    
    path = "C:/Users/" + os.getlogin() + "/Desktop/"

    files = os.listdir(path)
    
    dir = folder()

    for file in files:
        misc = True
        file_name = os.path.splitext(file)

        if file == name or file_name[0] == "else":
            continue
        else:
            for category in categories:
                if file_name[-1] in category:
                    move(path, file, file_name, dir + category[0])
                    misc = False
            if misc:
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
    

organize()