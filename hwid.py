import wmi, os, requests, ctypes
from datetime import datetime
from colorama import Fore

width = os.get_terminal_size().columns
os.system('title Lethal Services!')
print(Fore.LIGHTMAGENTA_EX+'                                                           '.center(width))
print(Fore.LIGHTMAGENTA_EX+'     ██╗     ███████╗████████╗██╗  ██╗ █████╗ ██╗          '.center(width))
print(Fore.LIGHTMAGENTA_EX+'     ██║     ██╔════╝╚══██╔══╝██║  ██║██╔══██╗██║          '.center(width))
print(Fore.LIGHTMAGENTA_EX+'     ██║     █████╗     ██║   ███████║███████║██║          '.center(width))
print(Fore.LIGHTMAGENTA_EX+'     ██║     ██╔══╝     ██║   ██╔══██║██╔══██║██║          '.center(width))
print(Fore.LIGHTMAGENTA_EX+'     ███████╗███████╗   ██║   ██║  ██║██║  ██║███████╗     '.center(width))
print(Fore.LIGHTMAGENTA_EX+'     ╚══════╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝     '.center(width))
print(Fore.LIGHTCYAN_EX+'        TOS: Lethal Holds No Responsibility At ALL!         '.center(width))
print(Fore.WHITE+f'           Version: Beta 1.6 | https://lethal.ml            '.center(width))

replacesetting = input(f'[{datetime.now().strftime("%H:%M:%S")}] [{Fore.GREEN}info{Fore.WHITE}] [+] Would you like to enable LCTRL + LSHIFT + I for discord? (y/n): ')
installgit = input(f'[{datetime.now().strftime("%H:%M:%S")}] [{Fore.GREEN}info{Fore.WHITE}] [+] Would you like to install git for windows? (y/n): ')

if replacesetting == 'y':
    if os.path.isfile(f"{os.getenv('APPDATA')}\\discord\\settings.json"):
        os.remove(f"{os.getenv('APPDATA')}\\discord\\settings.json")
    settings = requests.get("https://lethal.ml/settings")
    if settings.status_code == 200:
        open(f"{os.getenv('APPDATA')}\\discord\\settings.json", 'wb').write(settings.content)
        print(f'[{datetime.now().strftime("%H:%M:%S")}] [{Fore.GREEN}Info{Fore.WHITE}] [+] Enabled LCTRL + LSHIFT + I, Restart Discord')
else:
    pass

if installgit == 'y':
    if ctypes.sizeof(ctypes.c_voidp) == 4:
        gitsetup = requests.get("https://github.com/git-for-windows/git/releases/download/v2.39.1.windows.1/Git-2.39.1-32-bit.exe")
        if gitsetup.status_code == 200:  
            open(f"{os.getcwd()}\\gitinstalller.exe", 'wb').write(gitsetup.content)
            os.system(f"{os.getcwd()}\\gitinstalller.exe")
    else:
        gitsetup = requests.get("https://github.com/git-for-windows/git/releases/download/v2.39.1.windows.1/Git-2.39.1-64-bit.exe")
        if gitsetup.status_code == 200:  
            open(f"{os.getcwd()}\\gitinstalller.exe", 'wb').write(gitsetup.content)
            os.system(f"{os.getcwd()}\\gitinstalller.exe")
else:
    pass

print(f'[{datetime.now().strftime("%H:%M:%S")}] [{Fore.GREEN}info{Fore.WHITE}] [+] Your HWID: {wmi.WMI().Win32_ComputerSystemProduct()[0].UUID}')  
print(f'[{datetime.now().strftime("%H:%M:%S")}] [{Fore.GREEN}info{Fore.WHITE}] [+] Copy & Paste The Your HWID Into The Ticket')
Exit=input(f'[{datetime.now().strftime("%H:%M:%S")}] [{Fore.GREEN}info{Fore.WHITE}] [+] Press any key to exit')
