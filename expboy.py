from __future__ import print_function
try:
    from googlesearch import search
    from googlesearch import exceptions as gsexceptions
except ImportError:
    print("")

import sys
import time
import random
import requests

def make_request(url, proxy=None):
    if proxy:
        proxies = {
            'http': proxy,
            'https': proxy
        }
        response = requests.get(url, proxies=proxies)
    else:
        response = requests.get(url)
    
    return response
    
# Dorks Eye v1.0

if sys.version[0] in "2":
    print ("\n[x] ..n00b.. Dorks Eye Is Not Supported For python 2.x Use Python 3.x \n")
    print ("\n\n\tDorks Eye \033[1;91mI like to See Ya, Hacking \033[0m😃\n\n")
    exit()

class colors:
    CRED2 = "\33[91m"
    CBLUE2 = "\33[94m"
    ENDC = "\033[0m"

banner = ("""
    ▓█████▄  ▒█████   ██▀███   ██ ▄█▀  ██████    ▓█████▓██   ██▓▓█████
    ▒██▀ ██▌▒██▒  ██▒▓██ ▒ ██▒ ██▄█▒ ▒██    ▒    ▓█   ▀ ▒██  ██▒▓█   ▀
    ░██   █▌▒██░  ██▒▓██ ░▄█ ▒▓███▄░ ░ ▓██▄      ▒███    ▒██ ██░▒███
    ░▓█▄   ▌▒██   ██░▒██▀▀█▄  ▓██ █▄   ▒   ██▒   ▒▓█  ▄  ░ ▐██▓░▒▓█  ▄
    ░▒████▓ ░ ████▓▒░░██▓ ▒██▒▒██▒ █▄▒██████▒▒   ░▒████▒ ░ ██▒▓░░▒████▒
    ▒▒▓  ▒ ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░▒ ▒▒ ▓▒▒ ▒▓▒ ▒ ░   ░░ ▒░ ░  ██▒▒▒ ░░ ▒░ ░
    ░ ▒  ▒   ░ ▒ ▒░   ░▒ ░ ▒░░ ░▒ ▒░░ ░▒  ░ ░    ░ ░  ░▓██ ░▒░  ░ ░  ░
    ░ ░  ░ ░ ░ ░ ▒    ░░   ░ ░ ░░ ░ ░  ░  ░        ░   ▒ ▒ ░░     ░
    ░        ░ ░     ░     ░  ░         ░        ░  ░░ ░        ░  ░
    ░                                                  ░ ░  v1.0 """)

for col in banner:
    print(colors.CRED2 + col, end="")
    sys.stdout.flush()
    time.sleep(0.0025)

x = ("""
                Author:  Jolanda de Koff | Bulls Eye
                Github:  https://github.com/BullsEye0
                Website: https://HackingPassion.com
                Patreon: https://www.patreon.com/jolandadekoff\n """)
for col in x:
    print(colors.CBLUE2 + col, end="")
    sys.stdout.flush()
    time.sleep(0.0040)

y = "\n\t\tHi there, Shall we play a game..? 😃\n"
for col in y:
    print(colors.CRED2 + col, end="")
    sys.stdout.flush()
    time.sleep(0.0040)

z = "\n"
for col in z:
    print(colors.ENDC + col, end="")
    sys.stdout.flush()
    time.sleep(0.4)

try:
    data = input("\n[+] Do You Like To Save The Output In A File? (Y/N) ").strip()
    l0g = ("")

except KeyboardInterrupt:
        print ("\n")
        print ("\033[1;91m[!] User Interruption Detected..!\033[0")
        time.sleep(0.5)
        print ("\n\n\t\033[1;91m[!] I like to See Ya, Hacking \033[0m😃\n\n")
        time.sleep(0.5)
        sys.exit(1)

def logger(data):
    file = open((l0g) + ".txt", "a")
    file.write(str(data))
    file.write("\n")
    file.close()

if data.lower().startswith("y"):
    l0g = input("[~] Give The File a Name: ")
    print ("\n" + "  " + "»" * 78 + "\n")
    logger(data)
else:
    print ("[!] Saving is Skipped...")
    print ("\n" + "  " + "»" * 78 + "\n")

def dorks():
    use_proxy = input("\n[+] Do you want to use a proxy? (Y/N): ").strip().lower()
    if use_proxy.startswith('y'):
        proxy = input("[+] Enter the proxy (e.g., http://username:password@proxy_ip:proxy_port): ").strip()
    else:
        proxy = None
        
    try:
        dork = input("\n[+] Enter The Dork Search Query: ")
        amount = input("[+] Enter The Number Of Websites To Display: ")
        print ("\n ")

        requ = 0
        counter = 0

        for results in search(dork, tld="com", lang="en", num=int(amount), start=0, stop=None, pause=5):
            counter += 1
            print(results)
            time.sleep(0.1)
            requ += 1
            if requ >= int(amount):
                break

            data = (counter, results)
            logger(data)
            time.sleep(0.1)

    except KeyboardInterrupt:
        print ("\n")
        print ("\033[1;91m[!] User Interruption Detected..!\033[0")
        time.sleep(0.5)
        print ("\n\n\t\033[1;91m[!] I like to See Ya, Hacking \033[0m😃\n\n")
        time.sleep(0.5)
        sys.exit(1)

    print ("[•] Done... Exiting...")
    print ("\n\t\t\t\t\033[34mDorks Eye\033[0m")
    print ("\t\t\033[1;91m[!] I like to See Ya, Hacking \033[0m😃\n\n")
    sys.exit()

# Main
if __name__ == "__main__":
    dorks()
