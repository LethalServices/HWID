try:
    import wmi, os
    from datetime import datetime
    from colorama import Fore
except ImportError as e:
    print('Please wait while I install the required packages.')
    os.system("pip install -r requirements.txt")

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
print(Fore.WHITE+f'           Version: Beta 1.5 | https://lethal.ml            '.center(width))
print(f'[{datetime.now().strftime("%H:%M:%S")}] [{Fore.GREEN}info{Fore.WHITE}] [+] {wmi.WMI().Win32_ComputerSystemProduct()[0].UUID}')  
print(f'[{datetime.now().strftime("%H:%M:%S")}] [{Fore.GREEN}info{Fore.WHITE}] [+] Copy & Paste The Text Into Your Ticket')
k=input(f'[{datetime.now().strftime("%H:%M:%S")}] [{Fore.GREEN}info{Fore.WHITE}] [+] Press Close To Exit') 
