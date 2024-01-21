import os, sys, time, string, requests, threading, sys, time, random, ctypes, webbrowser,re, hashlib, datetime, os.path
from typing import Optional
from colorama import Fore
import pathlib
import threading, sys, time, random, ctypes, webbrowser,re, hashlib, datetime, os.path
import colorama
from colorama import Fore, init, Back, Style
from datetime import date
from time import localtime, strftime, sleep
from traceback import format_exc
from typing import Union
from colorama import Fore, Style
from tasksio import TaskPool
from multiprocessing.pool import ThreadPool
from os import system
import httpx


ctypes.windll.kernel32.SetConsoleTitleW(f'Magenta Tool | Version 1.0.0 | Early Access')

def set_title(msg):
    "Magnolia"


#logo
banner = (
Fore.CYAN +"""
    \t\t\t.88b  d88.  .d8b.   d888b  d8b   db  .d88b.  db      d888888b  .d8b.  
    \t\t\t88'YbdP`88 d8' `8b 88' Y8b 888o  88 .8P  Y8. 88        `88'   d8' `8b 
    \t\t\t88  88  88 88ooo88 88      88V8o 88 88    88 88         88    88ooo88 
    \t\t\t88  88  88 88~~~88 88  ooo 88 V8o88 88    88 88         88    88~~~88 
    \t\t\t88  88  88 88   88 88. ~8~ 88  V888 `8b  d8' 88booo.   .88.   88   88 
    \t\t\tYP  YP  YP YP   YP  Y888P  VP   V8P  `Y88P'  Y88888P Y888888P YP   YP
""" + Fore.RESET)


#token gen
nitrocount = 0
current_path = os.path.dirname(os.path.realpath(__file__))

tokencount = 0
current_path = os.path.dirname(os.path.realpath(__file__))


#checking app version
print(f"""[{Fore.CYAN}INFO{Fore.RESET}] >>> Checking for updates ...""")
sleep(5)
os.system('cls')


#options
while True:

    print(f"""{banner}
    \n[{Fore.CYAN}+{Fore.RESET}] 1.0.0 | Developed by @gullososa
	\n[{Fore.CYAN}1{Fore.RESET}] Token Generator
	\n[{Fore.CYAN}2{Fore.RESET}] Nitro Generator
    \n[{Fore.CYAN}3{Fore.RESET}] My discord
        """)


    choice = input(f"""[{Fore.CYAN}USER{Fore.RESET}] >>> """)

    choice = choice.strip()

    if choice == '1':
        os.system("cls")
        print(banner)
        print(f"""[{Fore.CYAN}INFO{Fore.RESET}] >>> Input amount of tokens to generate""")
        cantidad = input(f"""[{Fore.CYAN}USER{Fore.RESET}] >>> """)
        while int(tokencount)<int(cantidad):
            Generated = "MTE"+random.choice(string.ascii_letters)+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(23))+"."+random.choice(string.ascii_letters).upper()+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))+"."+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(26))
            f= open(current_path +"/"+str("Tokens")+str("")+".txt","a")
            f.write(Generated+"\n")
            print(f"""[{Fore.CYAN}INFO{Fore.RESET}] >>> Token generated succesfully!""")
            print(f"""[{Fore.CYAN}INFO{Fore.RESET}] >>> Generated Token -> {Fore.CYAN}{Generated}{Fore.RESET}""")
            tokencount+=1
            if int(tokencount)==int(cantidad):
                print(f"""\n[{Fore.CYAN}INFO{Fore.RESET}] >>> You generated {tokencount} tokens, they will be saved to Tokens.txt""")
                print(f"""\n[{Fore.CYAN}INFO{Fore.RESET}] >>> You will be returned to menu in 10 seconds""")
                sleep(10)
                os.system("cls")

            pass
        pass

    
    elif choice == '2':
        os.system('cls')
        print(banner)
        print(f"""[{Fore.CYAN}INFO{Fore.RESET}] >>> Amount of nitro to generate""")
        cantidad=input(f"""[{Fore.CYAN}USER{Fore.RESET}] >>> """)
        while int(nitrocount)<int(cantidad):
            TKNGenerated = "https://discord.gift/"+''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))
            f=open(current_path + "/"+str("Nitro")+str("")+".txt","a")
            f.write(TKNGenerated+"\n")
            print(f"""[{Fore.CYAN}INFO{Fore.RESET}] >>> Nitro generated succesfully!""")
            print(f"""[{Fore.CYAN}INFO{Fore.RESET}] >>> Generated Nitro -> {Fore.CYAN}{TKNGenerated}{Fore.RESET}""")
            nitrocount+=1
            if int(nitrocount)==int(cantidad):
                print(f"""\n[{Fore.CYAN}INFO{Fore.RESET}] >>> You generated {nitrocount} nitro, they will be saved to Nitro.txt""")
                print(f"""\n[{Fore.CYAN}INFO{Fore.RESET}] >>> You will be returned to menu in 10 seconds""")
                sleep(10)
                os.system("cls")

            pass
        pass


    else:
        os.system('cls')
        print(banner)
        print('Invalid option')
        sleep(5)
        os.system('cls')
        
            