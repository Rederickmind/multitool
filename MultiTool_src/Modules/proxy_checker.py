import random, time, sys, subprocess, threading, pycurl, os, requests
from colorama import Fore


class Proxy_Checker():
    def __init__(self):
        subprocess.call('clear', shell=True)
        sys.setrecursionlimit(10**6) 
        print(f"""{Fore.BLUE}
 ██▓███  ██▀███  ▒█████ ▒██   ██▓██   ██▓   ▄▄▄█████▓▒█████  ▒█████  ██▓    
▓██░  ██▓██ ▒ ██▒██▒  ██▒▒ █ █ ▒░▒██  ██▒   ▓  ██▒ ▓▒██▒  ██▒██▒  ██▓██▒    
▓██░ ██▓▓██ ░▄█ ▒██░  ██░░  █   ░ ▒██ ██░   ▒ ▓██░ ▒▒██░  ██▒██░  ██▒██░    
▒██▄█▓▒ ▒██▀▀█▄ ▒██   ██░░ █ █ ▒  ░ ▐██▓░   ░ ▓██▓ ░▒██   ██▒██   ██▒██░    
▒██▒ ░  ░██▓ ▒██░ ████▓▒▒██▒ ▒██▒ ░ ██▒▓░     ▒██▒ ░░ ████▓▒░ ████▓▒░██████▒
▒▓▒░ ░  ░ ▒▓ ░▒▓░ ▒░▒░▒░▒▒ ░ ░▓ ░  ██▒▒▒      ▒ ░░  ░ ▒░▒░▒░░ ▒░▒░▒░░ ▒░▓  ░
░▒ ░      ░▒ ░ ▒░ ░ ▒ ▒░░░   ░▒ ░▓██ ░▒░        ░     ░ ▒ ▒░  ░ ▒ ▒░░ ░ ▒  ░
░░        ░░   ░░ ░ ░ ▒  ░    ░  ▒ ▒ ░░       ░     ░ ░ ░ ▒ ░ ░ ░ ▒   ░ ░   
           ░        ░ ░  ░    ░  ░ ░                    ░ ░     ░ ░     ░  ░
                                 ░ ░                                        

""")
        self.yes = ["yes", "y", "ye", "Y", "YES", 'YE']
        self.no = ["no", "n", "NO", "n"]

        self.thr = 100
        self.TARGET = input(f"{Fore.BLUE}[CONSOLE] Please enter full target url to check the proxies: ")
        self.verbose = input(f"{Fore.BLUE}[CONSOLE] Input bad requests too?: ")
        self.proxy_type = input(f"{Fore.BLUE}[CONSOLE] Proxy type (http, socks4, socks5): ")
        get_proxies = input(f'{Fore.BLUE}[CONSOLE] Get the proxies or you already have http proxy list? (get/n):')

        if get_proxies == 'get':
            try:
                os.remove("ProxyChecker/http_proxies.txt")
                os.remove("ProxyChecker/good_proxies.txt")
            except:
                pass
            
            proxylist = open(f'ProxyChecker/{self.proxy_type}_proxies.txt', 'a+')
            try:
                r1 = requests.get(f'https://api.proxyscrape.com?request=getproxies&proxytype={self.proxy_type}&ssl=yes')
                proxylist.write(r1.text)
            except:
                pass
            proxylist.close()
            self.proxy_file = f'ProxyChecker/{self.proxy_type}_proxies.txt'

        else:
            self.proxy_file = input(f"{Fore.BLUE}[CONSOLE] Please enter the proxy filename: ")
        self.timeout = int(input(f"{Fore.BLUE}[CONSOLE] Please enter proxy timeout (10-100): "))

        self.pro = open("ProxyChecker/good_proxies.txt", "a+")

        self.checked = 0
        self.good = 0

        self.headers= [
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
            'Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
            'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',
            'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000',
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)", 
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)", 
            "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)", 
            "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)", 
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)", 
            "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)", 
            "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)", 
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)", 
            "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6", 
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1", 
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0", 
            "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5", 
            "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6", 
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11", 
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20", 
            "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
        ]

    
    def proxy_checker(self, proxy):
        if self.proxy_type == "http":
            try:
                ip, port = proxy.split(":")[0].replace('\n', ''), proxy.split(":")[1].replace('\n', '')
                c = pycurl.Curl()
                c.setopt(pycurl.URL, self.TARGET)
                c.setopt(pycurl.PROXY, ip)
                c.setopt(pycurl.PROXYPORT, int(port))
                c.setopt(pycurl.PROXYTYPE, pycurl.PROXYTYPE_HTTP)
                c.setopt(pycurl.HTTPHEADER, [f'user-agent: {random.choice(self.headers)}'])
                c.setopt(pycurl.CONNECTTIMEOUT, self.timeout)
                c.setopt(pycurl.WRITEFUNCTION, lambda x: None)
                c.perform()

                if c.getinfo(pycurl.HTTP_CODE) != 403:
                    print(f"{Fore.GREEN}Good Proxy: {proxy}")
                    self.good += 1
                    self.pro.write(f"{proxy}\n")
                
                else:
                    if self.verbose in self.yes:
                        print(f"{Fore.RED}Bad Proxy: {proxy}")                   

            except pycurl.error:
                if self.verbose in self.yes:
                    print(f"{Fore.RED}Bad Proxy: {proxy}")
            except Exception as e:
                print(f'{Fore.RED}{e}')
    
        elif self.proxy_type == "socks4":
            try:
                ip, port = proxy.split(":")[0].replace('\n', ''), proxy.split(":")[1].replace('\n', '')
                c = pycurl.Curl()
                c.setopt(pycurl.URL, self.TARGET)
                c.setopt(pycurl.PROXY, ip)
                c.setopt(pycurl.PROXYPORT, int(port))
                c.setopt(pycurl.PROXYTYPE, pycurl.PROXYTYPE_SOCKS4)
                c.setopt(pycurl.HTTPHEADER, [f'user-agent: {random.choice(self.headers)}'])
                c.setopt(pycurl.CONNECTTIMEOUT, self.timeout)
                c.setopt(pycurl.WRITEFUNCTION, lambda x: None)
                c.perform() 

                print(f"{Fore.GREEN}Good Proxy: {proxy}")
                self.good += 1
                self.pro.write(f"{proxy}\n")

            except pycurl.error:
                if self.verbose in self.yes:
                    print(f"{Fore.RED}Bad Proxy: {proxy}")
            except Exception as e:
                print(f'{Fore.RED}{e}')

        elif self.proxy_type == "socks5":
            try:
                ip, port = proxy.split(":")[0].replace('\n', ''), proxy.split(":")[1].replace('\n', '')
                c = pycurl.Curl()
                c.setopt(pycurl.URL, self.TARGET)
                c.setopt(pycurl.PROXY, ip)
                c.setopt(pycurl.PROXYPORT, int(port))
                c.setopt(pycurl.PROXYTYPE, pycurl.PROXYTYPE_SOCKS5)
                c.setopt(pycurl.HTTPHEADER, [f'user-agent: {random.choice(self.headers)}'])
                c.setopt(pycurl.CONNECTTIMEOUT, self.timeout)
                c.setopt(pycurl.WRITEFUNCTION, lambda x: None)
                c.perform() 

                print(f"{Fore.GREEN}Good Proxy: {proxy}")
                self.good += 1
                self.pro.write(f"{proxy}\n")

            except pycurl.error:
                if self.verbose in self.yes:
                    print(f"{Fore.RED}Bad Proxy: {proxy}")
            except Exception as e:
                print(f'{Fore.RED}{e}')


    def start(self):
        print(f"{Fore.YELLOW}[CONSOLE] Okay! I'm searching for the best proxies. It may take some time...")

        proxys = open(f"{self.proxy_file}", "r", encoding="utf-8", errors='ignore')
        proxies = [proxy.replace("\n", "") for proxy in proxys]

        threads = []
        length = 0
        for _ in proxies:
            length +=1

        while True:
            if threading.active_count() <self.thr:
                if self.checked < length:
                    t = threading.Thread(target=self.proxy_checker, args=(proxies[self.checked],))
                    threads.append(t)
                    t.start()
                    self.checked +=1
            
                else:
                    print(f"\n\n{Fore.RED}[CONSOLE] Closing proxy threads.")
                    for th in threads:
                        th.join()
                    print(f"\n\n{Fore.YELLOW}[CONSOLE] Found {self.good} proxies out of {length}.")
                    proxys.close()
                    self.pro.close()
                    return