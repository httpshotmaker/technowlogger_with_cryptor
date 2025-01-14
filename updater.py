import subprocess
from urllib.request import urlopen
import banners
import time
from colorama import init
from colorama import Fore, Back, Style
import random


def update_client_version(version):
    with open("version.txt", "r") as vnum:
        if vnum.read() != version:
            return True
        else:
            return False


def main():
    try:
        version = urlopen("https://raw.githubusercontent.com/httpshotmaker/technowlogger_with_cryptor/master/version.txt").read()
        version = str(version)
        version = version.replace('\\', '')
        version = version.replace("'", "")
        version = version.replace('r', '')
        version = version.replace('n', '')
        version = version.replace('v', '')
        version = version.replace('b', '')
    except Exception as e:
        print(f"{Fore.RED}[!] Unable to Fletch Origin version.txt")
        print("[!] Please Check Your Internet Connection!")
        print("[*] Exiting ...")
        quit()
        
    if update_client_version(version) is True:
        subprocess.call(["git", "pull", "origin", "master"])
        with open('version.txt', 'w') as upd:
            upd.write(version)
        subprocess.call(["git", "add", "."])
        id = random.randint(1, 9999999999)
        subprocess.call(["git", "commit", "-m", f"update_{id}"])
        return f"{Fore.GREEN}[+] Updated to latest version: v{version}.."
    else:
        return f"{Fore.GREEN}[*] You are already up to date with git origin master :)"


if __name__ == '__main__':
    print(f'{Fore.RED}')
    print(banners.get_banner())
    print("\t\tAuthor: httpshotmaker | Github: github.com/httpshotmaker\n")
    print("[*] Welcome to Technowlogger's Auto Updater")
    print("[++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++]")
    print(f"{Fore.GREEN}[*] Please Note : Git must be installed in order to use \"updater.py\"")
    time.sleep(5)
    print("[++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++]")
    print(f"{Fore.YELLOW}[*] Checking Technowlogger's version information..")
    print(main())
    print("[*] Exiting ...")
