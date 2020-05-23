from threading import Thread
from queue import Queue
import json
import requests
import os

print("\n******************************************************")
print("*                                                    *")
print("*  __  __ _____  _____ _                             *")
print("* |  \\/  |  __ \\|_   _| |                            *")
print("* | \\  / | |__) | | | | |                            *")
print("* | |\\/| |  _  /  | | | |                            *")
print("* | |  | | | \\ \\ _| |_| |____                        *")
print("* |_|  |_|_|  \\_\\_____|______|                       *")
print("*                                                    *")
print("* Mass Reverse IP Lookup                             *")
print("* Coded by thebish0p                                 *")
print("* https://github.com/thebish0p/                      *")
print("******************************************************\n")

INPUT_HANDLE=input('[*] Enter ip addresses file: ')
OUTPUT_HANDLE = open('output.txt', 'a')

addresses = [account.rstrip() for account in open(INPUT_HANDLE.strip()).readlines()]
THREADS =int(input("[*] Enter number of threads: "))

address_q = Queue()
for addy in addresses:
    address_q.put(addy)
class ReverseIP(Thread):
    def __init__(self, address_q):
        self.address_q = address_q
        Thread.__init__(self)

    def run(self):
        while not self.address_q.empty():
            ipaddy = self.address_q.get()
            self.address_q.task_done()
            s = requests.Session()
            try:
                print(f"[*] Reversing {ipaddy} ...")
                s.headers.update({
                    'authority': 'domains.yougetsignal.com',
                    'accept': 'text/javascript, text/html, application/xml, text/xml, */*',
                    'x-prototype-version': '1.6.0',
                    'x-requested-with': 'XMLHttpRequest',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
                    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                    'origin': 'https://www.yougetsignal.com',
                    'sec-fetch-site': 'same-site',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-dest': 'empty',
                    'referer': 'https://www.yougetsignal.com/tools/web-sites-on-web-server/',
                    'accept-language': 'en-US,en;q=0.9,ar;q=0.8,fr;q=0.7',
                })

                data = {
                  'remoteAddress': ipaddy,
                  'key': '',
                  '_': ''
                }

                response = s.post('https://domains.yougetsignal.com/domains.php', data=data)

                if '{"status":"Fail"' in response.text:
                    print('[*] Limit reached change your IP!')
                    exit()
                try:
                    loaded_json=(json.loads(response.text)['domainArray'])
                except:
                    print(f"[*] No domains found for {ipaddy}")
                    return
                OUTPUT_HANDLE.write('Results for '+ipaddy+' :\n')
                print(f"[*] {len(loaded_json)} domains found for {ipaddy}")
                for i in range(len(loaded_json)):
                    OUTPUT_HANDLE.write(loaded_json[i][0]+'\n')
                    OUTPUT_HANDLE.flush()
                OUTPUT_HANDLE.write('=================================================\n')



            except Exception as e:
                print(e)

threads = []
for j in range(THREADS):
    threads.append(ReverseIP(address_q))
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

print("******************************************************")
print('[*] Scan is done')
print(f'[*] Output file: {os.getcwd()}/output.txt')
print("******************************************************")
