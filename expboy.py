from __future__ import print_function
try:
    from googlesearch import search
    from googlesearch import exceptions as gsexceptions
except ImportError:
    print("")

import sys
import time
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

def test_proxy(proxy):
    try:
        response = requests.get("https://www.example.com", proxies={'http': proxy, 'https': proxy}, timeout=10)
        if response.status_code == 200:
            print("Proxy is working properly.")
        else:
            print("Proxy returned status code:", response.status_code)
    except Exception as e:
        print("Error occurred while testing proxy:", e)

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

def logger(data, log_filename):
    with open(log_filename + ".txt", "a") as file:
        file.write(str(data) + "\n")

def dorks(proxy, dork, amount, log_filename):
    test_proxy(proxy)
    proxies = {
        'http': proxy,
        'https': proxy
    }
        
    try:
        print("\n ")
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
            logger(data, log_filename)
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
    proxy = "http://cavacyke-rotate:p464jtmegae6@p.webshare.io:80"  # Add your proxy here
    dork = "example dork search query"  # Add your dork query here
    amount = 10  # Number of websites to display
    log_filename = "output_log"  # Log file name
    dorks(proxy, dork, amount, log_filename)
    
