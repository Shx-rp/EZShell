# EZShell
Makes Reverse shell easy and acessible.

## WARNING
This program requires MSFVenom to properly run. otherwise MSFVenom payloads will be generated but wont be able to execute.

## Required Dependencies
### Pyperclip
Instalation: `pip3 install pyperclip`
## How to use
just execute `python3 EZShell.py` and navigate menus using numbers.

## Features
+ Intuitive and simple to navigate menus.
+ A multitude of shells to choose from.
+ Hability to choose the type of shell to open (At the moment only `sh` `BASH` and `powershell` support)
+ Automatically copies the full shell to clipboard.
+ Hability to spawn a MSFVenom payload in a  couple of seconds

## UPDATE V1.00
### **NEW**
+ Revamped Verbose System
+ Option for Verbose now in main menu
+ Added support for various architectures in platform select menu
+ Added support for base64 encryption
### **FIXES**
+ fixed a bug that allowed you to spawn a MSFVenom payload for an architecture that the payload doesnt support
