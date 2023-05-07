import wmi, os, requests, ctypes
from datetime import datetime
from colorama import Fore
from tqdm import *

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
print(Fore.WHITE+f'           Version: Beta 1.9.3 | https://lethals.org            '.center(width))

def get_download(url, filename):
    with requests.get(url, stream=True) as r:
        if r.status_code == 200:
            with open(filename, 'wb') as f:           
                bar = tqdm(total=int(r.headers['Content-Length']), colour='green', desc=f'[{datetime.now().strftime("%H:%M:%S")}] [{Fore.GREEN}Info{Fore.WHITE}] [+] Downloading, Please Wait')
                for data in r.iter_content(chunk_size=8192):
                    if data:  
                        f.write(data)
                        bar.update(len(data))

def get_download_json(url, filename):
    with requests.get(url, stream=True) as r:
        if r.status_code == 200:
            with open(f'{os.getenv("APPDATA")}\\discord\\{filename}', 'wb') as f:           
                bar = tqdm(total=int(len(r.content)),  colour='green', desc=f'[{datetime.now().strftime("%H:%M:%S")}] [{Fore.GREEN}Info{Fore.WHITE}] [+] Downloading, Please Wait')
                for data in r.iter_content(chunk_size=8192):
                    if data:  
                        f.write(data)
                        bar.update(len(data)) 
                 
def get_discord_settings_json():
    replacesetting = input(f'\n\n[{datetime.now().strftime("%H:%M:%S")}] [{Fore.GREEN}info{Fore.WHITE}] [+] Would you like to enable LCTRL + LSHIFT + I for discord? (y/n): ')
    if replacesetting == 'y':
        if os.path.isfile(f"{os.getenv('APPDATA')}\\discord\\settings.json"):
            os.remove(f"{os.getenv('APPDATA')}\\discord\\settings.json")                 
            get_download_json('https://lethals.org/api/settings', 'settings.json')
            print(f'[{datetime.now().strftime("%H:%M:%S")}] [{Fore.GREEN}Info{Fore.WHITE}] [+] Enabled LCTRL + LSHIFT + I, Restart Discord')
    else:
        pass

def get_hwid():
    print(f'\n\n[{datetime.now().strftime("%H:%M:%S")}] [{Fore.GREEN}info{Fore.WHITE}] [+] Your HWID: {Fore.LIGHTYELLOW_EX}{wmi.WMI().Win32_ComputerSystemProduct()[0].UUID}{Fore.WHITE}')  
    print(f'[{datetime.now().strftime("%H:%M:%S")}] [{Fore.GREEN}info{Fore.WHITE}] [+] Copy & Paste Your HWID Into The Ticket\\Bot Command Field')
    Exit=input(f'[{datetime.now().strftime("%H:%M:%S")}] [{Fore.GREEN}info{Fore.WHITE}] [+] Press any key to exit')

def main():
    get_discord_settings_json()
    get_hwid()

if __name__ == "__main__":
	main()
