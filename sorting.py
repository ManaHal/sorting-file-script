import os
import shutil
from os import listdir,mkdir
from os.path import isfile,join,isdir
from shutil import move,copy



def parsing (strin):
    strin = strin.replace("[","")
    artist, tittle = strin.split("] ")
    return (artist, tittle)

def dir_maker(dp_output,foname):
    path=join(dp_output,foname)
    if isdir(path):
        pass
    else:
        mkdir(path)

def mov_file(dp_input,file,dp_output,foname):
    dp_input= join(dp_input,file)
    dp_output=join(join(dp_output,foname),file)
    copy(dp_input,dp_output)
    # move(dp_input,dp_output)


if __name__=='__main__':
    
    print("source dir: ")
    dp_input= input()
    print ("target dir : ")
    dp_output=input()
    dirs = listdir(dp_input)
    for file in dirs:
        foname,finame=parsing(file)
        dir_maker(dp_output,foname)
        mov_file (dp_input,file,dp_output,foname)
